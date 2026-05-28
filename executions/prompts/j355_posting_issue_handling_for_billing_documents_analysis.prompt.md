# 1. CONTEXTO

Actúa como consultor SAP especializado en activación estándar de funcionalidades del catálogo **SAP Business AI** (Joule, SAP Document AI, SAP Analytics Cloud, SAP Signavio, SAP LeanIX, SAP Datasphere, SAP Build, SAP Integration Suite, SAP Cloud ALM y demás productos del AI Foundation Catalog).

# 2. OBJETO DE ANÁLISIS

Analiza el caso de uso **J355** — *Posting Issue Handling for Billing Documents*.

---

# 3. REGLAS DE FUENTES (CRÍTICAS — NO NEGOCIABLES)

## 3.1 Antes de escribir cualquier contenido

Abre el archivo `processed/AI_Features_Data_Enriched.xlsx` y localiza la fila correspondiente al **Identifier `J355`** en estas hojas:

- **"AI Features & Agents"** — campos: `Name`, `Commercial Type`, `Product`, `Package`, `Detail Page`, `Overview`, `Beneficios`, `Business Value`.
- **"Initial Setup"** — campos: `Prerequisitos`, `Procedimiento`, `Próximos Pasos`, `Dificultad estimada`, `Tipo`, `Link` (URL oficial de SAP Help Portal asociada a este ID).
- **"Pricing Premium"** — solo si `Commercial Type = Premium`. Campo: `Pricing Details`.

Esa fila del XLSX es tu **fuente principal de trabajo**. 

## 3.2 Fuentes permitidas (orden de prioridad)

### Fuente principal (cuando existe)

1. **El `Link` de la hoja "Initial Setup"** para este ID (URL de SAP Help Portal). **Es la fuente principal del análisis.** Cuando existe, la mayor parte del contenido — sobre todo prerequisitos técnicos, pasos de activación y dificultad — debe basarse en esta URL.

### Fuentes complementarias (siempre permitidas, oficiales de SAP)

Puedes usarlas para **complementar** la fuente principal cuando cubra un campo que el Link de Initial Setup omite, o como **fuente sustituta** cuando el Link no existe:

2. **La `Detail Page`** del ID (URL de SAP Discovery Center). Fuente natural para Overview, beneficios, valor de negocio, disponibilidad (GA / wave), `Commercial Type`, `Product`, `Package`.
3. **La sección `Pricing Details`** de la `Detail Page` (solo Premium). Fuente para licenciamiento, AI Units, paquete comercial.
4. **Otras páginas del SAP Help Portal** directamente relacionadas con este caso de uso (la página de la app Fiori involucrada, la página del módulo funcional, la página de Joule Integration, la página de IAM apps, etc.). Usa **solo** páginas que la fuente principal o la Detail Page enlacen, o cuyo tema sea inequívocamente el de este ID.
5. **SAP Road Map Explorer** — solo cuando la `Detail Page` o el Initial Setup lo referencie, para confirmar disponibilidad o wave.
6. **SAP AI Foundation Catalog** (Joule capability catalog) — para confirmar Base / Premium y disponibilidad del catálogo si la información en el XLSX está incompleta.

### Regla clave

Toda fuente que uses debe ser **publicada por SAP** en uno de sus dominios oficiales (`help.sap.com`, `discovery-center.cloud.sap`, `roadmap.sap.com`, `community.sap.com/topics/road-map-explorer`, páginas oficiales de producto en `sap.com`). Si una URL no es claramente oficial de SAP, **no la uses**.

## 3.3 Fuentes PROHIBIDAS

