#!/usr/bin/env python3
"""Render prompts for IDs in the enriched XLSX that don't already have one.

Reads `processed/AI_Features_Data_Enriched.xlsx` for (Identifier, Name) pairs
and renders `prompt/PROMPT_USO_IA_ESFUERZO.md` with substitutions, writing
each output to:

    effort/prompts/<id_lower>_<slug>_analysis.prompt.md

Skips any output file that already exists (idempotent).

Usage:
  python scripts/render_pending_prompts.py
  python scripts/render_pending_prompts.py --force   # overwrite existing prompts
"""
import argparse
import re

import openpyxl

from _paths import ENRICHED_FINAL, PROMPT_ANALYSIS, EXEC_PROMPTS_DIR


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (text or "").lower()).strip("_")


def render(template: str, code: str, name: str) -> str:
    return template.replace("{{code}}", code).replace("{{name}}", name)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true", help="Overwrite existing prompts")
    args = p.parse_args()

    if not ENRICHED_FINAL.exists():
        print(f"ERROR: {ENRICHED_FINAL} does not exist. Run merge_enriched_batches.py first.")
        return 1
    if not PROMPT_ANALYSIS.exists():
        print(f"ERROR: template not found at {PROMPT_ANALYSIS}")
        return 2

    template = PROMPT_ANALYSIS.read_text(encoding="utf-8")
    EXEC_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.load_workbook(ENRICHED_FINAL, read_only=True, data_only=True)
    ws = wb["AI Features & Agents"]
    rows = ws.iter_rows(values_only=True)
    header = next(rows)
    id_idx, name_idx = header.index("Identifier"), header.index("Name")

    written, skipped = 0, 0
    for r in rows:
        if not r:
            continue
        code, name = r[id_idx], r[name_idx]
        if not code or not name:
            continue
        slug = slugify(str(name))
        out = EXEC_PROMPTS_DIR / f"{str(code).lower()}_{slug}_analysis.prompt.md"
        if out.exists() and not args.force:
            skipped += 1
            continue
        out.write_text(render(template, str(code), str(name)), encoding="utf-8")
        written += 1
        print(f"  {code}\t-> {out.relative_to(EXEC_PROMPTS_DIR.parent.parent)}")
    print(f"\nWritten: {written}  |  Skipped (already existed): {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
