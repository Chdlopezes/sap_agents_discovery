# Análisis caso de uso J313 — Expiring Price Handling

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature J313. Los campos para los que la fuente oficial no provee información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/ — usada solo para metadatos del XLSX (Commercial Type, Product, Availability, Business Value, Beneficios). La página es un SPA JavaScript y no se renderizó su contenido completo.
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices — **fuente principal**, renderizada vía `scripts/fetch_sap_page.py` (Playwright + headless Chrome). Toda la información técnica de las secciones 1.4, 1.5, 1.6, 2 y 4 viene de esta página.
- Pricing Details (SAP Discovery Center): No aplica (Commercial Type = Base; caso no presente en la hoja Pricing Premium del XLSX).
- Fuentes complementarias oficiales SAP: Ninguna.

**Resumen del caso:** Capacidad de Joule (publicada bajo *Joule Capabilities → Joule in SAP S/4HANA Cloud Public Edition → Sales → Expiring Price Handling*) que habilita a los **pricing specialists** a gestionar la expiración de precios de manera más eficiente: consultar precios — almacenados como *condition records for pricing in sales* — que expirarán pronto, y renovarlos extendiendo períodos de validez y ajustando montos o ratios de condición.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** (campo `Product` del XLSX; confirmado por el breadcrumb de la página oficial: *Joule in SAP S/4HANA Cloud Public Edition → Sales*).
- **Joule** habilitado en el tenant (la página está bajo `help.sap.com/docs/joule/`).
- Componente funcional **SD – Pricing** operativo (la página opera sobre *condition records for pricing in sales*).
- Componentes funcionales adicionales: No documentado en la fuente oficial.

### 1.2 Licenciamiento / entitlement / paquete
- **Commercial Type:** Base.
- **Package:** No aplica un paquete Premium (caso no presente en la hoja Pricing Premium del XLSX).
- **AI Units / volúmenes / precio:** No aplica para caso Base.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
La fuente oficial nombra explícitamente:

- **Business catalog requerido (cita textual de la sección *Prerequisites* de la página):** *"To be able to use this capability, you must have the following business catalog assigned: Master Data - Prices (SAP_SD_BC_PRICE_MANAGE_MC)."*
- **Business role template que ya contiene ese catalog por defecto (cita textual):** *"Pricing Specialist (SAP_BR_PRICING_SPECIALIST) is one of the business role templates that contain this business catalog by default."*
- **App Fiori vinculada (destino de navegación desde Joule):** **Manage Prices - Sales** (la página dice: *"Open prices and job details in the Manage Prices - Sales app."*).

### 1.5 Datos maestros / transaccionales previos
La fuente oficial menciona los siguientes objetos sobre los que opera la capability:

- **Condition records de pricing en ventas** (el objeto sobre el que actúan las consultas y renovaciones).
- **Condition types** (la página da como ejemplos `PPR0` y `PCP0`).
- **Sales organizations** (ejemplo de la página: `1710`).
- Otros criterios de búsqueda explícitamente listados en la página: **Distribution channel, Product, Customer, Customer project ID**.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Availability:** Generally Available (campo `Availability` del XLSX).
- **Restricción de alcance documentada literalmente en la página:** *"Searching for prices whose validity ended in the past is not in the scope."* La capability **no opera sobre precios ya expirados**, solo sobre los que están por expirar.
- **Idioma del material de capacitación:** el video tutorial *"How to Renew Product Prices with Joule"* está etiquetado en la página como **"English Only"**.
- Edición / región / idioma productivo de Joule más allá del video: No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

La fuente oficial describe **un único prerrequisito de configuración** para habilitar el uso de la capability: la asignación del business catalog. El resto del contenido de la página describe el **uso conversacional** de la capability (Examples, Sample Requests, Check job progress), no pasos administrativos de activación.

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asignar el business catalog **`SAP_SD_BC_PRICE_MANAGE_MC`** (*Master Data - Prices*) a los usuarios objetivo. Alternativa: asignar directamente el business role template **`SAP_BR_PRICING_SPECIALIST`** (*Pricing Specialist*), que ya contiene este catalog por defecto. | Business Role / Business Catalog | Particular (por usuario o grupo de pricing specialists) | Consultor Seguridad SAP S/4HANA Cloud Public Edition | 2 |

> **Nota:** la fuente oficial no describe pasos administrativos adicionales. Toda la sección *Examples* enumera **prompts conversacionales** que el pricing specialist puede dirigir a Joule (mostrar precios por filtros, extender valid-to dates, ajustar amounts/ratios, verificar el job de renovación), pero esos son **uso funcional**, no configuración del consultor. La capability queda operativa una vez asignado el catalog/rol.

**Esfuerzo total estimado (activación estándar): ~2 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (ejecutar al menos un ciclo completo "Show expiring prices → Renew expiring prices → Check job progress", verificando que el job de mass creation se complete y que los nuevos condition records aparezcan correctamente en *Manage Prices - Sales*) | Consultor Funcional SD / Pricing | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración del business role / catalog) | Consultor Funcional SD / Pricing | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (incluyendo los prompts de ejemplo publicados por SAP: filtros por condition type / sales organization / fecha; extensión de validez por período o a fecha; ajustes proporcionales por porcentaje; verificación de job) | Consultor Funcional SD / Pricing | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- **Capacidades operativas expuestas por la fuente oficial** (qué puede pedirle el usuario a Joule, listado literal de la sección *Tasks*):
  - *"Fetch and display prices approaching expiration based on certain criteria."*
  - *"Extend valid-to dates by a period or to a specific date."*
  - *"Adjust condition amounts or ratios proportionally for the new validity period."*
  - *"Create new condition records for the price renewal in a single job."*
  - *"Track the job progress."*
  - *"Open prices and job details in the Manage Prices - Sales app."*

- **Orden de ejecución recomendado por la fuente:** la sección *Examples* indica *"The tasks should be performed sequentially"* — empezar siempre por *"Show expiring prices"* (marcado en la página como *"Always start from here"*), luego renovar, y finalmente verificar el job.

- **Definición oficial de "expiring price" (cita literal):** *"Expiring prices are the condition records that will expire soon based on the queried time frame but have not yet expired as of today. Additionally, an expiring price is one that does not have an immediate successor condition record, meaning its valid-to date is not followed by another validity period without gaps."*

- **Restricción de alcance (cita literal):** *"Searching for prices whose validity ended in the past is not in the scope."*

- **Idioma del material de capacitación oficial:** *"Video: How to Renew Product Prices with Joule (English Only)."*

- **Valor de negocio publicado por SAP** (campo `Business Value` del XLSX): Reducción estimada del 95% en el esfuerzo para detectar y actualizar precios próximos a expirar.

- **Beneficios** (campo `Beneficios` del XLSX): Ayuda a detectar precios próximos a vencer; facilita la creación o actualización de condiciones de precio; reduce esfuerzo manual en tareas de mantenimiento de pricing.

Otras consideraciones (idioma productivo de Joule más allá del video, restricciones regionales, fair-use, gobernanza de cambios masivos a precios, AI Units) **no están documentadas en la fuente oficial** y por lo tanto no se incluyen aquí.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- SAP Help Portal — Initial Setup (Joule Capabilities Guide → Sales → Expiring Price Handling): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices
- SAP Discovery Center — Pricing Details: No aplica (caso Base)

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 2 |
| Validación + documentación + KT | 11 |
| **Total** | **13** |