- **Tu conocimiento previo o entrenamiento**. Aunque "sepas" que un caso típico de Joule usa SAP Build Work Zone, NO lo incluyas a menos que UNA fuente oficial de SAP **lista en 3.2** lo mencione explícitamente para este caso.
- **Inferencia desde casos similares**. Cada ID es independiente. No copies pasos, scope items, IAM apps ni horas desde otros análisis ya escritos.
- **Fuentes no oficiales**: blogs (SAP Community blog posts incluidos), Medium, foros, Stack Overflow, SAP Notes y KBAs (acceso restringido del cliente), documentación de consultoras / integradores, Google, ChatGPT, etc.
- **Suposiciones plausibles**. Si ninguna fuente oficial menciona un scope item, NO escribas "[verificar en SAP Signavio Process Navigator]" — escribe "No documentado en la fuente oficial".

## 3.4 Qué hacer cuando la información NO existe en la fuente oficial

Para CADA campo del análisis donde la fuente oficial SAP no provea información explícita, debes elegir **exactamente una** de estas frases canónicas y usarla literalmente:

- **"No aplica"** — cuando el concepto no es relevante para este caso (p. ej. *Scope item* en un caso que no es S/4HANA).
- **"No existe en la fuente oficial"** — cuando el concepto sería relevante pero SAP no publica el dato.
- **"No documentado en la fuente oficial"** — cuando la fuente del ID existe pero omite ese campo específico.

**Nunca uses estas otras fórmulas** ni inventes datos:
- ❌ "[verificar en SAP Help]" — esto sugería que existía y solo faltaba validar; ya no lo usamos.
- ❌ "Típicamente requiere…" / "Suele incluir…" / "Generalmente…"
- ❌ Listas de "ejemplos plausibles".
- ❌ Horas estimadas sin base en la complejidad descrita por SAP.

## 3.5 Si el `Link` de Initial Setup no existe o está incompleto

El XLSX puede tener el campo `Link` vacío o con texto del tipo "No existe enlace de Initial Setup en la sección Resources". Esto sucede porque a veces el proceso de enriquecimiento no logra extraer la URL correctamente — **no significa necesariamente que SAP no publique información**.

Procede en este orden:

1. **Verifica primero la `Detail Page`** del ID y revisa si su sección *Resources* enlaza a alguna página de SAP Help Portal o documentación oficial. Si la encuentras, **úsala como fuente principal sustituta**.
2. **Busca en SAP Help Portal y SAP Discovery Center** otras páginas oficiales (ver lista 3.2 puntos 2–6) que cubran el caso de uso `J355` o el caso `Posting Issue Handling for Billing Documents` sobre el producto exacto del XLSX. Solo URLs claramente oficiales de SAP.
3. **Si tras agotar las fuentes oficiales no encuentras pasos de activación**, declara explícitamente en la sección 2:

   > **No se registran pasos de activación.** No se encontró fuente oficial SAP (Initial Setup, Detail Page Resources ni páginas relacionadas en SAP Help Portal) que describa un procedimiento de activación específico para este caso de uso. El caso puede venir habilitado por defecto al cumplirse los prerequisitos, o SAP no publica un setup explícito.

4. **No fabriques pasos genéricos.** Aunque sospeches que aplica el procedimiento base de Joule sobre S/4HANA, no lo asumas para este ID si no hay fuente oficial que lo respalde.

5. **Sección de prerequisitos:** combina lo que digan las fuentes oficiales disponibles (Detail Page + páginas relacionadas en SAP Help Portal). Para los campos que ninguna fuente oficial cubra, usa **"No documentado en la fuente oficial"**.

**Importante:** registra en el bloque "Fuentes oficiales consultadas" del encabezado del análisis **todas** las URLs que hayas usado (la fuente principal + cualquier fuente complementaria), no solo el `Link` del XLSX.

---

# 4. ESTRUCTURA OBLIGATORIA DEL ANÁLISIS

Produce un único archivo Markdown con exactamente las siguientes secciones, en este orden.

## 4.1 Encabezado

