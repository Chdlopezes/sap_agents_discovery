# SAP Business AI — Pipeline de Análisis de Esfuerzo

Pipeline reproducible que transforma el catálogo público de **SAP Business AI**
(features y agentes IA) en un corpus de **análisis de esfuerzo de activación**
en español, listo para usarse como contexto en un sistema RAG.

## Entrada

Un único archivo CSV en `inputs/AI Features Data.csv` exportado desde
**SAP Discovery Center**. Columnas mínimas: `Identifier`, `Name`,
`Commercial Type`, `Product`, `Detail Page`.

## Salida

- `processed/AI_Features_Data_Enriched.xlsx` — XLSX con 2 hojas
  (*AI Features & Agents*, *Pricing Premium*) enriquecido con `Overview`,
  `Beneficios`, `Business Value` y `Pricing Details`. (La información de
  Initial Setup ya no se pre-enriquece aquí: se resuelve en vivo al generar
  cada análisis.)
- `state/id_slug_map.json` — mapa `JNNN → slug` para uso externo.
- `executions/prompts/*.md` — un prompt por caso de uso.
- `executions/analyses/*.md` — un análisis estructurado por caso de uso.
- `executions/compiled/analyses_compiled.md` — corpus único, RAG-friendly.

## Ejecución (agentic, vía Claude Code)

Este proyecto está pensado para ser **ejecutado por un agente Claude Code**.
Con el repo abierto, basta con pedirle al agente:

> *"Corre el pipeline SAP Business AI"*

El agente lee [`CLAUDE.md`](CLAUDE.md), corre `python scripts/pipeline_status.py`
para ver qué falta, y ejecuta solo las etapas pendientes siguiendo
[`docs/AGENT_GUIDE.md`](docs/AGENT_GUIDE.md).

### Reanudable y idempotente

Toda etapa es reanudable: si te quedas sin tokens o algo falla, los
checkpoints quedan en disco (un XLSX por lote enriquecido, un `.md`
por análisis). Al reanudar, el agente detecta y procesa solo lo nuevo.

### Para correrlo en otro computador

1. Clona / copia el repo.
2. Instala dependencias: `pip install openpyxl`.
3. Pon tu `AI Features Data.csv` en `inputs/`.
4. Abre Claude Code en la carpeta del proyecto.
5. Dile al agente: *"Corre el pipeline SAP Business AI"*.

El agente hará todo lo demás. Si el repo ya viene con análisis previos
en `executions/analyses/`, se reaprovecharán: solo se procesarán los IDs
nuevos del CSV.

## Pipeline (5 etapas)

```
inputs/AI Features Data.csv
  ▼ Stage 1 (agente + WebFetch, lotes de 10)
enriched_data/batches/AI_Features_Data_lote_<a>_<b>_enriquecido.xlsx
  ▼ scripts/merge_enriched_batches.py
processed/AI_Features_Data_Enriched.xlsx
  ▼ scripts/build_id_slug_map.py
state/id_slug_map.json
  ▼ scripts/render_pending_prompts.py
executions/prompts/<id>_<slug>_analysis.prompt.md
  ▼ Stage 4 (agente escribe cada análisis)
executions/analyses/<id>_<slug>_analysis.md
  ▼ scripts/compile_analyses.py
executions/compiled/analyses_compiled.md   ← corpus RAG
```

## Scripts (todos en `scripts/`)

| Script                          | Qué hace                                                  |
|---------------------------------|-----------------------------------------------------------|
| `pipeline_status.py`            | Reporta pendientes en cada etapa.                         |
| `save_enriched_batch.py`        | Persiste un lote enriquecido como XLSX de 2 hojas.        |
| `merge_enriched_batches.py`     | Une todos los lotes en el XLSX final.                     |
| `build_id_slug_map.py`          | Genera el mapa `id → slug` desde el XLSX final.           |
| `render_pending_prompts.py`     | Renderiza prompts faltantes desde el XLSX final.          |
| `run_prompt.py`                 | Renderizado ad-hoc (CSV o `--code/--name`).               |
| `compile_analyses.py`           | Compila incremental el corpus RAG.                        |

## Prompts (en `prompt/`)

- `prompt_enriquecimiento_ia_csv.md` — instrucciones para Stage 1.
- `PROMPT_USO_IA_ESFUERZO.md` — plantilla para los prompts por caso.

## Estructura del repositorio

```
inputs/                          # AI Features Data.csv (entrada)
prompt/                          # Prompts del sistema
scripts/                         # Pipeline scripts (Python, idempotentes)
docs/                            # AGENT_GUIDE.md
enriched_data/batches/           # XLSX por lote (checkpoints)
processed/                       # XLSX final enriquecido
executions/prompts/              # Prompts renderizados
executions/analyses/             # Análisis escritos (Markdown ES)
executions/compiled/             # analyses_compiled.md (corpus RAG)
state/                           # id_slug_map.json, compiled_state.json
state/historical/                # Snapshots de referencia (tier2/3_context)
CLAUDE.md                        # Guía para el agente
```

## Convenciones de nombres

- Slug = `slugify(Name)`: lowercase + `[^a-z0-9]+` → `_` + strip `_`.
- Prompt:   `executions/prompts/<id_lower>_<slug>_analysis.prompt.md`
- Análisis: `executions/analyses/<id_lower>_<slug>_analysis.md`
- Lote enriched: `enriched_data/batches/AI_Features_Data_lote_<start>_<end>_enriquecido.xlsx`

## Licencia / origen de datos

Todo el contenido enriquecido proviene de **fuentes públicas de SAP**
(SAP Discovery Center, SAP Help Portal, SAP AI Foundation Catalog,
SAP Road Map Explorer). Los análisis marcan con `[verificar en SAP Help]`
cualquier valor que requiera validación oficial antes de uso productivo.
