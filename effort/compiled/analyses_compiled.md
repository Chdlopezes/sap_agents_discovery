# SAP Business AI — Análisis de Esfuerzo de Activación (Corpus RAG)

> **Última actualización:** 2026-06-05T20:05:31+00:00
> **Análisis incluidos:** 123

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

## [J1003] — Allocation Run Results

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1003 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/58e5fdf9-b00a-414b-97ef-74c65c21b10b/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/viewing-business-data?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Funcionalidad de Joule para analistas de negocio y contadores de costos que permite consultar montos asignados entre objetos como centros de costo, objetos de rentabilidad o centros de beneficio, y navegar rápidamente al job y al reporte detallado de la corrida de asignación.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): This section describes how to integrate Joule with the technical product SAP S/4HANA Cloud Public Edition. These steps comprise the Joule-specific and product-specific prerequisites and depend on your initial system setup. For example, you must first set up the technical environment, such as the SAP Business Technology Platform (BTP) with the entitlements for Joule and SAP Build Work Zone, standard edition (foundation/standard plan). You are guided through the integration steps with instructions, for example, you run the Joule booster that - among other settings - enables the communication scenario SAP_COM_0882 (SAP Digital Assistant Services) in the background. To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. You fulfill the general Prerequisites for Customer Managed Provisioning for Joule. You have reviewed the Customer Managed Provisioning for Joule and have carried out the necessary steps. To integrate Joule with SAP S/4HANA Cloud Public Edition, you must carry out the following steps: To be able to view specific business data, you must have the required authorizations for the involved business objects.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Register the SAP S/4HANA Cloud Public Edition System | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Create SAP Build Work Zone Application and Instance | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/58e5fdf9-b00a-414b-97ef-74c65c21b10b/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/capabilities-guide/viewing-business-data?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J1047] — Sales Order Status Check

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1047 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8e12da05-b0e4-490f-9cf4-0cc2a9482f71/
- Initial Setup (SAP Help Portal — Integrating Joule with SAP S/4HANA Cloud Public Edition): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition
- AI Feature (SAP Help Portal — Sales Order Status Check): https://help.sap.com/docs/joule/capabilities-guide/sales-order-status-check?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule permite a los representantes de ventas comprobar si el cumplimiento de un pedido está en curso y detectar problemas que bloquean su finalización, consultando estado, causas y posibles acciones desde un flujo conversacional en SAP S/4HANA Cloud Public Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** con Joule.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- La fuente indica que el acceso a Joule en SAP S/4HANA Cloud Public Edition **puede requerir entitlement y autorización adicionales** (consultar al account executive).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, deben cumplirse los **Prerequisites generales de Joule** y ejecutarse la integración técnica de Joule con SAP S/4HANA Cloud Public Edition (ver sección 2).
- Según la página **AI Feature** oficial ("Sales Order Status Check"), el usuario debe tener asignados los **business catalogs**: **`SAP_SD_BC_SO_PROC_MC`** (Sales - Sales Order Processing) y **`SAP_SD_BC_SLS_ORD_TRACKING_PC`** (Sales - Sales Order Monitoring and Tracking).

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Cumplir los **Prerequisites generales de Joule**, confirmar el entitlement/autorización para Joule en S/4HANA Cloud Public Edition y **asignar a los usuarios los business catalogs** `SAP_SD_BC_SO_PROC_MC` y `SAP_SD_BC_SLS_ORD_TRACKING_PC` | Prerequisitos generales de Joule / business catalogs | Particular (por usuario / rol) | Consultor SAP BTP + Funcional S/4HANA | 3 |
| 2 | Configurar la confianza al **Identity Authentication Tenant** (Configure Trust to the Identity Authentication Tenant) | SAP Cloud Identity Services / Trust | General | Consultor SAP BTP / Identidad | 4 |
| 3 | Exponer el contenido del **SAP Fiori Launchpad** a SAP BTP y registrar el sistema S/4HANA Cloud Public Edition | SAP Fiori Launchpad / registro de sistema | General | Consultor SAP BTP + S/4HANA | 4 |
| 4 | Configurar el **Identity Provisioning Service** y mantener la **Custom Content Security Policy** | IPS / CSP | General | Consultor SAP BTP | 3 |
| 5 | **Habilitar el icono de Joule** en el SAP Fiori Launchpad para los usuarios | SAP Fiori Launchpad (Joule) | General | Consultor SAP BTP + Seguridad | 2 |

**Esfuerzo total estimado (activación / configuración): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (consultar estado y problemas de cumplimiento de pedidos vía Joule) | Consultor Funcional SAP S/4HANA (Ventas) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (Ventas) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (Ventas) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Los pasos de la sección 2 corresponden a la integración técnica de Joule con S/4HANA Cloud Public Edition descrita por la fuente; son comunes a las capacidades de Joule sobre este producto.
- El acceso puede requerir entitlement/autorización adicionales (consultar al account executive).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8e12da05-b0e4-490f-9cf4-0cc2a9482f71/
- SAP Help Portal — Initial Setup (Integrating Joule with SAP S/4HANA Cloud Public Edition): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition
- SAP Help Portal — AI Feature (Sales Order Status Check): https://help.sap.com/docs/joule/capabilities-guide/sales-order-status-check?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |

---

## [J108] — AI-Assisted Search

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J108 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- Initial Setup (SAP Help Portal — Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- AI Feature (SAP Help Portal — Natural Language Search): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/04170c64c1004fc58d7f235aea0e4970.html?locale=en-US&state=PRODUCTION&version=cloud
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

**Resumen del caso:** Habilita consultas de búsqueda en lenguaje natural directamente en SAP Datasphere (repository explorer, data builder, catalog y data marketplace). La búsqueda aumentada con IA interpreta solicitudes complejas y devuelve resultados sobre los objetos y artefactos del tenant.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): activación mediante **AI Units**; precio bajo solicitud (métrica Flat Fee). Se requieren AI Units para usar la oferta en el servicio cloud subyacente.

### 1.3 Scope item relacionado
- No aplica (SAP Datasphere no utiliza scope items de SAP S/4HANA).

- Según el Initial Setup oficial ("Enable SAP Business AI for SAP Datasphere"), para habilitar SAP Business AI se debe contar con un **rol global** que otorgue los privilegios requeridos; la fuente indica que el rol global **DW Administrator**, por ejemplo, otorga esos privilegios.
- SAP Business AI es un servicio gestionado por SAP; se habilita SAP Business AI y Joule para SAP Datasphere para integrar recomendaciones de contenido de IA.
- Según la página **AI Feature** oficial ("Natural Language Search"), para usar la búsqueda en lenguaje natural ésta debe estar habilitada en el tenant (ver *Enable SAP Business AI for SAP Datasphere*) y el usuario debe tener **un rol scoped y un rol global** a la vez:
  - **Rol scoped** con los privilegios *Data Warehouse General (-R------)* —acceder a SAP Datasphere— y *Spaces Files (-R------)* —acceder a objetos de un espacio.
  - **Rol global** con el privilegio *Data Warehouse AI Consumption (----E---)* —usar las funciones de SAP Business AI.
  - Las plantillas **DW Modeler** (scoped) y **DW AI Consumer** (global), aplicadas juntas, otorgan estos privilegios.
- La búsqueda en lenguaje natural está disponible en el **Repository Explorer**, la página de inicio del **Data Builder** y el **Source Browser** (según la página AI Feature).

### 1.5 Datos maestros / transaccionales previos
- Artefactos de datos del tenant (modelos, vistas, objetos, espacios) sobre los que realizar la búsqueda.

### 1.6 Restricciones funcionales / técnicas / idioma
- Según la página **AI Feature** oficial, la búsqueda en lenguaje natural está **soportada solo en inglés** (puede arrojar resultados utilizables en otros idiomas, sin garantía).
- El uso de lenguaje natural depende de la longitud de la cadena: con **una palabra** no se usa; con **dos palabras** se usa solo si la búsqueda estándar no devuelve resultados; con **tres o más palabras** se usa siempre.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asignar al usuario un **rol scoped** (*DW Modeler*: privilegios Data Warehouse General y Spaces Files) **y un rol global** (*DW AI Consumer*: privilegio Data Warehouse AI Consumption) que habiliten el uso de SAP Business AI | Roles scoped y globales / privilegios de SAP Datasphere | Particular (por usuario / rol) | Consultor Seguridad SAP Datasphere | 3 |
| 2 | **Habilitar SAP Business AI y Joule para SAP Datasphere** (Enable SAP Business AI for SAP Datasphere) | Configuración del tenant (System → Configuration) | General | Consultor SAP Datasphere | 3 |
| 3 | Confirmar el entitlement de **AI Units** para el tenant | AI Units | General | Consultor BTP / Licencias | 2 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (búsquedas en lenguaje natural sobre artefactos del tenant) | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura por **AI Units** (precio bajo solicitud, métrica Flat Fee), según *Pricing Details*.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- SAP Help Portal — Initial Setup (Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- SAP Help Portal — AI Feature (Natural Language Search): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/04170c64c1004fc58d7f235aea0e4970.html?locale=en-US&state=PRODUCTION&version=cloud
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J1104] — Processing of Payment Advices with SAP Document AI

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1104 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/11193ef55baa4904a5b25bd639e51a0f.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/2e825c652f9f4f0f899b80ac9dacbe28.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/#pricing

**Resumen del caso:** Processing of Payment Advices with SAP Document AI automatiza el procesamiento multilingüe de avisos de pago mediante extracción y lectura asistida por IA.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito. Al estar basado en SAP Document AI, pueden aplicar requisitos comerciales asociados a Document AI según la configuración requerida.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Manage Document AI Schema Registration Subscriptions For the set-up, for every SAP S/4HANA Cloud Public Edition tenant, one central tenant of SAP Document AI, Embedded Edition, can be integrated through scope item 7TC. For every SAP S/4HANA Cloud Public Edition tenant, a separate SAP Document AI tenant must be integrated. The integration includes one communication scenario for the UI integration for SAP Document AI FIORI applications into the SAP S/4HANA Cloud Public Edition launchpad and one communication scenario for the inbound and outbound API integration through technical user communication. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Cancel Payment Card Authorization in Open Items The Payment Advice Document Extraction (PAYMENT_ADVICE_STANDARD) schema must be activated in the Manage Document AI Schema Registration Subscriptions app. For more information, see PAYMENT_ADVICE_STANDARD and Manage Document AI Schema Registration Subscriptions.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Install Additional Software | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Create Sales Orders - AI-Assisted Extraction | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Create Correspondence | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Assign Open Items | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Create Outgoing Invoices | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Create Refunds for Digital Payments | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Review the extracted information and then choose Create. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~28 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/11193ef55baa4904a5b25bd639e51a0f.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/2e825c652f9f4f0f899b80ac9dacbe28.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 28 |
| Validación + documentación + KT | 11 |
| **Total** | **39** |

---

## [J1114] — Supplier Confirmation Mass Creation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1114 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b8dfd079-2d74-417a-ad38-8a5251110a4d/
- Initial Setup (SAP Help Portal): No accesible (el enlace aparece en *Resources* pero no fue posible acceder a su contenido tras reintentos).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite crear de forma masiva varias confirmaciones de proveedor mediante Joule en SAP S/4HANA Cloud Public Edition. El comprador puede ingresar varios pedidos de compra y apoyarse en Joule para acelerar la creación de confirmaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b8dfd079-2d74-417a-ad38-8a5251110a4d/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J112] — Process Analyzer‚ Text to Insight

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J112 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Process Analyzer, Text to Insight permite consultar datos de procesos mediante lenguaje natural y obtener insights inmediatos dentro de SAP Signavio Process Intelligence.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J1137] — Electronic Document Error Handling

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1137 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d755130d-328a-4e41-b5b8-b0f507ee396c/
- Initial Setup (SAP Help Portal): No accesible (no existe enlace 'Initial Setup' ni 'AI Feature' accesible en *Resources*).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ofrece explicaciones en lenguaje natural para errores técnicos o complejos de documentos electrónicos con Joule.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document and Reporting Compliance**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP DRC (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP DRC (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP DRC (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d755130d-328a-4e41-b5b8-b0f507ee396c/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J1143] — BPMN Simulation Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1143 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-modeler/user-guide/using-ai-assisted-bpmn-simulation-insights?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/#pricing

**Resumen del caso:** Feature de SAP Signavio que integra simulaciones BPMN directamente en diagramas de proceso y convierte métricas como costos, tiempos de ciclo y uso de recursos en insights impulsados por IA.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have an SAP Signavio Process Modeler license and write access to the workspace that stores the BPMN model. Your workspace administrator has Joule integrated with SAP Signavio solutions. For more information, see Integration with SAP Signavio Solutions. Your workspace administrator created an SAP for Me ticket with the BPI-SIG-PM-MOD-SIM label to request the AI capability to be enabled. Once enabled, your workspace administrator must activate this capability for the users. For more information, see Activate Embedded AI Capabilities and Assign Users. Access to these features depends on your license and access rights.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-modeler/user-guide/using-ai-assisted-bpmn-simulation-insights?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J114] — Generation of SAP Fiori Elements and SAPUI5 Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J114 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/08cc63b7-8fd7-4535-a9d6-f66a9030174c/
- Initial Setup (SAP Help Portal): No existe en la fuente oficial (la sección *Resources* de la Detail Page no incluye un enlace "Initial Setup - SAP Help Portal").
- AI Feature (SAP Help Portal — SAP Build Code, Generative AI-Powered Development / Joule Options for UI5 Applications): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/3ce576a7d4b64931b446607c1710f63d.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Project Accelerator simplifica el desarrollo convirtiendo requerimientos de negocio (texto, imágenes o ambos) en un proyecto full-stack con una aplicación SAP Fiori elements funcional. Se puede acceder desde el panel de SAP Fiori o mediante un comando en Joule.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Code** con **Joule** (desarrollo asistido por IA generativa).
- La fuente complementaria describe el uso de Joule en **SAP Business Application Studio** (accesible también desde VS Code).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (SAP Build Code no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente complementaria (página de AI Feature de SAP Build Code), el uso se realiza con **Joule** dentro del entorno de desarrollo (SAP Business Application Studio / VS Code), empleando comandos como **/ui5** para invocar funcionalidades de Joule en el desarrollo de aplicaciones UI5/Fiori elements.
- La fuente describe el **uso** de la capacidad, no un procedimiento administrativo de activación específico.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La sección *Resources* de la Detail Page no incluye un enlace "Initial Setup - SAP Help Portal", y la página oficial complementaria (SAP Build Code) describe el **uso** de la capacidad con Joule en el entorno de desarrollo, sin detallar un procedimiento administrativo de activación. El caso de uso queda disponible al disponer de SAP Build Code con Joule habilitado en SAP Business Application Studio; SAP no publica pasos de activación adicionales para esta capacidad.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (generar una app Fiori elements/SAPUI5 desde una descripción con Project Accelerator / comandos /ui5 en Joule) | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente complementaria describe comandos de Joule como **/ui5** y **/ui5-typescript** (p. ej. para crear una app SAPUI5 freestyle o migrar de JavaScript a TypeScript) dentro de SAP Business Application Studio.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/08cc63b7-8fd7-4535-a9d6-f66a9030174c/
- SAP Help Portal — Initial Setup: No existe en la fuente oficial
- SAP Help Portal — AI Feature (SAP Build Code, Generative AI-Powered Development / Joule Options for UI5 Applications): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/3ce576a7d4b64931b446607c1710f63d.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J115] — Generation of SAP Mobile Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J115 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code. Puede generar componentes a partir de lenguaje natural, incluyendo código, modelos de datos, servicios, lógica de negocio, datos de ejemplo y pruebas unitarias.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Code**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have created a global account in the SAP BTP cockpit. See Getting a Global Account. The correct way to subscribe to SAP Build Code is using the booster and not the manual setup. If you already have a subscription to one or more of the services included in SAP Build Code and you would like to upgrade to the SAP Build Code plan, see Changing Service Plans. Access your global account in the SAP BTP cockpit and choose Boosters from the navigation pane. This booster is relevant for the standard service plan. If you are working in the trial plan, you need to run a different booster. Make sure to select the booster relevant to the plan in which you want to work. This option is only available if you are working in the build-code or the build-default plan. See Application Plans.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Code | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 2 | Open the booster to see the overview, components, and additional resources. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 3 | Create a Project | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 4 | Select a section of code. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 5 | Open Joule () from the activity bar. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |

**Esfuerzo total estimado (activación / configuración): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 11 |
| **Total** | **31** |

---

## [J116] — Generation of SAP HANA Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J116 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código. La capacidad ayuda a crear modelos de datos, servicios, lógica de aplicación y pruebas desde lenguaje natural; además, incluye herramientas generativas para crear sentencias SQL desde prompts.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Code**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have created a global account in the SAP BTP cockpit. See Getting a Global Account. The correct way to subscribe to SAP Build Code is using the booster and not the manual setup. If you already have a subscription to one or more of the services included in SAP Build Code and you would like to upgrade to the SAP Build Code plan, see Changing Service Plans. Access your global account in the SAP BTP cockpit and choose Boosters from the navigation pane. This booster is relevant for the standard service plan. If you are working in the trial plan, you need to run a different booster. Make sure to select the booster relevant to the plan in which you want to work. This option is only available if you are working in the build-code or the build-default plan. See Application Plans.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Code | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 2 | Open the booster to see the overview, components, and additional resources. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 3 | Create a Project | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 4 | Select a section of code. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 5 | Open Joule () from the activity bar. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |

**Esfuerzo total estimado (activación / configuración): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 11 |
| **Total** | **31** |

---

## [J117] — Form Extension in Localization as a Self-Service

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J117 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/60a09f68f2444ceca31dcac2e7017945/cdaf20a1b93c429eb03d360b670dd17e.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/#pricing

**Resumen del caso:** Genera y actualiza automáticamente formularios localizados personalizados según requisitos de negocio, enlaza fuentes de datos y carga los formularios en SAP S/4HANA Cloud Public Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units. Precio bajo solicitud. AI Units requeridas para usar esta oferta de IA en el Cloud Service subyacente. Solo puede comprarse como parte del paquete Joule Premium for Financial Management y no está disponible por separado. Tiene prerequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: The administrator has assigned you the corresponding business role that has the authorization defined in business catalog Extensibility - Localization Extensibility (SAP_CORE_BC_LOC_EXT_PC) as described in Granting App Access to Your Business Users. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/60a09f68f2444ceca31dcac2e7017945/cdaf20a1b93c429eb03d360b670dd17e.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J1182] — Settlement Rule Proposal for Asset Capitalization

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1182 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/43cfa9f3-485c-4021-8dd1-e1349f471bea/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a6bcb3e6679b4a31a9441939ec9430db/0be222af7c8a40538506ecd66f1f5534.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Propone reglas de liquidación para la capitalización de activos en medidas de inversión. La funcionalidad asiste la creación de reglas completas y ayuda a determinar receptores de liquidación mediante IA generativa.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You may require additional authorizations to use this AI-assisted feature. Contact your account executive for more information. Setting Up the Connection to Intelligent Scenario Lifecycle Management Activating the Intelligent Scenario

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Maintain Instruction Profile | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Maintain the user instruction profile. | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Select the target investment measure in the app. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Review and edit proposal | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 5 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/43cfa9f3-485c-4021-8dd1-e1349f471bea/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a6bcb3e6679b4a31a9441939ec9430db/0be222af7c8a40538506ecd66f1f5534.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J1195] — SAP Joule for Developers‚ ABAP AI capabilities

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1195 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/795cf9fa-d0cc-42b0-a3d7-52e8067e847d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/subscribing-to-joule-for-developers-abap-ai-capabilities?version=s4_hana_cloud_pce
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule for Developers con capacidades ABAP AI apoya el desarrollo ABAP en SAP S/4HANA Cloud Private Edition, ayudando a desarrolladores con asistencia generativa dentro del ciclo de desarrollo.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Subscribing to SAP Joule for Developers, ABAP AI Capabilities Subscribing to SAP Joule for Developers, ABAP AI Capabilities Here's how you as an administrator can subscribe to SAP Joule for developers, ABAP AI capabilities. Please ensure that the following requirements are met before subscribing to SAP Joule for developers, ABAP AI capabilities: You have a subaccount in SAP BTP, Cloud Foundry environment. See Managing Subaccounts Using the Cockpit.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/795cf9fa-d0cc-42b0-a3d7-52e8067e847d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/subscribing-to-joule-for-developers-abap-ai-capabilities?version=s4_hana_cloud_pce
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J120] — Performance Indicators Recommender

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J120 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-performance-measures
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/#pricing

