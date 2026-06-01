# 1. CONTEXTO

Actúa como consultor SAP especializado en activación estándar de funcionalidades del catálogo **SAP Business AI** (Joule, SAP Document AI, SAP Analytics Cloud, SAP Signavio, SAP LeanIX, SAP Datasphere, SAP Build, SAP Integration Suite, SAP Cloud ALM y demás productos del AI Foundation Catalog).

# 2. OBJETO DE ANÁLISIS

Analiza el caso de uso **J606** — *Anomaly Detection*.

---

# 3. REGLAS DE FUENTES (CRÍTICAS — NO NEGOCIABLES)

## 3.1 Antes de escribir cualquier contenido

> **El XLSX `processed/AI_Features_Data_Enriched.xlsx` NO es la fuente del análisis. Es solo un *índice* (2 hojas) que apunta a las URLs oficiales de SAP. La fuente real son las páginas web a las que esas URLs llevan.** La URL del Initial Setup **no está en el XLSX**: se resuelve **en vivo** desde la sección *Resources* de la `Detail Page` (ver 3.1.1).

Localiza la fila del Identifier `J606` en estas hojas del XLSX y anota las URLs:

- **"AI Features & Agents"** — toma: `Name`, `Commercial Type`, `Product`, `Package`, `Detail Page` (**URL** — punto de partida para resolver el Initial Setup en vivo), `Overview` (resumen, usable para el bloque "Resumen del caso"), `Beneficios`, `Business Value`, `Availability`.
- **"Pricing Premium"** — solo si `Commercial Type = Premium`. URL = `Detail Page` + ancla a *Pricing Details*. Campo `Pricing Details` del XLSX = resumen del enriquecimiento; confírmalo en la página.

## 3.1.1 Flujo OBLIGATORIO para obtener la fuente

> Para **cómo abrir una URL en este entorno** (qué herramienta usar, cómo detectar SPAs JavaScript, cómo descubrir enlaces dentro de una página), consulta la sección **"Cómo abrir páginas web"** en `docs/AGENT_GUIDE.md` (path desde la raíz del repositorio). Aquí solo se describe **qué fuente buscar y en qué orden**.

> **REGLA BASE (no negociable): la URL del Initial Setup se resuelve EN VIVO desde la sección _Resources_ de la `Detail Page`.** El XLSX (2 hojas) **no** contiene esa URL ni los pasos de activación: solo aporta la `Detail Page` como punto de partida. Toda afirmación técnica del análisis (prerequisitos, business catalogs/roles, pasos, dificultad) debe provenir de una página oficial SAP **abierta en vivo**, nunca del XLSX.

Antes de escribir cualquier sección del análisis, obtén la fuente principal siguiendo este orden:

1. **Abre la `Detail Page` del XLSX y lista los enlaces de su sección _Resources_.** En este entorno:
   `python scripts/fetch_sap_page.py "<Detail Page>" --links`
   En la sección `## Links` del output, busca la línea con el texto **exacto** `Initial Setup - SAP Help Portal` y toma su URL. Esa es tu **fuente principal**. Ábrela:
   `python scripts/fetch_sap_page.py "<URL Initial Setup>"`
   Cita literalmente lo que leas (prerequisitos, business catalogs, roles, apps, pasos).

2. **Si _Resources_ NO tiene un enlace "Initial Setup - SAP Help Portal":** usa como sustituto el enlace **`AI Feature - SAP Help Portal`** de la misma sección _Resources_ (describe la capacidad y suele listar prerequisitos accionables y modo de uso). Ábrelo y trátalo como fuente principal. *(Esta vía fue validada y produce buenos resultados; úsala siempre que falte el Initial Setup.)*

3. **Si la página resuelta no carga** (muro de login "Don't have a SAP ID?", o "We couldn't find the version you were looking for", o contenido < ~200 caracteres), **reintenta antes de rendirte**:
   a. la MISMA URL variando el parámetro `?version=` (quítalo, o prueba una versión vigente);
   b. el enlace `AI Feature - SAP Help Portal` de _Resources_ como fuente complementaria.
   Si tras estos reintentos sigue sin cargar, **decláralo honestamente** en el encabezado y en la sección 2 ("el enlace aparece en _Resources_ pero no fue posible acceder tras reintentos") y aplica el bloque canónico de "No se registran pasos" (ver 3.5). **Nunca fabriques** pasos ni prerequisitos para rellenar.

