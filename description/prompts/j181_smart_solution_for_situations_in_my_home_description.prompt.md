# Ficha descriptiva de AI Feature — J181 · Smart Solution for Situations in My Home

Eres un agente experto en SAP Business AI. Tu tarea es producir **una ficha
explicativa en español** que permita a cualquier lector entender, sin ambigüedad,
**qué hace** esta AI Feature, **cómo funciona** y **cómo se usaría en un escenario
real**.

## Caso a documentar

- **Identificador:** J181
- **Nombre:** Smart Solution for Situations in My Home
- **Producto:** SAP S/4HANA Cloud Public Edition
- **Tipo de IA:** AI Feature
- **Tipo comercial:** No disponible
- **Disponibilidad:** Beta
- **Detail Page (fuente principal):** https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/

## Fuente (obligatoria)

Funda la ficha en el **contenido vivo de la `Detail Page`** de SAP Discovery
Center indicada arriba. Ábrela y léela con:

```bash
python scripts/fetch_sap_page.py "https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/"
```

De esa página toma como mínimo: **Overview**, **Benefits**, **Business Value** y
la sección **Additional Information** (Support Component, industrias aplicables,
disponibilidad, líneas de negocio, etc.) cuando existan.

- Si la página no carga tras reintentos, decláralo honestamente en la ficha
  ("La Detail Page no fue accesible tras reintentos") y construye lo que puedas
  con la metadata del caso; **no inventes** capacidades que la página no afirma.

## Archivo de salida

Escribe la ficha en:

```
description/fichas/j181_smart_solution_for_situations_in_my_home_description.md
```

en **español**, con esta estructura (usa exactamente estos encabezados):

```markdown
# J181 — Smart Solution for Situations in My Home

## En una frase
(1–2 líneas: qué resuelve, para quién, con qué tecnología SAP.)

## ¿Qué es?
(Overview sintetizado desde la Detail Page: propósito, qué automatiza o asiste.)

## Beneficios
- (Beneficios operativos/funcionales tomados de la página, en viñetas.)

## Valor de negocio
(Business Value publicado por SAP: métricas o impacto declarado, sin exagerar.)

## ¿Cómo funciona?
(Explicación del flujo de uso de la capability: entradas → procesamiento IA →
salida/acción. Describe la interacción típica del usuario, p. ej. conversación
con Joule, extracción de un documento, recomendación, etc.)

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión;
> no son escenarios oficiales de SAP.

1. **Escenario:** … **Cómo ayuda la feature:** …
2. **Escenario:** … **Cómo ayuda la feature:** …

## ¿Cuándo usarla?
(En qué situaciones aporta más; y, si aplica, cuándo NO es la herramienta
adecuada o qué prerequisito de producto se necesita.)

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J181 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | No disponible |
| Disponibilidad | Beta |
| Support Component / Industrias | (de Additional Information, si existe) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/
```

## Reglas

1. **Español** en todo el contenido (los términos propios de SAP pueden quedar en
   su forma original: *Joule*, *business catalog*, *scope item*, etc.).
2. **No fabriques hechos oficiales.** El Overview, Beneficios y Business Value
   deben derivarse de la Detail Page. Si un dato no está, omítelo u dilo.
3. Los **ejemplos de casos de uso SÍ pueden ser inventados**, pero deben ir bajo
   "Casos de uso (ilustrativos)" y marcarse como tales. Deben ser plausibles y
   coherentes con lo que la feature realmente hace.
4. Redacta de forma **clara, ejecutiva y concreta**; evita relleno y promesas
   exageradas.
5. La ficha es **autocontenida**: alguien que no conoce el caso debe entenderlo
   solo con leerla.