**Resumen del caso:** Ayuda a pasar del problema de negocio a un enfoque de medición recomendando KPIs y PPIs relevantes desde un repositorio amplio de indicadores de desempeño de procesos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. Pricing Details indica uso de AI Estimator para estimar AI Units y costos; se muestra activación mediante AI Units, pero el contenido accesible no dejó un bloque completo de cantidad/costo. Precio final sujeto a la estimación y condiciones comerciales aplicables.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: With SAP Signavio Process Insights' KPIs, you have the option to select Open KPI catalog to view detailed information about the KPI in a separate tab.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select the Process AI recommendation service in the top header. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 2 | Select the Find measures prompt. This becomes the prefix for your query. Then, use natural language to complete the query. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-performance-measures
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J121] — Process Recommender

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J121 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-model
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/#pricing

**Resumen del caso:** Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select the  Process AI recommendation service in the top header. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 2 | Select the Find process models prompt. This becomes the prefix for your query. Then, use natural language to complete the query. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 3 | Select View template, to preview the process model. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-model
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J127] — Joule with SAP Signavio solutions

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J127 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/
- Initial Setup (SAP Help Portal — Joule in SAP Signavio solutions): https://help.sap.com/docs/signavio-process-transformation-suite/joule-in-sap-signavio-solutions-dcd44974e9b24ca684923bc484d954c2/joule-in-sap-signavio-solutions
- AI Feature (SAP Help Portal — Joule in SAP Signavio Process Transformation Suite): https://help.sap.com/docs/joule/capabilities-guide/joule-in-sap-signavio-process-transformation-suite?ai=true
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural con Joule.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions** (SAP Signavio Process Transformation Suite).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base** (clasificación del XLSX).
- La fuente indica que el acceso a Joule en Signavio **puede requerir entitlement y autorización adicionales** (consultar al account executive) y describe modalidades **Base/Premium consumiendo AI Units**.
- Según la página **AI Feature** oficial, el usuario debe poseer los **derechos de acceso** correspondientes y las **licencias apropiadas de los productos SAP Signavio** implicados; el acceso a Joule puede requerir además la **compra del SKU de Joule Base o del SKU de AI** (consultar al account executive).

### 1.3 Scope item relacionado
- No aplica (SAP Signavio no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe **crear un user group en SAP Cloud Identity Services** y contar con un **rol de administrador en el tenant** conectado a Joule con SAP Signavio.
- La fuente remite al paso 8 del procedimiento **"Integration with SAP Signavio Solutions"**.
- Opcionalmente, para la capacidad de tipo informacional con document grounding, se debe **configurar Document Grounding** (Set Up Document Grounding).

### 1.5 Datos maestros / transaccionales previos
- Contenido de Signavio (diagramas de proceso, diccionario, documentos, métricas) sobre el que operar.

### 1.6 Restricciones funcionales / técnicas / idioma
- El acceso a Joule en SAP Signavio puede requerir entitlement/autorización adicionales.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar el entitlement/autorización para Joule en SAP Signavio (consultar al account executive) | Entitlement / autorización | General | Consultor SAP Signavio | 3 |
| 2 | Crear el user group en **SAP Cloud Identity Services** y asegurar el rol de administrador en el tenant conectado a Joule (procedimiento "Integration with SAP Signavio Solutions", paso 8) | SAP Cloud Identity Services / tenant | General | Consultor SAP Signavio + BTP/Identidad | 4 |
| 3 | (Opcional) Configurar **Document Grounding** para la capacidad informacional que usa documentos propios | Document Grounding | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (consultas en lenguaje natural sobre diagramas, diccionario, documentos y métricas) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente describe variantes de capacidad **Base/Premium** con consumo de **AI Units**.
- El document grounding es opcional y sirve para añadir contexto propio a las respuestas de Joule.
- **Privacidad (página AI Feature):** no se debe introducir información personal o sensible en las consultas; si se introduce, se envía a un LLM para su procesamiento, que **no la almacena ni la usa para entrenamiento**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/
- SAP Help Portal — Initial Setup (Joule in SAP Signavio solutions): https://help.sap.com/docs/signavio-process-transformation-suite/joule-in-sap-signavio-solutions-dcd44974e9b24ca684923bc484d954c2/joule-in-sap-signavio-solutions
- SAP Help Portal — AI Feature (Joule in SAP Signavio Process Transformation Suite): https://help.sap.com/docs/joule/capabilities-guide/joule-in-sap-signavio-process-transformation-suite?ai=true
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J1284] — Document Data Extraction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1284 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/document-information-extraction-process-automation?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Extrae y procesa automáticamente información clave de PDFs e imágenes escaneadas usando IA, con o sin plantillas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Before you can work in SAP Build Process Automation, your SAP BTP account administrator must subscribe your SAP BTP subaccount to the SAP Build Process Automation application. Once subscribed, you can then configure additional product extensions. You have the following options for processing documents and extracting data: The document information extraction activities that were previously available in the PDF SDK have been deprecated. You need to replace these activities with similar activities from the Document Information Extraction SDK. You need to upgrade your project SDK and create a new template or schema to apply the new datatype structure.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Process Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Automation Capabilities | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Create a Business Site Using SAP Build Work Zone | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Configure Product Extensions | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Enable Notifications | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Integrate and Connect With Other Services | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Set Up Specific Use Cases | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/document-information-extraction-process-automation?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J1310] — Purchase Order Approvals Reminder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1310 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/generating-draft-reminder-emails-for-purchase-orders?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La capacidad ayuda a dar seguimiento a aprobaciones de órdenes de compra, identificar aprobadores y enviar recordatorios automatizados dentro del flujo de trabajo de compras.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): This section describes how to integrate Joule with the technical product SAP S/4HANA Cloud Public Edition. These steps comprise the Joule-specific and product-specific prerequisites and depend on your initial system setup. For example, you must first set up the technical environment, such as the SAP Business Technology Platform (BTP) with the entitlements for Joule and SAP Build Work Zone, standard edition (foundation/standard plan). You are guided through the integration steps with instructions, for example, you run the Joule booster that - among other settings - enables the communication scenario SAP_COM_0882 (SAP Digital Assistant Services) in the background. To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. You fulfill the general Prerequisites for Customer Managed Provisioning for Joule. You have reviewed the Customer Managed Provisioning for Joule and have carried out the necessary steps. To integrate Joule with SAP S/4HANA Cloud Public Edition, you must carry out the following steps: To be able to use this capability, you must have the following business catalogs assigned:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Register the SAP S/4HANA Cloud Public Edition System | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Create SAP Build Work Zone Application and Instance | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/capabilities-guide/generating-draft-reminder-emails-for-purchase-orders?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J135] — Conversational Planning

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J135 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/ae5ea1c82b2f48e2874f94783c6ea0ae.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/#pricing

**Resumen del caso:** Apoya a los planificadores en la creación de planes de transporte eficientes, incluyendo cadenas de acciones con múltiples instrucciones, mediante lenguaje natural en el transportation cockpit. El cockpit puede mostrar los requerimientos de planificación y las capacidades disponibles.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Esta oferta de IA solo puede adquirirse como parte del paquete 'Joule Premium for Supply Chain Management' y no está disponible por separado; los precios corresponden al paquete completo. Descripción del paquete: impulsa la agilidad de la cadena de suministro con IA premium que optimiza la programación de mantenimiento, mitiga disrupciones en planta y acelera la planificación de transporte, entre otros. Pricing del paquete por métrica 'Users': hasta 39 usuarios → 8 AI Units por métrica (tarifa EUR 7 por AI Unit; EUR 56 por métrica); hasta 200 → 7,2; hasta 550 → 6,5; hasta 1.000 → 5,7; desde 1.000 → 5. Incluye hasta 5.200 requests sin costo adicional; las solicitudes adicionales se cobran en bloques de 1.000 a 2 AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. You have configured the settings related to Intelligent Scenario Lifecycle Management (ISLM) that are required to use generative AI in Transportation Management (TM). First, you have requested an SAP Business Technology Platform (SAP BTP) service key for the intelligent scenario GENAI_TM_COPL_GPT40. Make sure you have noted down the name of the intelligent scenario, as you will need it later in the setup process. For more information, see Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP). Then you have performed the subsequent steps. For more information, see Customizing for Transportation Management under Basic Functions  Generative Artificial Intelligence. For more information about ISLM setup, see SAP Delivered Generative AI Scenarios. You have defined a generative AI profile of type Conversational Planning (conversational planning profile). In this profile, you have indicated one or several capabilities, that is, planning operations, that you would like to perform in the transportation cockpit using generative AI.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select all freight orders going to Spain | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Select the truck with the highest weight capacity | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Assign freight units to freight orders | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Assign freight units to trucks | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 5 | Assign trucks to freight orders | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 6 | Assign all freight units from New York to the small truck | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/ae5ea1c82b2f48e2874f94783c6ea0ae.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J1394] — Document Summary

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1394 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/111df0da-5177-4769-88ea-6a200ecae091/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/cloud-alm/applicationhelp/documents?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite resumir documentación de SAP Cloud ALM mediante capacidades de IA dentro de la aplicación de documentos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Cloud ALM**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Before you can use the AI-generated summary, you need to fulfill the following prerequisites. You have activated the AI feature. To do so: Log on to SAP for Me. For more information about access to SAP for Me, see Access and Authorizations. To activate a feature, select Request Activation next to the feature name. A pop-up titled Tenants appears. In the Tenants pop-up, select create a support case. An information pop-up appears.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Tricentis Test Automation for SAP | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |
| 2 | Open this video in a new window | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |
| 3 | Assign and unassign tags to documents on the object page. | Configuración de SAP Cloud ALM | Particular (por usuario / rol) | Consultor SAP Cloud ALM | 3 |
| 4 | Select a document that contains content. | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |
| 5 | Review the AI-generated summary and make manual changes if needed. | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |
| 6 | Select Apply to save the summary or Regenerate to create a new summary. | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Cloud ALM | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Cloud ALM | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Cloud ALM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/111df0da-5177-4769-88ea-6a200ecae091/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/cloud-alm/applicationhelp/documents?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J139] — Chart Summary

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J139 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/#pricing

**Resumen del caso:** Con el add-in de SAP Analytics Cloud para Microsoft PowerPoint, genera mediante IA generativa un resumen de texto de tres viñetas correspondiente a un gráfico de SAP Analytics Cloud. El resumen se inserta en la presentación como un comentario de texto editable y puede regenerarse bajo demanda para reflejar cambios en los valores de datos del gráfico asociado.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Se puede estimar la cantidad aproximada de AI Units y los costos asociados con el AI Estimator. Métrica: Requests (solicitudes); 0,06 AI Units por métrica; tarifa de EUR 7 por AI Unit (EUR 7 por métrica de referencia). Funcionalidad Premium facturada por consumo de AI Units.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J145] — Joule with SAP Build Work Zone

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J145 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/integration-with-joule
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo. También soporta acceso remoto mediante SAP Mobile Start o sitio móvil.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Work Zone**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Service Plans and Metering New subscriptions in SAP Build Work Zone, standard edition created after 20th March, 2025 are directly connected to Identity Authentication by default. If your subscription was created before this date, and you aren't connected to Identity Authentication, you need to switch over. For more information, see Switching to SAP Cloud Identity Services - Identity Authentication Joule requires a trust configuration of type OpenID Connect with your Identity Authentication tenant. SAML based trust is not supported. Before completing the Joule onboarding tasks, you'll need to ensure that you've met the required prerequisites for both SAP Build Work Zone, standard edition and for Joule. For a list of these prerequisites, please refer to: Prerequisites. To integrate Joule with both the standard and advanced editions, you can create an additional subscription to Joule in another subaccount and use one edition per subaccount.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Work Zone | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Work Zone | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Work Zone | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/integration-with-joule
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J146] — SAP Joule for Consultants

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J146 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/serviceguide/provisioning-sap-joule-for-consultants
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/serviceguide/sap-consulting-capability-for-joule
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/#pricing

**Resumen del caso:** SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud. Está orientado a consultores y equipos de implementación que necesitan acceso guiado a conocimiento, recomendaciones y soporte durante actividades de delivery.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Joule for Consultants**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **SAP Joule for Consultants**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details muestra métrica Requests / usuario-mes para SAP Joule for Consultants. La información visible indica 35 AI Units por métrica, tarifa de EUR 7 por AI Unit y costo por métrica de EUR 245, con cantidad incluida hasta 22.900 solicitudes.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): To start using SAP Joule for Consultants, you must have to following: The SAP AI Units must be assigned to the existing BTP global account where you intend to activate SAP Joule for Consultants. If you do not have a BTP global account, an account will be provisioned free of charge when purchasing SAP AI Units. This account provides sufficient capabilities to enable SAP Joule for Consultants. For a step-by-step guide on how to obtain a BTP global account, please refer to this Learning Journey. BTP global account administrator. SAP Cloud Identity Services administrator.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure the SAP BTP subaccount | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Create a subaccount and select region (i.e. EU10, EU11, US10 or AP10). | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 3 | Add the service plans: | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 4 | Establish Trust with SAP Cloud Identity Services | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 5 | Select the appropriate SAP Cloud Identity Services tenant and establish trust. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 6 | Subscribe to SAP Joule for Consultants | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 7 | Select the service SAP Consulting Capability and the plan standard-ga, click on Next. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 8 | Review the details and click Create. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP + Funcional | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP + Funcional | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/serviceguide/provisioning-sap-joule-for-consultants
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/serviceguide/sap-consulting-capability-for-joule
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J147] — Script Optimization

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J147 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/
- Initial Setup (SAP Help Portal — SAP Integration Suite, Artificial Intelligence): https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence
- AI Feature (SAP Help Portal — Optimize Groovy Scripts with AI): https://help.sap.com/docs/integration-suite/sap-integration-suite/optimize-groovy-scripts-ai
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP Integration Suite que ayuda a optimizar scripts personalizados (Groovy) con IA generativa. La Detail Page indica que la función está disponible como promoción gratuita por tiempo limitado.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Integration Suite** (capacidad Cloud Integration / scripts Groovy en integration flows).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- La Detail Page indica disponibilidad como **promoción gratuita por tiempo limitado** (sujeta a cambios).
- Según la página **AI Feature** oficial, las funciones de IA son accesibles **solo con las ediciones Premium y Enhanced**; se ofrecen como promoción gratuita **hasta septiembre de 2026** y posteriormente se comercializarán como AI features con **AI Units**. La función está disponible únicamente para el **service plan Premium** de SAP Integration Suite (SAP Note 2903776).

### 1.3 Scope item relacionado
- No aplica (SAP Integration Suite no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, un **administrador de tenant** activa y gestiona las features de IA; las features disponibles dependen de las **capabilities activadas** en el tenant.
- La fuente indica: "Upon activation, enhance your Groovy scripts using Generative AI" — es decir, tras **activar** la feature correspondiente, se puede optimizar/mejorar los scripts Groovy con IA generativa.
- Según la página **AI Feature** oficial, hay que asegurar que la feature **Script Optimization** esté habilitada en el tenant de SAP Integration Suite (ver *Artificial Intelligence*), y el usuario necesita el rol **`WebToolingWorkspace.Write`** para ejecutar la optimización.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- La Detail Page indica disponibilidad como promoción gratuita por tiempo limitado.
- Según la página **AI Feature** oficial: la optimización aplica **solo a scripts Groovy** (no JavaScript) y requiere el **editor de scripts en modo edición**; el botón *Optimize* puede tener **límite de uso por minuto** (rate limit) y un límite de tamaño de script. No se debe exponer información sensible en los scripts al usar *Optimize* (SAP Note 3542713).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asegurar un tenant de SAP Integration Suite con la **capability** correspondiente activada (Activating and Managing Capabilities) | Capabilities de SAP Integration Suite | General | Consultor SAP Integration Suite | 3 |
| 2 | Como **administrador de tenant**, activar la feature de IA para la optimización de scripts Groovy (Activating and Managing AI features) | Features de IA del tenant | General | Consultor SAP Integration Suite (administrador) | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (optimizar un script Groovy con IA) | Consultor SAP Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La Detail Page indica que la función está disponible como **promoción gratuita por tiempo limitado** (sujeta a cambios).
- El administrador del tenant gestiona las features de IA disponibles según las capabilities activadas.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/
- SAP Help Portal — Initial Setup (SAP Integration Suite — Artificial Intelligence): https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence
- SAP Help Portal — AI Feature (Optimize Groovy Scripts with AI): https://help.sap.com/docs/integration-suite/sap-integration-suite/optimize-groovy-scripts-ai
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J148] — Analytical Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J148 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/3d8afae09f1e48e79aac5b2102b2aa7b.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/fd25d2bb0fcb4450a1d2ea3c99728597.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP. Se integra con Just Ask de SAP Analytics Cloud dentro de SAP Business Data Cloud.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Index Your Data Using Just Ask and Test Your Integration The Joule 2506 release has introduced a change that affects Joule analytical insights. SAP Build Work Zone is now required as part of the integration to provision and sync users and roles from SAP Analytics Cloud to SAP Build Work Zone. If you have activated analytical insights in Joule before the 2506 release, you need to redo the setup using the instructions found in this guide. You must be an SAP BTP global account administrator to follow the steps in this guide and set up the capability. You must have appropriate Joule entitlements. You must have SAP Build Work Zone as part of the integration to provision and sync users and roles from SAP Analytics Cloud to SAP Build Work Zone. Joule works with data from models that are indexed by the just ask feature of SAP Analytics Cloud. This means that the administrator for just ask in the SAP Analytics Cloud tenant in your SAP BTP landscape determines what models, and therefore data, are available to Joule once the analytical insights capability is enabled.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable the Analytical Insights Capability in Joule | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Provision Users from SAP Analytics Cloud to SAP Build Work Zone Using IPS | Configuración de Joule | Particular (por usuario / rol) | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP + Funcional | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP + Funcional | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/3d8afae09f1e48e79aac5b2102b2aa7b.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/fd25d2bb0fcb4450a1d2ea3c99728597.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J151] — Master Data Governance

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J151 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/
- Initial Setup (SAP Help Portal — Master Data Governance): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/74e2472ca36440a1aaaa96393fbd33bf.html
- AI Feature (SAP Help Portal — MDG: Assisted Changes and Summarize Changes): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/27286d49774f4750b8365c8fd1a9d5fa.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/#pricing