4. **Si _Resources_ no trae "Initial Setup" ni "AI Feature":** sigue cualquier otro enlace de _Resources_ a `help.sap.com` claramente pertinente (Setup Guide, Configuration Guide, página del módulo/app). Si ninguno aplica, usa la `Detail Page` como única fuente y declara en la sección 2 el bloque canónico (ver 3.5, Caso 3).

5. **Valida antes de escribir:** no escribas ninguna sección hasta haber abierto al menos una URL oficial **en vivo**. El XLSX **no basta** (no contiene la fuente). Si todo el fetching falla, pide al usuario que pegue el contenido.

Toda URL que uses debe ser **publicada por SAP** en un dominio oficial. Si una URL no es claramente oficial de SAP, no la uses.

## 3.2 Fuentes permitidas (orden de prioridad)

### Fuente principal (cuando existe)

1. **La página de Initial Setup** resuelta en vivo desde la sección *Resources* de la `Detail Page` (paso 1 de 3.1.1; URL de SAP Help Portal). **Es la fuente principal del análisis.** La mayor parte del contenido — sobre todo prerequisitos técnicos, pasos de activación y dificultad — debe basarse en esta URL.

### Fuentes complementarias (siempre permitidas, oficiales de SAP)

Puedes usarlas para **complementar** la fuente principal cuando ésta omita un campo, o como **fuente sustituta** cuando no hay enlace de Initial Setup en *Resources*:

2. **El enlace `AI Feature - SAP Help Portal`** de la sección *Resources* de la `Detail Page`. Es el **sustituto principal** del Initial Setup cuando éste no existe en *Resources* (paso 2 de 3.1.1): describe la capacidad y suele listar prerequisitos accionables, business roles y modo de uso.
3. **La `Detail Page`** del ID (URL de SAP Discovery Center). Fuente natural para Overview, beneficios, valor de negocio, disponibilidad (GA / wave), `Commercial Type`, `Product`, `Package`.
4. **La sección `Pricing Details`** de la `Detail Page` (solo Premium). Fuente para licenciamiento, AI Units, paquete comercial.
5. **Otras páginas del SAP Help Portal** directamente relacionadas con este caso de uso (la página de la app Fiori involucrada, la página del módulo funcional, la página de Joule Integration, la página de IAM apps, etc.). Usa **solo** páginas que la fuente principal o la Detail Page enlacen, o cuyo tema sea inequívocamente el de este ID.
6. **SAP Road Map Explorer** — solo cuando la `Detail Page` o el Initial Setup lo referencie, para confirmar disponibilidad o wave.
7. **SAP AI Foundation Catalog** (Joule capability catalog) — para confirmar Base / Premium y disponibilidad del catálogo si la información en el XLSX está incompleta.

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

## 3.5 Resultado final del flujo de fuentes (resumen para la sección 2)

Después de ejecutar el flujo 3.1.1 (pasos A–E), una de estas situaciones será cierta. Actúa según la que corresponda:

### Caso 1 — Tienes contenido de una fuente oficial SAP (lo más común)

Usa ese contenido para describir prerequisitos, pasos de activación, apps, business roles, restricciones, etc. **Cita literalmente** los identificadores técnicos que la fuente nombre (catalogs, business roles, IAM apps, condition types, scope items, app Fiori). No agregues nada que la fuente no diga.

### Caso 2 — La fuente oficial existe pero NO describe pasos de activación

Algunas páginas oficiales (especialmente en `help.sap.com/docs/joule/capabilities-guide/...`) describen **cómo usar** la capability pero no enumeran pasos administrativos de activación. En ese caso:

- Si la fuente menciona al menos un **prerequisito accionable** (p. ej. "you must have the business catalog X assigned"), registra **ese único paso** en la sección 2 (asignar el catalog/rol).
- Si la fuente no menciona ningún prerequisito accionable, declara en la sección 2 el bloque canónico:

  > **No se registran pasos de activación.** La fuente oficial SAP consultada describe el uso de la capability pero no detalla un procedimiento de activación administrativo. El caso de uso aparece habilitado por defecto al cumplirse los prerequisitos del producto base.

### Caso 3 — Tras los pasos A–D no existe fuente oficial SAP que describa el caso

Declara en la sección 2:

> **No se registran pasos de activación.** Tras consultar el Initial Setup, la sección *Resources* de la Detail Page y SAP Help Portal restringido a dominios oficiales, no se encontró una página oficial SAP que describa un procedimiento de activación específico para este caso de uso. El caso puede venir habilitado por defecto al cumplirse los prerequisitos, o SAP no publica un setup explícito.

**No fabriques pasos genéricos** en ninguno de los tres casos. Aunque sospeches que aplica el procedimiento base de Joule sobre S/4HANA, no lo asumas si no hay fuente oficial que lo respalde para este ID.

**Importante:** registra en el bloque "Fuentes oficiales consultadas" del encabezado del análisis **todas** las URLs que efectivamente abriste y leíste (la fuente principal + cualquier fuente complementaria) — no solo el `Link` que está escrito en el XLSX.

---

# 4. ESTRUCTURA OBLIGATORIA DEL ANÁLISIS

Produce un único archivo Markdown con exactamente las siguientes secciones, en este orden.

## 4.1 Encabezado

```markdown
# Análisis caso de uso J606 — Anomaly Detection

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J606 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): <URL exacta del campo Detail Page del XLSX>
- Initial Setup (SAP Help Portal): <URL resuelta en vivo desde *Resources* (paso 1 de 3.1.1), o "No existe en la fuente oficial" si no hay enlace accesible>
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

Lista únicamente los pasos que **la fuente viva describe textualmente** (la página de Initial Setup —o su sustituto "AI Feature - SAP Help Portal"— que abriste según 3.1.1). El XLSX **no contiene pasos**: no inventes ni infieras; si la fuente viva no describe pasos, aplica el bloque canónico de 3.5.

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

## 5.1 Sobre la fuente

- ¿Resolví la URL del Initial Setup **en vivo** desde la sección *Resources* de la `Detail Page` (paso 1 de 3.1.1)? → Si solo usé el XLSX y nunca abrí ninguna URL en vivo, **el análisis no se puede guardar**. Vuelve al paso 1.
- ¿Si no había "Initial Setup" en *Resources*, usé el enlace **"AI Feature - SAP Help Portal"** como sustituto (paso 2), y reintenté variantes/versión antes de declarar algo inaccesible (paso 3)? → Si no, hazlo.
- ¿Cada afirmación técnica del análisis (nombre de business catalog, business role, IAM app, app Fiori, scope item, condition type, horas) está respaldada por algo que leí literalmente en la URL abierta? → Si una afirmación no está respaldada, elimínala o reemplázala por la frase canónica correspondiente.
- ¿Las URLs listadas en "Fuentes oficiales consultadas" y "Referencias oficiales" son las que efectivamente abrí (no solo las que estaban en el XLSX)? → Si no, corrige.

## 5.2 Sobre el contenido

- ¿Hay una hora estimada sin que la fuente oficial sugiera complejidad? → Reemplaza por "No estimable sin información adicional".
- ¿Hay un nombre de app, scope item, business role o IAM app que NO esté en la fuente oficial citada? → Reemplaza por "No documentado en la fuente oficial".
- ¿Hay frases como "típicamente", "generalmente", "suele requerir", "[verificar en SAP Help]"? → Elimínalas o reemplázalas por la frase canónica correspondiente.
- ¿El resumen del caso parafrasea el Overview de la **fuente oficial abierta** (no el campo `Overview` del XLSX) o es coherente con ambos? → Si no, corrige.

## 5.3 Regla de oro

El objetivo de este análisis es ser **auditable**: cualquier persona debe poder abrir las URLs citadas en el archivo y encontrar literalmente cada afirmación. Si una afirmación no se puede verificar abriendo esas URLs, **no debe estar en el análisis**.
