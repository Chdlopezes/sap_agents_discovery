# Agent Guide — Pipeline SAP Business AI

Procedimiento paso a paso para operar este repositorio desde Claude Code.
Lee [`CLAUDE.md`](../CLAUDE.md) primero para la vista general y las reglas.

---

## Prerrequisitos del entorno

- Python 3.10+ con `openpyxl` y `playwright` instalados:
  ```bash
  pip install openpyxl playwright
  # Si el sistema no tiene Chrome:
  playwright install chromium
  ```
- El archivo `inputs/AI Features Data.csv` debe existir, con al menos las
  columnas `Identifier`, `Name`, `Detail Page`, `Commercial Type`.

Verifica con:
```bash
python scripts/pipeline_status.py
```

El comando reporta cuántos IDs hay y qué falta en cada etapa. Si todo está
en cero salvo *compile*, basta con compilar el corpus.

---

## Cómo abrir páginas web (Detail Page, Initial Setup, otras fuentes oficiales SAP)

El pipeline te pedirá repetidamente abrir URLs — principalmente del XLSX
(`Detail Page`, `Link` de Initial Setup) o enlaces dentro de la sección
*Resources* de una Detail Page. Sigue este flujo de fetching general,
independiente del caso de uso:

### 1) Intenta primero con `WebFetch`

```
WebFetch(url=<URL>, prompt="extrae el contenido relevante para …")
```

`WebFetch` baja el HTML, lo convierte a Markdown y le aplica un LLM ligero
con el prompt que le pasas. Funciona bien para páginas estáticas o
server-rendered, y en esas el output preserva enlaces como `[texto](url)`.

### 2) Si `WebFetch` no devuelve contenido útil, usa `scripts/fetch_sap_page.py`

Las páginas de `help.sap.com`, `discovery-center.cloud.sap` y similares son
**SPAs JavaScript**: `WebFetch` solo recibe el shell HTML (~900 bytes,
título `SAP Help Portal | SAP Online Help` y nada más) porque no ejecuta JS.

Cuando notes ese síntoma — output muy corto, "Loading…", o solo metadatos
genéricos — cambia a:

```bash
python scripts/fetch_sap_page.py "<URL>"
```

El helper usa Playwright + headless Chrome, espera a que la SPA renderice y
emite el `innerText` por stdout. Está restringido a dominios oficiales SAP
por defecto.

### 3) Para descubrir enlaces dentro de una página, añade `--links`

Cuando necesitas seguir un enlace mencionado dentro de una página
(p. ej. encontrar el enlace al *Initial Setup - SAP Help Portal* dentro de
la sección *Resources* de una Detail Page), el texto plano no basta porque
los `<a href>` quedan reducidos a su texto:

```bash
python scripts/fetch_sap_page.py "<URL>" --links
```

Output: tras el texto del cuerpo aparece una sección `## Links` con
`- [texto](url)` por cada `<a href>` de la página. **Tú decides qué etiqueta
buscar** leyendo el output (p. ej. "Initial Setup", "Setup Guide",
"Documentation", "Pricing Details", el nombre del módulo, etc.). No hay
código específico por etiqueta — la asociación texto↔URL queda visible en
el output y el agente la interpreta.

Si quieres acotar la salida a links que coincidan con una palabra:
```bash
python scripts/fetch_sap_page.py "<URL>" --links --filter "Setup"
```
(`--filter` es opcional, solo conveniencia para filtrar por substring del texto del enlace.)

### 4) Si todo falla

- Verifica que Playwright y Chrome estén instalados (`playwright install chromium`).
- Reporta al usuario que ni `WebFetch` ni `scripts/fetch_sap_page.py` lograron
  cargar la URL y pídele el contenido pegado.
- **No escribas el análisis sin tener la fuente abierta** — el XLSX es solo
  un índice; la fuente real son las URLs renderizadas. Recurrir a "lo que
  parece típico de Joule sobre S/4HANA" o frases plausibles está prohibido
  por las reglas del prompt template.

### Buenas prácticas

- WebFetch tiene cache de 15 minutos — repetir la misma URL es barato.
- `fetch_sap_page.py` arranca Chrome cada vez; agrúpalo si vas a abrir
  muchas URLs seguidas en un mismo lote.
- Los dominios oficiales aceptados son `help.sap.com`,
  `discovery-center.cloud.sap`, `roadmap.sap.com`, `community.sap.com`,
  `sap.com`. Para cualquier otro dominio el script pide `--allow-any-domain`
  explícito — esto es una salvaguarda contra usar fuentes no oficiales por
  accidente en el pipeline.

---

## Stage 1 — Enrichment (lotes de 10)

### Cuándo

Cuando `pipeline_status.py` reporta `pending enrichment > 0`.

### Cómo (para CADA lote)

1. **Selecciona el siguiente lote** de IDs pendientes ordenados como
   aparecen en `inputs/AI Features Data.csv` (1-indexed). Por defecto
   el tamaño del lote es **10**.