**Resumen del caso:** Permite usar lenguaje natural para crear y actualizar solicitudes de cambio (change requests) de datos maestros dentro de los procesos de Master Data Governance en SAP S/4HANA Cloud Private Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition** con **Master Data Governance (MDG)**.
- La fuente de Initial Setup corresponde a la documentación de **Master Data Governance** (incluye "Configuration of MDG, Central Governance" y "Working with MDG, Central Governance").

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management** (esta oferta solo puede adquirirse como parte del paquete; los precios corresponden al paquete completo).
- Pricing del paquete (sección *Pricing Details* de la Detail Page), por métrica **Users**: hasta 39 → 8 AI Units por métrica (EUR 7 por AI Unit; EUR 56 por métrica); hasta 200 → 7,2; hasta 550 → 6,5; hasta 1.000 → 5,7; desde 1.000 → 5. Incluye hasta 5.200 requests sin costo adicional; las solicitudes adicionales se cobran en bloques de 1.000 a 2 AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la documentación de MDG enlazada como Initial Setup, el uso de change requests requiere los elementos de **MDG, Central Governance**: concepto de **Change Requests**, **Authorizations for Change Requests**, y los procesos de **creación y procesamiento de change requests** (Single-Object / Collective / Mass Change).
- Según la página **AI Feature** oficial ("Assisted Changes and Summarize Changes"), el prerrequisito directo es tener **una change request creada**. La función *Assisted Changes* usa el **campo de prompt en la pestaña Assisted Changes** de la change request para cambiar atributos de datos maestros de los modelos **MM (Material) y BP (Business Partner)**; la pestaña *Summaries* genera resúmenes en lenguaje natural de los cambios registrados.

### 1.5 Datos maestros / transaccionales previos
- Dominios de datos maestros gestionados por MDG (la documentación cubre MDG para Material, Business Partner, Supplier, Customer, FI Contract Account, Financials, Custom Objects).

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Private Edition** (la fuente es la documentación on-premise/Private Edition de MDG).
- Según la página **AI Feature** oficial, *Assisted Changes* y *Summarize Changes* están **disponibles solo en SAP S/4HANA Cloud Private Edition**, operan sobre los modelos **MM y BP**, y los **resúmenes solo pueden solicitarse para change requests no basados en edición** (*non-edition-based*). Su uso puede requerir **entitlement y autorización adicionales** (consultar al account executive).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asegurar que **MDG, Central Governance** esté configurado y operativo (sección "Configuration of MDG, Central Governance" de la documentación oficial) | Configuración de MDG, Central Governance | General | Consultor SAP MDG | 4 |
| 2 | Configurar los procesos de **Change Request** (concepto, tipos y procesamiento) para los dominios de datos maestros aplicables | Change Request / workflows MDG | General | Consultor SAP MDG | 4 |
| 3 | Definir las **autorizaciones para Change Requests** y asignar los roles a solicitantes y procesadores | Authorizations for Change Requests / roles | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

> **Nota de trazabilidad:** el enlace de Initial Setup de Resources apunta a la documentación de producto de **Master Data Governance** (configuración de MDG y procesos de change request); no describe un procedimiento discreto y separado de "activación de la capacidad de IA". Los pasos anteriores recogen los prerrequisitos de MDG que la fuente sí documenta. La habilitación específica de Joule/IA debe revalidarse en la guía de integración de Joule correspondiente.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (crear/actualizar change requests por lenguaje natural) | Consultor SAP MDG | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP MDG | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP MDG | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: solo adquirible dentro del paquete **Joule Premium for Financial Management**; el consumo se factura por **AI Units** (ver sección 1.2).
- Restringido a **SAP S/4HANA Cloud Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/
- SAP Help Portal — Initial Setup (Master Data Governance): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/74e2472ca36440a1aaaa96393fbd33bf.html
- SAP Help Portal — AI Feature (MDG: Assisted Changes and Summarize Changes): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/27286d49774f4750b8365c8fd1a9d5fa.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J162] — SAP Joule for Developers‚ ABAP AI capabilities

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J162 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/7f373198-9a41-4416-9eed-bdfca445d37a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/start
- AI Feature (SAP Help Portal): https://help.sap.com/docs/ABAP_Cloud/bbcee501b99848bdadecd4e290db3ae4/joule-for-developers-abap-ai-capabilities?version=sap_btp
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule for Developers con capacidades ABAP AI ayuda a acelerar el desarrollo ABAP en SAP BTP, ABAP environment mediante asistencia generativa para tareas de desarrollo.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP BTP‚ ABAP environment**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Getting Started (Administrators) Learn more how you can get SAP Joule for Developers, ABAP AI capabilities and which business roles are required. To leverage Joule's capabilities on-stack, you need to purchase an additional license: For SAP BTP ABAP environment and SAP S/4HANA Cloud Public Edition, see SAP Note 3571857 . For more information on how to integrate SAP Joule for Developers, ABAP AI capabilities into ABAP development tools for Eclipse, see Getting Started (Administrators).

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7f373198-9a41-4416-9eed-bdfca445d37a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/start
- SAP Help Portal — AI Feature: https://help.sap.com/docs/ABAP_Cloud/bbcee501b99848bdadecd4e290db3ae4/joule-for-developers-abap-ai-capabilities?version=sap_btp
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J1684] — Enterprise Architecture Decision Management

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1684 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/leanix/ea/ai-capabilities#prerequisites
- AI Feature (SAP Help Portal): https://help.sap.com/docs/leanix/ea/architecture-decisions
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Analiza y extrae datos relevantes para generar entradas de decisiones de arquitectura con el contexto e información que los stakeholders necesitan para aprobarlas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process. Duplicating an architecture decision helps you save time when you need to create similar decisions. You can reuse the structure and selected content instead of starting from scratch.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 2 | Open this video in a new window | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 3 | Create a target architecture diagram. Define relevant transformations. For details, see Target Architecture Diagrams. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 4 | Open the generated decision in draft state to review and adjust it as needed. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 5 | Review the decision content, including embedded diagrams and the current status. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 6 | Maintain a linear, sequential log of decisions that follows best practices. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 7 | Open the architecture decision. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |
| 8 | Select the version you want to display. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/leanix/ea/ai-capabilities#prerequisites
- SAP Help Portal — AI Feature: https://help.sap.com/docs/leanix/ea/architecture-decisions
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J169] — Sales Order Fulfillment Monitoring

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J169 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/perform-sales-order-fields-changes-and-resolve-fulfillment-issues
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/#pricing

**Resumen del caso:** La capacidad ayuda a los equipos de ventas a monitorear y resolver problemas de cumplimiento de pedidos mediante IA. Los pedidos se resumen a nivel de cabecera e ítem en lenguaje natural, se identifican problemas de fulfillment y se facilita la navegación hacia acciones correctivas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details indica que esta oferta requiere AI Units y solo puede adquirirse como parte del paquete Joule Premium for Financial Management; no está disponible por separado. La página muestra que el paquete está disponible mediante compra de AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your account executive for more information. You must have the SAP_BR_INTERNAL_SALES_REP business role assigned. You've enabled Intelligent Scenario Lifecycle Management (ISLM) by performing the following steps: Available Intelligent Scenarios You've implemented the SAP Note 3459573  under SAP S/4HANA Cloud Private Edition 2023. This allows you to perform sales order field changes and resolve fulfillment issues.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure an intelligent scenario. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Deploy the intelligent scenario. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Activate the deployment to consume the inference in your business application. You can use the following: | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/capabilities-guide/perform-sales-order-fields-changes-and-resolve-fulfillment-issues
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J178] — Inventory Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J178 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/inventory-builder
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/#pricing

**Resumen del caso:** SAP LeanIX Inventory Builder acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units Precio bajo solicitud AI Units requeridas para usar la oferta en el Cloud Service subyacente. Tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: The inventory builder is a premium AI feature. To use it in production workspaces, you must accept the AI terms and have AI units assigned to your tenant. In some test or demo workspaces, you may be able to try premium AI features without buying AI units. You have accepted the AI terms. You have purchased AI units and they are assigned to your tenant.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open this video in a new window | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |
| 2 | Review the proposed fact sheets and relations. While reviewing, you can make the following changes: | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/inventory-builder
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J180] — SAP HANA application migration

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J180 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/manually-migrate-xs-classic-application-to-sap-cap-and-sap-hana-cloud-a581b87f52d44d9d9e26b8005cd2ab68
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La función automatiza la migración de la capa de servicios SAP HANA XS/XSA hacia SAP CAP usando GenAI. Ayuda a convertir artefactos como XSJSLIB, XSODATA y XSJS en servicios modernos basados en CAP, alineados con la guía de desarrollo de SAP BTP.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP HANA Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You need to provide details of the source instance of SAP HANA on-premise instance which contains the XS advanced applications that you want to migrate. You need access to an SAP BTP sub account where an HTTP destination is defined for the source SAP HANA platform database, which contains the XS advanced applications that you want to migrate. For more information about configuring the required destination, see the steps below. You must have a subscription to SAP Business Application Studio (BAS) or SAP Build. Generative-AI tools are only available in SAP Build plans, which you need to migrate the service layer. To migrate an XS advanced application to SAP CAP, you need to perform the following steps: Connect SAP Cloud Connector to the SAP BTP account where the subscription to SAP Business Application Studio was created.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Cloud Connector and navigate to the correct sub account. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 2 | Add a service channel in the category On-premise to Cloud. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 3 | Configure the new On-premise to Cloud service channel as indicated below. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 4 | Configure the mapping between the internal and virtual (Cloud-side) hosts. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP HANA Cloud / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP HANA Cloud / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/manually-migrate-xs-classic-application-to-sap-cap-and-sap-hana-cloud-a581b87f52d44d9d9e26b8005cd2ab68
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J193] — UI Generation from Data

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J193 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/691b7e82-b4ee-41f2-aae3-43b5b81be6f6/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-apps/service-guide/generate-pages-using-ai?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite generar automáticamente páginas de aplicación a partir de entidades de datos ya integradas en un proyecto de SAP Build Apps, incluyendo operaciones CRUD como punto de partida.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Apps**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: The Enable Generative AI feature in the Lobby is switched on. To enable it, open the Lobby and select Control Tower  Tenant Configuration  Generative AI. When enabling the feature, you should accept the AI Usage Terms and Conditions. SAP BTP Authentication is enabled for your application and you have integrated a BTP Destination with the necessary data entities enabled. To learn more, see BTP Destinations

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select any data entity from the list and make sure it's enabled. | Configuración de SAP Build Apps | General | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/691b7e82-b4ee-41f2-aae3-43b5b81be6f6/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-apps/service-guide/generate-pages-using-ai?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J195] — Skill Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J195 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/00c231a71c6e4255afdacd31264418a6.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite extender Joule mediante skills ajustadas a necesidades de negocio. Las skills ejecutan operaciones predefinidas desde la interfaz conversacional de Joule y pueden integrarse con sistemas SAP y no SAP.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule Studio**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): An outline of the required subscriptions, licenses, and supported environments for both customers and partners using Joule Studio. Understanding these requirements ensures proper activation and use of SAP Build services and avoids compatibility issues. You have subscribed to SAP Build with the build-default service plan. An active user (developer) license is required to build, test, and deploy your custom Joule skills. For more information about the active user (developer) license for SAP Build, refer to SAP Build - Service Plans and Metering. You have any of the following Joule (base or higher) licenses: Joule Premium (SKU 8019164) (Includes AI Units) You have created a Joule Studio project.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Joule Studio | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 2 | Assign Users to Roles | Configuración de Joule Studio | Particular (por usuario / rol) | Consultor SAP Joule Studio / BTP | 3 |
| 3 | Create AI Capabilities | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 4 | Create an Action Project | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 5 | Activate the SAP Build Process Automation service, ensuring you select the build-default plan during setup. | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 6 | Create a Joule Studio Project | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 7 | Create a Joule Skill | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 8 | Add Activities to the Skill | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Joule Studio / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Joule Studio / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Joule Studio / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/00c231a71c6e4255afdacd31264418a6.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J202] — Content Creation and Summary

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J202 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/39ef0f64-fc3b-4420-92ee-fa5e052d486b/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/enabling-ai-features
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/how-to-use-ai-features-to-create-content
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ayuda a los usuarios de negocio de SAP Build Work Zone a crear y refinar contenido directamente en las workpages. Genera texto a partir de los prompts del usuario y resume contenido existente en formatos claros y concisos, integrando la asistencia de IA en el proceso de autoría para producir contenido de alta calidad con rapidez y mantener claridad entre páginas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Work Zone, advanced edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Service Plans and Metering Users are entitled to trigger up to 100,000 requests per calendar month across all SAP Build Work Zone, advanced edition instances within your SAP BTP global account. If the monthly requests exceed the limit in this global account, users will receive a message accordingly. The following month the quota will be reset, and users can continue to use the features. A document opens that includes terms and conditions for using the AI features. You need to accept or decline these terms. Before you can use AI features in your site, your administrator needs to have enabled them. For more information, see Enabling AI Features. You will be entitled to trigger a limited number of requests per calendar month. You have the option to accept the suggested text or you can discard it and try again.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Content list of the workspace from the workspace navigation bar and select the content item that you want to summarize. | Configuración de SAP Build Work Zone, advanced edition | General | Consultor SAP Build Work Zone | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Work Zone | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Work Zone | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Work Zone | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/39ef0f64-fc3b-4420-92ee-fa5e052d486b/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/enabling-ai-features
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/how-to-use-ai-features-to-create-content
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J212] — Process Analyzer‚ Text To Widget

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J212 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6d74c5e9-32c1-443c-be23-c7ebbc51d573/
- Initial Setup (SAP Help Portal): No accesible (el enlace aparece en *Resources* pero no fue posible acceder a su contenido tras reintentos).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Process Analyzer, Text to Widget permite crear widgets de dashboard a partir de consultas en lenguaje natural sobre datos de procesos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6d74c5e9-32c1-443c-be23-c7ebbc51d573/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J213] — Process Modeler

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J213 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-manager/user-guide/creating-bpmn-diagram-with-ai-assisted-process-modeling
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/#pricing

**Resumen del caso:** Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Diagram | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 2 | Open and Save Diagrams | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 3 | Add and Connect Elements | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 4 | Create Subprocesses | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 5 | Add Live Insights | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 6 | Add Links to SAP Signavio Process Insights Content | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-manager/user-guide/creating-bpmn-diagram-with-ai-assisted-process-modeling
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J214] — Database Administration

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J214 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/28b14ec8-e7be-4966-b33e-787021b2d05d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/3ec50257efcf49adacebd37babb7455c.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ofrece una nueva experiencia de usuario para administradores de base de datos potenciada por IA generativa: navegación por aplicaciones, conversión de lenguaje natural a SQL, resúmenes de alertas, aprovisionamiento de nuevas instancias y respuesta a preguntas sobre SAP HANA Cloud. Mejora la eficiencia operativa simplificando tareas complejas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP HANA Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Subscribing to the SAP HANA Cloud Administration Tools

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select your user icon and navigate to the Settings   Gen AI. | Configuración de SAP HANA Cloud | Particular (por usuario / rol) | Consultor SAP HANA Cloud / BTP | 3 |
| 2 | Enable the Joule with Limited Features and Gen AI toggle button | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 3 | Select the checkbox and select Accept to confirm. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP HANA Cloud / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP HANA Cloud / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/28b14ec8-e7be-4966-b33e-787021b2d05d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/3ec50257efcf49adacebd37babb7455c.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J224] — Content Generation for Catalog

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J224 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/1218c12e72c34cfd96293e566badb60c.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/#pricing

**Resumen del caso:** Ayuda a los data stewards a automatizar la generación de descripciones de negocio, términos de negocio y KPIs. Genera descripciones de negocio precisas, contextuales y completas para el activo (automatización de descripción de activos) y automatiza la clasificación de datos con etiquetas apropiadas derivadas de una lista jerárquica de tags (auto-tagging de activos).

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Se puede estimar la cantidad aproximada de AI Units y los costos asociados con el AI Estimator. Métrica: Requests (solicitudes); 0,29 AI Units por métrica; tarifa de EUR 7 por AI Unit (EUR 7 por métrica de referencia). Funcionalidad Premium facturada por consumo de AI Units.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You must complete the following Joule configuration procedures before activating Joule in SAP Datasphere. Users with a catalog administrator role can set up governance for assets using hierarchical tags and business glossaries, create KPIs to measure progress towards company goals, and publish assets, glossary terms, and KPIs to the catalog.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Your SAP Datasphere Service Instance in SAP BTP | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 2 | Configure the Size of Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 3 | Review and Manage Links to SAP Analytics Cloud and SAP Business Data Cloud Tenants | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 4 | Enable SAP HANA for SQL Data Warehousing on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 5 | Enable the SAP HANA Cloud Script Server on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 6 | Enable SAP Business AI for SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 7 | Enable Choropleth Layers for Geographical Visualizations | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 8 | Create OAuth2.0 Clients to Authenticate Against SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/1218c12e72c34cfd96293e566badb60c.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J225] — Enterprise Search

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J225 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e69295d106654923be99d4ff4e22d751.html?version=2508.500
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Búsqueda empresarial asistida por IA para SAP S/4HANA Cloud Public Edition que ayuda a los usuarios a encontrar datos relevantes de objetos de negocio mediante lenguaje natural desde SAP Fiori Launchpad.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): In the SAP Fiori launchpad, you can use the Enterprise Search feature to access business data efficiently. Depending on your business role, you see a list of business objects in the SAP Fiori launchpad search dropdown. This AI-assisted feature allows you to use natural language for searching business data. You can enter your search queries in natural language in the SAP Fiori launchpad search bar to find the information you need. To enable natural language search on the business objects, you must select the checkbox Enable AI Natural Language Search from the user profile settings [Goto User Profile  Settings  Search]. On selecting the checkbox, you can view the list of business objects that are configured for natural language search. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Install Additional Software | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e69295d106654923be99d4ff4e22d751.html?version=2508.500
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J226] — Smart Personalization of My Home

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J226 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/ea019a92ffc944d694851dc8ef704654.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4428a5a678bb407f8ad9f816c5ef589c.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/#pricing

