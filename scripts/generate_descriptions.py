#!/usr/bin/env python3
"""Generate rich SPANISH description fichas — self-contained & idempotent.

For every AI Feature in `processed/AI_Features_Data_Enriched.xlsx` that does not
yet have a ficha, this script:

  1. Opens its live `Detail Page` (SAP Discovery Center) with Playwright
     (reusing `fetch_sap_page.fetch`).
  2. Extracts pricing, support component, applicable industries and the tagline
     from that live page.
  3. Takes the **Spanish** Overview / Beneficios / Business Value from the
     enriched XLSX (produced in Stage 1 from the same Detail Page) — this
     guarantees the faithful sections are in Spanish.
  4. Composes the synthesized sections (¿Cómo funciona? / Casos de uso
     ilustrativos / ¿Cuándo usarla?) in Spanish, tailored per interaction
     modality (Joule, document, generation, summary, recommend, analysis).
  5. Writes `description/fichas/<id>_<slug>_description.md`.

Idempotent: skips any ficha that already exists. This protects both previously
generated fichas and any **hand-written** ones — UNLESS you pass `--force`,
which regenerates every ficha from this template (hand edits would be lost).

Usage:
  python scripts/generate_descriptions.py                 # only missing fichas
  python scripts/generate_descriptions.py --jobs 6        # parallel page fetch
  python scripts/generate_descriptions.py --only J313 J148
  python scripts/generate_descriptions.py --force         # regenerate all
"""
import argparse
import asyncio
import re
import sys

import openpyxl

from _paths import ENRICHED_FINAL, DESC_FICHAS_DIR
from fetch_sap_page import fetch

# --------------------------------------------------------------------------- #
# Loading metadata + Spanish enriched fields from the XLSX
# --------------------------------------------------------------------------- #

def slugify(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (t or "").lower()).strip("_")


def clean(s: str) -> str:
    return re.sub(r"[​­]", "", (s or "")).strip()


def load_rows() -> dict:
    wb = openpyxl.load_workbook(ENRICHED_FINAL, read_only=True, data_only=True)
    ws = wb["AI Features & Agents"]
    rows = ws.iter_rows(values_only=True)
    h = list(next(rows))
    ix = {c: h.index(c) for c in h}
    out = {}
    for r in rows:
        if not r or not r[ix["Identifier"]]:
            continue
        jid = str(r[ix["Identifier"]])
        out[jid] = dict(
            name=str(r[ix["Name"]] or ""),
            product=str(r[ix["Product"]] or ""),
            ai_type=str(r[ix.get("AI Type", -1)] or "") if "AI Type" in ix else "",
            commercial=str(r[ix["Commercial Type"]] or ""),
            availability=str(r[ix["Availability"]] or ""),
            detail=str(r[ix["Detail Page"]] or ""),
            overview_es=str(r[ix["Overview"]] or "") if "Overview" in ix else "",
            benefits_es=str(r[ix["Beneficios"]] or "") if "Beneficios" in ix else "",
            bvalue_es=str(r[ix["Business Value"]] or "") if "Business Value" in ix else "",
        )
    return out


# --------------------------------------------------------------------------- #
# Live Detail Page extraction (pricing / support / industries / tagline)
# --------------------------------------------------------------------------- #

def extract_live(raw: str) -> dict:
    lines = [l.rstrip() for l in (raw or "").splitlines()]
    nl = [l.strip() for l in lines if l.strip()]

    tagline = ""
    for i, s in enumerate(nl):
        if s == "AI Feature" and i > 0:
            tagline = nl[i - 1]
            break

    def after(label: str) -> str:
        for i, s in enumerate(nl):
            if s == label and i + 1 < len(nl):
                val = nl[i + 1]
                return "" if val == "Info Label" else val
        return ""

    support = after("Support Component")
    industries = after("Applicable Industries")
    pricing = ""
    for i, s in enumerate(nl):
        if s == "Message Strip Information" and i + 1 < len(nl):
            pricing = nl[i + 1]
            break
    return dict(tagline=tagline, support=support, industries=industries, pricing_note=pricing)


# --------------------------------------------------------------------------- #
# Spanish synthesized sections (per modality)
# --------------------------------------------------------------------------- #

def first_sentence(text: str) -> str:
    t = clean(text)
    m = re.search(r"^(.+?[.])(\s|$)", t)
    return (m.group(1) if m else t).strip()


def split_benefits(s: str) -> list:
    parts = re.split(r"\s*;\s*|\s*•\s*", clean(s))
    return [p.strip(" .").strip() for p in parts if p.strip(" .").strip()]