```markdown
# Análisis caso de uso J355 — Posting Issue Handling for Billing Documents

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J355 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): <URL exacta del campo Detail Page del XLSX>
- Initial Setup (SAP Help Portal): <URL exacta del campo Link de la hoja Initial Setup, o "No existe en la fuente oficial" si está vacío>
- Pricing Details (SAP Discovery Center): <URL Detail Page + "#pricing", solo si Commercial Type = Premium; "No aplica" en caso contrario>
- Fuentes complementarias oficiales SAP (si aplican): <una línea por cada URL adicional usada — SAP Help Portal, SAP Road Map Explorer, SAP AI Foundation Catalog, página oficial del producto. Si no usaste fuentes complementarias, omite esta línea o pon "Ninguna">

**Resumen del caso:** <Copia o parafrasea directamente el campo `Overview` del XLSX. Si está vacío, usa `Description`. Si ambos están vacíos: "No existe en la fuente oficial.">
```

## 4.2 Sección 1 — Prerequisitos para la activación

Una sub-sección por cada categoría. Para cada una, registra **solo** lo que aparezca explícitamente en las fuentes oficiales de este ID:

### 1.1 Producto / componente SAP requerido
- Toma el valor del campo `Product` del XLSX.
- Si la `Detail Page` o el `Initial Setup` mencionan componentes funcionales adicionales (p. ej. "FI-AA", "MM-PUR"), inclúyelos textualmente.
- Sin más.

### 1.2 Licenciamiento / entitlement / paquete
- `Commercial Type` (Base / Premium) del XLSX.
- Si es Premium: el campo `Package` del XLSX + el resumen del campo `Pricing Details` de la hoja Pricing Premium.
- Si es Base sin paquete específico: "No aplica un paquete Premium".
- **No** inventes AI Units, volúmenes ni precios que no aparezcan en `Pricing Details`.

### 1.3 Scope item relacionado
- Solo si la `Detail Page` o el `Initial Setup` mencionan un scope item por ID o por nombre.
- Caso contrario: **"No documentado en la fuente oficial"**.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Solo apps, servicios, IAM apps, communication arrangements, etc., **nombrados textualmente** por la fuente oficial.
- Si la fuente oficial dice "IAM app SAP Business AI - Smart Summarization (F7924_SUM_TRAN)", úsalo exacto.
- Si no nombra nada: **"No documentado en la fuente oficial"**.

### 1.5 Datos maestros / transaccionales previos
- Solo si la fuente los lista explícitamente.
- Caso contrario: **"No documentado en la fuente oficial"**.

### 1.6 Restricciones funcionales / técnicas / idioma
- Solo si la fuente lo describe (p. ej. "disponible solo en S/4HANA Cloud Private Edition", "idioma inglés", "restricción regional").
- Caso contrario: **"No documentado en la fuente oficial"**.

## 4.3 Sección 2 — Pasos de activación / configuración estándar

Lista únicamente los pasos que **el Link de Initial Setup describe textualmente** (o el campo `Procedimiento` del XLSX si resume el Link correctamente).

**Si la fuente oficial no describe pasos de activación**, escribe el bloque exacto siguiente y NO incluyas tabla:

> **No se registran pasos de activación.** La fuente oficial SAP para este caso de uso (`Link` de Initial Setup) no describe un procedimiento de activación específico, o no existe enlace de Initial Setup en la sección Resources de la Detail Page. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos, o SAP no publica pasos en este momento.

**Si sí hay pasos en la fuente oficial**, úsalos en esta tabla:

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | … | … | General / Particular (por …) | … | … |

Reglas estrictas de la tabla:
- **Actividad estándar**: paráfrasis directa del paso descrito en la fuente. Una fila por paso explícito.
- **Objeto de configuración**: el nombre exacto del objeto/app/IAM app/business role tal como aparece en la fuente. Si la fuente lo nombra "Maintain Business Roles", úsalo así.
- **Tipo de configuración**: "General" si aplica a todo el tenant; "Particular (por <dato>)" donde `<dato>` es el dato variable explicado por la fuente (p. ej. "Particular (por usuario)", "Particular (por tipo de documento)").
- **Consultor requerido**: rol genérico (Consultor Funcional X, Consultor BTP, Consultor Seguridad, etc.) derivado del área que la fuente menciona. No inventes especialidades que la fuente no sugiera.
- **Tiempo estimado**: estimación profesional basada en la complejidad descrita en la fuente. Si la fuente no permite estimar (p. ej. un solo paso sin detalle), escribe **"No estimable sin información adicional"** en esa celda.