**Resumen del caso:** Permite personalizar My Home en SAP S/4HANA Cloud Public Edition agregando insights cards mediante lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units. La oferta solo puede adquirirse como parte del paquete Joule Premium for Financial Management y no está disponible por separado; el paquete se adquiere mediante AI Units. Precio bajo solicitud; duración de contrato disponible bajo solicitud. Incluye prerrequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Administrators can enable the AI-assisted smart personalization of My Home for insights cards. Users can then enter their queries in natural language, and generate cards to add on the My Home in SAP S/4HANA Cloud Public Edition. their business users need to have the following business catalog assigned: SAP Business AI - User Interface Features - Smart Personalization – Display (SAP_CORE_BC_AIU_PER_PC) To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Select the role and go to the Business Catalogs tab. Ensure that the SAP_CORE_BC_AIU_PER_PC business catalog is assigned to the role. You can also click Add to search for it. Select it and click OK. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 5 | Maintain Bill of Material | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/ea019a92ffc944d694851dc8ef704654.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4428a5a678bb407f8ad9f816c5ef589c.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J227] — Error Explanation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J227 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/fbcd177357284dd5846347f04e1cea67.html?version=2602.500
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/34de9c8078094a908190e8e517b497a7.html?version=2602.00
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/#pricing

**Resumen del caso:** Genera descripciones y recomendaciones de resolución en lenguaje natural para errores en SAP S/4HANA Cloud Public Edition, ayudando a usuarios de distintos niveles de experiencia a entender el problema y continuar con el proceso.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Their business users need to have the following business catalog assigned: SAP Business AI - User Interface Features - Error Explanation - Display (SAP_CORE_BC_AIU_EXP_PC). To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows: By enabling this feature as an administrator, your business users can use generative AI to better understand issues they encounter when working on an object page in an SAP Fiori elements application. The AI-assisted error explanation also provides recommendations how to resolve these issues.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Select the role and go to the Business Catalogs tab. Ensure the SAP_CORE_BC_AIU_EXP_PC business catalog is assigned to the role, or click Add to search for it. Select it and click OK. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 5 | Set Up Your SAP S/4HANA Cloud Public Edition | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/fbcd177357284dd5846347f04e1cea67.html?version=2602.500
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/34de9c8078094a908190e8e517b497a7.html?version=2602.00
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J240] — In-house Service Initiation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J240 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/da1c8b47160a49a9820d3a63e1d97c06.html?version=2023.003
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/6942a37b4e9d4922adc293faf9b2b1ae.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/#pricing

**Resumen del caso:** Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos. El personal de reparación puede escanear o fotografiar documentos entrantes, como órdenes de compra; el sistema extrae datos relevantes y genera objetos de reparación asociados al servicio interno.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have performed the following steps to set up Intelligent Scenario Lifecycle Management: Configuring Business Roles for the Backend Configuring Business Roles for the Frontend Subscription Order Management Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. Once you have uploaded the document in the app, the following steps are performed by Document Information Extraction and In-House Service:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open a support ticket on the SAP Support Portal on component CA-S4H-BTPAI. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Review the results of the data extraction and data enrichment | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Create In-House Services and Add In-House Service Objects | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/da1c8b47160a49a9820d3a63e1d97c06.html?version=2023.003
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/6942a37b4e9d4922adc293faf9b2b1ae.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J241] — Maintenance Order Recommendation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J241 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/ff90ad7fa38a41a5a0f3a8faa21189f9.html?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/46af82ff1a4e47159f6cc00a06b94e91.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/#pricing

**Resumen del caso:** Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento. El planificador revisa las recomendaciones y selecciona una orden como referencia para crear una nueva orden de mantenimiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta se adquiere como parte de Joule Premium for Supply Chain Management y no por separado; el precio está disponible bajo solicitud. Las solicitudes adicionales se cobran en bloques de 1.000 por 2 AI Unit(s).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): As a system administrator, you need to perform some initial setup steps to enable the system to generate order recommendations. Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. Required Users and Authorizations Make sure that you have access to the Intelligent Scenario Management app (F4470), which is included in the business role template for the Analytics Specialist (SAP_BR_ANALYTICS_SPECIALIST). Personalized Recommendation is a service provided on SAP Business Technology Platform (SAP BTP). To use this service, contact SAP to request a service instance for Personalized Recommendation and to be onboarded to the intelligent scenario EAM_MAINTORD_RECMDN. Make sure you have noted down the name of the intelligent scenario, as you will need it later in the setup process. For more information, see Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP). Intelligent Scenario Lifecycle Management

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/ff90ad7fa38a41a5a0f3a8faa21189f9.html?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/46af82ff1a4e47159f6cc00a06b94e91.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J243] — API traffic prediction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J243 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f74d29df-40d1-498f-905d-90b7af685799/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-anomaly-detection?locale=en-US&state=PRODUCTION&version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/integration-suite/sap-integration-suite/predictions?locale=en-US&version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Funcionalidad de SAP Integration Suite que identifica tendencias en llamadas API y predice volúmenes futuros de tráfico para apoyar decisiones sobre capacidad, carga y estrategia API.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Integration Suite**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Subscribing to Notification Alerts The role collection APIPortal.Administrator must be assigned to you. The role collection APIManagement.SelfService.Administrator must be assigned to you to enable intelligent recommendations. Availability of this feature depends upon the SAP Integration Suite service plan that you use. For more information about different service plans and their supported feature set, see SAP Note 2903776.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate anomaly detection, intelligent recommendations, and API call prediction to enhance monitoring and forecasting capabilities for API calls. | Configuración de SAP Integration Suite | General | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f74d29df-40d1-498f-905d-90b7af685799/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-anomaly-detection?locale=en-US&state=PRODUCTION&version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/integration-suite/sap-integration-suite/predictions?locale=en-US&version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J247] — Journal Upload

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J247 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/cab97d8445064be79d3dcb868ccddf94.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/#pricing

**Resumen del caso:** Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition. Mediante una app SAP Fiori con capacidades de IA generativa, permite crear casos de carga, asociar una guía o política de contabilización en lenguaje natural, generar propuestas, validarlas y publicar asientos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta se adquiere como parte de Joule Premium for Financial Management y no por separado; el precio está disponible bajo solicitud. Las solicitudes adicionales se cobran en bloques de 1.000 por 2 AI Unit(s).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. Approval Workflow Integration: You can submit proposals for review, and designated approvers can verify and approve them before posting. To do this, you need to configure and manage approval workflows for journal upload cases. Setting Up the Connection to Intelligent Scenario Lifecycle Management Activating the Intelligent Scenario

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/cab97d8445064be79d3dcb868ccddf94.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J25] — Natural Language Query

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J25 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/61a8150e7e7944c4848c79d0ec032bd2.html?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/95dbe296761940c2bf4e18d54a20f3df.html?q=Exploring%20Your%20Data%20with%20Just%20Ask
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Natural Language Query es una función de IA generativa de SAP Analytics Cloud diseñada para democratizar la analítica, permitiendo solicitar datos mediante lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Searching Your Data Using Just Ask Exploring Your Data with Just Ask Use configuration settings to prepare and maintain Just Ask for your system users. A Just Ask administrator can control the following: There are two access points for Just Ask: Highlighting results for "Exploring Your Data with Just Ask"

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Sample Question entries to help end users to search their data. | Configuración de SAP Analytics Cloud | Particular (por usuario / rol) | Consultor SAP Analytics Cloud | 4 |
| 2 | Select the Edit Description icon above the search field. You can use this free text field to provide any general information about the system for your end users. | Configuración de SAP Analytics Cloud | Particular (por usuario / rol) | Consultor SAP Analytics Cloud | 4 |
| 3 | Select + Create label to create a new label entry. | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 4 | Add models to Just Ask | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 5 | Select  Sync model under Model Synchronization to complete any pending indexing for the model. | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 6 | Select the Settings tab to specify settings that can improve the accuracy of results returned when users query the model. | Configuración de SAP Analytics Cloud | Particular (por usuario / rol) | Consultor SAP Analytics Cloud | 4 |
| 7 | Create Synonyms for Dimensions or Measures | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 8 | Select the  (Edit) icon for the value you want to specify a synonym. | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/61a8150e7e7944c4848c79d0ec032bd2.html?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/95dbe296761940c2bf4e18d54a20f3df.html?q=Exploring%20Your%20Data%20with%20Just%20Ask
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J275] — AI-Assisted Commenting

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J275 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html?version=2025.15 — **el enlace versionado de *Resources* no resolvió ("We couldn't find the version"); la información de activación se tomó de la página AI Feature (ver línea siguiente).**
- AI Feature (SAP Help Portal — About AI-Assisted Features / AI-Assisted Commenting): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/00ca4ae380794468ba42ea46d10a4045.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/#pricing

**Resumen del caso:** Permite resumir comentarios existentes y reformular nuevos comentarios durante la autoría en SAP Analytics Cloud. Los analistas de negocio pueden resumir comentarios por celda y agregarlos, agilizando la generación y revisión de comentarios.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): el consumo se estima con el AI Estimator. Métrica **Requests**; **0,08 AI Units por request**; tarifa **EUR 7 por AI Unit**. Funcionalidad Premium facturada por consumo de AI Units.

### 1.3 Scope item relacionado
- No aplica (SAP Analytics Cloud no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la página **AI Feature** oficial ("About AI-Assisted Features"), el prerrequisito de activación es que un **administrador habilite las AI-Assisted Features para SAP Analytics Cloud** (ver *Enable AI-Assisted Features for SAP Analytics Cloud*); una vez habilitadas, las funciones aparecen integradas en la UI con indicadores visuales de contenido generado por IA.
- La capacidad opera **dentro de una story**: permite **resumir comentarios** sobre celdas de datos de tabla y dentro de un **comment widget**, tanto comentarios individuales como hilos, e incluso resumir comentarios de los descendientes de un nodo padre.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Según la página **AI Feature** oficial, la capacidad está disponible al trabajar en **stories** sobre comentarios de celdas de datos y del comment widget; requiere que las AI-Assisted Features estén habilitadas a nivel de tenant por un administrador.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Como **administrador**, habilitar las **AI-Assisted Features for SAP Analytics Cloud** en el tenant (procedimiento "Enable AI-Assisted Features for SAP Analytics Cloud") | Configuración del tenant (AI-Assisted Features) | General | Consultor SAP Analytics Cloud (administrador) | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

> Nota: la página AI Feature describe la **habilitación general** de las AI-Assisted Features de SAP Analytics Cloud (prerrequisito común a varias capacidades, incluida AI-Assisted Commenting); no detalla un procedimiento administrativo adicional específico solo para el comentado asistido.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura por **AI Units** según el modelo de *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.
- **Trazabilidad:** el enlace *versionado* de Initial Setup de Resources no resolvió; la información de activación se obtuvo de la **página AI Feature** oficial (accesible sin el parámetro de versión). El paso de habilitación de AI-Assisted Features es común a las capacidades de IA de SAP Analytics Cloud.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html?version=2025.15 (enlace versionado no accesible)
- SAP Help Portal — AI Feature (About AI-Assisted Features / AI-Assisted Commenting): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/00ca4ae380794468ba42ea46d10a4045.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J284] — Joule with SAP LeanIX

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J284 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): https://help.sap.com/docs/leanix/ea/joule-in-sap-leanix?locale=en-US&version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Search the inventory by fact sheet name, by applying filters, or using natural language. If you have the required permissions, you can create, update, or archive fact sheets without leaving the conversation. You can update the fact sheet name, description, lifecycle, and quality seal from the conversation. View fact sheet subscribers and their roles, and contact them directly from the conversation. Find users by name or email and see which fact sheets they’re subscribed to.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open a fact sheet to view related to-dos and their status. Create new to-dos without leaving the conversation. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Early Adopter Care (EAC)**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: https://help.sap.com/docs/leanix/ea/joule-in-sap-leanix?locale=en-US&version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J288] — Explanation of Fixed Asset Key Figures

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J288 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/3e5fcf2c768746049b5627bd5a42f720/cc4d416d14284e4abe6da0602d5b9966.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/#pricing

**Resumen del caso:** Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones en lenguaje natural de cálculos complejos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units. Precio bajo solicitud. AI Units requeridas para usar esta oferta de IA en el Cloud Service subyacente. Solo puede comprarse como parte del paquete Joule Premium for Financial Management y no está disponible por separado. Tiene prerequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. For more details about the AI features for Asset Accounting, in particular about the prerequisite authorizations, see the sections below. Authorization and more Information To enable users to access the AI feature, their business users need to have the following business catalog and IAM app assigned:: Business catalog: Asset Accounting – Explain Depreciation Key (AI) (SAP_FIN_BC_AA_AI_EXDEPRKEY_PC)

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Company Code | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Perform Legacy Data Transfer with Subsequent Balance Carryforward | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/3e5fcf2c768746049b5627bd5a42f720/cc4d416d14284e4abe6da0602d5b9966.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J28] — Goods Receipt Processing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J28 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/30d87325d6964ec18da12bd2fe927009.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/#pricing

**Resumen del caso:** Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA. Permite extraer información relevante de documentos de flete en papel, publicarla en el sistema y detectar anomalías que pueden retrasar la validación de freight orders.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units Precio bajo solicitud AI Units requeridas para usar la oferta en el Cloud Service subyacente. Tiene prerrequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. To onboard AI-Assisted Goods Receipt Analysis, you need to request an SAP Business Technology Platform (SAP BTP) service key with the intelligent scenario SCMTMS_DOX_DLV_NOTE for the delivery note and SCMTMS_TMDOX for the shipping document. For more information, see SAP Delivered Document Information Extraction Scenario and Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP).

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/30d87325d6964ec18da12bd2fe927009.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J294] — Joule with SAP Datasphere

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J294 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a2bc2dd0-4f0b-4d82-9f94-c3baaac6c83b/
- Initial Setup (SAP Help Portal): No accesible (no existe enlace 'Initial Setup' ni 'AI Feature' accesible en *Resources*).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Con Joule embebido en SAP Datasphere, los usuarios pueden realizar tareas informativas, navegacionales y transaccionales de forma fluida, incluyendo consultas sobre uso del producto y tareas comunes de administración.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Datasphere (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Early Adopter Care (EAC)**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a2bc2dd0-4f0b-4d82-9f94-c3baaac6c83b/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J298] — Creation of Fixed Asset Master Data

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J298 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/095edf47-cb36-48d8-bd8f-9a4bc9517991/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/004d0286cf1a40239e9a96417c4eba72.html?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La solución agiliza la creación de datos maestros de activos fijos a través de una interfaz conversacional (Joule).

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): This section describes how to integrate Joule with the technical product SAP S/4HANA Cloud Public Edition. These steps comprise the Joule-specific and product-specific prerequisites and depend on your initial system setup. For example, you must first set up the technical environment, such as the SAP Business Technology Platform (BTP) with the entitlements for Joule and SAP Build Work Zone, standard edition (foundation/standard plan). You are guided through the integration steps with instructions, for example, you run the Joule booster that - among other settings - enables the communication scenario SAP_COM_0882 (SAP Digital Assistant Services) in the background. To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. You fulfill the general Prerequisites for Customer Managed Provisioning for Joule. You have reviewed the Customer Managed Provisioning for Joule and have carried out the necessary steps. To integrate Joule with SAP S/4HANA Cloud Public Edition, you must carry out the following steps: To be able to use this capability, you must have the following business catalog assigned:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Register the SAP S/4HANA Cloud Public Edition System | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Create SAP Build Work Zone Application and Instance | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/095edf47-cb36-48d8-bd8f-9a4bc9517991/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/004d0286cf1a40239e9a96417c4eba72.html?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J305] — Electronic Document Error Handling

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J305 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/1a1b66db-191d-41e6-b01d-d69b4d645850/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/660d8a3f12c6412c938eb9ad84fd5f4d.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ofrece explicaciones fáciles de entender para errores de documentos electrónicos con Joule en SAP Document and Reporting Compliance.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document and Reporting Compliance**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: To utilize this feature effectively, you must have the following business catalog assigned: Business Catalog, Technical Name Joule: Sure! Could you provide the error message or the unique identifier (eDocSourceKey) of the electronic document you need help with? If you know the specific process ID (e.g., INEINV, INEWB), please share that too. This info will help me analyze the error accurately.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP DRC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP DRC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP DRC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1a1b66db-191d-41e6-b01d-d69b4d645850/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/660d8a3f12c6412c938eb9ad84fd5f4d.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J308] — Agent Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J308 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/
- Initial Setup (SAP Help Portal — Joule Studio, Initial Setup and Prerequisites): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- AI Feature (SAP Help Portal — Create a Joule Agent): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/193461e9d8494995bab4889b22afac93.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite construir agentes de Joule (en Joule Studio) para automatizar procesos de negocio complejos. Los agentes pueden ejecutar flujos adaptativos, razonar, planificar y coordinar procesos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule Studio** (parte de SAP Build).
- La fuente describe la integración de Joule Studio con **SAP Build**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- La fuente exige una licencia de Joule (base o superior): **Joule Base (SKU 8019544)** o **Joule Premium (SKU 8019164)** (este último incluye AI Units).
- No aplica un paquete Premium específico para este caso (clasificado como Base).

