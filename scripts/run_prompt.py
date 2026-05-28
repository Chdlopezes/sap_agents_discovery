#!/usr/bin/env python3
"""Render the SAP IA prompt for one or more (code, name) pairs.

Usage:
    python scripts/run_prompt.py --code J600 --name "Joule with SAP Multi-Bank Connectivity"
    python scripts/run_prompt.py --csv inputs/input.csv
    python scripts/run_prompt.py --csv inputs/input.csv --only J600

Output: one rendered prompt per case at executions/prompts/<code>_<slug>_analysis.prompt.md
The analysis itself (LLM response) is expected to be saved as
executions/analyses/<code>_<slug>_analysis.md.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "prompt" / "PROMPT_USO_IA_ESFUERZO.md"
OUT_DIR = ROOT / "executions" / "prompts"
ANALYSES_DIR = ROOT / "executions" / "analyses"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def render(code: str, name: str) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    return tpl.replace("{{code}}", code).replace("{{name}}", name)


def write_prompt(code: str, name: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(name)
    path = OUT_DIR / f"{code.lower()}_{slug}_analysis.prompt.md"
    path.write_text(render(code, name), encoding="utf-8")
    return path


def iter_csv(csv_path: Path, only: str | None):
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code, name = row["code"].strip(), row["name"].strip()
            if only and code != only:
                continue
            yield code, name


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--code")
    p.add_argument("--name")
    p.add_argument("--csv", type=Path)
    p.add_argument("--only", help="Filter CSV by a single code")
    p.add_argument("--skip-existing", action="store_true",
                   help="Do not overwrite prompt files that already exist")
    args = p.parse_args()

    if args.csv:
        pairs = list(iter_csv(args.csv, args.only))
    elif args.code and args.name:
        pairs = [(args.code, args.name)]
    else:
        p.error("Provide --code/--name or --csv")

    written, skipped = 0, 0
    for code, name in pairs:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUT_DIR / f"{code.lower()}_{slugify(name)}_analysis.prompt.md"
        if out.exists() and args.skip_existing:
            skipped += 1
            continue
        out.write_text(render(code, name), encoding="utf-8")
        written += 1
        print(f"{code}\t{name}\t-> {out.relative_to(ROOT)}")
    if args.skip_existing:
        print(f"\nWritten: {written}  |  Skipped (already existed): {skipped}")


if __name__ == "__main__":
    main()
