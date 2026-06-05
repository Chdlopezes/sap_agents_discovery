#!/usr/bin/env python3
"""Incrementally compile effort/analyses/*.md into one RAG-ready .md file.

- Tracks which analysis files have already been included in
  `effort/compiled/analyses_compiled.md` via `state/compiled_state.json`.
- On each run, appends any new files (sorted alphabetically by filename for
  deterministic order) and updates the state.
- Initializes the compiled file with a static header explaining its purpose
  and structure so that a downstream RAG / embedding system understands what
  the corpus contains.

Usage:
  python scripts/compile_analyses.py            # incremental
  python scripts/compile_analyses.py --rebuild  # discard state and recompile from scratch
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from _paths import EXEC_ANALYSES_DIR, COMPILED_MD, COMPILED_STATE, STATE_DIR

HEADER_TEMPLATE = """# SAP Business AI — Análisis de Esfuerzo de Activación (Corpus RAG)

> **Última actualización:** {timestamp}
> **Análisis incluidos:** {n_total}

## Qué contiene este documento

Este archivo es la **concatenación canónica** de los análisis de esfuerzo de
activación para los casos de uso de IA del catálogo **SAP Business AI**
(Joule, SAP Document AI, SAP Analytics Cloud, SAP Signavio, SAP LeanIX,
SAP Datasphere, SAP Build, SAP Integration Suite, SAP Cloud ALM y otros).

Cada análisis describe, para un caso de uso identificado por su código
`JNNN` y nombre oficial, los siguientes bloques:

1. **Resumen del caso** — qué hace, sobre qué producto, valor de negocio
   publicado por SAP.
2. **Prerequisitos para la activación** — productos / componentes,
   licenciamiento (Base / Premium, AI Units, paquetes), scope items, apps
   Fiori, datos maestros / transaccionales, restricciones (idioma, edición,
   roles, región).
3. **Pasos de activación / configuración estándar** — tabla con actividad,
   objeto de configuración, tipo (General / Particular), consultor requerido
   y horas estimadas para un consultor nivel Medium.
4. **Pasos adicionales de validación** — prueba unitaria, documentación,
   transferencia de conocimiento.
5. **Consideraciones especiales** — políticas, gobernanza, roadmap,
   data residency, fair-use.
6. **Referencias oficiales** — enlaces a SAP Discovery Center y SAP Help Portal.
7. **Resumen ejecutivo de esfuerzo** — totales en horas.

## Reglas de la fuente

- Toda la información proviene de fuentes públicas de SAP (SAP Discovery Center,
  SAP Help Portal, SAP AI Foundation Catalog, SAP Road Map Explorer).
- Los valores marcados como `[verificar en SAP Help]` requieren validación
  contra la documentación oficial vigente antes de ser usados en una
  propuesta o activación real con el cliente.
- Los análisis están escritos en **español**.

## Cómo está estructurado este archivo

- Cada análisis aparece como una sección independiente, separada por una
  línea horizontal `---` y precedida por un encabezado de nivel 2 con el
  formato `## [JNNN] — Nombre del caso de uso`.
- El contenido de cada sección es el texto completo del análisis individual,
  tal como existe en `effort/analyses/<id>_<slug>_analysis.md`.

> Para cargar este corpus en un sistema RAG: trocea por sección de nivel 2
> (`##`) y trata el texto bajo cada encabezado como una unidad semántica.

---

"""


def _section_for(path: Path) -> str:
    """Read an analysis file and return its section text (with separator)."""
    text = path.read_text(encoding="utf-8").rstrip()
    # First line is typically "# Análisis caso de uso JNNN — Name"; demote it
    # to level 2 so that ## becomes the section anchor in the compiled doc.
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        # Normalize: "Análisis caso de uso JNNN — Name" -> "[JNNN] — Name"
        # Robust extraction: find token starting with J and digits
        import re
        m = re.search(r"\bJ\d+\b", title)
        code = m.group(0) if m else ""
        # Strip the leading "Análisis caso de uso JNNN —" if present
        cleaned = re.sub(r"^An[aá]lisis caso de uso\s+J\d+\s*[—-]\s*", "", title)
        new_title = f"[{code}] — {cleaned}" if code else title
        lines = [f"## {new_title}", *lines[1:]]
        text = "\n".join(lines)
    return text + "\n\n---\n\n"


def _load_state() -> set[str]:
    if not COMPILED_STATE.exists():
        return set()
    try:
        data = json.loads(COMPILED_STATE.read_text(encoding="utf-8"))
        return set(data.get("compiled_files", []))
    except Exception:
        return set()


def _save_state(files: set[str]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    COMPILED_STATE.write_text(
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

    if not EXEC_ANALYSES_DIR.exists():
        print(f"ERROR: {EXEC_ANALYSES_DIR} does not exist.")
        return 1

    all_files = sorted(p.name for p in EXEC_ANALYSES_DIR.glob("*.md"))
    if not all_files:
        print(f"No analyses in {EXEC_ANALYSES_DIR}.")
        return 0

    if args.rebuild or not COMPILED_MD.exists():
        already = set()
        # Start fresh; will fully rewrite below.
        new_files = list(all_files)
    else:
        already = _load_state()
        new_files = [f for f in all_files if f not in already]

    if not new_files and not args.rebuild:
        print(f"Nothing new to compile. Compiled file: {COMPILED_MD}")
        return 0

    COMPILED_MD.parent.mkdir(parents=True, exist_ok=True)

    # Decision: rewrite the file each time we add anything. This keeps the
    # header (with up-to-date counts/timestamp) consistent. The state file
    # still lets us *know* what's new (logs/printing); the on-disk output
    # is the full corpus in deterministic order.
    final_files = sorted(set(already) | set(new_files))
    header = HEADER_TEMPLATE.format(
        timestamp=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        n_total=len(final_files),
    )
    body_parts = []
    for fn in final_files:
        body_parts.append(_section_for(EXEC_ANALYSES_DIR / fn))
    COMPILED_MD.write_text(header + "".join(body_parts), encoding="utf-8")

    _save_state(set(final_files))

    print(f"Compiled file: {COMPILED_MD}")
    print(f"  Total analyses included: {len(final_files)}")
    print(f"  New in this run:         {len(new_files)}")
    if new_files:
        for fn in new_files[:10]:
            print(f"    + {fn}")
        if len(new_files) > 10:
            print(f"    + ... (+{len(new_files)-10} more)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