### 1.3 Scope item relacionado
- No aplica (el producto base — Joule Studio / SAP Build — no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial (Prerequisites for Customers):
  - Suscripción a **SAP Build** con el service plan **build-default**.
  - **Licencia de usuario activo (developer)** para construir, probar y desplegar las skills/agentes propios de Joule.
  - Modelo comercial unificado de SAP Build, disponible en cuatro modalidades: **Subscription, BTPEA (BTP Enterprise Agreement), PAYG (Pay As You Go), CPEA (Cloud Platform Enterprise Agreement)**.
- Según la página **AI Feature** oficial ("Create a Joule Agent"), antes de construir un agente debes haber **creado las Joule skills** que el agente va a utilizar. La página recomienda crear agentes pequeños y específicos por tarea para mejorar el rendimiento.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- La fuente distingue prerrequisitos para **clientes** y para **partners**; este análisis recoge la vía de cliente.
- Según la página **AI Feature** oficial, el *agent builder* está soportado solo en determinados **data centers**: **US30, US21, US10, JP10, EU30, EU20, EU12, EU10, AP11, AP10** (consultar *Supported Data Centers* de Joule Studio para la lista completa). Además, un agente solo puede eliminarse si no tiene "parents".

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar la suscripción a SAP Build (service plan build-default), la licencia de usuario developer y la licencia de Joule (Base SKU 8019544 o Premium SKU 8019164) | Suscripción / entitlement SAP Build + Joule | General | Consultor SAP BTP / Licencias | 4 |
| 2 | Configurar Joule Studio según el escenario aplicable ("Setup Scenarios for Joule Studio" → "Set Up Joule Studio") | Joule Studio (SAP Build) | General | Consultor SAP Build / Joule Studio | 4 |
| 3 | Asignar usuarios a los roles ("Assign Users to Roles") | Roles de SAP Build / Joule Studio | Particular (por usuario / rol) | Consultor Seguridad / SAP Build | 3 |
| 4 | Crear AI capabilities y/o un Action Project ("Create AI Capabilities" / "Create an Action Project") como base para construir los agentes | AI Capabilities / Action Project en Joule Studio | General | Consultor SAP Build / Joule Studio | 4 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (construir, probar y monitorear una capability/agente) | Consultor SAP Build / Joule Studio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Joule Studio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Joule Studio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente advierte (Caution) sobre la correcta combinación de suscripciones y licencias para evitar problemas de compatibilidad al activar y usar los servicios de SAP Build.
- La documentación de Joule Studio incluye además los bloques "Building Capabilities for Joule", "Managing Joule Studio Projects", "Monitor AI Capabilities" y "Security" como parte del ciclo de vida del agente.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/
- SAP Help Portal — Initial Setup (Joule Studio — Initial Setup and Prerequisites): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- SAP Help Portal — AI Feature (Create a Joule Agent): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/193461e9d8494995bab4889b22afac93.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J313] — Expiring Price Handling

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J313 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- Initial Setup (SAP Help Portal — Joule Capabilities Guide, Expiring Price Handling): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule para SAP S/4HANA Cloud Public Edition que permite a un especialista de precios gestionar la expiración de precios de forma más eficiente. El usuario puede pedir a Joule que recupere precios (condition records de pricing en ventas) próximos a expirar y los renueve extendiendo su periodo de validez y ajustando los importes o ratios de las condiciones.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** con Joule.
- Funcionalidad de pricing en ventas (condition records); la fuente cita la app **Manage Prices - Sales** para abrir precios y detalles del job.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe tener asignado el business catalog **Master Data - Prices (SAP_SD_BC_PRICE_MANAGE_MC)**.
- La fuente indica que el rol de negocio **Pricing Specialist (SAP_BR_PRICING_SPECIALIST)** es una de las plantillas que contienen ese business catalog por defecto.
- App referenciada por la fuente: **Manage Prices - Sales**.

### 1.5 Datos maestros / transaccionales previos
- Condition records de pricing en ventas existentes (precios con periodos de validez), según la definición de "expiring prices" de la fuente.

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Public Edition** (la fuente es la Joule Capabilities Guide para Public Edition).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activar SAP Business AI y asignar usuarios a Joule (paso general "Activating Business AI and Assigning Users" referenciado por la Joule Capabilities Guide) | Activación de Business AI / asignación de usuarios | General | Consultor Funcional SAP S/4HANA + Seguridad | 3 |
| 2 | Asignar el business catalog **Master Data - Prices (SAP_SD_BC_PRICE_MANAGE_MC)** a los usuarios objetivo (p. ej. mediante el rol **Pricing Specialist — SAP_BR_PRICING_SPECIALIST**) | Business Catalog / Business Role | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (consultar precios por expirar, extender validez, ajustar importes, crear condition records, seguir el job) | Consultor Funcional SAP S/4HANA (SD / Pricing) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (SD / Pricing) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (SD / Pricing) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente describe la capacidad como un flujo conversacional secuencial: mostrar precios por expirar (con criterios como condition type o sales organization), extender valid-to, ajustar importes/ratios y crear los nuevos condition records en un único job, con seguimiento del progreso.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- SAP Help Portal — Initial Setup (Joule Capabilities Guide — Expiring Price Handling): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J326] — Meeting Location Planner Agent

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J326 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/65b25edc-21cc-4b54-8f3c-eb4524ab3117/
- Initial Setup (SAP Help Portal): No accesible (no existe enlace 'Initial Setup' ni 'AI Feature' accesible en *Resources*).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ayuda a empleados a organizar reuniones offsite sugiriendo ubicaciones que minimizan tiempos de viaje, proponiendo hoteles y mostrando una vista general de costos para planificar dentro del presupuesto.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **No documentado en la fuente oficial**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Early Adopter Care (EAC)**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/65b25edc-21cc-4b54-8f3c-eb4524ab3117/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J327] — Expense Report Validation Agent

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J327 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ba618aac-87c8-485d-8d3c-3338f6a8658a/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/COMPLETE/70b4acb7cfef4c0da0deef8e7ee653cc/302b5f2b75684754beb35a168eee9e30.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Agente para ayudar a viajeros de negocio a completar y enviar reportes de gastos, simplificando el proceso de entendimiento y preparación de la información requerida.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **No documentado en la fuente oficial**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Complete Mobile App | Configuración de la solución | General | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Early Adopter Care (EAC)**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ba618aac-87c8-485d-8d3c-3338f6a8658a/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/COMPLETE/70b4acb7cfef4c0da0deef8e7ee653cc/302b5f2b75684754beb35a168eee9e30.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J329] — Semantic Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J329 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/2fc1d26ebff748e4905d724247d33531.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/#pricing

**Resumen del caso:** Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas. El onboarding semántico toma tablas, contenido y semántica asociada como monedas, unidades, medidas, hechos, dimensiones y asociaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units para usar la oferta de IA en el servicio cloud subyacente. El método de activación indicado es “Activate with AI Units”. Precio bajo solicitud; duración de contrato disponible bajo solicitud. Incluye prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You must complete the following Joule configuration procedures before activating Joule in SAP Datasphere.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Your SAP Datasphere Service Instance in SAP BTP | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 2 | Configure the Size of Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 3 | Review and Manage Links to SAP Analytics Cloud and SAP Business Data Cloud Tenants | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 4 | Enable SAP HANA for SQL Data Warehousing on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 5 | Enable the SAP HANA Cloud Script Server on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 6 | Enable SAP Business AI for SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 7 | Enable Choropleth Layers for Geographical Visualizations | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 8 | Create OAuth2.0 Clients to Authenticate Against SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/2fc1d26ebff748e4905d724247d33531.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J336] — Error Resolution for Cost Accounting

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J336 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/56d1e4d0-5c07-4aa8-b226-64c8dd99750d/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/518ff9f0566e41dabf853463823accc4.html?locale=en-US&version=2602.00
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ayuda a los contadores de costos a identificar y resolver errores relacionados con contabilidad de costos, ofreciendo orientación asistida para atender incidencias del proceso.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Your SAP S/4HANA Cloud Public Edition | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/56d1e4d0-5c07-4aa8-b226-64c8dd99750d/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/518ff9f0566e41dabf853463823accc4.html?locale=en-US&version=2602.00
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J342] — Embedded Edition

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J342 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_DOCUMENT_AI/5fa7265b9ff64d73bac7cec61ee55ae6/0d68dc0002f0484ba25f85f3170166e0.html?locale=en-US&state=PRODUCTION&version=SHIP
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/#pricing

**Resumen del caso:** Automatiza tareas de procesamiento documental de punta a punta, ejecución de workflows e integración de canales.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document AI**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activación con AI Units. El detalle de pricing de Discovery Center muestra tarifas por volumen y permite agregar la feature a una estimación. Precio bajo solicitud. Pricing Details muestra: Up to 100,000 = 0.0786; Up to 300,000 = 0.0614; Up to 500,000 = 0.0443; From 500,000 = 0.0364. La unidad exacta no quedó explícita en el texto extraído. Se requieren AI Units para usar esta oferta de IA en el servicio cloud subyacente. La página indica que tiene prerequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Service Plans and Metering You have set up your global account and at least one subaccount on SAP BTP. If you’re working in an enterprise account, you need to add quotas to the services you purchased in your subaccount before they appear in the service marketplace. Otherwise, only default free-of-charge services are listed. Quotas are automatically assigned to the resources available in trial accounts. For more information, see Configure Entitlements and Quotas for Subaccounts. SAP Document AI allows you to move subaccounts between your global accounts. For more information, see Relationship Between Global Accounts, Subaccounts, and Directories.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable X.509 Authentication | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 3 |
| 2 | Run SAP Document AI in a Multitenant Application | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Document AI / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Document AI / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DOCUMENT_AI/5fa7265b9ff64d73bac7cec61ee55ae6/0d68dc0002f0484ba25f85f3170166e0.html?locale=en-US&state=PRODUCTION&version=SHIP
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J346] — Note Corrections for Project Billing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J346 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/#pricing

**Resumen del caso:** La función Smart Notes en Manage Project Billing propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta solo puede comprarse como parte de Joule Premium for Financial Management y no está disponible por separado; precio y duración de contrato bajo solicitud.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you use the standard role (SAP_BR_PROJ_BILLG_SPCLST), the following conditions are applicable: If the feature toggle PROJ_BILLG_SMART_NOTE is turned on, the business catalog SAP_PS_BC_BILLG_AI_SNOTE_PC will be added automatically and you can use the Smart Notes feature. Even if the feature toggle is turned off later, the business catalog will still be part of the standard business role. However, you cannot use the Smart Notes feature if the feature toggle PROJ_BILLG_SMART_NOTE is turned off. If the feature toggle PROJ_BILLG_SMART_NOTE is turned on, you have to manually add the Business Catalog SAP_PS_BC_BILLG_AI_SNOTE_PC in order to view and access the Smart Notes feature. If the feature toggle PROJ_BILLG_SMART_NOTE is turned off, you cannot view and access the Smart Notes feature. You will need to manually remove the business catalog.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J355] — Posting Issue Handling for Billing Documents

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J355 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f558354e-8de3-4b95-ae75-4cc5055cf911/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/posting-issue-handling-for-billing-documents?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Asiste a billing clerks a recuperar y visualizar documentos de facturación con problemas de contabilización según criterios determinados.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: To use this capability, you must have the following business catalog assigned: Sales - Billing Documents (SAP_SD_BC_BIL_DOC_PC). The Billing Clerk (SAP_BR_BILLING_CLERK) business role template contains this business catalog by default. By default, the system uses the billing date as the posting date for financial accounting. However, if you have set the deviating posting date that deviates from the billing date, the system uses this new date as the posting date when the created billing document is posted to financial accounting. For more information, see Important Information for Changing Specific Fields.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Perform price determination analysis for billing documents with pricing errors | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Perform a repricing for a single billing document item | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f558354e-8de3-4b95-ae75-4cc5055cf911/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/capabilities-guide/posting-issue-handling-for-billing-documents?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J358] — Processing of Incoming Quality Certificates with SAP Document AI

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J358 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/46a0ffd9c19d4dde88861505889b14b1.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/#pricing

**Resumen del caso:** Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito. La página también indica que, para activar esta capacidad, se requieren SAP Document AI, embedded edition y un workspace de SAP Document AI, por lo que pueden aplicar sus detalles de pricing.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have configured incoming quality certificates with one or more certificate types for which enhanced certificate processing is enabled. Users have the business catalog QM - Incoming Quality Certificates (SAP_QM_BC_INCG_QLTY_CERT_PC) or the apps Manage Certificate Receipts (F3233), Review Certificate Document Matches (F8537), and Upload Quality Certificate Documents (F8858) assigned to one of their roles. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Review Certificate Document Matches | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/46a0ffd9c19d4dde88861505889b14b1.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J36] — Generation of Full-Stack Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J36 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/758d28f15c044b43936230b258d1ebb7.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural. Con Joule, la capacidad genera modelos de datos, servicios, datos de ejemplo, anotaciones de UI, lógica de aplicación y pruebas unitarias, dentro de un entorno de desarrollo cloud alineado con SAP Business Application Studio y buenas prácticas de SAP BTP.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Code**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have created a global account in the SAP BTP cockpit. See Getting a Global Account. The correct way to subscribe to SAP Build Code is using the booster and not the manual setup. If you already have a subscription to one or more of the services included in SAP Build Code and you would like to upgrade to the SAP Build Code plan, see Changing Service Plans. Access your global account in the SAP BTP cockpit and choose Boosters from the navigation pane. This booster is relevant for the standard service plan. If you are working in the trial plan, you need to run a different booster. Make sure to select the booster relevant to the plan in which you want to work.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Code | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 2 | Open the booster to see the overview, components, and additional resources. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 3 | Create a Project | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 4 | Open Joule () from the activity bar. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 5 | Open the Data Editor. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 6 | Open the Generative AI-Powered Development guide, expand the Unit Testing  Run Unit Test section, and click Run Test. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/758d28f15c044b43936230b258d1ebb7.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J404] — Sales Order Creation from Unstructured Data

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J404 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/565f8b8bd23944f1b04836a1b424c647.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/#pricing

**Resumen del caso:** La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes. Después de cargar el archivo, la información se procesa automáticamente para generar una solicitud de pedido de venta que luego puede convertirse en pedido.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details indica que la función puede agregarse al AI Estimator para estimar la cantidad aproximada de AI Units y costos relacionados. No se muestra un importe fijo visible en la información extraída de la sección.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use both the Create Sales Orders - AI-Assisted Extraction and Create Sales Orders - Automatic Extraction apps to create sales orders from purchase order files. The Create Sales Orders - AI-Assisted Extraction app uses the SAP Document AI (Embedded Edition) for data extraction, whereas the Create Sales Orders - Automatic Extraction app uses the SAP Document AI (Base Edition). Compared with the Base Edition, the Embedded Edition of SAP Document AI supports more languages and smarter document processing capabilities. For more information, see Service Plans and Metering and SAP Document AI. The Extraction of Purchase Order (SALES_ORDER_REQUEST_EXTRACTION) schema is activated in the Manage Document AI Schema Registration Subscriptions app (F8996). For more information, see PURCHASE_ORDER_EXTENDED_STANDARD and Manage Document AI Schema Registration Subscriptions. The schema must be activated in each tenant where you want to use the Create Sales Orders - AI-Assisted Extraction app. To know which system client you are working in, click on your user on the SAP Fiori launchpad, choose About  System, and check the system name field. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. After the file is uploaded, the system creates a sales order request (containing the uploaded file as an attachment) and starts data extraction. You need to wait some time to view the extraction result. You can retry if data extraction fails.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the SAP Document AI workspace. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the standard Sales_Order_Request schema (version 1). | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Create Sales Orders - Automatic Extraction | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/565f8b8bd23944f1b04836a1b424c647.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J43] — Sales Order Automatic Completion

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J43 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/39a49e49-3ab6-46f5-889d-2035d9378cab/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/4ee364ca1af446929d4e2c4fc2f709b9.html?locale=en-US&version=2408.00
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Mediante datos históricos y machine learning, la función recomienda valores para completar campos vacíos en órdenes de venta incompletas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Your analytics specialist can train the model in the Intelligent Scenario Management app. Manual training allows you to set training filters and deactivate prediction for certain fields. For detailed instructions, see Tips on Training the Machine Learning Model. As of SAP S/4HANA Cloud 2408, the system enables auto training when scope item 73P is activated. You can also enable or disable auto training in the Intelligent Scenario Management app. With auto training, the system trains the model periodically based on business data from the past year, and the prediction is active for all six fields. To access the Monitor Recommendations for Sales Document Completion app, business users need to have the following business catalog assigned: Sales - Sales Document Autocompletion Monitoring (SAP_SD_BC_SDAC_MONITOR_PC) Intelligent Scenario Management

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Your SAP S/4HANA Cloud | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Activate the scope item 73P. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/39a49e49-3ab6-46f5-889d-2035d9378cab/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/4ee364ca1af446929d4e2c4fc2f709b9.html?locale=en-US&version=2408.00
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J45] — Inventory Prompts

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J45 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/ai-capabilities
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Inventory Prompts combina la información del inventario SAP LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial. Provee una interfaz de lenguaje natural para consultar datos y obtener insights usando preguntas cotidianas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/ai-capabilities
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J46] — Context Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J46 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/fa2762c1-5080-480b-bf93-103933a0af11/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/ai-capabilities
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** El contexto generado por IA aporta información e insights adicionales analizando los datos y el contexto existentes, ayudando a los usuarios a comprender mejor las tareas o solicitudes y a tomar decisiones informadas. Forma parte de las Base AI capabilities de SAP LeanIX, embebidas en la interfaz del inventory y del workspace.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/fa2762c1-5080-480b-bf93-103933a0af11/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/ai-capabilities
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J470] — Data Actions

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J470 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/#pricing

**Resumen del caso:** Proporciona a los usuarios profesionales de planificación herramientas para generar scripts de Advanced Formulas de SAP Analytics Cloud o comentarios. También permite generar comentarios de negocio a partir de un Advanced Formulas Script existente para apoyar la documentación y la transferencia de conocimiento, y generar fácilmente una descripción para una data action, incluyendo sus pasos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Se puede estimar la cantidad aproximada de AI Units y los costos asociados con el AI Estimator. Métrica: Requests (solicitudes); 0,23 AI Units por métrica; tarifa de EUR 7 por AI Unit (EUR 7 por métrica de referencia). Funcionalidad Premium facturada por consumo de AI Units.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J471] — AI-Assisted Calculations

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J471 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/00ca4ae380794468ba42ea46d10a4045.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/#pricing