def modality(name: str, overview: str, tagline: str, product: str) -> str:
    t = f"{name} {overview} {tagline}".lower()
    p = product.lower()
    if "joule" in t or "joule" in p or "conversational" in t:
        return "joule"
    if "document" in t or "extraction" in t or "document ai" in p:
        return "document"
    if any(k in t for k in ["generation", "generate", "creation", "create", "builder", "authoring"]):
        return "generation"
    if any(k in t for k in ["summary", "summar", "explanation", "explain", "description generat"]):
        return "summary"
    if any(k in t for k in ["recommend", "proposal", "propose", "suggest", "advisor"]):
        return "recommend"
    if any(k in t for k in ["search", "insight", "analyz", "predict", "detection", "matching", "forecast"]):
        return "analysis"
    return "assist"


def how(m: str, product: str) -> str:
    joule_loc = "a Joule" if "joule" in product.lower() else f"a Joule dentro de {product}"
    if m == "joule":
        return (f"1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural {joule_loc}.\n"
                "2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del "
                "sistema y resuelve la tarea.\n"
                "3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar "
                "manualmente por las transacciones.")
    if m == "document":
        return ("1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal "
                "como un buzón de correo).\n"
                "2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo "
                "definido.\n"
                f"3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de {product}, "
                "reduciendo la captura y validación manual.")
    if m == "generation":
        return ("1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de "
                f"apoyo) lo que necesita en {product}.\n"
                "2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, "
                "aplicando las buenas prácticas del producto.\n"
                "3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo "
                "en lo específico en vez del trabajo repetitivo.")
    if m == "summary":
        return (f"1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en {product}.\n"
                "2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.\n"
                "3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede "
                "editarse y regenerarse si cambian los datos de origen.")
    if m == "recommend":
        return (f"1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en {product}.\n"
                "2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.\n"
                "3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin "
                "reemplazar el criterio del responsable.")
    if m == "analysis":
        return (f"1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en {product}.\n"
                "2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.\n"
                "3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos "
                "para informar una decisión de negocio.")
    return (f"1. **Disparador:** el usuario inicia la tarea dentro de {product}.\n"
            "2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.\n"
            "3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.")


def use_cases(m: str, product: str, ben: str) -> str:
    short = re.split(r"[;,.]", ben)[0].strip() if ben else ""
    benref = f" Apoya en: _{short}_." if short else ""
    frames = {
        "joule": [
            (f"Un usuario de negocio necesita resolver una tarea recurrente en {product} sin recordar la transacción exacta.",
             "le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús."),
            ("Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez.",
             "formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje."),
        ],
        "document": [
            (f"El equipo recibe un alto volumen de documentos que alimentan procesos en {product} y la captura manual es un cuello de botella.",
             "la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos."),
            ("Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite.",
             "el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción."),
        ],
        "generation": [
            (f"Un equipo necesita producir rápidamente un primer entregable en {product} para una demo o validación temprana.",
             "describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial."),
            ("Un perfil con poca experiencia técnica debe entregar un artefacto estándar.",
             "lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico."),
        ],
        "summary": [
            (f"Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en {product}.",
             "genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo."),
            ("Los datos de origen se actualizan poco antes de la entrega.",
             "regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes."),
        ],
        "recommend": [
            (f"Un especialista enfrenta una decisión repetitiva en {product} que consume tiempo de análisis manual.",
             "la IA le propone una opción con su justificación y el especialista solo valida y confirma."),
            ("Existe un backlog de casos pendientes que frena el proceso.",
             "las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano."),
        ],
        "analysis": [
            (f"Un usuario de negocio necesita entender una situación en {product} sin dominar las herramientas analíticas.",
             "ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir."),
            ("Surge una incidencia que requiere identificar rápidamente su causa o estado.",
             "el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva."),
        ],
        "assist": [
            (f"Un usuario realiza de forma recurrente una tarea manual en {product} con esfuerzo elevado.",
             "la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados."),
            ("El proceso depende de pasos repetitivos que ralentizan al equipo.",
             "la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor."),
        ],
    }
    f = frames[m]
    return (f"1. **Escenario:** {f[0][0]} **Cómo ayuda la feature:** {f[0][1]}{benref}\n"
            f"2. **Escenario:** {f[1][0]} **Cómo ayuda la feature:** {f[1][1]}")


def when(product: str, is_prem: bool) -> str:
    out = [f"- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de {product} "
           "y el trabajo manual es lento o propenso a errores."]
    if is_prem:
        out.append("- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); "
                   "conviene dimensionar el volumen esperado.")
    else:
        out.append(f"- Requiere el producto base **{product}** correctamente habilitado; suele incluirse sin costo "
                   "adicional de IA cuando aplica (ver *Datos clave*).")
    out.append("- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final "
               "permanece en el usuario.")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Ficha builder
# --------------------------------------------------------------------------- #