2. **Lee** [`prompt/prompt_enriquecimiento_ia_csv.md`](../prompt/prompt_enriquecimiento_ia_csv.md)
   y sigue sus reglas estrictamente. En particular:
   - Para **AI Features & Agents** usa SOLO la URL `Detail Page` del CSV.
   - Para **Pricing Premium** incluye solo IDs con `Commercial Type = Premium`
     y usa SOLO la sección *Pricing Details* de la misma `Detail Page`.
   - El enriquecimiento genera **2 hojas** (AI Features & Agents, Pricing
     Premium). La antigua hoja *Initial Setup* fue eliminada: ese contenido
     ahora se produce en vivo en la Stage 4b (desde *Resources* de la Detail
     Page), no se pre-enriquece aquí.

3. **Visita cada `Detail Page`** con `WebFetch`. Extrae el contenido
   relevante para las 2 hojas. Para campos que no aparecen, usa los
   textos estándar definidos en el prompt (no inventes datos).

4. **Compila el payload JSON** con la forma documentada en
   `scripts/save_enriched_batch.py`. Ejemplo mínimo:

   ```json
   {
     "start": 1,
     "end": 10,
     "ai_features_agents": [
       {
         "Name": "Back Order Processing",
         "AI Type": "AI Feature",
         "Commercial Type": "Base",
         "Product": "SAP S/4HANA Cloud Public Edition",
         "Description": "...",
         "Product Category": "Supply Chain Management",
         "Package": "",
         "Quick Filters": "Joule",
         "Availability": "Generally Available",
         "Identifier": "J597",
         "Detail Page": "https://discovery-center.cloud.sap/ai-feature/...",
         "Overview": "...",
         "Beneficios": "...",
         "Business Value": "..."
       }
     ],
     "pricing_premium": []
   }
   ```

5. **Guarda el XLSX** del lote con el helper:
   ```bash
   python scripts/save_enriched_batch.py --json /tmp/batch_1_10.json
   ```
   Salida: `enriched_data/batches/AI_Features_Data_lote_1_10_enriquecido.xlsx`.

6. **Repite** con el siguiente lote hasta que `pipeline_status.py` reporte
   `pending enrichment: 0`.

### Recuperación

Si te interrumpen a mitad del Stage 1, el último XLSX completo guardado en
`enriched_data/batches/` es el checkpoint. Al reanudar, vuelve a correr
`pipeline_status.py` y procesa solo los IDs aún pendientes.

---

## Stage 2 — Merge

Cuando hay batches sin mergear (o un batch nuevo), corre:
```bash
python scripts/merge_enriched_batches.py
```

Esto regenera `processed/AI_Features_Data_Enriched.xlsx` con las 2 hojas
unificadas y deduplicadas por `Identifier` (último batch gana en conflictos).

---

## Stage 3 — Mapa id→slug

```bash
python scripts/build_id_slug_map.py
```

Genera `state/id_slug_map.json` con `{ "JNNN": "slug_kebab_o_snake" }`
para cada caso de la hoja "AI Features & Agents" del enriquecido final.

---

## Stage 4a — Renderizar prompts pendientes

```bash
python scripts/render_pending_prompts.py
```

Lee el XLSX enriquecido, calcula el nombre del prompt esperado para cada ID
(`<id_lower>_<slug>_analysis.prompt.md`), y renderiza solo los que no existen.
Idempotente.

(También sigue funcionando `python scripts/run_prompt.py --csv <file> --skip-existing`
para casos puntuales.)

---

## Stage 4b — Escribir cada análisis pendiente

Para cada `executions/prompts/<id>_<slug>_analysis.prompt.md` sin su
`executions/analyses/<id>_<slug>_analysis.md` correspondiente:

1. **Lee el prompt** (`Read`).
2. **Resuelve la fuente EN VIVO** (el XLSX ya **no** incluye datos de Initial
   Setup; solo aporta la `Detail Page` como punto de partida). Procedimiento
   validado:
   - Abre la `Detail Page` y lista sus enlaces de *Resources*:
     `python scripts/fetch_sap_page.py "<Detail Page>" --links`
   - En la sección `## Links` identifica **ambos** enlaces (los que existan):
     **`Initial Setup - SAP Help Portal`** y **`AI Feature - SAP Help Portal`**.
   - **Abre y explora TODOS los que existan** (`fetch_sap_page.py "<URL>"`): los
     dos son **fuentes fundamentales**, no uno sustituto del otro. El *Initial
     Setup* aporta el procedimiento administrativo; el *AI Feature* describe la
     capacidad y suele traer prerequisitos/business catalogs/roles/apps igual de
     relevantes para la activación. **Combina la información de ambas.** Si solo
     existe uno, ése es la fuente principal.
   - **Si alguna página no carga** (login, "We couldn't find the version", < ~200
     chars): reintenta variando `?version=`. Si una carga y la otra no, usa la que
     cargó. Si **ninguna** carga tras reintentos, decláralo honestamente ("no fue
     posible acceder tras reintentos") y aplica el bloque canónico "No se
     registran pasos". **No fabriques** pasos.
   - El `Overview`/`Beneficios`/`Business Value` del XLSX (provienen de la
     Detail Page) sí sirven para el "Resumen del caso"; el `Pricing Details`
     se confirma en la Detail Page (#pricing) si es Premium.
3. **Escribe** el análisis siguiendo **exactamente** la estructura de la
   **Sección 4 del prompt renderizado** (encabezado con "Fuentes oficiales
   consultadas", secciones 1–4, Referencias oficiales y Resumen ejecutivo de
   esfuerzo). En "Fuentes oficiales consultadas" / "Referencias" lista **todas
   las URLs que realmente abriste** (Detail Page + Initial Setup o su sustituto
   "AI Feature - SAP Help Portal" + Pricing si Premium). Esquema:

   ```markdown
   # Análisis caso de uso JNNN — Name

   > Análisis construido únicamente a partir de las fuentes oficiales de SAP
   > abiertas en vivo. Campos sin dato: "No aplica" / "No existe en la fuente
   > oficial" / "No documentado en la fuente oficial". Sin conocimiento general
   > ni inferencia desde otros casos.

   **Resumen del caso:** <Overview de la fuente abierta / del XLSX>

   ---

   ## 1. Prerequisitos para la activación
   ### 1.1 Productos / componentes SAP requeridos
   ### 1.2 Licenciamiento / entitlement / paquete
   ### 1.3 Scope item relacionado
   ### 1.4 Aplicaciones / apps Fiori / servicios requeridos
   ### 1.5 Datos maestros / transaccionales previos
   ### 1.6 Restricciones funcionales / técnicas / idioma

   ## 2. Pasos de activación / configuración estándar
   | # | Actividad estándar | Objeto | Tipo | Consultor | Horas |

   ## 3. Pasos adicionales de validación
   | # | Actividad | Consultor | Horas |
   (siempre: Prueba unitaria, Documentación, Transferencia de conocimiento)

   ## 4. Consideraciones especiales (según guía SAP)

   ## Referencias oficiales
   - SAP Discovery Center — Detail Page: …
   - SAP Help Portal — Initial Setup: …

   ## Resumen ejecutivo de esfuerzo
   | Bloque | Horas |
   ```

4. **Para cualquier dato que la fuente viva no confirme, usa la frase
   canónica** que corresponda — `"No aplica"`, `"No existe en la fuente
   oficial"` o `"No documentado en la fuente oficial"` (ver sección 3.4 del
   prompt). **Nunca** uses `[verificar en SAP Help]`, "típicamente",
   "generalmente" ni inventes IDs de scope item, IAM apps, business roles ni
   horas sin base en la fuente abierta.

5. **Guarda** con `Write`. El nombre debe ser exactamente
   `<id_lower>_<slug>_analysis.md`.

### Throughput

Por presupuesto de tokens, escribe los análisis en lotes (p. ej. 5–10
por turno) y haz checkpoints en disco después de cada uno.

---

## Stage 5 — Compilar corpus RAG

Cuando `pipeline_status.py` reporta `pending compile > 0`:

```bash
python scripts/compile_analyses.py
```

- Es **incremental**: solo agrega los análisis nuevos al estado.
- Reescribe `executions/compiled/analyses_compiled.md` con un encabezado
  RAG-friendly y todos los análisis ordenados alfabéticamente por nombre
  de archivo, separados por `---` y con `## [JNNN] — Name` como anchor.
- Mantiene `state/compiled_state.json` con los archivos ya incluidos.

Para reconstruir desde cero (rara vez necesario):
```bash
python scripts/compile_analyses.py --rebuild
```

---

## Resolución de problemas

| Síntoma                                       | Acción                                           |
|-----------------------------------------------|--------------------------------------------------|
| `openpyxl not found`                          | `pip install openpyxl`                           |
| `pending enrichment > 0` pero no quieres re-procesar | Verifica que los IDs faltantes existan en el XLSX final; quizá hay typos en el CSV |
| Un análisis quedó incompleto                  | Bórralo manualmente y vuelve a correr Stage 4b   |
| Una `Detail Page` es inaccesible              | Usa el texto estándar del prompt de enriquecimiento ("La sección Pricing Details no contiene información de pricing explícita" o equivalente) |
| El compile pone secciones desordenadas        | El orden es alfabético por nombre de archivo. Renombra si necesitas otro orden. |

---

## Checklist de cierre

Antes de reportar "pipeline ejecutado":

1. `python scripts/pipeline_status.py` reporta 0 en todas las etapas.
2. `processed/AI_Features_Data_Enriched.xlsx` tiene las 2 hojas y filas == filas del CSV.
3. `executions/compiled/analyses_compiled.md` existe y su encabezado tiene
   la cuenta correcta.
4. `state/id_slug_map.json` tiene una entrada por cada ID del enriched.