**Resumen del caso:** Permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos de SAP Analytics Cloud, y también explicar fórmulas existentes en lenguaje claro.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Your SAP Analytics Cloud tenant is on a data center that supports SAP Business AI. You've purchased the SAP AI Units license. For more information about the SAP AI Units license, contact your Account Executive. Searching Your Data Using Just Ask If you're an administrator looking to enable SAP Analytics Cloud AI-assisted features, see Enable AI-Assisted Features for SAP Analytics Cloud.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure System Settings | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 2 | Enable AI-Assisted Features for SAP Analytics Cloud | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 3 | Configure Data Storage for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 4 | Enable Bring Your Own Key Encryption with SAP Analytics Cloud and SAP Data Custodian | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 5 | Set Up Third-Party Access with OAuth Clients | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 6 | Configure Email Server | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 7 | Configure Data Change Log Notifications | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 8 | Configure Comments Encryption | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/00ca4ae380794468ba42ea46d10a4045.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J47] — AI-Assisted Texting

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J47 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/ai-capabilities
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite crear o mejorar textos analizando contenido y contexto, con opciones para reescribir o resumir información existente. Un ejemplo indicado es generar descripciones concisas y precisas para fact sheets.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/ai-capabilities
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J48] — Translation Support

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J48 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/ai-capabilities
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La traducción asistida por IA permite a administradores agregar y traducir etiquetas y textos de ayuda para atributos nuevos o existentes en la configuración del metamodelo de SAP LeanIX.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/ai-capabilities
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J535] — Central Governance

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J535 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/30b09a79645d4137a187835e5010e53d.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule embebido en SAP Master Data Governance sobre SAP S/4HANA Cloud Private Edition permite a usuarios de negocio (p. ej. gerentes de ventas y especialistas de compras) operar funciones de MDG mediante lenguaje natural, sin conocimiento técnico extenso. Usa procesamiento de lenguaje natural para interpretar los prompts del usuario contra la estructura de los datos maestros y ejecutar los cambios: buscar, visualizar, crear nuevos business partners o modificar existentes, y consultar el estado de los procesos de gobierno.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud for master data governance, private edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You provision and configure Joule yourself using SAP BTP, with full control over subaccounts, entitlements, and system integrations. You have checked the general prerequisites for provisioning. A global account, subaccounts, and entitlements have been set up by performing administrative actions in the SAP BTP cockpit. Make sure you have completed the configuration steps before you run the Joule booster. Authorization Objects Used by Master Data Governance

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud for master data governance, private edition | Particular (por usuario / rol) | Consultor SAP MDG (S/4HANA) | 4 |
| 3 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 4 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 5 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 6 | Configure Opt-in/Out of Conversation Log Storage | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 7 | Set Up Document Grounding | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |

**Esfuerzo total estimado (activación / configuración): ~28 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP MDG (S/4HANA) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP MDG (S/4HANA) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP MDG (S/4HANA) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/30b09a79645d4137a187835e5010e53d.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 28 |
| Validación + documentación + KT | 11 |
| **Total** | **39** |

---

## [J54] — Joule with SAP S/4HANA Cloud Private Edition

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J54 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/98ee8608-82bb-49c3-b4ca-805bd6594314/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-private-edition?locale=en-US&version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/09becc58afa645bab4f51e830bc928dc.html?locale=en-US&version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite usar lenguaje natural para expresar requerimientos de negocio y acceder a capacidades informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Private Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have carried out the steps described in Customer Managed Provisioning. You have referred to the Security related information for Joule. You have fulfilled the necessary prerequisites as mentioned in Prerequisites for Customer Managed Provisioning. You have integrated the SAP S/4HANA Cloud Private Edition with Identity Authentication as Joule leverages the IAS setup of the SAP product for user login. You have created a service instance and generated a service key for SAP Build Work Zone, standard edition (foundation plan). For more information, see Create SAP Build Work Zone Application and Instance.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Set Up SAP S/4HANA Cloud Private Edition as a Content Provider | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Destinations | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/98ee8608-82bb-49c3-b4ca-805bd6594314/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-private-edition?locale=en-US&version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/09becc58afa645bab4f51e830bc928dc.html?locale=en-US&version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J57] — Joule with SAP Business Technology Platform

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J57 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/btp/sap-business-technology-platform/enable-joule-in-sap-btp-cockpit
- AI Feature (SAP Help Portal): https://help.sap.com/docs/btp/sap-business-technology-platform/account-administration-using-joule?ai=true&locale=en-US&version=Cloud
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Business Technology Platform**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have the Administrator role for the global account for which you'd like to enable Joule in the cockpit. Joule is available for your global account (P-/S-users). Make sure you are accessing the cockpit from the SAP default identity provider. This version of Joule is provided free of charge in non-trial BTP Global Accounts and is limited to supporting BTP administration capabilities only within SAP BTP cockpit. Navigate to the global account settings by selecting  (Global Account Settings). After a global account administrator has enabled Joule for the global account, the Joule diamond icon  will become visible in the cockpit tool header for all global account users. A Global Account Administrator must enable Joule in the Global Account settings by accepting the legal Terms and Conditions for Generative AI. Only then will the Joule icon appear in the cockpit tool header. Check out Enable Joule in the Cockpit to learn more.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable Joule in the Cockpit | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |
| 2 | Enable Joule in SAP BTP cockpit to access Generative AI capabilities. | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |
| 3 | Open the global account for which you'd like to enable Joule in SAP BTP cockpit. | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/btp/sap-business-technology-platform/enable-joule-in-sap-btp-cockpit
- SAP Help Portal — AI Feature: https://help.sap.com/docs/btp/sap-business-technology-platform/account-administration-using-joule?ai=true&locale=en-US&version=Cloud
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J586] — Project Services

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J586 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/bccabd59-564e-4a4d-84b3-67d6933348cd/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/619518deb7284e6485b78383fa7a42b3.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/viewing-business-data
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule incorpora una interfaz conversacional para apoyar actividades rutinarias de gestión de proyectos en SAP S/4HANA Cloud Public Edition. La capacidad ayuda a monitorear cumplimiento de tiempos, resumir cambios de proyecto y ofrecer autoservicio con IA para equipos de proyecto.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. To be able to view specific business data, you must have the required authorizations for the involved business objects. You can view data of the following business objects, depending on your role and authorizations: Required Business Catalogs SAP_CA_BC_SITN_MYSITUATION_PC

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/bccabd59-564e-4a4d-84b3-67d6933348cd/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/619518deb7284e6485b78383fa7a42b3.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/capabilities-guide/viewing-business-data
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J597] — Back Order Processing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J597 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/
- Initial Setup (SAP Help Portal — Joule Capabilities Guide, Executing Backorder Processing (BOP) Run): https://help.sap.com/docs/joule/capabilities-guide/executing-backorder-processing-bop-run?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución de Back Order Processing (BOP) mediante interacciones en lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** con Joule.
- Proceso de **Back Order Processing (BOP)** de Order Fulfillment.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe tener asignado el business catalog **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)**.
- La fuente indica que el rol de negocio **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)** es una de las plantillas que contienen ese business catalog por defecto.
- La fuente referencia el documento **Maintain Business Roles** para comparar/ajustar roles existentes con la última plantilla SAP.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Public Edition** (fuente: Joule Capabilities Guide para Public Edition).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activar SAP Business AI y asignar usuarios a Joule (paso general "Activating Business AI and Assigning Users") | Activación de Business AI / asignación de usuarios | General | Consultor Funcional SAP S/4HANA + Seguridad | 3 |
| 2 | Asignar el business catalog **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)** a los usuarios objetivo (rol de negocio del mismo nombre); si se usan roles existentes, compararlos con la plantilla SAP vigente (Maintain Business Roles) | Business Catalog / Business Role | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (ejecutar un BOP run vía Joule) | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente recomienda comparar los roles existentes con la última plantilla SAP y ajustarlos según se requiera para la capability BOP de Joule.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/
- SAP Help Portal — Initial Setup (Joule Capabilities Guide — Executing Backorder Processing (BOP) Run): https://help.sap.com/docs/joule/capabilities-guide/executing-backorder-processing-bop-run?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J600] — Joule with SAP Multi-Bank Connectivity

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J600 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Proporciona respuestas rápidas sobre SAP Multi-Bank Connectivity a partir de documentación del producto en SAP Help Portal, resumidas de forma contextual y clara.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Multi-Bank Connectivity**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: In this situation, you already have a global account, subaccounts, and entitlements set up. You also have users onboarded and trust set up to support your platform. Since the BTP platform is ready, you simply need to initiate the booster to prepare Joule and then configure the trusted domains. Make sure you Configure Trust to the Identity Authentication Tenant and Configure User Attributes for Joule from the Identity Directory before running the Joule booster. If you haven't set up a BTP platform, then you'll need to set up BTP first. This involves administrative actions in the SAP BTP cockpit. After you set up the platform, you can onboard Joule.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Document Grounding | Configuración de SAP Multi-Bank Connectivity | General | Consultor SAP Multi-Bank Connectivity | 4 |
| 2 | Run the Joule Booster | Configuración de SAP Multi-Bank Connectivity | General | Consultor SAP Multi-Bank Connectivity | 4 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Multi-Bank Connectivity | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Multi-Bank Connectivity | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Multi-Bank Connectivity | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J606] — Anomaly Detection

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J606 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-anomaly-detection?version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/integration-suite/sap-integration-suite/anomaly-detection
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP Integration Suite para identificar patrones inusuales o desviaciones en el tráfico de APIs mediante IA, apoyando la detección temprana de anomalías.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Integration Suite**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Subscribing to Notification Alerts The role collection APIPortal.Administrator must be assigned to you. The role collection APIManagement.SelfService.Administrator must be assigned to you to enable intelligent recommendations. Availability of this feature depends upon the SAP Integration Suite service plan that you use. For more information about different service plans and their supported feature set, see SAP Note 2903776.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate anomaly detection, intelligent recommendations, and API call prediction to enhance monitoring and forecasting capabilities for API calls. | Configuración de SAP Integration Suite | General | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-anomaly-detection?version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/integration-suite/sap-integration-suite/anomaly-detection
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J638] — Process Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J638 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/
- Initial Setup (SAP Help Portal — SAP Build Process Automation, Generative AI): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal — Generate Processes): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Genera artefactos de proceso (procesos de negocio, decisiones, formularios y script tasks) a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (SAP Build Process Automation no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, se debe **habilitar la IA generativa a nivel de tenant** y **aceptar los términos y condiciones**. Tras habilitarla, la función **Generate** queda disponible (aprox. 5 minutos después) en la pantalla Overview del proyecto y en el process editor.
- Según la página **AI Feature** oficial ("Generate Processes"), para usar la generación el usuario debe haber **creado un proyecto** (Business Process Project) y haber **habilitado la IA generativa y aceptado los términos y condiciones** del tenant.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Según la página **AI Feature** oficial: la función *Generate* permite generar únicamente **formularios, procesos y data types**; **no** puede añadir flow controls (branches, go-to steps) ni liberar, desplegar o eliminar un proyecto. El prompt debe tener entre **5 y 1000 caracteres**. Al regenerar un proceso existente, las **variables de proceso (input/output/custom) no se actualizan ni eliminan**, y los inputs de tipo objeto que referencian un data type no están soportados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Habilitar la **IA generativa a nivel de tenant** en SAP Build Process Automation y aceptar los términos y condiciones | Configuración de tenant (Generative AI) | General | Consultor SAP Build Process Automation | 3 |
| 2 | Verificar (tras ~5 minutos) que la función **Generate** esté disponible en la pantalla Overview del proyecto y en el process editor | Función Generate (process editor) | General | Consultor SAP Build Process Automation | 2 |

**Esfuerzo total estimado (activación / configuración): ~5 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (generar un proceso/decisión/formulario desde lenguaje natural) | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La función Generate queda disponible aproximadamente 5 minutos después de habilitar la IA generativa y aceptar los términos y condiciones.
- La IA generativa permite generar procesos de negocio, decisiones, formularios y script tasks.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/
- SAP Help Portal — Initial Setup (SAP Build Process Automation — Generative AI): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature (Generate Processes): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 5 |
| Validación + documentación + KT | 11 |
| **Total** | **16** |

---

## [J639] — Process Editing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J639 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/143f1e51-609a-45d9-ab96-bf286e044a03/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Process Editing ayuda a desarrolladores durante el diseño e implementación de automatizaciones, permitiendo editar artefactos de proceso mediante instrucciones en lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have created a project. For more information, see Create a Business Process Project. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. You interact and improve on your process flow until you have a finalized version.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Create a Guided Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Create an Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Create a File | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Create a Data Type | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/143f1e51-609a-45d9-ab96-bf286e044a03/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J640] — Process Summarization

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J640 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Process Summarization genera resúmenes en lenguaje natural de procesos o artefactos complejos para facilitar la comprensión, revisión y transferencia de conocimiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have created a project. For more information, see Create a Business Process Project. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. You interact and improve on your process flow until you have a finalized version.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Create a Guided Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Create an Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Create a File | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Create a Data Type | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J641] — Form Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J641 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ff9ca9a1-b443-405d-95bd-9b53a8a503db/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/PROCESS_AUTOMATION/a331c4ef0a9d48a89c779fd449c022e7/e53d5dc73f3e4a98bf5d1a449e9a6188.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Genera formularios de automatización de procesos a partir de descripciones en lenguaje natural en SAP Build Process Automation.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have created a project. For more information, see Create a Business Process Project. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. To generate a form, enter a prompt with a description of the form you need, and the generative AI creates the form for you.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Configure Process Variables | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Configure Process Attributes | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Add Flow Controls | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Add Process Steps | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ff9ca9a1-b443-405d-95bd-9b53a8a503db/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/PROCESS_AUTOMATION/a331c4ef0a9d48a89c779fd449c022e7/e53d5dc73f3e4a98bf5d1a449e9a6188.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J642] — Decision Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J642 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0517fabc-df67-4042-9015-a57c1a9079ba/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-decision#use-generative-ai-in-a-decision
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Asiste el diseño de procesos al generar artefactos de decisión a partir de descripciones en lenguaje natural de las reglas deseadas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. You must have one of the following roles to use generative AI: For more information, see Authorizations. You must have created at least one decision to use the Explain this Decision feature.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Create a Guided Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Create an Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Create a File | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Create a Data Type | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0517fabc-df67-4042-9015-a57c1a9079ba/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-decision#use-generative-ai-in-a-decision
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J643] — Decision Summarization

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J643 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-decision#use-generative-ai-in-a-decision
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Asiste a los usuarios en el diseño e implementación de automatizaciones al generar resúmenes de negocio de reglas ya modeladas que no tienen documentación.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. You must have one of the following roles to use generative AI: For more information, see Authorizations. You must have created at least one decision to use the Explain this Decision feature.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Create a Guided Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Create an Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Create a File | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Create a Data Type | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-decision#use-generative-ai-in-a-decision
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J644] — Script Task Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J644 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f2310927-98ed-410a-86bb-1ca9ece68e21/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-script-using-generative-ai-in-script-task?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite generar código JavaScript ejecutable mediante lenguaje natural dentro de SAP Build Process Automation. La tarea de script integra capacidades de IA generativa para que el desarrollador cree código a partir de prompts y pueda apoyarse en acciones predefinidas alineadas con las restricciones del runtime.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions. You have created a project. For more information, see Create a Business Process Project. You have enabled generative AI for your tenant and have accepted the terms and conditions. For more information, see Generative AI. The script task integrates generative AI capabilities, allowing you to automatically generate a new code based on a given prompt. Besides using prompts, you have access to predefined AI Actions to manage specific coding tasks that align with the workflow runtime's constraints: Since the context is not included by default, you need to pass the variable name in the prompt.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Business Process Project | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Agents | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Enable the use of generative AI features. | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Create a Business Process | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Configure Process Variables | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Configure Process Attributes | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 7 | Add Flow Controls | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 8 | Add Process Steps | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f2310927-98ed-410a-86bb-1ca9ece68e21/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-script-using-generative-ai-in-script-task?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J650] — Booking Agent

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J650 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/47844870-d3f6-4ffd-abdf-945d6bc20ae7/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/CONCUR_TRAVEL/f71981185ec74d0ea824394ce06fd26c/56c42ceab8804c288ffe7be4792eed4a.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Agente de Joule en Concur Travel que entrega recomendaciones personalizadas de vuelos y hoteles analizando preferencias del viajero, políticas de viaje de la empresa y restricciones de presupuesto.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **No documentado en la fuente oficial**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: End users and administrators must work with their IT teams to enable Joule Base.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/47844870-d3f6-4ffd-abdf-945d6bc20ae7/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/CONCUR_TRAVEL/f71981185ec74d0ea824394ce06fd26c/56c42ceab8804c288ffe7be4792eed4a.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J652] — Architecture Guidance

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J652 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/leanix/ea/ai-assisted-architecture-guidance
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP LeanIX que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Confirm that the relevant AI terms have been signed. Contact your customer success manager if you have questions. If insights are already available, they appear as tiles on the Architecture Guidance page. If you've just activated the feature, it can take some time before insights are displayed.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate AI Assisted Architecture Guidance under Administration  Optional Features & Early Access. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |
| 2 | Add new applications and business capabilities to your inventory, for example, look into a new department or line of business, see Define the Scope of Your Application Portfolio Assessment | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/leanix/ea/ai-assisted-architecture-guidance
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J669] — Insights Description Generator

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J669 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0614d66c-4e6d-42bc-b45b-135ba035d843/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-transformation-manager/user-guide/creating-insights?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP Signavio Process Transformation Manager que ayuda a crear descripciones claras, consistentes y amigables para usuarios de negocio al capturar y colaborar sobre insights de SAP Signavio Process Intelligence.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio Process Transformation Manager**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Access to this feature depends on your license. For more information, see User Administration, Authentication, and Authorization in the Security Guide for SAP Signavio Process Transformation Manager.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select the links below to learn more about each topic. | Configuración de SAP Signavio Process Transformation Manager | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0614d66c-4e6d-42bc-b45b-135ba035d843/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-transformation-manager/user-guide/creating-insights?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J671] — Performance Preparation Agent

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J671 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/761a2305-b0a2-4262-b9a3-abd4945ad314/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/successfactors-platform/setting-up-and-using-joule-in-sap-successfactors/configuring
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** El Performance Preparation Agent automatiza la recopilación de datos, genera talking points personalizados para managers y sugiere próximos pasos accionables para reuniones one-on-one.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **No documentado en la fuente oficial**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You need to make configurations before using the Performance Preparation Agent. You've enabled Joule in SAP SuccessFactors. You have the Administrator Permissions   Manage AI Capabilities  AI Services Administration permission. The Performance Preparation Agent is currently available for trial on a promotional basis. This means you can activate and evaluate the agent without purchasing an additional AI license (SKU). When enabling the agent, you’ll be prompted to review and accept the applicable Terms and Conditions. Once accepted, the agent can be used throughout the promotion period.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Grant users the User Permissions  AI Access  Performance & Goals Agent permission. | Configuración de la solución | Particular (por usuario / rol) | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/761a2305-b0a2-4262-b9a3-abd4945ad314/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/successfactors-platform/setting-up-and-using-joule-in-sap-successfactors/configuring
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J74] — Joule with SAP S/4HANA Cloud Public Edition

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J74 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/27d870bda64547febeb48482aeee77d5.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/a955cb79db3c4f5c89ed3f00bb05f080.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): This section describes how to integrate Joule with the technical product SAP S/4HANA Cloud Public Edition. These steps comprise the Joule-specific and product-specific prerequisites and depend on your initial system setup. For example, you must first set up the technical environment, such as the SAP Business Technology Platform (BTP) with the entitlements for Joule and SAP Build Work Zone, standard edition (foundation/standard plan). You are guided through the integration steps with instructions, for example, you run the Joule booster that - among other settings - enables the communication scenario SAP_COM_0882 (SAP Digital Assistant Services) in the background. To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. You fulfill the general Prerequisites for Customer Managed Provisioning for Joule. You have reviewed the Customer Managed Provisioning for Joule and have carried out the necessary steps. To integrate Joule with SAP S/4HANA Cloud Public Edition, you must carry out the following steps:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Register the SAP S/4HANA Cloud Public Edition System | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Create SAP Build Work Zone Application and Instance | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/27d870bda64547febeb48482aeee77d5.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/a955cb79db3c4f5c89ed3f00bb05f080.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J757] — Supplier Delivery Date Mass Update

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J757 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d7b65dad-4fa1-4430-a860-6c8eba5ff8e1/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite realizar actualizaciones masivas de fechas de entrega para múltiples pedidos de compra utilizando Joule en SAP S/4HANA Cloud Public Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: To use this capability, you must have the following business catalogs assigned: SAP_MM_BC_PO_MPROCESS_PC (Materials Management - Mass Processing of Purchase Orders)

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Supplier Confirmations for Purchase Orders | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d7b65dad-4fa1-4430-a860-6c8eba5ff8e1/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J762] — Joule and Microsoft 365 Copilot

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J762 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integrating-joule-with-microsoft-365-copilot?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/serviceguide/using-joule-with-microsoft-365-copilot?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365. Permite consultar datos y tareas de SAP desde Copilot y aprovechar información/flujos de Microsoft 365 desde Joule.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have at least one SAP business tenant (Such as SAP S/4HANA Private Cloud, SAP SuccessFactors) integrated with Joule. You have set up trust between Entra and SAP Cloud Identity Services – Identity Authentication, registering Entra as the Corporate IdP based on OIDC. For more information, see Configuring SAP Cloud Identity Services and Microsoft Entra ID for Joule. You have a Microsoft M365 Copilot license and have rolled out M365 Copilot to the intended user base. For more information, see Getting Started with Microsoft 365 Copilot. Joule maintains a 1:1 relationship with a Microsoft Entra ID tenant. Hence, a single Entra ID tenant cannot be used for configuring multiple Joule environments. In which case, your development and production tenants cannot use the same Microsoft Entra ID tenant. Therefore, to establish a testing environment for the Microsoft 365 Copilot integration, it is recommended to utilize a dedicated M365 tenant for testing purposes. Note down your Microsoft M365 Tenant Id corresponding to your productive Microsoft M365 Copilot/Teams deployment. You'll need to provide this during the Joule landscape setup. Roles and Authorizations for Joule with Microsoft 365 Copilot/Microsoft Teams

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Document Grounding | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Install the SAP Joule app via the Microsoft 365 Admin Center. | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP + Funcional | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP + Funcional | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integrating-joule-with-microsoft-365-copilot?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/serviceguide/using-joule-with-microsoft-365-copilot?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J765] — Behavioral Insights for Contract Accounting

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J765 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/
- Initial Setup / AI Feature (SAP Help Portal — *Resources* enlaza ambos a la misma página oficial): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/0ceda0e195ef45ac914ea301ba6b6fec.html?version=2023.002
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/#pricing

