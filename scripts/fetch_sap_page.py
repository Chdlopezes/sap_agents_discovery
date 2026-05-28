#!/usr/bin/env python3
"""Render a SAP Help Portal / SAP Discovery Center page with headless Chrome.

`WebFetch` cannot read SAP's JavaScript SPAs (help.sap.com, discovery-center.cloud.sap)
because they need a browser to render. This script uses Playwright with the
system Chrome (or Chromium) to render the page and emit the plain text content.

Usage:
  python scripts/fetch_sap_page.py <url>
  python scripts/fetch_sap_page.py <url> --selector "main"     # custom content selector
  python scripts/fetch_sap_page.py <url> --raw                 # also print HTML to stderr
  python scripts/fetch_sap_page.py <url> --links               # append a Links section
  python scripts/fetch_sap_page.py <url> --links --filter "Initial Setup"   # only matching links

Output: rendered visible text on stdout. With --links, appends a `## Links` section
listing `[text](url)` entries from `<a href>` elements, after the body text.

Prerequisites:
  pip install playwright
  # System Chrome at /usr/bin/google-chrome is preferred; Playwright will
  # otherwise download its own Chromium with `playwright install chromium`.
"""
import argparse
import asyncio
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    sys.exit("ERROR: playwright not installed. Run: pip install playwright")


SAP_DOMAINS = (
    "help.sap.com",
    "discovery-center.cloud.sap",
    "roadmap.sap.com",
    "community.sap.com",
    "sap.com",
)


async def fetch(url: str, selector: str | None, timeout_ms: int, post_wait_ms: int,
                emit_raw: bool, with_links: bool, link_filter: str | None) -> str:
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            # Fallback: use Playwright's bundled Chromium (requires `playwright install`)
            browser = await p.chromium.launch(headless=True)
        try:
            ctx = await browser.new_context(
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            )
            page = await ctx.new_page()
            await page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)

            # Try to wait for the article content. Selectors specific to SAP Help.
            wait_selectors = [selector] if selector else [
                "article", "main", "[role=main]", ".topic", ".content",
            ]
            for sel in wait_selectors:
                if not sel:
                    continue
                try:
                    await page.wait_for_selector(sel, timeout=15000)
                    break
                except Exception:
                    continue

            await page.wait_for_timeout(post_wait_ms)

            if emit_raw:
                html = await page.content()
                print("---RAW HTML BEGIN---", file=sys.stderr)
                print(html, file=sys.stderr)
                print("---RAW HTML END---", file=sys.stderr)

            text = await page.evaluate("() => document.body.innerText")

            if with_links:
                # Extract all <a> elements with absolute hrefs and their visible text.
                # Dedupe by (text, url) and skip empty/anchor-only links.
                links = await page.evaluate("""
                    () => {
                      const out = [];
                      const seen = new Set();
                      for (const a of document.querySelectorAll('a[href]')) {
                        const href = a.href;
                        const label = (a.innerText || a.textContent || '').trim().replace(/\\s+/g, ' ');
                        if (!href || href.startsWith('javascript:') || href === '#') continue;
                        const key = label + '||' + href;
                        if (seen.has(key)) continue;
                        seen.add(key);
                        out.push({label, href});
                      }
                      return out;
                    }
                """)
                if link_filter:
                    needle = link_filter.lower()
                    links = [l for l in links if needle in (l["label"] or "").lower()]
                text += "\n\n## Links\n"
                if not links:
                    text += "(no links matched)\n"
                else:
                    for l in links:
                        label = l["label"] or "(no text)"
                        text += f"- [{label}]({l['href']})\n"

            return text
        finally:
            await browser.close()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--selector", default=None,
                   help="CSS selector to wait for before extracting text")
    p.add_argument("--timeout", type=int, default=60000,
                   help="Page goto timeout in ms (default 60000)")
    p.add_argument("--post-wait", type=int, default=5000,
                   help="Extra wait after content loads, in ms (default 5000)")
    p.add_argument("--raw", action="store_true",
                   help="Also emit rendered HTML to stderr")
    p.add_argument("--links", action="store_true",
                   help="Append a `## Links` section with [text](url) for every <a href>")
    p.add_argument("--filter", default=None,
                   help="With --links: keep only links whose text contains this substring (case-insensitive)")
    p.add_argument("--allow-any-domain", action="store_true",
                   help="Skip the SAP-domains-only safety check")
    args = p.parse_args()

    # Safety: only fetch SAP-official domains by default
    if not args.allow_any_domain:
        if not any(d in args.url for d in SAP_DOMAINS):
            sys.exit(
                f"ERROR: URL is not on an SAP official domain ({', '.join(SAP_DOMAINS)}).\n"
                f"Use --allow-any-domain to override (not recommended for the pipeline)."
            )

    text = asyncio.run(fetch(args.url, args.selector, args.timeout, args.post_wait,
                              args.raw, args.links, args.filter))
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
