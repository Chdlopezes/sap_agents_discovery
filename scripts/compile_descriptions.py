#!/usr/bin/env python3
"""Incrementally compile description/fichas/*.md into one RAG-ready .md file.

- Tracks which fichas are already included in
  `description/compiled/descriptions_compiled.md` via
  `state/descriptions_compiled_state.json`.
- On each run, (re)writes the corpus in deterministic order (sorted by
  filename) with an up-to-date header, and records the state.

Usage:
  python scripts/compile_descriptions.py            # incremental
  python scripts/compile_descriptions.py --rebuild  # recompile from scratch
"""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from _paths import DESC_FICHAS_DIR, DESC_COMPILED_MD, DESC_COMPILED_STATE, STATE_DIR

HEADER_TEMPLATE = """# SAP Business AI — Fichas Descriptivas de AI Features (Corpus RAG)

> **Última actualización:** {timestamp}
> **Fichas incluidas:** {n_total}

## Qué contiene este documento

Este archivo es la **concatenación canónica** de las fichas explicativas de los
casos de uso de IA del catálogo **SAP Business AI**. A diferencia del corpus de
*esfuerzo de activación* (`effort/`), aquí el foco es **entender qué hace cada
AI Feature y cómo se usa**, no estimar su esfuerzo.

Cada ficha, identificada por su código `JNNN` y nombre oficial, contiene:

1. **En una frase** — síntesis ultra-breve.
2. **¿Qué es?** — Overview tomado de la Detail Page de SAP Discovery Center.
3. **Beneficios** y **Valor de negocio** — publicados por SAP.
4. **¿Cómo funciona?** — flujo de uso de la capability.
5. **Casos de uso (ilustrativos)** — escenarios de ejemplo (no oficiales) para
   facilitar la comprensión.
6. **¿Cuándo usarla?** y **Datos clave**.

## Reglas de la fuente

- El Overview, Beneficios y Valor de negocio provienen de la **Detail Page**
  oficial de SAP Discovery Center (contenido vivo).
- Los **casos de uso** marcados como *ilustrativos* son ejemplos redactados para
  facilitar la comprensión y **no** son escenarios oficiales de SAP.
- Las fichas están escritas en **español**.

## Cómo está estructurado este archivo

- Cada ficha es una sección de nivel 2 con el formato `## [JNNN] — Nombre`,
  separada por una línea horizontal `---`.

> Para cargar este corpus en un sistema RAG: trocea por sección de nivel 2
> (`##`) y trata el texto bajo cada encabezado como una unidad semántica.

---

"""


def _section_for(path: Path) -> str:
    """Read a ficha file and return its section text (with separator)."""
    text = path.read_text(encoding="utf-8").rstrip()
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        m = re.search(r"\bJ\d+\b", title)
        code = m.group(0) if m else ""
        cleaned = re.sub(r"^J\d+\s*[—-]\s*", "", title)
        new_title = f"[{code}] — {cleaned}" if code else title
        lines = [f"## {new_title}", *lines[1:]]
        text = "\n".join(lines)
    return text + "\n\n---\n\n"


def _load_state() -> set[str]:
    if not DESC_COMPILED_STATE.exists():
        return set()
    try:
        data = json.loads(DESC_COMPILED_STATE.read_text(encoding="utf-8"))
        return set(data.get("compiled_files", []))
    except Exception:
        return set()


def _save_state(files: set[str]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    DESC_COMPILED_STATE.write_text(
        json.dumps({
            "compiled_files": sorted(files),
            "last_updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--rebuild", action="store_true",
                   help="Discard state and rebuild the compiled file from scratch.")
    args = p.parse_args()

    if not DESC_FICHAS_DIR.exists():
        print(f"ERROR: {DESC_FICHAS_DIR} does not exist.")
        return 1

    all_files = sorted(p.name for p in DESC_FICHAS_DIR.glob("*.md"))
    if not all_files:
        print(f"No fichas in {DESC_FICHAS_DIR}.")
        return 0

    if args.rebuild or not DESC_COMPILED_MD.exists():
        already = set()
        new_files = list(all_files)
    else:
        already = _load_state()
        new_files = [f for f in all_files if f not in already]

    if not new_files and not args.rebuild:
        print(f"Nothing new to compile. Compiled file: {DESC_COMPILED_MD}")
        return 0

    DESC_COMPILED_MD.parent.mkdir(parents=True, exist_ok=True)

    final_files = sorted(set(already) | set(new_files))
    header = HEADER_TEMPLATE.format(
        timestamp=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        n_total=len(final_files),
    )
    body_parts = [_section_for(DESC_FICHAS_DIR / fn) for fn in final_files]
    DESC_COMPILED_MD.write_text(header + "".join(body_parts), encoding="utf-8")

    _save_state(set(final_files))

    print(f"Compiled file: {DESC_COMPILED_MD}")
    print(f"  Total fichas included: {len(final_files)}")
    print(f"  New in this run:       {len(new_files)}")
    if new_files:
        for fn in new_files[:10]:
            print(f"    + {fn}")
        if len(new_files) > 10:
            print(f"    + ... (+{len(new_files)-10} more)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