**Resumen del caso:** Feature para SAP S/4HANA Cloud Private Edition que ayuda a especialistas de cobranza a predecir y explicar riesgos de pago analizando comportamiento histórico de clientes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): ISLM Machine Learning Scenarios

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate Features | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/
- SAP Help Portal — Initial Setup / AI Feature (misma página): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/0ceda0e195ef45ac914ea301ba6b6fec.html?version=2023.002
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J777] — Retrieval of Equipment Information in Service Management

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J777 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/
- Initial Setup (SAP Help Portal): No accesible (el enlace aparece en *Resources* pero no fue posible acceder a su contenido tras reintentos).
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/#pricing

**Resumen del caso:** Los service managers pueden acceder rápidamente a detalles completos del equipo instalado en sitios de cliente, incluyendo garantía, historial de transacciones de servicio y recomendaciones o resúmenes asistidos por IA.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details muestra consumo asociado a AI Units, con cantidad incluida indicada como 0 AI Units; las solicitudes adicionales estarían sujetas al consumo/estimación correspondiente de AI Units. No se muestra un precio unitario fijo en la información visible.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J778] — Requirement Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J778 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/cloud-alm/applicationhelp/ai-assisted-requirement-generation
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/#pricing

**Resumen del caso:** Esta función de SAP Cloud ALM permite generar automáticamente requerimientos de negocio de alta calidad a partir de transcripciones o notas de talleres Fit-to-Standard.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Cloud ALM**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details indica que la función puede agregarse al estimador para calcular una cantidad aproximada de AI Units y costos relacionados mediante AI Estimator. No se muestra un precio unitario fijo en la información visible de Pricing Details.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You have created a document in the Documents app containing the Fit-to-Standard workshop transcript. You have activated the AI feature. To do so: Log on to SAP for Me. For more information about access to SAP for Me, see Access and Authorizations. To activate a feature, select Request Activation next to the feature name. A pop-up titled Tenants appears. In the Tenants pop-up, select create a support case. An information pop-up appears.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Tricentis Test Automation for SAP | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |
| 2 | Review and adjust the generated content. Edit or delete any inappropriate or unnecessary data. You can also discard the requirement without saving. | Configuración de SAP Cloud ALM | General | Consultor SAP Cloud ALM | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Cloud ALM | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Cloud ALM | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Cloud ALM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/cloud-alm/applicationhelp/ai-assisted-requirement-generation
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J792] — SAP Joule for Developers‚ ABAP AI capabilities

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J792 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3c06a28b-576b-47ba-a2be-de0588391d6a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/start
- AI Feature (SAP Help Portal): https://help.sap.com/docs/ABAP_Cloud/bbcee501b99848bdadecd4e290db3ae4/joule-for-developers-abap-ai-capabilities?version=sap_btp
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule for Developers con capacidades ABAP AI apoya a desarrolladores en SAP S/4HANA Cloud Public Edition para acelerar tareas de desarrollo ABAP mediante asistencia de IA.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Getting Started (Administrators) Learn more how you can get SAP Joule for Developers, ABAP AI capabilities and which business roles are required. To leverage Joule's capabilities on-stack, you need to purchase an additional license: For SAP BTP ABAP environment and SAP S/4HANA Cloud Public Edition, see SAP Note 3571857 . For more information on how to integrate SAP Joule for Developers, ABAP AI capabilities into ABAP development tools for Eclipse, see Getting Started (Administrators).

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3c06a28b-576b-47ba-a2be-de0588391d6a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/abap-ai/generative-ai-in-abap-cloud/start
- SAP Help Portal — AI Feature: https://help.sap.com/docs/ABAP_Cloud/bbcee501b99848bdadecd4e290db3ae4/joule-for-developers-abap-ai-capabilities?version=sap_btp
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J811] — Supplier Delivery Date Prediction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J811 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/
- Initial Setup (SAP Help Portal — Intelligent Scenario Lifecycle Management, Activate Features): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html?locale=en-US
- AI Feature (SAP Help Portal — Predictive Scenario for Monitoring Purchase Order Items): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/69908735733a41eeb84bc61d9d0e4208.html?version=2023.002
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition** — el caso se apoya en **Intelligent Scenario Lifecycle Management (ISLM)** (Cross Components → Process Management and Integration).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, el caso se gestiona mediante **ISLM**, cuyo framework consta de dos apps SAP Fiori: **Intelligent Scenarios** e **Intelligent Scenario Management**, que ofrecen una interfaz unificada para crear, desplegar, monitorear y activar el modelo a consumir por la aplicación de negocio.
- ISLM integra con **Generative AI Hub, SAP BTP AI services y SAP HANA ML**; un intelligent scenario es una representación ABAP del caso de uso.
- Según la página **AI Feature** oficial ("Predictive Scenario for Monitoring Purchase Order Items"), se trata de un **predictive scenario predefinido** que un data scientist / experto en ML habilita vía ISLM. Artefactos requeridos: **Predictive Model `Suplr_Delvry_Pred`** y **Predictive Scenario `SUPLRDELIVPREDICT`**. El modelo se **entrena con datos históricos mediante la app *Predictive Models*** (cada entrenamiento crea una nueva versión) y **se debe fijar una versión activa**: si no hay modelo activo, las apps que usan el escenario no pueden predecir ni mostrar resultados.

### 1.5 Datos maestros / transaccionales previos
- **Datos históricos** de fechas de entrega / posiciones de pedidos de compra para el entrenamiento del modelo (la capacidad usa datos históricos y parámetros relevantes, según la Detail Page).

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para **SAP S/4HANA Cloud Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configurar los prerrequisitos de **ISLM** para el caso (integración con Generative AI Hub / SAP BTP AI services / SAP HANA ML según el intelligent scenario) | ISLM (framework) | General | Consultor Funcional SAP S/4HANA + BTP | 4 |
| 2 | Activar el **intelligent scenario `SUPLRDELIVPREDICT`**, **entrenar el modelo `Suplr_Delvry_Pred`** con datos históricos (app *Predictive Models*) y **fijar una versión activa**; ejecutar las operaciones de ciclo de vida (retraining, despliegue) mediante **Intelligent Scenario Management** | Intelligent Scenario / Predictive Model | General | Consultor Funcional SAP S/4HANA (ISLM) | 4 |
| 3 | Habilitar el acceso de los usuarios a la feature (asignación de roles/autorizaciones requeridos) | Roles / Autorizaciones | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (predicción de fechas de entrega en posiciones de pedidos de compra) | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- ISLM soporta operaciones de ciclo de vida como entrenamiento programado y retraining, además del despliegue y activación del modelo, directamente dentro de SAP S/4HANA (escenarios embedded y side-by-side).
- La predicción usa datos históricos; la calidad del modelo depende de la disponibilidad y calidad de esos datos.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/
- SAP Help Portal — Initial Setup (Intelligent Scenario Lifecycle Management — Activate Features): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html?locale=en-US
- SAP Help Portal — AI Feature (Predictive Scenario for Monitoring Purchase Order Items): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/69908735733a41eeb84bc61d9d0e4208.html?version=2023.002
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |

---

## [J824] — Resolution of Implausible Meter Readings

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J824 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4d67f2b1-6f72-4c6f-bce3-e6d4c0e89b1c/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2ac7fe29a0c94cdd88fb80c2cb9f7758/0fdbf93ccc784715b45bb00f308ff1aa.html?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e688c39484924d11961e87616f8338fa/d8fb92254821474697e0ebe615029cd4.html?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La capacidad se integra en el procesamiento de lecturas de medidor en IS-U para apoyar con machine learning la resolución de lecturas implausibles.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Enabling of the Intelligent Scenario Lifecycle Management (ISLM) to define an active predictive model for the predictive scenario UTI_MR_IMPLAUSIBLE. Intelligent Scenario and Model The Intelligent Scenario Lifecycle Management (ISLM) to access the predictive scenario and model. For more information about the Intelligent Scenario Lifecycle Management (ISLM), see Intelligent Scenario Lifecycle Management.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Add Customer-Specific Fields to the Device Master Data | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Provision of training and apply-relevant datasets to access and utilize machine learning-relevant information for implausible meter reading results | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4d67f2b1-6f72-4c6f-bce3-e6d4c0e89b1c/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2ac7fe29a0c94cdd88fb80c2cb9f7758/0fdbf93ccc784715b45bb00f308ff1aa.html?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e688c39484924d11961e87616f8338fa/d8fb92254821474697e0ebe615029cd4.html?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J825] — Resolution of Outsorted Billing Documents

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J825 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f9a4201e-955f-4aaf-b41a-d2479fb13ed1/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/021b182b0c47416c8fafed67ebfd78a9/e668f657772ebc12e10000000a4450e5.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e688c39484924d11961e87616f8338fa/a7875203275243ae8910dd132f2948ee.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La capacidad se integra en el proceso de billing de IS-U para apoyar el procesamiento de documentos de facturación apartados u outsorted.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Roles, Business Catalogs and Technical Catalogs This app is available for the role Billing Specialist (Utilities) (SAP_BR_BILLING_SPECIALIST_ISU). After you have successfully performed an action, the worklist is refreshed, and the related billing document is removed from the worklist. After you have reversed the document, further actions are possible, such as Change Contract, Change Rate Data, or Correct Meter Reading Results. You can simulate and create the bill after you have made your changes. If you have already defined your own CI_ERCH includes in the database table ERCH, you can display the related fields in this app. Intelligent Scenario and Model

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Perform actions for one or more billing documents directly from the worklist: | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Perform actions: | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Provision of training and apply-relevant datasets to access and utilize machine learning-relevant information for outsorted billing documents. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9a4201e-955f-4aaf-b41a-d2479fb13ed1/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/021b182b0c47416c8fafed67ebfd78a9/e668f657772ebc12e10000000a4450e5.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e688c39484924d11961e87616f8338fa/a7875203275243ae8910dd132f2948ee.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J831] — Sales Order Creation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J831 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5d3d1312-92d7-478a-8e95-f0f0130f5666/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/2dcf49a616b842b096e0a3cad4dac458.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta desde archivos de compra no estructurados en PDF o imágenes; la información se extrae automáticamente y se propone en campos de la solicitud.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: This app calls the SAP Document AI service to extract data from purchase order files. You do not need to have an enterprise account on SAP Business Technology Platform (which requires a separate license) to use the service. After the file is uploaded, the system creates a sales order request (containing the uploaded file as an attachment) and starts data extraction. You need to wait some time to view the extraction result. You can retry if data extraction fails. If request data is incomplete, you must edit it on the object page. If needed, you can open the purchase order file in an embedded pane or in a new window to verify purchasing details.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Sales Orders - VA01 | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Create Sales Orders - Automatic Extraction | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Create Sales Orders - AI-Assisted Extraction | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Create sales orders | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5d3d1312-92d7-478a-8e95-f0f0130f5666/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/2dcf49a616b842b096e0a3cad4dac458.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J832] — Sales Order Creation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J832 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/836b7ca4-0177-4757-8152-51846c586f1e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/2dcf49a616b842b096e0a3cad4dac458.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La capacidad permite crear pedidos de venta a partir de datos no estructurados, como archivos PDF o imágenes de órdenes de compra. El sistema extrae la información del archivo, propone valores para la solicitud de pedido y permite convertirla posteriormente en un pedido de venta.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: After the file is uploaded, the system creates a sales order request (containing the uploaded file as an attachment) and starts data extraction. You need to wait some time to view the extraction result. You can retry if data extraction fails. If request data is incomplete, you must edit it on the object page. If needed, you can open the purchase order file in an embedded pane or in a new window to verify purchasing details.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Sales Orders - VA01 | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Create Sales Orders - Automatic Extraction | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Create sales orders | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/836b7ca4-0177-4757-8152-51846c586f1e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/2dcf49a616b842b096e0a3cad4dac458.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J846] — Sales Order Creation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J846 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/451531fc-438b-4ecd-a3be-3efb74cb99f5/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/2dcf49a616b842b096e0a3cad4dac458.html?version=2023.002
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta a partir de archivos de órdenes de compra en PDF o imagen. El sistema extrae información y propone valores para la solicitud de orden.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: After the file is uploaded, the system creates a sales order request (containing the uploaded file as an attachment) and starts data extraction. You need to wait some time to view the extraction result. You can retry if data extraction fails. If request data is incomplete, you must edit it on the object page. If needed, you can open the purchase order file in an embedded pane or in a new window to verify purchasing details.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Sales Orders - VA01 | Configuración de SAP S/4HANA | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Create Sales Orders - Automatic Extraction | Configuración de SAP S/4HANA | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Create sales orders | Configuración de SAP S/4HANA | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/451531fc-438b-4ecd-a3be-3efb74cb99f5/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/2dcf49a616b842b096e0a3cad4dac458.html?version=2023.002
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J848] — Supplier Delivery Date Prediction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J848 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e0dd79ff-4ed9-4d79-9461-2be67e664a3c/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/69908735733a41eeb84bc61d9d0e4208.html?version=2023.002
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra con base en datos históricos y múltiples parámetros del proceso de aprovisionamiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Intelligent Scenario Lifecycle Management What is an Intelligent Scenario Intelligent Scenarios in ISLM Intelligent Scenario Lifecycle Management is a standardized framework to build and manage AI use cases, enabling seamless integration with Generative AI Hub, SAP BTP AI services, and SAP HANA ML. It standardizes the integration and consumption of intelligent scenarios within SAP S/4HANA for both embedded and side-by-side scenarios. An intelligent scenario is an ABAP representation of a business-specific use case. This predefined predictive scenario allows you, as a data scientist or machine learning expert to enable your users to predict the delivery dates for purchase order items, based on historical data and using Intelligent Scenario Lifecycle Management. You can also train the prediction model, based on the historical data in your system. With each training using the Predictive Models app, you are creating a new version of the model. You must set an active version of the model. If there are no active models, the apps using this scenario cannot predict the results or display predicted results.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate Features | Configuración de SAP S/4HANA | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Create Purchase Order - Advanced (ME21N, ME22N, ME23N) | Configuración de SAP S/4HANA | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e0dd79ff-4ed9-4d79-9461-2be67e664a3c/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/69908735733a41eeb84bc61d9d0e4208.html?version=2023.002
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J85] — Joule with Regulatory Change Manager

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J85 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/REGULATORY_CHANGE_MANAGER/8d691963179a42858de62e51939bafe3/6a2270b857024325a4d643487e1bba6a.html?version=Public
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Regulatory Change Manager**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Only IT Users have access to Joule and are limited to asking 15 questions per week. Once you have asked 10 questions in a week, Joule will notify you about the remaining questions. The quota of 15 questions will be reset every Sunday.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Regulatory Change Manager | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Regulatory Change Manager | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Regulatory Change Manager | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/REGULATORY_CHANGE_MANAGER/8d691963179a42858de62e51939bafe3/6a2270b857024325a4d643487e1bba6a.html?version=Public
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J86] — Explanation of Fixed Asset Depreciation Keys

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J86 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/3e5fcf2c768746049b5627bd5a42f720/cc4d416d14284e4abe6da0602d5b9966.html?locale=en-US&version=2602.500#ai-generated-explanation-of-depreciation-keys
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/#pricing