def build(jid: str, meta: dict, live: dict) -> str:
    name = clean(meta.get("name", "")) or jid
    product = clean(meta.get("product", "")) or "el producto SAP"
    comm = clean(meta.get("commercial", "")) or "Base"
    is_prem = comm.lower() == "premium"
    overview_es = clean(meta.get("overview_es", ""))
    benefits_es = split_benefits(meta.get("benefits_es", ""))
    bvalue_es = clean(meta.get("bvalue_es", ""))
    m = modality(name, overview_es, live.get("tagline", ""), product)

    L = [f"# {jid} — {name}\n"]
    L.append("## En una frase")
    L.append((first_sentence(overview_es) if overview_es else f"{name} en {product}.") + "\n")
    L.append("## ¿Qué es?")
    if overview_es:
        L.append(f"{overview_es} Es una capacidad de IA **{comm}** de {product}.\n")
    else:
        L.append("No documentado en la fuente oficial.\n")
    L.append("## Beneficios")
    if benefits_es:
        L += [f"- {b}" for b in benefits_es]
    else:
        L.append("- No documentados explícitamente en la fuente oficial.")
    L.append("")
    L.append("## Valor de negocio")
    if bvalue_es:
        L.append(bvalue_es)
    else:
        L.append("La fuente oficial no publica una métrica cuantitativa de valor de negocio para este caso; el valor "
                 "se expresa en los beneficios listados arriba.")
    L.append("")
    L.append("## ¿Cómo funciona?")
    L.append(how(m, product) + "\n")
    L.append("## Casos de uso (ilustrativos)")
    L.append("> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios "
             "oficiales de SAP.\n")
    L.append(use_cases(m, product, benefits_es[0] if benefits_es else "") + "\n")
    L.append("## ¿Cuándo usarla?")
    L.append(when(product, is_prem) + "\n")
    L.append("## Datos clave")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append(f"| Identificador | {jid} |")
    L.append(f"| Producto | {product} |")
    L.append(f"| Tipo de IA | {clean(meta.get('ai_type', '')) or 'AI Feature'} |")
    L.append(f"| Tipo comercial | {comm} |")
    L.append(f"| Disponibilidad | {clean(meta.get('availability', '')) or 'No documentada'} |")
    if clean(live.get("support", "")):
        L.append(f"| Support Component | {clean(live['support'])} |")
    L.append(f"| Industrias aplicables | {clean(live.get('industries', '')) or 'No documentadas'} |")
    if clean(live.get("pricing_note", "")):
        L.append(f"| Pricing | {clean(live['pricing_note'])} |")
    L.append(f"| Detail Page | {clean(meta.get('detail', ''))} |")
    L.append("")
    L.append("## Fuente")
    L.append(f"- SAP Discovery Center — Detail Page: {clean(meta.get('detail', ''))}")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #

async def fetch_live(url: str) -> dict:
    if not url:
        return {}
    try:
        raw = await fetch(url, None, 55000, 3500, False, False, None)
        return extract_live(raw)
    except Exception as e:
        print(f"    ! fetch failed ({e}); ficha will rely on enriched fields only", file=sys.stderr)
        return {}


async def run(pending: dict, jobs: int) -> int:
    sem = asyncio.Semaphore(max(1, jobs))
    wrote = 0

    async def work(jid: str, meta: dict):
        nonlocal wrote
        async with sem:
            live = await fetch_live(meta.get("detail", ""))
        slug = slugify(meta.get("name", ""))
        out = DESC_FICHAS_DIR / f"{jid.lower()}_{slug}_description.md"
        out.write_text(build(jid, meta, live), encoding="utf-8")
        wrote += 1
        print(f"  {jid}\t-> {out.name}")

    await asyncio.gather(*(work(jid, meta) for jid, meta in pending.items()))
    return wrote


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true", help="Regenerate every ficha (overwrites hand-written ones)")
    p.add_argument("--only", nargs="+", metavar="ID", help="Only these IDs (e.g. J313 J148)")
    p.add_argument("--jobs", type=int, default=6, help="Concurrent page fetches (default 6)")
    p.add_argument("--limit", type=int, default=0, help="Cap number of fichas (0 = no cap)")
    args = p.parse_args()

    if not ENRICHED_FINAL.exists():
        print(f"ERROR: {ENRICHED_FINAL} does not exist. Run merge_enriched_batches.py first.")
        return 1

    rows = load_rows()
    DESC_FICHAS_DIR.mkdir(parents=True, exist_ok=True)

    only = set(args.only) if args.only else None
    pending = {}
    for jid, meta in rows.items():
        if only and jid not in only:
            continue
        slug = slugify(meta.get("name", ""))
        out = DESC_FICHAS_DIR / f"{jid.lower()}_{slug}_description.md"
        if out.exists() and not args.force:
            continue
        pending[jid] = meta
        if args.limit and len(pending) >= args.limit:
            break

    if not pending:
        print("Nothing to generate — all fichas already exist (use --force to regenerate).")
        return 0

    print(f"Generating {len(pending)} fichas (jobs={args.jobs}, force={args.force}) ...")
    wrote = asyncio.run(run(pending, args.jobs))
    print(f"\nWritten: {wrote}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
