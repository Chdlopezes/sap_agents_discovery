# CLAUDE.md — Guía para agentes Claude Code en este proyecto

Eres un agente operando en este repositorio. Tu objetivo es ejecutar el
**pipeline SAP Business AI** descrito abajo. Lee siempre **antes de actuar**:

- Este archivo (vista general + decisiones de diseño).
- [`docs/AGENT_GUIDE.md`](docs/AGENT_GUIDE.md) (procedimiento paso a paso).

## Resumen del pipeline (5 etapas)

```
inputs/AI Features Data.csv
        │
        ▼ [Stage 1] Enrichment   (agente + WebFetch, por lotes)
enriched_data/batches/AI_Features_Data_lote_<a>_<b>_enriquecido.xlsx
        │
        ▼ scripts/merge_enriched_batches.py
processed/AI_Features_Data_Enriched.xlsx
        │
        ▼ scripts/build_id_slug_map.py
state/id_slug_map.json
        │
        ▼ scripts/render_pending_prompts.py
effort/prompts/<id>_<slug>_analysis.prompt.md
        │
        ▼ [Stage 4] Analysis      (agente, SAP knowledge, por archivo)
effort/analyses/<id>_<slug>_analysis.md
        │
        ▼ scripts/compile_analyses.py
effort/compiled/analyses_compiled.md   ← corpus RAG
```

## Reglas operativas (no negociables)

1. **Idempotencia**: cualquier etapa puede re-ejecutarse. Los scripts saltan
   trabajo ya hecho. No re-proceses un ID que ya esté enriquecido, ni
   re-escribas un análisis que ya exista.
2. **Estado en disco**: la "verdad" es el contenido de los directorios.
   Antes de cualquier acción significativa corre:
   `python scripts/pipeline_status.py`
3. **Reanudación**: si te interrumpen a mitad de la Stage 1 o 4, el
   trabajo ya guardado (XLSX por lote o `.md` por caso) está intacto en
   disco. Al reanudar, `pipeline_status.py` te dice qué falta.
4. **Sin fuentes externas no permitidas**: la Stage 1 usa **únicamente** la
   URL `Detail Page` del CSV (y su sección *Pricing Details* para los Premium)
   para generar las **2 hojas** del enriquecido. No uses Google, blogs, KBAs ni
   SAP Help directo. (La resolución del Initial Setup ocurre en la Stage 4, en
   vivo desde *Resources* — ver regla 7.) Reglas detalladas en [`prompt/prompt_enriquecimiento_ia_csv.md`](prompt/prompt_enriquecimiento_ia_csv.md).
5. **Lotes pequeños**: Stage 1 trabaja en lotes de **10 IDs** por defecto.
   Esto limita el uso de tokens y crea checkpoints frecuentes en disco.
6. **Nunca modifiques** `prompt/PROMPT_USO_IA_ESFUERZO.md` ni
   `prompt/prompt_enriquecimiento_ia_csv.md` para evadir las reglas (sí puedes
   reforzarlas para mejorar la calidad).
7. **Stage 4 — fuente en vivo, no el XLSX**: cada análisis se fundamenta en la
   página oficial abierta **en vivo**, resolviendo la URL desde la sección
   *Resources* de la `Detail Page`. **Abre y combina AMBAS páginas cuando
   existan** — `Initial Setup - SAP Help Portal` **y** `AI Feature - SAP Help
   Portal` son fuentes fundamentales (no una sustituto de la otra). El XLSX
   (2 hojas) **no** contiene datos de Initial Setup; solo aporta la `Detail Page`.
   Si la página no carga tras reintentos (versión/login), decláralo
   honestamente y usa el bloque canónico "No se registran pasos"; **no fabriques**.
   Detalle en [`docs/AGENT_GUIDE.md`](docs/AGENT_GUIDE.md) Stage 4b.

## Convenciones de nombres

- Slug = `slugify(Name)` = lowercase + `[^a-z0-9]+ → _` + strip `_`.
- Prompt:   `effort/prompts/<id_lower>_<slug>_analysis.prompt.md`
- Análisis: `effort/analyses/<id_lower>_<slug>_analysis.md`
- Batch enriched: `enriched_data/batches/AI_Features_Data_lote_<start>_<end>_enriquecido.xlsx`

## Estructura del repositorio

```
inputs/                  AI Features Data.csv  (entrada del usuario)
prompt/                  PROMPT_USO_IA_ESFUERZO.md, prompt_enriquecimiento_ia_csv.md
scripts/                 Pipeline scripts (Python, idempotentes)
docs/                    AGENT_GUIDE.md (procedimiento detallado)
enriched_data/batches/   XLSX por lote, generados por el agente
processed/               XLSX final enriquecido
effort/prompts/      Prompts renderizados por caso
effort/analyses/     Análisis escritos por caso (Markdown ES)
effort/compiled/     analyses_compiled.md (corpus RAG)
state/                   id_slug_map.json, compiled_state.json
```

## Cuándo usar herramientas

| Tarea                                  | Quién         | Cómo                                          |
|----------------------------------------|---------------|-----------------------------------------------|
| Detectar qué falta                     | Scripts       | `python scripts/pipeline_status.py`           |
| Extraer datos de SAP Discovery Center  | **Agente**    | `WebFetch`; si falla → `python scripts/fetch_sap_page.py <URL>` |
| Renderizar una URL SAP (SPA JS)        | Script        | `python scripts/fetch_sap_page.py <URL>` (Playwright + headless Chrome) |
| Guardar un lote enriquecido            | Helper script | `python scripts/save_enriched_batch.py --json` |
| Mergear lotes                          | Script        | `python scripts/merge_enriched_batches.py`    |
| Mapa id→slug                           | Script        | `python scripts/build_id_slug_map.py`         |
| Renderizar prompts                     | Script        | `python scripts/render_pending_prompts.py`    |
| Resolver fuente del análisis (en vivo) | **Agente**    | `python scripts/fetch_sap_page.py "<Detail Page>" --links` → abrir y combinar **ambos** enlaces de *Resources* cuando existan: **`Initial Setup - SAP Help Portal`** y **`AI Feature - SAP Help Portal`** (los dos son fundamentales). El XLSX no contiene esas URLs. |
| Escribir cada análisis                 | **Agente**    | `Write` un `.md` por caso siguiendo el prompt, **fundamentado en la fuente viva** (no en el XLSX) |
| Compilar corpus RAG                    | Script        | `python scripts/compile_analyses.py`          |

## Dependencias

- Python 3.10+
- `openpyxl` — para leer/escribir los XLSX del pipeline
- `playwright` + Chrome / Chromium — para renderizar páginas oficiales SAP (SPAs JavaScript que `WebFetch` no carga)

```bash
pip install openpyxl playwright
# Si el sistema no tiene Chrome:
playwright install chromium
```

## Si el usuario te dice "corre el pipeline"

1. `python scripts/pipeline_status.py` para ver qué falta.
2. Atiende solo lo pendiente. Si todo está en cero, recompila el corpus
   con `python scripts/compile_analyses.py` y reporta el resultado.
3. Sigue [`docs/AGENT_GUIDE.md`](docs/AGENT_GUIDE.md) para cada etapa.
