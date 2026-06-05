#!/usr/bin/env python3
"""Render description prompts for IDs that don't already have one.

Reads `processed/AI_Features_Data_Enriched.xlsx` and renders
`prompt/PROMPT_DESCRIPCION_AI_FEATURE.md` per case, writing each to:

    description/prompts/<id_lower>_<slug>_description.prompt.md

Each rendered prompt carries the case's Detail Page URL so the generating
agent knows exactly which live page to open. Skips outputs that already
exist (idempotent).

Usage:
  python scripts/render_pending_descriptions.py
  python scripts/render_pending_descriptions.py --force   # overwrite existing
"""
import argparse
import re

import openpyxl

from _paths import ENRICHED_FINAL, PROMPT_DESCRIPTION, DESC_PROMPTS_DIR


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (text or "").lower()).strip("_")


FIELDS = {
    "{{name}}": "Name",
    "{{product}}": "Product",
    "{{ai_type}}": "AI Type",
    "{{commercial_type}}": "Commercial Type",
    "{{availability}}": "Availability",
    "{{detail_page}}": "Detail Page",
}


def render(template: str, code: str, slug: str, row: dict) -> str:
    out = template.replace("{{code}}", code).replace("{{code_lower}}", code.lower())
    out = out.replace("{{slug}}", slug)
    for ph, col in FIELDS.items():
        out = out.replace(ph, str(row.get(col) or "").strip() or "No disponible")
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true", help="Overwrite existing prompts")
    args = p.parse_args()

    if not ENRICHED_FINAL.exists():
        print(f"ERROR: {ENRICHED_FINAL} does not exist. Run merge_enriched_batches.py first.")
        return 1
    if not PROMPT_DESCRIPTION.exists():
        print(f"ERROR: template not found at {PROMPT_DESCRIPTION}")
        return 2

    template = PROMPT_DESCRIPTION.read_text(encoding="utf-8")
    DESC_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.load_workbook(ENRICHED_FINAL, read_only=True, data_only=True)
    ws = wb["AI Features & Agents"]
    rows = ws.iter_rows(values_only=True)
    header = list(next(rows))
    idx = {col: header.index(col) for col in header}

    written, skipped = 0, 0
    for r in rows:
        if not r:
            continue
        row = {col: r[i] for col, i in idx.items()}
        code, name = row.get("Identifier"), row.get("Name")
        if not code or not name:
            continue
        code, slug = str(code), slugify(str(name))
        out = DESC_PROMPTS_DIR / f"{code.lower()}_{slug}_description.prompt.md"
        if out.exists() and not args.force:
            skipped += 1
            continue
        out.write_text(render(template, code, slug, row), encoding="utf-8")
        written += 1
        print(f"  {code}\t-> {out.relative_to(DESC_PROMPTS_DIR.parent.parent)}")
    print(f"\nWritten: {written}  |  Skipped (already existed): {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