## 4.4 Sección 3 — Pasos adicionales de validación

Estos pasos son parte estándar de cualquier entregable de activación y se incluyen siempre:

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | <mismo consultor de la sección 2, o "Consultor Funcional del producto base" si la sección 2 no aplica> | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | <mismo consultor> | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | <mismo consultor> | 3 |

Estos pasos sí se incluyen incluso cuando no hay pasos de activación en la sección 2 (la validación / documentación / KT siempre aplican al entregable de consultoría).

## 4.5 Sección 4 — Consideraciones especiales

Solo consideraciones que la **fuente oficial mencione explícitamente** sobre este ID:
- Idiomas soportados (si la fuente los lista por idioma).
- Restricción de edición (Public / Private), región o data residency (si la fuente lo describe).
- Notas de pricing / consumo de AI Units (de `Pricing Details`).
- Disponibilidad / roadmap (p. ej. "Generally Available", "promoción gratuita hasta X").

**Si la fuente no menciona consideraciones especiales**, escribe textualmente:
> **No se registran consideraciones especiales adicionales en la fuente oficial SAP.**

NO incluyas consideraciones genéricas sobre Joule, AI Units o fair-use a menos que la fuente de ESTE ID las mencione.

## 4.6 Referencias oficiales

Incluye **todas** las URLs oficiales de SAP que usaste, no solo las del XLSX:

```markdown
- SAP Discovery Center — Detail Page: <URL>
- SAP Help Portal — Initial Setup: <URL o "No existe en la fuente oficial">
- SAP Discovery Center — Pricing Details: <URL o "No aplica">
- <Una línea por cada fuente complementaria oficial SAP que hayas usado, con dominio claramente identificable (help.sap.com, discovery-center.cloud.sap, roadmap.sap.com, sap.com).>
```

## 4.7 Resumen ejecutivo de esfuerzo

**Si hay pasos en la sección 2 con horas estimadas**:

| Bloque | Horas |
|---|---|
| Activación / configuración | <suma horas sección 2; excluye filas "No estimable sin información adicional"> |
| Validación + documentación + KT | 11 |
| **Total** | **<suma>** |

Si alguna fila de la sección 2 dice "No estimable sin información adicional", agrega esta nota debajo de la tabla:
> **Nota:** El total de activación excluye <N> paso(s) que la fuente oficial no permite estimar con rigor.

**Si la sección 2 declaró "No se registran pasos de activación"**, escribe en su lugar:

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

# 5. VERIFICACIÓN ANTES DE GUARDAR

Antes de escribir el archivo `.md`, autorevisa el análisis y descarta cualquier frase que viole estas reglas:

- ¿Hay una hora estimada sin que la fuente oficial sugiera complejidad? → Reemplaza por "No estimable sin información adicional".
- ¿Hay un nombre de app, scope item, business role o IAM app que NO esté en la fuente oficial citada? → Reemplaza por "No documentado en la fuente oficial".
- ¿Hay frases como "típicamente", "generalmente", "suele requerir", "[verificar en SAP Help]"? → Elimínalas o reemplázalas por la frase canónica correspondiente.
- ¿Cada URL en "Fuentes oficiales consultadas" y en "Referencias oficiales" coincide con lo que está en el XLSX para este ID? → Si no, corrige.
- ¿El resumen del caso es paráfrasis del `Overview` del XLSX y no de tu conocimiento general? → Si no, corrige.

El objetivo de este análisis es ser **auditable**: cualquier persona debe poder abrir las URLs citadas y encontrar literalmente cada afirmación.