**Resumen del caso:** Explica cómo operan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema en lenguaje natural, comprensible para usuarios de negocio.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units. Precio bajo solicitud. AI Units requeridas para usar esta oferta de IA en el Cloud Service subyacente. Solo puede comprarse como parte del paquete Joule Premium for Financial Management y no está disponible por separado. Tiene prerequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. For more details about the AI features for Asset Accounting, in particular about the prerequisite authorizations, see the sections below. Authorization and more Information To enable users to access the AI feature, their business users need to have the following business catalog and IAM app assigned:: Business catalog: Asset Accounting – Explain Depreciation Key (AI) (SAP_FIN_BC_AA_AI_EXDEPRKEY_PC)

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Company Code | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Perform Legacy Data Transfer with Subsequent Balance Carryforward | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/3e5fcf2c768746049b5627bd5a42f720/cc4d416d14284e4abe6da0602d5b9966.html?locale=en-US&version=2602.500#ai-generated-explanation-of-depreciation-keys
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J885] — Run Forecasts in Time Series or Line Charts

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J885 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/ca67817bec1c4f6582126d5d9dab68bb.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/76c9d4bb842b4504af627e48ecaa32bb.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Los analistas de negocio pueden generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de SAP Analytics Cloud.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Creating and Provisioning Your SAP Analytics Cloud Tenant in SAP BTP Cockpit This setting lets you define if creators of calendar events on your tenant can enable the integration of their calendar events with Microsoft tools, like Microsoft Outlook and Microsoft Teams. To turn on this setting, enter the IDs of the application (client) and the directory (tenant) from your Microsoft Azure Active Directory. This setting allows SAP Product Support to create a support user on your tenant during troubleshooting processes without requiring internal user credentials. By default, this setting is disabled. This setting enables you to prevent users from uploading data without permission by an administrator. By default, this setting is disabled until you turn it on. Before you can create a forecast on a time series chart, using a remote model from an SAP HANA, SAP BW, SAP Universe or SAP S/4HANA system, your administrator must configure the following option: Enable Time Series Forecast and Smart Grouping on Live Data Models. The data will be processed on SAP servers. You cannot run forecasts on Line charts using remote models.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure System Settings | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 2 | Enable AI-Assisted Features for SAP Analytics Cloud | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 3 | Configure Data Storage for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 4 | Enable Bring Your Own Key Encryption with SAP Analytics Cloud and SAP Data Custodian | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 5 | Set Up Third-Party Access with OAuth Clients | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 6 | Configure Email Server | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 7 | Configure Data Change Log Notifications | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 8 | Configure Comments Encryption | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/ca67817bec1c4f6582126d5d9dab68bb.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/76c9d4bb842b4504af627e48ecaa32bb.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |

---

## [J886] — Smart Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J886 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/c9eb30cc1e5b4c439cb871bf9612d2ac.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Analiza desviaciones y puntos de datos dentro del modelo subyacente de SAP Analytics Cloud para entregar explicaciones en texto y visualizaciones asociadas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Searching Your Data Using Just Ask

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Add Smart Insights Charts and Text to Your Story | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 2 | Add Dynamic Text to Stories | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 3 | Add Variance to Charts (Classic) | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/c9eb30cc1e5b4c439cb871bf9612d2ac.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J88] — Analytical Business Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J88 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/#pricing

**Resumen del caso:** Panel lateral de IA generativa en Cost Center Review Booklet que permite analizar y resumir datos financieros en lenguaje natural para convertirlos en insights accionables de negocio.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Activación con AI Units / suscripción. La página muestra modelo de suscripción con métrica Flat Fee y precio oculto. Precio bajo solicitud Requiere AI Units para usar la oferta de IA. Registro Premium incluido en el paquete Joule Premium for Financial Management. La página indica prerequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Depending on your business role, you can use specific AI features if you want to quickly interpret and efficiently analyze the data in the following review booklets: The data shown in tables or charts is provided to a large language model; therefore, you must not include personal data in your drilldown. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. To access the financial business insights side panel including quick actions, your business user needs to have the following authorizations assigned in the business role by an administrator: Business catalog: Analytics - Review Booklet Business Insights (SAP_BW_BC_RVB_ABI_PC)

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Install Additional Software | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Review Booklets | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Select the part of the table that you want to use a quick action on. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J892] — Smart Grouping

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J892 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/f0e5e294b8d9453d87df35e862ceab99.html?q=Smart+grouping&locale=en-US#applying-smart-grouping-to-your-chart
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Agrupa puntos de datos similares en gráficos de dispersión y burbuja de SAP Analytics Cloud mediante clustering basado en centroides.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Before you can create a forecast on a time series chart, using a remote model from an SAP HANA, SAP BW, SAP Universe or SAP S/4HANA system, your administrator must configure the following option: Enable Time Series Forecast and Smart Grouping on Live Data Models. The data will be processed on SAP servers.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Charts in Stories | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 2 | Select Accounts, Measures, and Dimensions | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 3 | Set Up Waterfall Charts | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 4 | Create Custom Calculations for Your Charts | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 5 | Add a chart to your SAP Analytics Cloud story or to an analytic applications page, or apply other properties to a chart. | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |
| 6 | Add a chart to a new story | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/f0e5e294b8d9453d87df35e862ceab99.html?q=Smart+grouping&locale=en-US#applying-smart-grouping-to-your-chart
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J893] — Smart Predict

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J893 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3e3dbf93-52e2-4a08-b6f3-58b7396bc445/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8eeb62419dbd4ea38e9108f2f05a938b.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/37db2128dab44d15b46e1918829c1ff1.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite crear modelos predictivos en SAP Analytics Cloud para entregar predicciones aplicables a escenarios de análisis y planificación.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Searching Your Data Using Just Ask You can create one or several predictive models within a predictive scenario. Each predictive model produces intuitive visualizations of the results making it easy to interpret its findings. Once you have compared the key quality indicators for different models, you choose the one that provides the best answers to your business question, so you can apply this predictive model to new data sources for predictions.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3e3dbf93-52e2-4a08-b6f3-58b7396bc445/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8eeb62419dbd4ea38e9108f2f05a938b.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/37db2128dab44d15b46e1918829c1ff1.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J894] — Predictive Planning

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J894 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/66eeff9e46334644b43b10e49e2022bf.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos. La capacidad ayuda a actualizar previsiones de forma más ágil y a reducir sesgos en los ciclos de planificación.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Define the Settings of Time Series Predictive Models for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/66eeff9e46334644b43b10e49e2022bf.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J898] — Depreciation Key Explanation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J898 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/#pricing

**Resumen del caso:** Explica en lenguaje natural cómo funcionan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J89] — Configuration for US Tax Jurisdictions

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J89 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/
- Initial Setup / AI Feature (SAP Help Portal — *Resources* enlaza ambos a la misma página oficial): https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/eecd222f00914c058e3268c8aed1f112.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/#pricing

**Resumen del caso:** Permite a los contadores de impuestos agilizar la configuración de sales & use tax para Estados Unidos mediante automatización inteligente. Utiliza modelos de lenguaje (LLMs) para extraer detalles de dirección a partir de entradas en lenguaje natural y determinar automáticamente la información de jurisdiction code, reduciendo drásticamente o eliminando el mantenimiento manual y mejorando la eficiencia operativa.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Esta oferta de IA solo puede adquirirse como parte del paquete 'Joule Premium for Financial Management' y no está disponible por separado; los precios corresponden al paquete completo. Descripción del paquete: incrementa la eficiencia de los procesos financieros centrales con IA avanzada que acelera el cierre de periodo, mejora la gobernanza de datos maestros y reduce los días de ventas pendientes (DSO), entre otros. Pricing del paquete por métrica 'Users': hasta 39 usuarios → 8 AI Units por métrica (tarifa EUR 7 por AI Unit; EUR 56 por métrica); hasta 200 → 7,2; hasta 550 → 6,5; hasta 1.000 → 5,7; desde 1.000 → 5. Incluye hasta 5.200 requests sin costo adicional; las solicitudes adicionales se cobran en bloques de 1.000 a 2 AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Within the Upload Tax Rates configuration activity, open the Quick Config tab. In the Address field, enter the address or ZIP code for the location for which you need to configure the sales and use tax jurisdiction information. Based on the street address and/or ZIP code information you provide in the Address field, the AI returns the relevant jurisdiction information for you to review. The Tax Code and Jurisdiction information contains up to three levels of the relevant taxation information, that is, at the state, county, and ZIP code levels, as defined by that state's taxation authority. Once you've verified the location information, manually enter the corresponding tax rates and maintain the validity dates for each level. Then select Configure to save your changes. You can also manually maintain the District (description) and District Jurisdiction (indicator) fields. These together comprise an optional fourth level that is used as an indicator for local special use taxes. Typically, the District Jurisdiction indicator is left unfilled and by default is recorded as "0". In some cases, however, you need to add a character to indicate the special use tax. Examples of such taxes include the Metropolitan Commuter Transportation District surcharge in New York or the Historic Triangle Region sales tax surcharge in Virginia. When you perform any manual tax jurisdiction code maintenance with the AI configuration tool active, you must format the jurisdiction codes according to the SAP default structure. This is a 2-2-5-1 structure, where the first two characters are the state code, the second two characters are the county (or, in some states, independent city), the next 5 characters are the ZIP code, and the final character is a special use tax indicator, if applicable. The state codes are the postal abbreviations for the state (or territory), such as NVfor Nevada or GU for Guam. You can find the state and county codes attached to SAP Note 3613837 . When You Have Jurisdiction Codes in Your System

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/
- SAP Help Portal — Initial Setup / AI Feature (misma página): https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/eecd222f00914c058e3268c8aed1f112.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |

---

## [J90] — Smart Summarization

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J90 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite a usuarios de SAP S/4HANA Cloud Public Edition resumir contenido de páginas de objeto basadas en SAP Fiori elements y generar propuestas de texto para comunicaciones o seguimientos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Administrators can enable the AI-assisted smart summarization so users can generate an efficient summarization of an SAP Fiori elements-based object page. their business users need to have the following business catalog assigned: SAP Business AI - User Interface Features - Smart Summarization - Display (SAP_CORE_BC_AIU_SUM_PC) To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Select the role and go to the Business Catalogs tab. Ensure the SAP_CORE_BC_AIU_SUM_PC business catalog is assigned to the role, or click Add to search for it. Select it and click OK. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J91] — Easy Filter

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J91 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Optimiza la experiencia de filtrado en reportes de lista basados en SAP Fiori elements mediante lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Administrators can enable the AI-assisted easy filter in SAP Fiori elements-based applications so users can define filter queries using natural language, instead of applying filters manually. their business users need to have the following business catalog assigned: SAP Business AI - User Interface Features - Easy Filter - Display (SAP_CORE_BC_AIU_FIL_PC). To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Select the role and go to the Business Catalogs tab. Ensure the SAP_CORE_BC_AIU_FIL_PC business catalog is assigned to the role, or click Add to search for it. Select it and click OK. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J924] — Workspace

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J924 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/document-ai/sap-document-ai/subscribing-to-sap-document-ai-workspace-with-identity-authentication-service
- AI Feature (SAP Help Portal): https://help.sap.com/docs/document-ai/sap-document-ai/using-key-features-of-sap-document-ai-workspace
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/#pricing

**Resumen del caso:** SAP Document AI, workspace ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document AI**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units para usar esta oferta de IA en el servicio cloud subyacente. El método de activación indicado es “Activate with AI Units”. Precio bajo solicitud; duración del contrato disponible bajo solicitud; tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Service Plans and Metering Subscribing to the SAP Document AI Workspace With the Identity Authentication Service You have an SAP BTP global account and a Cloud Foundry or Kyma subaccount. You’re a global account administrator. The Overview screen of the SAP Document AI workspace supports efficient document processing and management. It gives you rapid access to document extractions and administrator settings, making it easy to manage and monitor documents, schemas, channels, and document statuses.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable X.509 Authentication | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 2 | Run SAP Document AI in a Multitenant Application | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 3 | Subscribe to the SAP Document AI workspace using the Identity Authentication service to handle authentication and authorization tasks in SAP BTP. | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 4 | Open the SAP BTP cockpit and go to your subaccount. | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |

**Esfuerzo total estimado (activación / configuración): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Document AI / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Document AI / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/document-ai/sap-document-ai/subscribing-to-sap-document-ai-workspace-with-identity-authentication-service
- SAP Help Portal — AI Feature: https://help.sap.com/docs/document-ai/sap-document-ai/using-key-features-of-sap-document-ai-workspace
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |

---

## [J929] — Managing Supplier Invoices

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J929 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/1fa927d7-80ce-4b9b-8ea1-8ed95be8b8d3/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule ayuda a los contadores a ejecutar acciones estándar sobre facturas de proveedor para acelerar el tiempo de procesamiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1fa927d7-80ce-4b9b-8ea1-8ed95be8b8d3/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

## [J92] — Generation of Integrations

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J92 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/464fdfbe-5809-4a0a-b6e8-65c79033837d/
- Initial Setup (SAP Help Portal — SAP Integration Suite, Artificial Intelligence): https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence
- AI Feature (SAP Help Portal — Creating an Integration Flow / Generating Integration Flows with AI Assistance): https://help.sap.com/docs/integration-suite/sap-integration-suite/creating-integration-flow
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP Integration Suite que permite generar integration flows con asistencia de IA generativa: el usuario describe el escenario de integración y la herramienta propone el flujo.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Integration Suite** (capacidad Cloud Integration / diseño de integration flows).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (SAP Integration Suite no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, un **administrador de tenant** activa y gestiona las features de IA; las features disponibles dependen de las **capabilities activadas** en el tenant de SAP Integration Suite (ver "Activating and Managing Capabilities").
- La fuente indica que la generación asistida de integration flows **está siempre activada para optimizar el diseño y no puede desactivarse**; tras la activación de la capability correspondiente, se pueden crear integration flows con asistencia de IA generativa.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- La feature de generación de integration flows no puede desactivarse (siempre activa) según la fuente.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asegurar un tenant de SAP Integration Suite con la **capability** correspondiente activada (Activating and Managing Capabilities) | Capabilities de SAP Integration Suite | General | Consultor SAP Integration Suite | 3 |
| 2 | Verificar la disponibilidad de la asistencia de IA para crear integration flows (feature siempre activada; el administrador gestiona las features de IA del tenant) | Features de IA del tenant | General | Consultor SAP Integration Suite (administrador) | 2 |

**Esfuerzo total estimado (activación / configuración): ~5 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (describir un escenario y generar el integration flow con IA) | Consultor SAP Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La generación de integration flows con IA está siempre activada y no puede desactivarse, según la fuente.
- El administrador del tenant gestiona el conjunto de features de IA disponibles en función de las capabilities activadas.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/464fdfbe-5809-4a0a-b6e8-65c79033837d/
- SAP Help Portal — Initial Setup (SAP Integration Suite — Artificial Intelligence): https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence
- SAP Help Portal — AI Feature (Creating an Integration Flow / Generating Integration Flows with AI Assistance): https://help.sap.com/docs/integration-suite/sap-integration-suite/creating-integration-flow
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 5 |
| Validación + documentación + KT | 11 |
| **Total** | **16** |

---

## [J934] — Smart Personalization of My Home for Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J934 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html?version=2602.500
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/2ae43f58ee664e288374b59db9b95bc9.html?version=2602.500
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/#pricing

**Resumen del caso:** Ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a My Home para acceso directo desde la página inicial.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units. La oferta solo puede adquirirse como parte del paquete Joule Premium for Financial Management y no está disponible por separado; el paquete se adquiere mediante AI Units. Precio bajo solicitud; duración de contrato disponible bajo solicitud.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Administrators can enable the AI-assisted smart personalization of My Home for applications. Users can then enter their queries in natural language to find and add applications and insights tiles to the My Home in SAP S/4HANA Cloud Public Edition. Their business users need to have the following business catalog assigned: SAP Business AI - My Home - Smart App Finder – Display (SAP_CORE_BC_AIU_PRO_PC) To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html?version=2602.500
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/2ae43f58ee664e288374b59db9b95bc9.html?version=2602.500
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J966] — Fixed Asset Key Figures Explanation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J966 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/780e16a7-74cf-4118-b200-c13484d2f9b5/
- Initial Setup (SAP Help Portal — Asset Accounting FI-AA, AI feature setup): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE_UPA/8f80c477fd7649a6b5bbdf479e7e1044/4b0a79f041d840729345fb41571b0a97.html?version=2025.1_UPA
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ayuda a los contadores de activos a entender los key figures de activos fijos mediante explicaciones generadas en lenguaje natural, en SAP S/4HANA Cloud Private Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition** — componente **Asset Accounting (FI-AA)**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- La fuente advierte que, para acceder a esta feature de IA generativa, **puede requerirse un entitlement y autorización adicionales** (consultar al account executive).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar la feature se debe tener asignado el business role **SAP_BR_AA_ACCOUNTANT**.
- La activación del **intelligent scenario** se realiza mediante la app Fiori **Intelligent Scenario Management (App ID: F4470)** (o por el proceso auto-turnkey).
- Los usuarios requieren además las autorizaciones específicas que la fuente lista para acceder a la feature.

### 1.5 Datos maestros / transaccionales previos
- Datos maestros de activos fijos (FI-AA) existentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para **SAP S/4HANA Cloud Private Edition**; el acceso a la feature de IA generativa puede requerir entitlement/autorización adicionales.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar el entitlement y la autorización adicionales para la feature de IA generativa (consultar al account executive) | Entitlement / autorización | General | Consultor Funcional SAP S/4HANA (FI-AA) | 3 |
| 2 | Activar el intelligent scenario (esperar el proceso auto-turnkey o activarlo manualmente con la app **Intelligent Scenario Management — F4470**) | Intelligent Scenario (ISLM) | General | Consultor Funcional SAP S/4HANA (FI-AA) | 4 |
| 3 | Asignar el business role **SAP_BR_AA_ACCOUNTANT** y las autorizaciones requeridas a los usuarios objetivo | Business Role / Autorizaciones | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (pedir explicación de key figures de activos fijos) | Consultor Funcional SAP S/4HANA (FI-AA) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (FI-AA) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (FI-AA) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Una vez activado el intelligent scenario, la feature de IA queda disponible para los usuarios con la autorización adecuada.
- La feature puede requerir entitlement y autorización adicionales (consultar al account executive).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/780e16a7-74cf-4118-b200-c13484d2f9b5/
- SAP Help Portal — Initial Setup (Asset Accounting FI-AA — AI feature): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE_UPA/8f80c477fd7649a6b5bbdf479e7e1044/4b0a79f041d840729345fb41571b0a97.html?version=2025.1_UPA
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J967] — Transformation Advisory‚ Initiative Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J967 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/
- Initial Setup (SAP Help Portal): No accesible (no existe enlace 'Initial Setup' ni 'AI Feature' accesible en *Resources*).
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Ayuda a identificar oportunidades de transformación alineadas con la estrategia y acelera la ejecución mediante la creación de iniciativas en SAP Signavio solutions.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la sección *Resources* de la Detail Page (incl. el enlace 'AI Feature' cuando existe), no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |

---

