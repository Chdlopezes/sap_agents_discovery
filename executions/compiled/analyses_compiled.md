# SAP Business AI — Análisis de Esfuerzo de Activación (Corpus RAG)

> **Última actualización:** 2026-05-28T15:54:38+00:00
> **Análisis incluidos:** 113

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
  tal como existe en `executions/analyses/<id>_<slug>_analysis.md`.

> Para cargar este corpus en un sistema RAG: trocea por sección de nivel 2
> (`##`) y trata el texto bajo cada encabezado como una unidad semántica.

---

## [J1003] — Allocation Run Results

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **Joule** en **SAP S/4HANA Cloud Public Edition** para analistas de negocio y contadores de costos que permite consultar montos asignados entre centros de costo, objetos de rentabilidad o centros de beneficio, y navegar al job y al reporte detallado de la corrida de asignación. SAP indica una **reducción del 70%** del tiempo dedicado al análisis de resultados de asignación y **40% de resolución más rápida** de problemas de asignación.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **CO – Cost Center Accounting / Profitability Analysis** operativo.
- **SAP Build Work Zone** desplegado.
- **SAP Cloud Identity Services** para identidad / SSO.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- **Joule Base** sobre el producto base — capability incluida con el entitlement estándar **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Overhead Cost Accounting / Allocation** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori del área **Allocation / Cost Accounting** (*Run Cost Center Allocation*, *Allocation Result*, según escenario).
- **Joule** habilitado en el SAP Fiori Launchpad mediante **SAP Build Work Zone**.
- Contenido de SAP Fiori Launchpad expuesto a SAP BTP.

### 1.5 Datos maestros / transaccionales previos
- Centros de costo, objetos de rentabilidad y centros de beneficio configurados.
- Ciclos de asignación definidos y corridas ejecutadas con resultados disponibles.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización sobre los objetos de Controlling consultados.

> **Setup oficial SAP**: la página https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition describe la integración de Joule con S/4HANA Cloud Public Edition: SAP Build Work Zone, exposición de SAP Fiori Launchpad a BTP, configuración de confianza/identidad y ejecución del **Joule Booster**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlements de Joule, SAP Build Work Zone y S/4HANA Cloud Public Edition | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Configurar **SAP Build Work Zone** y exponer el contenido del SAP Fiori Launchpad a SAP BTP | SAP Build Work Zone | General | Consultor SAP Build Work Zone + BTP | 4 |
| 3 | Configurar **SAP Cloud Identity Services** (confianza / SSO) entre S/4HANA Public, BTP y Build Work Zone | SAP Cloud Identity Services | General | Consultor Identity / BTP | 3 |
| 4 | Ejecutar el **Joule Booster** para integrar Joule con SAP S/4HANA Cloud Public Edition | Joule Booster | General | Consultor BTP + Joule | 3 |
| 5 | Asignar a los usuarios objetivo los business roles de Controlling con la capability de Joule habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 6 | Pruebas iniciales con un usuario piloto (consultas sobre corridas de asignación reales en Quality) | Configuración funcional CO | General | Consultor Funcional CO | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (resultados de asignación de varios ciclos / periodos) | Consultor Funcional CO | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración integrada) | Consultor Funcional CO | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica) | Consultor Funcional CO | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- El **Joule Booster** simplifica la integración, pero la coordinación entre Joule, Build Work Zone, S/4HANA Public e Identity Services hace que el esfuerzo de activación inicial sea mayor que en una capability autónoma.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Si el cliente ya tiene **Joule operativo** sobre Public Edition, los pasos 2–4 pueden saltarse y el esfuerzo se reduce significativamente.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/58e5fdf9-b00a-414b-97ef-74c65c21b10b/
- SAP Help Portal — Integration with SAP S/4HANA Cloud Public Edition: https://help.sap.com/docs/joule/integrating-joule-with-sap/integration-with-sap-s-4hana-cloud-public-edition

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J1047] — Sales Order Status Check

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule permite a los representantes de ventas comprobar si el cumplimiento de un pedido está en curso y detectar problemas que bloquean su finalización. La experiencia se orienta a consultar estado, causas y posibles acciones desde un flujo conversacional. SAP indica: *Aporta valor al reducir el tiempo de análisis manual del estado de pedidos y al facilitar acciones tempranas sobre problemas que podrían retrasar el cumplimiento.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo (incluyendo Delivery & Billing).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Fulfillment / Order to Cash — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Sales Order Fulfillment - Analyze and Resolve Issues*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Sales orders activos con deliveries, billing, ATP info.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Order Fulfillment (status profiles, blocks) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Status | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales (consultas estado, identificación de bloqueos) | Configuración funcional SD | General | Consultor SD | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (consultar status, bloqueos, predicciones de entrega) | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **consulta y diagnostica**; la resolución se ejecuta en las apps SD.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J108] — AI-Assisted Search

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Datasphere** que habilita consultas de búsqueda en lenguaje natural directamente en repository explorer, data builder, catalog y data marketplace. SAP indica una reducción del **90% en el tiempo** dedicado a solicitudes complejas de búsqueda de artefactos de datos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** (suscripción activa).
- Tenant de SAP Datasphere en un **landscape que soporte SAP Business AI** **[verificar matriz de landscapes vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Datasphere**.
- Capability **Premium** — activación con **AI Units**.
- Licencia de **AI Units** asignada al tenant **[verificar volumen vigente; precio bajo solicitud, métrica Flat Fee]**.
- Tenant **habilitado para SAP Business AI**.

### 1.3 Scope item relacionado
- No aplica scope item (SAP Datasphere no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Datasphere** con repository explorer, data builder, catalog y data marketplace activos.
- **Joule** integrado con SAP Datasphere (el botón de Joule aparece en la shell bar para usuarios con privilegio adecuado).

### 1.5 Datos maestros / transaccionales previos
- Artefactos de datos del cliente cargados en el repository (modelos, vistas, tablas, espacios).
- Catalog y/o marketplace con metadatos suficientes para indexar y buscar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: búsqueda en lenguaje natural principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: rol global con privilegios *Data Warehouse General* y *System Information* (p. ej. **DW Administrator**) para configurar; **Data Warehouse AI Consumer** para los usuarios finales.
- **Disponibilidad**: depende del landscape del tenant.

> **Setup oficial SAP**: procedimiento documentado:
> 1. Ir a **System > Configuration**.
> 2. Abrir la pestaña **AI Services**.
> 3. En **AI Features**, marcar las opciones que se quieran usar.
> 4. **Guardar**.
> 5. Asignar a los usuarios el privilegio global **Data Warehouse AI Consumer**.
>
> Los usuarios con el privilegio requerido verán el botón de Joule en la shell bar.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar que el tenant de SAP Datasphere está habilitado para SAP Business AI y en landscape compatible | Tenant Datasphere | General | Consultor SAP Datasphere + BTP | 2 |
| 2 | Confirmar entitlement de AI Units para Datasphere | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Habilitar AI Services en **System > Configuration > AI Services** y marcar las features a usar | Datasphere — AI Services | General | Consultor SAP Datasphere | 2 |
| 4 | Asignar el privilegio global **Data Warehouse AI Consumer** a los usuarios objetivo | Roles / Privilegios Datasphere | Particular (por usuario / grupo) | Consultor Seguridad SAP Datasphere | 3 |
| 5 | Pruebas iniciales con un usuario piloto (consultas en repository explorer, data builder, catalog, marketplace) | Configuración funcional Datasphere | General | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (búsquedas complejas sobre artefactos representativos) | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- La calidad de la búsqueda depende de la **calidad de los metadatos** del repository/catalog: nombres, descripciones y tags consistentes mejoran los resultados.
- Joule respeta las autorizaciones del usuario en Datasphere: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J1104] — Processing of Payment Advices with SAP Document AI

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Processing of Payment Advices with SAP Document AI automatiza el procesamiento multilingüe de avisos de pago mediante extracción y lectura asistida por IA. SAP indica: *La capacidad busca reducir tiempos de procesamiento documental, disminuir correcciones manuales y mejorar la eficiencia del equipo de cuentas por cobrar.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP).
- Componente **FI-AR – Accounts Receivable** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con FI.
- Entitlement de **SAP Document AI** (capability Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Accounts Receivable - Incoming Payments / Payment Advice — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Payment Advices*, *Post Incoming Payments*.
- Communication arrangement S/4HANA ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Maestros de clientes con configuración de payment advice.
- Open items en AR pendientes de clearing.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas soportados por Document AI según matriz vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Formato del payment advice (PDF / email parseable) soportado.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar SAP Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de payment advice extraído al documento de clearing AR | Mapping Document AI ↔ Payment Advice | Particular (por layout/cliente) | Consultor FI + Integración | 6 |
| 4 | Asignar business roles AR con catálogos de payment advice a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales: cargar payment advices reales y validar matching + clearing | Configuración funcional FI-AR | General | Consultor FI | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real de payment advices (varios layouts) | Consultor FI | 6 |
| 2 | Documentación para el cliente | Consultor FI | 4 |
| 3 | Transferencia de conocimiento | Consultor FI | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de matching** depende del payment advice y del estado de los open items.
- Volumen sujeto a cuotas de Document AI.
- El usuario sigue validando casos no automáticos antes del clearing.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |

---

## [J1114] — Supplier Confirmation Mass Creation

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite crear de forma masiva varias confirmaciones de proveedor mediante Joule en SAP S/4HANA Cloud Public Edition. El comprador puede ingresar varios pedidos de compra y apoyarse en Joule para acelerar la creación de confirmaciones. SAP indica: *Aporta eficiencia operativa en compras al reducir tiempos de procesamiento, disminuir tareas repetitivas y mejorar la oportunidad con la que se registran confirmaciones de proveedor.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM-PUR – Purchasing** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Purchasing - Confirmations — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Purchase Orders*, *Confirmations* (vista por PO/item).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, materials, purchase orders con esquema de confirmaciones activo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones MM-PUR.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración de confirmation control keys / categorías | Configuración MM-PUR | General | Consultor MM | 3 |
| 3 | Asignar business roles MM-PUR a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para mass creation de confirmaciones | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales: crear múltiples confirmaciones vía Joule en QAS | Configuración funcional MM | General | Consultor MM | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (volúmenes representativos) | Consultor MM | 4 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Mass operations: validar volumen máximo recomendado por interacción **[verificar]**.
- Usuario confirma antes de aplicar la creación masiva.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J112] — Process Analyzer, Text to Insight

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio Process Intelligence** que permite consultar datos de procesos mediante lenguaje natural y obtener insights inmediatos. Posicionada como una forma de reducir el tiempo para descubrir insights clave de procesos y ampliar el acceso organizacional al process mining.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Intelligence** (suscripción activa).
- Datos de proceso cargados (event logs) en Process Intelligence.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio Process Intelligence — Process Analyzer**.

### 1.5 Datos maestros / transaccionales previos
- Event logs y modelos de proceso cargados y consistentes en Process Intelligence.
- Buenas prácticas de naming en variantes / actividades para mejorar la calidad de las preguntas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: consultas soportadas según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: Process Analyst con permisos sobre los process logs a consultar.

> **Setup oficial SAP**: la página https://help.sap.com/docs/signavio-process-transformation-suite/sap-signavio-process-transformation-suite-administration-guide/activate-embedded-ai-capabilities?version=1.0 documenta la activación de capacidades de IA embebidas en SAP Signavio Process Transformation Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Signavio Process Intelligence | Workspace Signavio + entitlement | General | Consultor SAP Signavio | 2 |
| 2 | Activar las capacidades de IA embebidas en la administración de Process Transformation Suite | Configuración Embedded AI | General | Consultor SAP Signavio | 2 |
| 3 | Verificar que los event logs y modelos de proceso estén cargados y consistentes | Process Intelligence — Datos | Particular (por proceso) | Consultor SAP Signavio | 3 |
| 4 | Asignar a los usuarios objetivo los roles Signavio con acceso a Process Analyzer | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 5 | Pruebas iniciales con un Process Analyst piloto (preguntas representativas) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios procesos / niveles de detalle) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + buenas prácticas de prompting) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de los insights depende **directamente de la calidad de los event logs** y de la nomenclatura de actividades.
- Definir **buenas prácticas de prompting** para que la organización aproveche la capability de manera consistente.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/
- SAP Help Portal — Activate Embedded AI Capabilities: https://help.sap.com/docs/signavio-process-transformation-suite/sap-signavio-process-transformation-suite-administration-guide/activate-embedded-ai-capabilities?version=1.0

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J1137] — Electronic Document Error Handling

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Ofrece explicaciones en lenguaje natural para errores técnicos o complejos de documentos electrónicos con **Joule** en **SAP Document and Reporting Compliance**. SAP indica una reducción del **80% del tiempo** (de aproximadamente 150 minutos a 30 minutos) dedicado a entender el error e identificar la causa raíz.

> **Nota**: este caso comparte nombre con J305 pero es un registro distinto en el AI Foundation Catalog. Confirmar con SAP qué identificador aplica al cliente según su versión / régimen.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document and Reporting Compliance** (DRC) activo.
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado **[verificar matriz vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document and Reporting Compliance**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **DRC** según país / régimen fiscal aplicable — **[verificar el ID exacto en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de **DRC** habilitadas (*eDocument Cockpit* / *Statutory Reporting* según escenario).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Documentos electrónicos generados y procesados por DRC para el país objetivo.
- Errores de validación / transmisión registrados en el log de DRC.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente y disponibilidad por país]**.
- **Edición**: aplica a **SAP S/4HANA Cloud Private Edition** integrado con DRC.
- **Roles**: el usuario debe tener autorización sobre los documentos electrónicos a analizar.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/ae0b823738ee4227b7ec12cc4fbf1b4c/769137a7913747e0b2ad2315dd2e9e4f.html indica prerequisitos relacionados con *Joule Initial Setup* y la integración de Joule con S/4HANA Cloud Private Edition para *Electronic Document Error Handling*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Private Edition y DRC | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Completar el **Joule Initial Setup** para Private Edition | Joule — Initial Setup | General | Consultor BTP + Consultor S/4HANA | 4 |
| 3 | Configurar / verificar la integración Joule ↔ DRC | Integración Joule – DRC | General | Consultor S/4HANA + DRC | 3 |
| 4 | Asignar a los usuarios objetivo los business roles con acceso a DRC y a la capability Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales en Quality (provocar errores controlados en documentos electrónicos y solicitar explicación a Joule) | Configuración funcional DRC | General | Consultor Funcional DRC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con errores reales del cliente (explicaciones sobre errores de varios países / regímenes) | Consultor Funcional DRC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor Funcional DRC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional DRC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las explicaciones son **apoyo a la operación**: el usuario sigue siendo responsable de aplicar la corrección y reenviar el documento conforme a la normativa local.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Confirmar la **disponibilidad por país** dentro de DRC y la cobertura de la capability sobre los regímenes que opera el cliente.
- Validar con SAP qué entrada del catálogo (J305 o J1137) aplica a la suscripción del cliente.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d755130d-328a-4e41-b5b8-b0f507ee396c/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ae0b823738ee4227b7ec12cc4fbf1b4c/769137a7913747e0b2ad2315dd2e9e4f.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J1143] — BPMN Simulation Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Feature de **SAP Signavio** que integra simulaciones BPMN directamente en diagramas de proceso y convierte métricas como costos, tiempos de ciclo y uso de recursos en insights impulsados por IA. SAP no publica un KPI cuantitativo específico en la página consultada; el valor se centra en acelerar la toma de decisiones de mejora de procesos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Manager / Modeler** (suscripción activa).
- Diagramas BPMN del cliente cargados con datos de simulación necesarios.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Premium** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio Process Manager / Modeler** con la función de simulación BPMN habilitada.

### 1.5 Datos maestros / transaccionales previos
- Diagramas BPMN modelados con suficiente granularidad.
- Parámetros de simulación: **costos**, **duración**, **frecuencia** y **recursos** definidos en los elementos del proceso.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Process Analyst / Process Owner con permisos sobre los diagramas BPMN a simular.

> **Setup oficial SAP**: la página https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams describe el uso de la simulación BPMN. No se identificaron prerequisitos técnicos de activación adicionales en el enlace consultado.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Premium de SAP Signavio | Workspace Signavio + entitlement Premium | General | Consultor SAP Signavio | 2 |
| 2 | Verificar que los diagramas BPMN tengan los parámetros de simulación correctos (costos, duración, recursos) | Diagramas BPMN del workspace | Particular (por diagrama / proceso) | Consultor SAP Signavio + Process Analyst | 4 |
| 3 | Asignar a los usuarios objetivo los roles SAP Signavio con acceso a simulación | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 4 | Pruebas iniciales con un Process Analyst piloto (ejecutar simulaciones y revisar los insights de IA) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con diagramas reales del cliente (simulaciones sobre procesos representativos y revisión de insights) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración de simulación) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad de los insights depende de la **calidad de los parámetros de simulación**: estimaciones poco realistas producen recomendaciones engañosas.
- Es una capability **Premium**: verificar entitlement vigente antes de planificar.
- Los insights son **apoyo a la decisión** del Process Analyst; la decisión final de rediseño sigue siendo humana.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/
- SAP Help Portal — Simulating BPMN diagrams: https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |

---

## [J114] — Generation of SAP Fiori Elements and SAPUI5 Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Project Accelerator simplifica el desarrollo convirtiendo requerimientos de negocio desde texto, imágenes o ambos en un proyecto full-stack con una aplicación SAP Fiori elements funcional. Se puede acceder desde el panel de SAP Fiori o mediante un comando en Joule. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar el desarrollo de aplicaciones Fiori/SAPUI5 y permitir que el equipo se enfoque en aspectos más complejos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- OData / RAP services back-end donde se generan las apps Fiori.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a backends OData/RAP | Destinations | Particular (por backend) | Consultor BTP | 3 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Fiori Elements/UI5 Generation | Configuración Build Code | General | Consultor BTP / Dev | 2 |
| 5 | Pruebas iniciales: generar app Fiori Elements | Configuración Build Code | General | Desarrollador Fiori | 4 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador Fiori | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador Fiori | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Fiori | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Código generado requiere review (annotations, navegación, performance).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 12 |
| **Total** | **26** |

---

## [J115] — Generation of SAP Mobile Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code. Puede generar componentes a partir de lenguaje natural, incluyendo código, modelos de datos, servicios, lógica de negocio, datos de ejemplo y pruebas unitarias. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar el desarrollo móvil y reducir esfuerzo manual en componentes técnicos repetitivos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.
- **SAP Mobile Services / Mobile Development Kit (MDK)** disponible **[verificar packaging vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.
- Entitlement Mobile Services / MDK si requerido.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.
- Mobile Services Cockpit (para despliegue / runtime).

### 1.5 Datos maestros / transaccionales previos
- Backends OData / RAP configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Mobile Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule + Mobile Services | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar Mobile Services (app registration, push) | Mobile Services Cockpit | General | Consultor Mobile | 5 |
| 3 | Asignar rol Mobile Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Mobile App Generation | Configuración Build Code | General | Consultor Mobile / Dev | 2 |
| 5 | Pruebas iniciales: generar app móvil de muestra y desplegar | Configuración Build Code | General | Desarrollador Mobile Sr | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria en device real (iOS/Android) | Desarrollador Mobile Sr | 6 |
| 2 | Documentación + buenas prácticas | Desarrollador Mobile Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Mobile Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- Considerar offline-first, security (MDM), distribución (stores corporativas).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 13 |
| **Total** | **30** |

---

## [J116] — Generation of SAP HANA Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código. La capacidad ayuda a crear modelos de datos, servicios, lógica de aplicación y pruebas desde lenguaje natural; además, incluye herramientas generativas para crear sentencias SQL desde prompts. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar extensiones y aplicaciones HANA, mejorar productividad del desarrollador y facilitar un enfoque clean core.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.
- **SAP HANA Cloud** disponible como backend.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.
- Entitlement HANA Cloud.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- HANA Cloud DB provisionada; esquemas / HDI containers configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Developer con permisos HANA Cloud.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule + HANA Cloud | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar conexión HANA Cloud (HDI container, schema) | DB setup | General | Consultor HANA | 4 |
| 3 | Asignar rol Developer + HANA roles | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar HANA App Generation | Configuración Build Code | General | Consultor HANA / Dev | 2 |
| 5 | Pruebas iniciales: generar app CAP+HANA con prompts | Configuración Build Code | General | Desarrollador HANA Sr | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador HANA Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador HANA Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador HANA Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Modelado de datos HANA (CDS, calculation views) merece review especializado.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |

---

## [J117] — Form Extension in Localization as a Self-Service

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Genera y actualiza automáticamente formularios localizados personalizados según requisitos de negocio, enlaza fuentes de datos y carga los formularios en SAP S/4HANA Cloud Public Edition. SAP indica: *Reducción estimada del 80% en tiempo y costo para crear plantillas de formularios localizados.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Framework de **Form Templates / Localization Toolkit** activo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción a S/4HANA Public Edition.
- Entitlement de Joule; capability **Base** **[verificar en AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- Scope items de localización del país objetivo (output management / forms) — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori *Maintain Form Templates* (o equivalente vigente).
- Output Management / Form determination configurado.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Form templates base por país disponibles y activos.
- Procesos de output que consuman dichos formularios.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- País/localización debe estar soportado por el set de templates vigente.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración de Output Management / Form Templates | Output Management / Forms | General | Consultor Funcional Output | 3 |
| 3 | Asignar business roles con catálogos de Form Templates a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar la capability de Joule para extensión de formularios | Joule capability scope | General | Consultor Funcional + Joule | 2 |
| 5 | Pruebas: extender un template por localización con prompt + validar render del documento | Configuración funcional Output | General | Consultor Funcional | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con templates reales del cliente | Consultor Funcional Output | 4 |
| 2 | Documentación para el cliente | Consultor Funcional Output | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional Output | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Es un **self-service**: el usuario clave (no desarrollador) extiende localizaciones sin código.
- Joule respeta los límites técnicos del framework de Forms; cambios estructurales fuertes pueden requerir extensión clásica.
- Revisar la lista de **localizaciones soportadas** en SAP Help antes del rollout.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J1182] — Settlement Rule Proposal for Asset Capitalization

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Propone reglas de liquidación para la capitalización de activos en medidas de inversión. La funcionalidad asiste la creación de reglas completas y ayuda a determinar receptores de liquidación mediante IA generativa. SAP indica: *Ahorro de tiempo en procesos de Asset Accounting y Project/Investment Management, menor riesgo de errores manuales en reglas de liquidación y mayor trazabilidad en la revisión de propuestas.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componentes **FI-AA – Asset Accounting** + **IM/PS – Investment / Project System** operativos.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Asset Capitalization / Investment Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de Investment Measures / Settlement Rules.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Maestros de Investment Orders / WBS, asset classes, settlement profiles.
- Histórico de settlements para entrenar/recomendar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones FI-AA / IM.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración FI-AA / IM (settlement profiles, asset classes) | Configuración FI-AA / IM | General | Consultor FI-AA | 4 |
| 3 | Asignar business roles FI-AA / IM a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Settlement Rule Proposal | Joule capability scope | General | Consultor Funcional FI-AA + Joule | 3 |
| 5 | Pruebas iniciales con investment orders reales | Configuración funcional FI-AA | General | Consultor FI-AA | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios tipos de capex) | Consultor FI-AA | 5 |
| 2 | Documentación para el cliente | Consultor FI-AA | 4 |
| 3 | Transferencia de conocimiento | Consultor FI-AA | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad de propuesta depende del histórico de capitalización.
- Aprobación / posting final lo decide el contador.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |

---

## [J1195] — SAP Joule for Developers, ABAP AI capabilities (S/4HANA Cloud Private Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante del caso para Private Edition. Ver J792 (Public) y J162 (BTP ABAP Environment) para las otras variantes.

**Resumen del caso:** Joule for Developers con capacidades ABAP AI apoya el desarrollo ABAP en SAP S/4HANA Cloud Private Edition, ayudando a desarrolladores con asistencia generativa dentro del ciclo de desarrollo. SAP indica: *La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA y beneficios de eficiencia en desarrollo.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con **Developer Extensibility / On-Stack Developer Extensibility** habilitada según release.
- **ADT (ABAP Development Tools) for Eclipse** actualizado.
- Joule habilitado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule for Developers (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A (capability transversal de desarrollo).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- ADT for Eclipse + extensión Joule.
- Conectividad ADT ↔ tenant.

### 1.5 Datos maestros / transaccionales previos
- Developer extensibility configurada; paquetes y transports existentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- En Private, validar compatibilidad de release y modelo de extensibilidad (cloud / classic) **[verificar matriz vigente]**.
- Usuario con rol de desarrollador.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar Developer Extensibility en Private | Configuración Developer Extensibility | General | Consultor S/4HANA Private | 4 |
| 3 | Instalar/actualizar extensión Joule en ADT | Setup ADT | Particular (por puesto) | Desarrollador ABAP | 2 |
| 4 | Asignar Developer Role | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con casos representativos | Configuración Developer | General | Desarrollador ABAP Sr | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador ABAP Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador ABAP Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador ABAP Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Code review humano obligatorio sobre código generado.
- En Private, considerar restricciones del modelo de extensibilidad clásico vs cloud.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J120] — Performance Indicators Recommender

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio** que ayuda a pasar del problema de negocio a un enfoque de medición recomendando KPIs y PPIs relevantes desde un repositorio amplio de indicadores de desempeño de procesos. SAP indica **5% menor erosión de valor** asociada a una selección deficiente de indicadores.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio solutions** (suscripción activa).
- Acceso a procesos / modelos relevantes del cliente en SAP Signavio.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Premium** — activación con **AI Units** según *Pricing Details*.
- **AI Units** asignadas; pricing estimable mediante el AI Estimator de SAP **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio** con modelos de proceso del cliente y acceso al repositorio de PPIs.

### 1.5 Datos maestros / transaccionales previos
- Definición clara del problema de negocio o proceso para el que se buscan indicadores.
- Modelos / event logs disponibles para conectar los indicadores recomendados con datos reales (cuando aplique).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Business Process Analyst / Process Owner.

> **Setup oficial SAP**: la página https://help.sap.com/docs/signavio-process-insights/business-content-reference/process-performance-indicators referencia el catálogo de indicadores. La activación de la capability se realiza mediante AI Units según el Pricing Details.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Premium y AI Units para SAP Signavio | Workspace Signavio + AI Units | General | Consultor SAP Signavio + BTP / Licencias | 2 |
| 2 | Estimar AI Units necesarios para el volumen previsto (AI Estimator) | AI Units — Estimación | General | Consultor SAP Signavio | 2 |
| 3 | Habilitar la capability del Performance Indicators Recommender en el workspace | Workspace Signavio — AI Capabilities | General | Consultor SAP Signavio | 2 |
| 4 | Asignar a los usuarios objetivo los roles Signavio con acceso a la capability | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 5 | Pruebas iniciales con un Process Analyst piloto (recomendaciones sobre procesos representativos) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (procesos / problemas representativos, revisión y adopción de KPIs/PPIs sugeridos) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: estimar el consumo con el AI Estimator de SAP antes del go-live.
- Los indicadores sugeridos son **recomendaciones**: deben validarse con stakeholders y conectarse con datos / event logs para que el marco de medición sea operativo.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/
- SAP Help Portal — Process Performance Indicators: https://help.sap.com/docs/signavio-process-insights/business-content-reference/process-performance-indicators

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |

---

## [J121] — Process Recommender (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio. SAP indica: *La capacidad apunta a mejorar la productividad de recursos BPM, reducir costos de consultoría para mapeo de procesos y disminuir el tiempo de capacitación interna.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Insights** o equivalente con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Insights / Recommendations **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Insights UI.

### 1.5 Datos maestros / transaccionales previos
- Process data conectado (S/4HANA / otros sistemas) suficientemente poblado.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Process Insights user.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Conectar data sources (S/4HANA / otros) | Conexiones Signavio | General | Consultor Signavio | 5 |
| 3 | Asignar roles a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Process Recommender | Signavio admin | General | Consultor Signavio | 2 |
| 5 | Pruebas iniciales (revisar recomendaciones) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Calidad de recomendaciones depende de la cobertura/volumen de datos del proceso.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 10 |
| **Total** | **24** |

---

## [J127] — Joule with SAP Signavio solutions

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural. SAP indica: *50% más rapidez en búsquedas informativas; 50% más rapidez en ejecución de tareas de navegación y transaccionales; mejor calidad de resultados de búsqueda y experiencia de usuario.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Transformation Suite** (Process Manager, Process Intelligence, Process Insights, etc.) activo.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio (módulos aplicables).
- Entitlement Joule + capability Signavio **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace Signavio.
- Joule integrado en Signavio UI.

### 1.5 Datos maestros / transaccionales previos
- Modelos BPMN, mining de datos, KPI definidos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Signavio.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Signavio + Joule capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO Signavio | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Signavio | Signavio admin | General | Consultor Signavio | 3 |
| 4 | Asignar roles Signavio a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas y acciones sobre procesos) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con modelos/datos reales | Consultor Signavio | 5 |
| 2 | Documentación para el cliente | Consultor Signavio | 4 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Cobertura de capabilities Joule dentro de Signavio se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |

---

## [J1284] — Document Data Extraction

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que extrae y procesa automáticamente información clave de **PDFs e imágenes escaneadas** usando IA, con o sin plantillas. SAP indica beneficios como **500 horas ahorradas por mes**, **70% de facturas procesadas sin intervención manual** y procesamiento de una factura en **menos de 1 minuto** desde la llegada hasta la contabilización.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Capacidad de extracción documental habilitada para PDFs e imágenes.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con módulos de procesos / workflow activos.
- Plantillas de extracción preconfiguradas o personalizadas (según el tipo de documento).

### 1.5 Datos maestros / transaccionales previos
- Documentos representativos de cada tipo a procesar (facturas, órdenes de compra, avisos de pago).
- Si se requiere salida a un sistema destino (p. ej. S/4HANA), conectividad y datos maestros del destino consistentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción documentados por SAP **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos escaneados con baja calidad reducen la tasa de extracción correcta.
- **Roles**: roles de Build Process Automation para definir y operar la extracción.

> **Setup oficial SAP**: la página https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai describe el uso de Document Data Extraction desde SAP Build Process Automation. El texto extraído no expone un paso a paso administrativo más detallado.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidad de extracción documental | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Habilitar / validar la capacidad de Document Data Extraction en el subaccount | Configuración Build Process Automation — Extracción | General | Consultor BTP / Build | 2 |
| 3 | Configurar plantillas (predefinidas o personalizadas) para los tipos de documento del cliente | Plantillas de extracción | Particular (por tipo de documento) | Consultor Build Process Automation | 4 |
| 4 | Configurar el flujo (workflow / proceso) que consume la extracción y la entrega al sistema destino | Workflow / Proceso Build | Particular (por proceso) | Consultor Build Process Automation | 4 |
| 5 | Asignar a los usuarios objetivo los roles con acceso a la operación | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 6 | Pruebas iniciales con documentos reales del cliente en Quality | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (facturas, OCs, avisos de pago de varios proveedores/formatos) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación / monitoreo) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión de operación) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La **tasa de extracción correcta** depende de la calidad de los documentos y de la cobertura de plantillas; planificar un periodo de afinamiento.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza: intervención humana o re-clasificación.
- Considerar **gobernanza** sobre dónde se procesa el documento (data residency) y sobre la **retención** de los datos extraídos.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- SAP Help Portal — Generative AI in Build Process Automation: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |

---

## [J1310] — Purchase Order Approvals Reminder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **Joule** en **SAP S/4HANA Cloud Public Edition** que ayuda a dar seguimiento a aprobaciones de órdenes de compra, identificar aprobadores y enviar recordatorios automatizados dentro del flujo de procurement. El valor se centra en reducir retrasos en aprobaciones y disminuir el seguimiento manual.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM – Procurement / Purchase Order Workflow** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Operational Procurement / Purchase Order Approval** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori del área **Procurement** (*Manage Purchase Orders*, *My Inbox* / *Manage Workflows*).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.
- Workflow de aprobación de órdenes de compra configurado.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de aprobadores y matriz de responsables definidos en el workflow.
- Órdenes de compra existentes con aprobaciones pendientes para validar la capability.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: Procurement Specialist / Approver con permisos sobre el workflow de aprobación.

> **Setup oficial SAP**: la página https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders sirve como referencia general de Joule capabilities en procurement. La configuración base de Joule debe estar completada antes de habilitar la capability.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Validar configuración base del **workflow de aprobación** de órdenes de compra (responsables, reglas) | Workflow PO Approval | Particular (por escenario / org) | Consultor MM / Procurement | 3 |
| 3 | Asignar a los usuarios objetivo los business roles de Procurement con la capability de Joule habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar la capability *Purchase Order Approvals Reminder* en Joule | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales con un usuario piloto (consultar aprobaciones pendientes, enviar recordatorios) | Configuración funcional MM | General | Consultor MM / Procurement | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (aprobaciones pendientes representativas y recordatorios end-to-end) | Consultor MM / Procurement | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor MM / Procurement | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor MM / Procurement | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **complementa el workflow de aprobación**, no lo reemplaza: si el workflow está mal configurado, los recordatorios irán al destinatario incorrecto.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Considerar **buenas prácticas de comunicación** (frecuencia de recordatorios) para evitar fatiga de notificaciones.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/
- SAP Help Portal — Joule Capabilities Guide (Procurement): https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J1394] — Document Summary

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Cloud ALM** que permite resumir documentación mediante IA dentro de la aplicación *Documents*. SAP no publica un KPI cuantitativo específico en la página consultada; el valor se centra en reducir el tiempo de lectura manual.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Cloud ALM** (suscripción activa).
- Aplicación **Documents** habilitada dentro del tenant SAP Cloud ALM.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Cloud ALM**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Cloud ALM — Documents**.

### 1.5 Datos maestros / transaccionales previos
- Documentos cargados en SAP Cloud ALM con contenido suficiente para que un resumen sea significativo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Cloud ALM **[verificar idiomas soportados vigentes]**.
- **Roles**: el usuario debe tener acceso al documento que va a resumir.
- **Tamaño / formato**: posibles límites sobre tamaño o tipo de documento **[verificar]**.

> **Setup oficial SAP**: la página https://help.sap.com/docs/cloud-alm/applicationhelp/documents indica que SAP Cloud ALM usa capacidades de IA para generar el resumen de contenido de documentos. El uso se realiza directamente desde la aplicación *Documents*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Cloud ALM con capacidades de IA | Tenant SAP Cloud ALM | General | Consultor SAP Cloud ALM | 2 |
| 2 | Asignar a los usuarios objetivo el rol de acceso a la app *Documents* | Roles SAP Cloud ALM | Particular (por usuario / grupo) | Consultor Seguridad SAP Cloud ALM | 2 |
| 3 | Pruebas iniciales con un usuario piloto (resumir documentos representativos en *Documents*) | Configuración funcional SAP Cloud ALM | General | Consultor SAP Cloud ALM | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (resumir documentos de varios tipos / longitudes) | Consultor SAP Cloud ALM | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Cloud ALM | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Cloud ALM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- El resumen es **descriptivo**: el usuario debe validar que captura los puntos clave antes de tomar decisiones.
- Útil principalmente en **handovers de proyecto y onboarding**: comunicar a los usuarios el alcance esperado.
- Sujeto a las condiciones de servicio vigentes de SAP Cloud ALM **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/111df0da-5177-4769-88ea-6a200ecae091/
- SAP Help Portal — Documents in SAP Cloud ALM: https://help.sap.com/docs/cloud-alm/applicationhelp/documents

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |

---

## [J145] — Joule with SAP Build Work Zone

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo. También soporta acceso remoto mediante SAP Mobile Start o sitio móvil. SAP indica: *50% más rapidez en búsquedas informativas; 59% más rapidez en ejecución de tareas de navegación y transaccionales; mayor satisfacción del usuario de negocio.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Work Zone** (standard edition o advanced) en BTP.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Build Work Zone.
- Entitlement Joule + capability Work Zone **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant Work Zone configurado.
- Joule habilitado dentro de Work Zone.

### 1.5 Datos maestros / transaccionales previos
- Aplicaciones integradas en Work Zone con sus destinations/roles.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Catálogo de apps con soporte Joule.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Work Zone + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Work Zone | Work Zone settings | General | Consultor Work Zone | 3 |
| 4 | Asignar roles a usuarios | Roles | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (interactuar con apps vía Joule en Work Zone) | Configuración Work Zone | General | Consultor Work Zone | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Work Zone | 4 |
| 2 | Documentación para el cliente | Consultor Work Zone | 4 |
| 3 | Transferencia de conocimiento | Consultor Work Zone | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Cobertura de apps con soporte Joule se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |

---

## [J146] — SAP Joule for Consultants

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud. Está orientado a consultores y equipos de implementación que necesitan acceso guiado a conocimiento, recomendaciones y soporte durante actividades de delivery. SAP indica: *La página posiciona el valor en acelerar la entrega de proyectos SAP, mejorar la productividad del equipo consultor y facilitar el acceso a conocimiento SAP relevante durante transformaciones cloud.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP con capability "for Consultants" **[verificar]**.
- Integración con **SAP Learning** / **SAP Help** / **Cloud ALM** según las funciones cubiertas.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule for Consultants (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible para consultores.

### 1.5 Datos maestros / transaccionales previos
- Cuenta consultor con accesos requeridos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule for Consultants | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO con identidad corporativa | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Asignar acceso a consultores | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Pruebas iniciales (consultas sobre best practices, soluciones) | Configuración base | General | Consultor Sr | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios típicos de proyecto | Consultor Sr | 4 |
| 2 | Documentación para el cliente | Consultor Sr | 3 |
| 3 | Transferencia de conocimiento | Consultor Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Pensado para acelerar consultores, no sustituirles.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 10 |
| **Total** | **23** |

---

## [J147] — Script Optimization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Integration Suite** que ayuda a optimizar scripts personalizados en Cloud Integration. SAP indica que la función está disponible como **promoción gratuita hasta septiembre de 2026** y posteriormente pasará a ser una función **Premium**.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (suscripción activa).
- **Cloud Integration** dentro de SAP Integration Suite con iFlows que contengan scripts personalizados.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Integration Suite**.
- Capability **Base** **hasta septiembre de 2026** (promoción gratuita); posteriormente pasa a **Premium** **[verificar fecha exacta de transición vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Integration Suite — Cloud Integration** con capacidades de IA habilitadas.

### 1.5 Datos maestros / transaccionales previos
- iFlows del cliente con scripts personalizados (Groovy / JavaScript) a optimizar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Lenguajes soportados**: principalmente Groovy y JavaScript según lo permitido por Cloud Integration **[verificar matriz vigente]**.
- **Roles**: Integration Developer con acceso a Cloud Integration y a artefactos de integración.

> **Setup oficial SAP**: la página https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence describe las capacidades de IA disponibles en SAP Integration Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Integration Suite con Cloud Integration | Subaccount BTP + entitlement Integration Suite | General | Consultor BTP | 2 |
| 2 | Habilitar / validar las capacidades de IA en SAP Integration Suite | Configuración Integration Suite — AI | General | Consultor Integration Suite | 2 |
| 3 | Asignar a los developers los roles con acceso a la capability | Roles SAP Integration Suite | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer piloto (optimizar scripts representativos) | Configuración funcional Integration Suite | General | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con scripts reales del cliente (revisión de recomendaciones y validación de comportamiento del iFlow tras los cambios) | Consultor Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de scripting) | Consultor Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica) | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Después de **septiembre de 2026** la función deja de ser gratuita: **planificar el modelo de costos** para uso continuo bajo el esquema Premium.
- Las recomendaciones son **sugerencias**: el developer debe revisar cada cambio antes de aplicarlo a un iFlow productivo.
- Definir un **proceso de control** sobre cuándo y quién aplica optimizaciones a iFlows productivos.
- Sujeto a las condiciones de servicio vigentes de SAP Integration Suite **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/
- SAP Help Portal — Artificial Intelligence in Integration Suite: https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J148] — Analytical Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **Joule** que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP, integrándose con **Just Ask** de SAP Analytics Cloud (SAC) dentro de SAP Business Data Cloud (BDC). SAP indica hasta **80% de reducción** en los pasos necesarios para obtener insights analíticos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado y operativo.
- **SAP Analytics Cloud (SAC)** o **SAP Business Data Cloud (BDC)** con **Just Ask** configurado.
- **SAP Build Work Zone** desplegado para entregar la experiencia integrada al usuario.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **Joule**.
- Suscripción vigente a **SAP Analytics Cloud** y/o **SAP Business Data Cloud**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **Joule** integrado con SAC / BDC.
- **Just Ask** activado y con datos indexados.
- **SAP Build Work Zone** con tarjetas / launchpad del usuario configurados.
- **Identity Provisioning Service (IPS)** para sincronización de usuarios y roles.

### 1.5 Datos maestros / transaccionales previos
- Modelos / historias de SAC publicadas con datos consistentes.
- Datos indexados en **Just Ask** para que las preguntas en lenguaje natural devuelvan resultados.
- Roles y permisos sincronizados desde el directorio fuente hacia SAP Build Work Zone.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: usuarios provisionados en SAP Build Work Zone con permisos SAC/BDC adecuados.
- **Integración**: requiere coexistencia funcional entre Joule, SAC/BDC, Just Ask y Work Zone.

> **Setup oficial SAP**: el procedimiento descrito en https://help.sap.com/docs/joule/integrating-joule-with-sap/enable-the-analytical-insights-capability-in-joule consiste en: habilitar la capability *Analytical Insights* en Joule, integrar SAC/BDC con Joule, sincronizar roles y permisos, provisionar usuarios hacia SAP Build Work Zone usando IPS, indexar datos con Just Ask y probar preguntas en lenguaje natural.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule, SAC/BDC y SAP Build Work Zone | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Configurar la integración Joule ↔ SAC / BDC | Joule capability *Analytical Insights* + integración SAC/BDC | General | Consultor BTP + Consultor SAC | 4 |
| 3 | Configurar **SAP Build Work Zone** con las tarjetas / espacios necesarios | SAP Build Work Zone | General | Consultor SAP Build Work Zone | 3 |
| 4 | Sincronizar usuarios y roles vía **Identity Provisioning Service (IPS)** | IPS — Provisioning | Particular (por usuarios / grupos) | Consultor Seguridad / Identity | 3 |
| 5 | Indexar datos en **Just Ask** y validar que las consultas devuelvan resultados | Just Ask — Indexing | General | Consultor SAC | 4 |
| 6 | Asignar a los usuarios objetivo los roles con la capability habilitada | Roles SAC / BDC + Joule | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 7 | Pruebas iniciales end-to-end con un usuario piloto (preguntas desde Joule sobre datos de SAC/BDC) | Configuración funcional integrada | General | Consultor SAC + Consultor Joule | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~21 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria end-to-end con datos reales (preguntas representativas de varios dominios funcionales) | Consultor SAC + Consultor Joule | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración integrada) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica) | Consultor SAC + Consultor BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una integración **multi-producto**: Joule + SAC/BDC + Just Ask + SAP Build Work Zone + IPS. Confirmar disponibilidad y compatibilidad de versiones antes de planificar.
- La calidad de las respuestas depende de **modelos publicados y datos indexados** en Just Ask: invertir en metadatos y semántica.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y a las cuotas vigentes de SAC **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/enable-the-analytical-insights-capability-in-joule

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 21 |
| Validación + documentación + KT | 11 |
| **Total** | **32** |

---

## [J151] — Master Data Governance

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite usar lenguaje natural para crear y actualizar solicitudes de cambio de datos maestros dentro de procesos de Master Data Governance en SAP S/4HANA Cloud Private Edition. SAP indica: *60% de reducción del esfuerzo para crear solicitudes de cambio de datos maestros; 20% de reducción del esfuerzo para revisar solicitudes de cambio; la página también indica una reducción adicional del 5% en un indicador que aparece truncado en el contenido accesible.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Master Data Governance (MDG)** activo (data domain aplicable: customers, suppliers, materials, finance, etc.).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition con MDG.
- Entitlement Joule **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Master Data Governance por dominio — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori MDG (*Manage Change Requests*, *Process Change Requests*).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Configuración MDG por dominio: data models, workflows, validation rules.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones MDG (requestor / processor / approver).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración MDG (workflows, change request types) | Configuración MDG | General | Consultor MDG | 4 |
| 3 | Asignar business roles MDG a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para creación de CRs y summaries | Joule capability scope | General | Consultor Funcional MDG + Joule | 3 |
| 5 | Pruebas iniciales: crear CR vía Joule + generar summary | Configuración funcional MDG | General | Consultor MDG | 3 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (CRs por dominio + summaries) | Consultor MDG | 5 |
| 2 | Documentación para el cliente | Consultor MDG | 4 |
| 3 | Transferencia de conocimiento | Consultor MDG | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Joule asiste, no sustituye al governance flow (approval levels siguen aplicando).
- Cobertura por dominio puede variar — revisar **Road Map Explorer**.
- Respeta autorizaciones MDG.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J162] — SAP Joule for Developers, ABAP AI capabilities (SAP BTP, ABAP environment)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante para SAP BTP, ABAP environment (Steampunk). Ver J792 (S/4HANA Public) y J1195 (S/4HANA Private).

**Resumen del caso:** Joule for Developers con capacidades ABAP AI ayuda a acelerar el desarrollo ABAP en SAP BTP, ABAP environment mediante asistencia generativa para tareas de desarrollo. SAP indica: *La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA, junto con mejoras de productividad en actividades de desarrollo.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP BTP, ABAP environment** (Steampunk) activo.
- **ADT (ABAP Development Tools) for Eclipse**.
- Joule habilitado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción BTP ABAP environment.
- Entitlement Joule for Developers (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A (capability transversal).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- ADT + extensión Joule.
- Conectividad ADT ↔ ABAP environment.

### 1.5 Datos maestros / transaccionales previos
- Service instance ABAP environment provisionada; paquetes; transports.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo cloud ABAP (RAP / ABAP for Cloud Development).
- Usuario Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement BTP ABAP env + Joule for Developers | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Crear/configurar service instance ABAP environment | Service Instance | General | Consultor BTP / ABAP | 4 |
| 3 | Instalar/actualizar extensión Joule en ADT | Setup ADT | Particular (por puesto) | Desarrollador ABAP | 2 |
| 4 | Asignar Developer Role | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (generar clase / RAP / unit tests con prompts) | Configuración Developer | General | Desarrollador ABAP Sr | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador ABAP Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador ABAP Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador ABAP Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Code review humano obligatorio.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |

---

## [J1684] — Enterprise Architecture Decision Management

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que analiza y extrae datos relevantes para generar entradas de decisiones de arquitectura con el contexto e información que los stakeholders necesitan para aprobarlas.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente con inventario y landscape cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture / Decision Management activos.

### 1.5 Datos maestros / transaccionales previos
- Inventario de aplicaciones, capacidades de negocio y stakeholders cargados en LeanIX.
- Procesos formales de decisión de arquitectura definidos (qué se decide y quién aprueba).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: Enterprise Architect / EA Admin con permisos sobre decisiones y stakeholders.

> **Nota**: el recurso *Initial Setup* existe en la página de detalle, pero no fue posible extraer texto suficiente desde la herramienta para identificar prerequisitos concretos. Aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Configurar el módulo de **Decision Management** según los procesos del cliente (categorías de decisión, stakeholders, plantillas) | Decision Management — Configuración | Particular (por categoría de decisión) | Consultor SAP LeanIX + Enterprise Architect | 4 |
| 4 | Asignar a los usuarios objetivo los roles LeanIX con acceso a la capability | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Enterprise Architect piloto (generar entradas de decisión asistidas por IA) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con decisiones reales del cliente (varios tipos / dominios) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación EA) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo de Enterprise Architecture | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de las entradas generadas depende **directamente del inventario y datos contextuales** del workspace.
- Las decisiones siguen siendo **responsabilidad de los stakeholders aprobadores**: la IA prepara, los humanos deciden.
- Definir **gobernanza** del flujo: quién revisa, quién aprueba, quién publica.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J169] — Sales Order Fulfillment Monitoring

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** La capacidad ayuda a los equipos de ventas a monitorear y resolver problemas de cumplimiento de pedidos mediante IA. Los pedidos se resumen a nivel de cabecera e ítem en lenguaje natural, se identifican problemas de fulfillment y se facilita la navegación hacia acciones correctivas. SAP indica: *La página destaca un 30% más de productividad del personal en consultas de pedidos de venta y una reducción del 10% en churn de clientes asociado a retrasos en fulfillment.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componentes **SD – Sales / LE / FI-AR** operativos.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule (capability con componente de IA) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Order to Cash / Sales Order Fulfillment — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori *Sales Order Fulfillment - Analyze and Resolve Issues*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Sales orders activos, deliveries, billing, payment.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Order Fulfillment / issues categorization | Configuración SD/LE | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Fulfillment Monitoring | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: identificar issues + sugerir resolución | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (bloqueos crédito, stock, billing) | Consultor SD | 5 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Joule sugiere resolución; ejecución la decide el clerk.
- Cobertura de issue types se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 12 |
| **Total** | **25** |

---

## [J178] — Inventory Builder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP LeanIX Inventory Builder** acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX. El valor se centra en reducir el esfuerzo manual para construir y mantener inventarios de arquitectura empresarial.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente disponible.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Premium** — activación con **AI Units** **[verificar volumen vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture activos.

### 1.5 Datos maestros / transaccionales previos
- Fuentes de datos a cargar / analizar (planillas, CMDB, exportaciones de otros sistemas) para que el builder pueda procesarlas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Formatos / volumen**: el contenido accesible no detalla límites técnicos exactos **[verificar]**.
- **Roles**: EA Admin / Workspace Admin con acceso a Inventory Builder.

> **Setup oficial SAP**: la página https://help.sap.com/docs/leanix/ea/ai-capabilities describe la activación de AI Capabilities en SAP LeanIX. El contenido completo del procedimiento específico de Inventory Builder no fue totalmente extractable.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Confirmar AI Units asignadas para Inventory Builder | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 4 | Preparar las fuentes de datos (formatos, calidad, mapeos) que va a procesar Inventory Builder | Fuentes de datos | Particular (por fuente) | Consultor SAP LeanIX + Cliente Funcional | 5 |
| 5 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Inventory Builder | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 6 | Pruebas iniciales con datos representativos (cargas controladas y validación de resultados) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (varios formatos / dominios) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Los datos cargados deben pasar por **revisión humana** antes de promoverse a producción: la IA acelera, no reemplaza el control de calidad de datos.
- Considerar **gobernanza** sobre qué fuentes de datos están autorizadas a ingresar al workspace.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 11 |
| **Total** | **28** |

---

## [J180] — SAP HANA application migration

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Función que automatiza la migración de la capa de servicios **SAP HANA XS/XSA** hacia **SAP CAP** usando GenAI. Convierte artefactos como **XSJSLIB, XSODATA y XSJS** en servicios modernos basados en CAP, alineados con la guía de desarrollo de SAP BTP.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP HANA Cloud** activo.
- Proyecto **SAP HANA XS Advanced (XSA)** o **XS Classic** del cliente a migrar.
- Entorno de desarrollo soportado (típicamente **Visual Studio Code** con la extensión correspondiente).
- Servicios SAP BTP / SAP AI según aplique para la conversión asistida por GenAI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP HANA Cloud**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP HANA Application Migration Assistant** (extensión para Visual Studio Code).
- Acceso a destino BTP (subaccount) para desplegar la aplicación CAP convertida.

### 1.5 Datos maestros / transaccionales previos
- Código fuente XS/XSA del cliente accesible.
- Estructuras de base de datos / datos del proyecto migrable accesibles desde el entorno de desarrollo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (es una herramienta para developers).
- **Cobertura**: la conversión cubre artefactos XSJSLIB, XSODATA y XSJS; lógica muy custom puede requerir reescritura manual.
- **Roles**: developer con acceso a SAP HANA Cloud y a BTP.

> **Setup oficial SAP**: la página https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/migrate-xs-advanced-application-to-sap-cap-and-sap-hana-cloud-with-sap-hana-application-migration-assistant-in-visual-studio-code describe el procedimiento de migración con el Migration Assistant.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP HANA Cloud y subaccount BTP destino | SAP HANA Cloud + Subaccount BTP | General | Consultor BTP / HANA | 2 |
| 2 | Preparar conectividad al sistema origen XS/XSA | Conectividad origen | General | Consultor SAP HANA + Cliente | 3 |
| 3 | Configurar el destino BTP donde se desplegará la aplicación CAP | Destino BTP | General | Consultor BTP | 3 |
| 4 | Crear dev space en Visual Studio Code con la extensión SAP HANA Application Migration Assistant | Dev space VSCode + Extensión | General | Consultor SAP HANA / Developer | 3 |
| 5 | Ejecutar el Migration Assistant sobre los artefactos XSJSLIB / XSODATA / XSJS | Migration Assistant | Particular (por proyecto) | Consultor SAP HANA / Developer | 6 |
| 6 | Validar manualmente la conversión, ajustar lógica y ejecutar pruebas funcionales | Aplicación CAP convertida | Particular (por proyecto) | Consultor SAP HANA / Developer | 8 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~25 horas.**

> **Nota**: el alcance estándar cubre la conversión asistida y un primer ajuste; proyectos con lógica custom extensa requerirán esfuerzo adicional fuera del alcance estándar.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales del proyecto migrado | Consultor SAP HANA / Developer | 4 |
| 2 | Documentación de la migración para el cliente (diferencias entre el código original y el convertido) | Consultor SAP HANA / Developer | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica) | Consultor SAP HANA / Developer | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una **herramienta para developers**: no aplica concepto de Joule capability ni AI Units en el sentido tradicional.
- La conversión es **asistida**: el código resultante debe revisarse, probarse y ajustarse manualmente — no es una migración cero-touch.
- Lógica muy custom o dependencias no soportadas pueden requerir **reescritura manual** fuera del alcance estándar.
- Sujeto a las condiciones de servicio vigentes de SAP HANA Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **acompaña** la modernización técnica; no entrega la aplicación final lista para producción sin trabajo adicional del developer.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- SAP Help Portal — Migration Guide: https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/migrate-xs-advanced-application-to-sap-cap-and-sap-hana-cloud-with-sap-hana-application-migration-assistant-in-visual-studio-code

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 25 |
| Validación + documentación + KT | 11 |
| **Total** | **36** |

---

## [J193] — UI Generation from Data (SAP Build Apps)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite generar automáticamente páginas de aplicación a partir de entidades de datos ya integradas en un proyecto de SAP Build Apps, incluyendo operaciones CRUD como punto de partida. SAP indica: *Reduce el tiempo de construcción de aplicaciones, mejora la productividad de equipos low-code y acelera la entrega de extensiones o aplicaciones empresariales basadas en datos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Apps** en BTP con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Apps + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SAP Build Apps.

### 1.5 Datos maestros / transaccionales previos
- Data entities integradas (OData / REST / DB) en Build Apps.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Citizen Developer / Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SAP Build Apps + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar data entities en Build Apps | Build Apps data | Particular (por entidad) | Consultor Build Apps | 5 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar UI Generation from Data | Configuración Build Apps | General | Consultor Build Apps | 2 |
| 5 | Pruebas iniciales (generar páginas desde entidades) | Configuración Build Apps | General | Consultor Build Apps | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Build Apps | 5 |
| 2 | Documentación + buenas prácticas | Consultor Build Apps | 4 |
| 3 | Transferencia de conocimiento | Consultor Build Apps | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Páginas generadas son base; pulir UX, navigation y validations.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |

---

## [J195] — Skill Builder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **Joule Studio** permite extender Joule mediante **skills** ajustadas a necesidades de negocio. Las skills ejecutan operaciones predefinidas desde la interfaz conversacional de Joule y pueden integrarse con sistemas SAP y no SAP. El valor se centra en reducir el tiempo para desplegar skills personalizadas y disminuir tareas repetitivas mediante automatización conversacional.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en el tenant del cliente.
- **Joule Studio** (suscripción activa).
- **SAP Build** y, opcionalmente, **SAP Build Process Automation** (según el booster recomendado por SAP).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripciones vigentes a **Joule** y **Joule Studio**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **Joule Studio** desplegado en BTP.
- **SAP Build** / SAP Build Process Automation (cuando se use el booster oficial para conectar Joule).
- Sistemas SAP / no SAP destino con APIs / connectivity disponibles.

### 1.5 Datos maestros / transaccionales previos
- Definición de los escenarios donde se ejecutarán las skills (operaciones, sistemas destino, datos de entrada / salida).
- Conectividad a los sistemas destino configurada (destinations / communication arrangements).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: developers / administradores con permisos sobre Joule Studio y los sistemas destino.

> **Setup oficial SAP**: la página https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html describe los escenarios de setup de Joule Studio. Una opción indicada es ejecutar un **booster** para conectar Joule con SAP Build Process Automation, luego asignar usuarios a roles y preparar capacidades de IA.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlements de Joule y Joule Studio en SAP BTP | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Ejecutar el **booster** oficial para preparar la integración Joule ↔ SAP Build Process Automation (cuando aplique) | Booster BTP | General | Consultor BTP / Joule Studio | 4 |
| 3 | Asignar a los developers los roles administrativos / de developer en Joule Studio | Roles Joule Studio | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Configurar las **destinations** y conectividad a los sistemas destino que usarán las skills | Destinations BTP | Particular (por sistema destino) | Consultor BTP | 4 |
| 5 | Definir y desarrollar las **skills** iniciales para los escenarios objetivo | Skill (Joule Studio) | Particular (por skill) | Consultor Joule Studio / Developer | 8 |
| 6 | Pruebas iniciales end-to-end de las skills desde la UI de Joule | Configuración funcional Joule | General | Consultor Joule Studio + Funcional | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~24 horas.**

> **Nota**: el esfuerzo del paso 5 depende del **número y complejidad** de las skills a desarrollar. La estimación corresponde a un conjunto inicial reducido.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria end-to-end por cada skill desarrollada (incluyendo autorizaciones y manejo de error) | Consultor Joule Studio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual técnico de las skills) | Consultor Joule Studio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica + sesión funcional) | Consultor Joule Studio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability de **desarrollo / extensión**: requiere governance sobre quién define y aprueba skills antes del rollout.
- Las skills **operan sobre datos productivos**: validar autorizaciones y manejo de error antes del go-live.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**, pero las skills deben respetar el principio de mínimo privilegio en sus destinations.
- Considerar **monitorización y auditoría** de skills en producción.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- El esfuerzo aquí cubre la **activación + un conjunto inicial reducido de skills**; cada skill adicional requiere esfuerzo adicional fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- SAP Help Portal — Joule Studio Setup: https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |

---

## [J212] — Process Analyzer, Text To Widget (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Analyzer, Text to Widget permite crear widgets de dashboard a partir de consultas en lenguaje natural sobre datos de procesos. SAP indica: *El valor se centra en acelerar el time-to-value de los dashboards de procesos, mejorar la autonomía de usuarios de negocio y reducir dependencia de equipos técnicos para análisis básicos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Intelligence** activo.
- Capability AI / Joule integrada en Signavio **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Intelligence con feature AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Analyzer.

### 1.5 Datos maestros / transaccionales previos
- Investigations / process data sources cargados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Process Analyst.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Asignar rol Process Analyst | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Text To Widget | Signavio admin | General | Consultor Signavio | 2 |
| 4 | Pruebas iniciales: generar widgets a partir de prompts | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con investigations reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Resultados dependen de la riqueza del modelo de datos cargado en Signavio.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 10 |
| **Total** | **19** |

---

## [J213] — Process Modeler (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio. SAP indica: *La página destaca una reducción del tiempo de modelado de procesos y un menor costo asociado al modelado manual, además de mejorar la colaboración entre negocio y equipos de procesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Manager** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Manager con feature AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Manager UI.

### 1.5 Datos maestros / transaccionales previos
- Diccionario / glosario, conventions BPMN del cliente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Process Modeler.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Asignar rol Process Modeler | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Modeler AI | Signavio admin | General | Consultor Signavio | 2 |
| 4 | Pruebas iniciales (generar BPMN desde texto/imagen) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con descripciones reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Diagrama generado es punto de partida; modeler debe revisar conventions.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 10 |
| **Total** | **19** |

---

## [J225] — Enterprise Search

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center, SAP Help Portal). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Búsqueda empresarial asistida por IA en **SAP S/4HANA Cloud Public Edition** que permite encontrar objetos de negocio mediante lenguaje natural desde el SAP Fiori Launchpad. SAP indica un ahorro estimado del **50% en el tiempo de búsqueda** de objetos de negocio.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **Enterprise Search** habilitado en S/4HANA Cloud Public Edition (índices de búsqueda activos).
- SAP Fiori Launchpad disponible para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule sobre S/4HANA Public **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No se identifica un scope item específico; aplica al motor transversal de Enterprise Search del producto base **[verificar en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Caja de búsqueda del **SAP Fiori Launchpad** activa para el usuario.
- Apps Fiori de los objetos de negocio que se desea buscar (los resultados navegan a las apps correspondientes).
- **Joule** habilitado en el Launchpad del usuario final.

### 1.5 Datos maestros / transaccionales previos
- Objetos de negocio (Business Partners, Materiales, Sales Orders, etc.) cargados y consistentes.
- Índices de Enterprise Search refrescados y operativos para los objetos a consultar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de búsqueda en lenguaje natural soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario sólo verá resultados sobre objetos para los que tiene autorización.

> **Nota**: SAP no publica un Initial Setup específico para este caso en Discovery Center; aplican los prerequisitos generales de Joule + Enterprise Search sobre S/4HANA Cloud Public Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar que **Enterprise Search** esté habilitado y los índices estén operativos | Configuración de Enterprise Search | General | Consultor Funcional S/4HANA + Basis Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los business roles con autorización sobre los objetos a buscar | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar el botón / capability de Joule en el Launchpad de los usuarios | Joule capability scope | General | Consultor Funcional S/4HANA | 2 |
| 5 | Pruebas iniciales en Quality con un usuario piloto (consultas en lenguaje natural sobre objetos comunes) | Configuración funcional / Launchpad | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (búsquedas representativas sobre objetos clave del cliente) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Joule respeta las autorizaciones del usuario: **no eleva privilegios**. Los resultados se filtran según el perfil de seguridad.
- La calidad de la búsqueda depende del **estado de los índices de Enterprise Search**; si están desactualizados, los resultados serán incompletos.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y objetos soportados.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J226] — Smart Personalization of My Home

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que permite personalizar **My Home** agregando **insights cards** mediante lenguaje natural. SAP indica un ahorro estimado del **50% del tiempo** para agregar insights cards a My Home.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Página **My Home** del SAP Fiori Launchpad disponible para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item específico; la capability opera sobre My Home / Fiori Launchpad.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad — My Home**.
- IAM app **SAP Business AI - User Interface Features - Smart Personalization (F8555_TRAN)** o el catálogo equivalente, asignada a los usuarios objetivo.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales disponibles en los módulos sobre los que se generan las insights cards (cuanto más datos relevantes haya, mejores serán las tarjetas propuestas).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización a las apps cuya información se mostrará en las insights cards (Joule respeta las autorizaciones).

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html describe el procedimiento: abrir *Maintain Business Roles*, asignar la **IAM app F8555_TRAN** al rol de negocio y dejar la capacidad habilitada para los usuarios. Los usuarios pueden usar *Add Content* en My Home → *Insights Cards*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar la disponibilidad de la **IAM app F8555_TRAN** en *Display IAM Apps* | IAM App F8555_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 4 | Asignar la IAM app **F8555_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales con un usuario piloto (*Add Content* → *Insights Cards*, consulta en lenguaje natural, generar / previsualizar / agregar tarjeta) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con usuarios reales (varios perfiles / módulos, tarjetas representativas) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Joule respeta las autorizaciones del usuario: las **insights cards no exponen datos a los que el usuario no tiene acceso**.
- Definir **buenas prácticas de prompting** para acelerar la adopción.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/
- SAP Help Portal — Smart Personalization of My Home: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J227] — Error Explanation

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que genera descripciones y recomendaciones de resolución en lenguaje natural para errores del sistema, ayudando a usuarios de distintos niveles de experiencia a entender el problema y continuar con el proceso.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Fiori Launchpad** con apps de los módulos donde se quiere ofrecer explicación de errores.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- No aplica un scope item específico; la capacidad opera transversalmente sobre errores del producto base.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad** del sistema S/4HANA Cloud Public Edition.
- Apps Fiori donde aparecen los errores que se quieren explicar.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de mensajes de error del sistema operativo.
- Datos transaccionales que generan los errores a explicar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: las explicaciones se publican principalmente en **inglés** **[verificar matriz de idiomas vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener acceso a la app donde ocurre el error.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/fbcd177357284dd5846347f04e1cea67.html (*Enabling the AI-Assisted Error Explanation*) indica que la activación se inicia como administrador en el SAP Fiori Launchpad del sistema.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Iniciar sesión como administrador en el SAP Fiori Launchpad del sistema S/4HANA Cloud Public Edition y habilitar *AI-Assisted Error Explanation* | Configuración Error Explanation | General | Consultor Funcional S/4HANA + Cliente Admin | 2 |
| 4 | Asignar a los usuarios objetivo los business roles con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales con un usuario piloto (provocar errores típicos y verificar explicaciones generadas) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con errores reales del cliente (varios módulos / niveles de severidad) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de aplicar la corrección.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/
- SAP Help Portal — Enabling AI-Assisted Error Explanation: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/fbcd177357284dd5846347f04e1cea67.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J240] — In-house Service Initiation

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos. El personal de reparación puede escanear o fotografiar documentos entrantes, como órdenes de compra; el sistema extrae datos relevantes y genera objetos de reparación asociados al servicio interno. SAP indica: *SAP indica aumento de 70% en productividad del trabajador de servicio al preparar órdenes de servicio. El valor está en reducir digitación manual, evitar pérdida de datos y acelerar el procesamiento de reparaciones.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Document AI** (para input papel/PDF).
- Componente **CS / Service Management** (Service Order / Notification) operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Document AI (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Service Management - In-house Repair / Customer Service — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Service Orders*, *Service Notifications*.
- Communication arrangement con Document AI.

### 1.5 Datos maestros / transaccionales previos
- Maestros de equipos, customers, service types, technicians.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Mapping de datos extraídos al service order / notification | Mapping Document AI ↔ Service | Particular (por tipo de service request) | Consultor Service + Integración | 6 |
| 4 | Asignar business roles Service a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con documentos reales | Configuración funcional Service | General | Consultor Service | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real | Consultor Service | 6 |
| 2 | Documentación para el cliente | Consultor Service | 4 |
| 3 | Transferencia de conocimiento | Consultor Service | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- Calidad de extracción depende del layout del documento de entrada.
- Usuario sigue validando antes de crear el service order/notification.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |

---

## [J241] — Maintenance Order Recommendation

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento. El planificador revisa las recomendaciones y selecciona una orden como referencia para crear una nueva orden de mantenimiento. SAP indica: *40% de aumento en productividad del planificador de mantenimiento; 1% de reducción del downtime no planificado; 5% de aumento en la tasa de resolución en el primer intento de técnicos de mantenimiento.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **PM / EAM – Plant Maintenance / Enterprise Asset Management** operativo.
- Datos históricos suficientes de maintenance orders para entrenar/recomendar.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule (capability puede ser Premium dado el componente ML) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Plant Maintenance / EAM — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Maintenance Orders*, *Maintenance Planner*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Functional locations, equipment, task lists, maintenance plans, historial de OTs cerradas.
- Volumen de datos históricos suficiente para que las recomendaciones tengan calidad.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones PM.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + capability ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración PM (order types, activity types, task lists) | Configuración PM | General | Consultor PM | 3 |
| 3 | Asignar business roles PM a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Maintenance Recommendation | Joule capability scope | General | Consultor Funcional PM + Joule | 3 |
| 5 | Pruebas iniciales: validar recomendaciones contra historial real | Configuración funcional PM | General | Consultor PM | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (recomendaciones por tipo de equipo) | Consultor PM | 5 |
| 2 | Documentación para el cliente | Consultor PM | 4 |
| 3 | Transferencia de conocimiento | Consultor PM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad de recomendación depende del volumen y limpieza del histórico.
- Validar periodicidad de reentrenamiento (si aplica).
- Usuario confirma antes de crear la OT.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J243] — API traffic prediction (SAP Integration Suite)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Funcionalidad de SAP Integration Suite que identifica tendencias en llamadas API y predice volúmenes futuros de tráfico para apoyar decisiones sobre capacidad, carga y estrategia API. SAP indica: *Mejora la planificación de recursos, la gestión de carga del sistema y la toma de decisiones sobre estrategia API. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (capability API Management).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Integration Suite con plan que incluya API Management.
- Capability AI activada **[verificar AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- N/A (capability de la plataforma).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Subaccount BTP con Integration Suite habilitado.
- API Management con proxies productivos y métricas habilitadas.

### 1.5 Datos maestros / transaccionales previos
- Histórico de tráfico de APIs por proxy / API Product (idealmente varias semanas).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI en inglés primariamente **[verificar]**.
- Calidad de predicción depende del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Integration Suite + capability AI | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Habilitar capability AI en API Management | API Management settings | General | Consultor Integración | 3 |
| 3 | Asignar roles API Admin / Analyst a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Validar histórico mínimo de tráfico para activación útil | Configuración API Management | General | Consultor Integración | 2 |
| 5 | Pruebas iniciales (revisar predicciones contra histórico) | Configuración AI | General | Consultor Integración | 3 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con APIs reales del cliente | Consultor Integración | 4 |
| 2 | Documentación para el cliente | Consultor Integración | 3 |
| 3 | Transferencia de conocimiento | Consultor Integración | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Útil para capacity planning y SLA management.
- Calidad mejora con volumen/estabilidad del tráfico.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 10 |
| **Total** | **22** |

---

## [J247] — Journal Upload

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition. Mediante una app SAP Fiori con capacidades de IA generativa, permite crear casos de carga, asociar una guía o política de contabilización en lenguaje natural, generar propuestas, validarlas y publicar asientos. SAP indica: *70% de reducción del esfuerzo para preparar journals manuales al cierre de período; 50% de reducción del esfuerzo para cargar y validar journals manuales al cierre.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **FI-GL – General Ledger** operativo.
- (Opcional) **SAP Document AI** si la entrada es PDF/Excel no estructurado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule **[verificar]**.
- Si aplica, entitlement Document AI (Premium).

### 1.3 Scope item relacionado
- Scope items de Record-to-Report / Period-End Close — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Post General Journal Entries*, *Upload General Journal Entries*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Chart of accounts, document types, periodos abiertos.
- Plantilla de upload (formato Excel SAP).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones FI-GL.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración FI-GL (doc types, posting keys) | Configuración FI-GL | General | Consultor FI | 3 |
| 3 | Asignar business roles FI-GL a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Journal Upload | Joule capability scope | General | Consultor Funcional FI + Joule | 2 |
| 5 | Pruebas iniciales con plantillas reales en QAS | Configuración funcional FI | General | Consultor FI | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con journals reales del cliente | Consultor FI | 4 |
| 2 | Documentación para el cliente | Consultor FI | 4 |
| 3 | Transferencia de conocimiento | Consultor FI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Acelera period-end; validar tolerancias y workflows de aprobación.
- Reglas de validación FI siguen aplicando.
- Usuario confirma posting.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J25] — Natural Language Query

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Función de IA generativa de **SAP Analytics Cloud (SAC)** que democratiza la analítica permitiendo solicitar datos mediante lenguaje natural. SAP indica una reducción del **80% del tiempo** para acceder a información relevante.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC sin necesidad de paquete Premium adicional **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias / modelos publicados sobre los que se quiera consultar.

### 1.5 Datos maestros / transaccionales previos
- Modelos / datasets de SAC publicados con métricas, dimensiones y jerarquías correctamente configuradas.
- Nombres / descripciones consistentes en el modelo para que la consulta en lenguaje natural funcione correctamente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: la consulta en lenguaje natural está disponible principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: el usuario debe tener permisos de visualización sobre los modelos / historias consultadas.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de SAP Analytics Cloud.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar la calidad / nomenclatura de los modelos donde se usará la consulta en lenguaje natural | Modelos SAC | Particular (por modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con permisos sobre los modelos / historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (consultas representativas en lenguaje natural) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios dominios / niveles de complejidad) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + buenas prácticas de prompting) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de las respuestas depende directamente de la **calidad de los modelos**: nomenclatura clara, jerarquías y métricas bien definidas.
- Joule / SAC respetan las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** y publicar ejemplos al inicio para acelerar adopción.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y funcionalidades disponibles.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J275] — AI-Assisted Commenting

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP for Me). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite resumir comentarios existentes y reformular nuevos comentarios durante la autoría. Permite resumir comentarios por celda, agregarlos a lo largo de una jerarquía y recibir traducciones según el idioma del usuario. SAP indica reducciones del **80%** en tiempo para reformular, agregar/traducir descendientes y resumir/traducir comentarios por celda o hilo.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).
- Tenant SAC desplegado en un **data center que soporte SAP Business AI** **[verificar matriz de data centers vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Premium** — activación con **AI Units** (consumo registrado y consultable en SAP for Me).
- **AI Units** asignadas al tenant para esta feature **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- No aplica scope item (SAP Analytics Cloud no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias / planning models donde se usen comentarios.
- Acceso a **SAP for Me** para administradores del tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Comentarios existentes (a nivel celda, hilo o jerarquía) en las historias / modelos donde se vaya a usar la capability.
- Configuración de comentarios habilitada en el modelo / historia.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: la capability soporta traducciones; idiomas soportados en función del modelo de IA subyacente **[verificar matriz vigente]**.
- **Disponibilidad regional**: depende del data center del tenant.
- **Roles**: el usuario debe tener permisos para leer/editar comentarios en las historias / modelos.

> **Setup oficial SAP**: el procedimiento documentado es el mismo que para otras features de IA de SAC:
> 1. Iniciar sesión en **SAP for Me**.
> 2. En el panel de navegación, elegir **Portfolio & Products**.
> 3. Elegir **Business AI**.
> 4. Seleccionar **Request Activation** junto al nombre de la feature.
>
> SAP Support notificará cuando la feature haya sido activada.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar que el tenant SAC está en un data center que soporta SAP Business AI | Tenant SAC | General | Consultor SAC + Consultor BTP | 1 |
| 2 | Confirmar entitlement de AI Units para SAC en el tenant del cliente | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Solicitar la activación de la feature *AI-Assisted Commenting* desde **SAP for Me** → *Portfolio & Products* → *Business AI* → *Request Activation* | SAP for Me — Request Activation | General | Consultor SAC + Cliente Admin | 1 |
| 4 | Esperar notificación de SAP Support sobre la activación | (Solicitud SAP Support) | General | (gestión con SAP Support) | 0 |
| 5 | Verificar que la capability de comentarios esté habilitada en las historias / modelos objetivo | Configuración SAC – Comments | Particular (por historia / modelo) | Consultor SAC | 2 |
| 6 | Asignar a los usuarios los roles SAC con permisos sobre comentarios | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 7 | Pruebas iniciales con un usuario piloto (resumir, reformular y traducir comentarios) | Configuración funcional SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas (excluyendo tiempo de SAP Support para activar la feature).**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con comentarios reales del cliente (resumen, reformulación, traducción y agregación por jerarquía) | Consultor SAC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La activación **no es self-service**: requiere **solicitud a SAP Support** vía SAP for Me. El tiempo de respuesta de SAP no es controlable.
- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- **Confirmar el data center** del tenant: solo data centers compatibles con SAP Business AI ofrecen la feature.
- Las traducciones y reformulaciones son **asistencia**: el usuario debe revisar el resultado, especialmente en contextos sensibles (planning narrative, comentarios contractuales).
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas / funcionalidades disponibles.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8dcc1f1915b241b3a10c8e5b8a76b062.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |

---

## [J284] — Joule with SAP LeanIX

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto. SAP indica: *50% menos esfuerzo para buscar documentación e información relevante, según la métrica mostrada en la página de detalle.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX** activo (EAM / Architecture suite).
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción LeanIX.
- Entitlement Joule + capability LeanIX **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace LeanIX.
- Joule integrado en LeanIX UI.

### 1.5 Datos maestros / transaccionales previos
- Inventario LeanIX poblado (applications, business capabilities, tech stack).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement LeanIX + Joule capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO entre LeanIX e identidad corporativa | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en LeanIX | LeanIX admin | General | Consultor LeanIX | 3 |
| 4 | Asignar roles LeanIX a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas NL sobre inventario) | Configuración LeanIX | General | Consultor LeanIX | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con inventario real | Consultor LeanIX | 4 |
| 2 | Documentación para el cliente | Consultor LeanIX | 4 |
| 3 | Transferencia de conocimiento | Consultor LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Calidad depende de la cobertura/limpieza del inventario LeanIX.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |

---

## [J288] — Explanation of Fixed Asset Key Figures

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones en lenguaje natural de cálculos complejos. SAP indica una **reducción de hasta 75%** en el esfuerzo para analizar valores de activos y responder preguntas de usuarios. La funcionalidad se accede desde la sección *Value Display* de la app *Manage Fixed Assets*.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **Asset Accounting (FI-AA)** operativo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- Scope items de **Asset Accounting** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Fixed Assets** habilitada para los usuarios objetivo (la funcionalidad se usa desde la sección *Value Display*).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de activos fijos cargado y consistente.
- Áreas de valoración, claves de depreciación y movimientos de valor cargados.
- Periodos contables abiertos / cerrados según necesidad de análisis.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización sobre el activo fijo cuyas key figures pretende explicar.

> **Setup oficial SAP**: la página de SAP Help Portal corresponde a *AI-Generated Explanation of Key Figures* (https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/ee5966f4b7f640ac8edbe3aa26bcc47b.html). El contenido disponible indica el uso en la sección *Value Display* de la app *Manage Fixed Assets*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP / Cockpit | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar configuración de Asset Accounting (áreas de valoración, claves, movimientos) | Configuración FI-AA | General | Consultor Funcional Asset Accounting | 3 |
| 4 | Asignar a los usuarios objetivo los business roles de Asset Accountant con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar la capability de Joule para *Explanation of Key Figures* en *Manage Fixed Assets* | Joule capability scope | General | Consultor Funcional Asset Accounting + Joule | 2 |
| 6 | Pruebas iniciales en Quality (consultas sobre key figures representativas en Value Display) | Configuración funcional FI-AA | General | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre key figures de activos representativos) | Consultor Funcional Asset Accounting | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Asset Accounting | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de la interpretación contable y de la decisión.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/ee5966f4b7f640ac8edbe3aa26bcc47b.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J28] — Goods Receipt Processing

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA. Permite extraer información relevante de documentos de flete en papel, publicarla en el sistema y detectar anomalías que pueden retrasar la validación de freight orders. SAP indica: *El valor está en reducir trabajo manual y errores durante la recepción de mercancía, acelerar validaciones y mejorar eficiencia operacional en transporte/logística.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP) para extracción de delivery notes.
- Componente **MM-IM – Inventory Management** + **MM-PUR – Purchasing** operativos.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement **Document AI** (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Procure-to-Pay / Goods Receipt — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Post Goods Receipt for Purchase Order*, *Goods Receipt Reversal*.
- Communication arrangement S/4HANA Private ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Materials, suppliers, purchase orders abiertos.
- Tipos de delivery notes (papel/PDF) soportados por Document AI.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Layout del documento debe ser razonablemente extraíble.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario S/4HANA Private ↔ Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al goods receipt | Mapping Document AI ↔ GR | Particular (por layout/proveedor) | Consultor MM + Integración | 6 |
| 4 | Asignar business roles Warehouse / Inventory a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con delivery notes reales | Configuración funcional MM-IM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real (varios layouts de proveedores) | Consultor MM | 6 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout del delivery note.
- Reglas de tolerancia y discrepancias siguen aplicando.
- Usuario sigue confirmando posting cuando hay discrepancias.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |

---

## [J294] — Joule with SAP Datasphere

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Con Joule embebido en SAP Datasphere, los usuarios pueden realizar tareas informativas, navegacionales y transaccionales de forma fluida, incluyendo consultas sobre uso del producto y tareas comunes de administración. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se orienta a productividad de usuarios y administradores en SAP Datasphere.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** activo en BTP.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Datasphere.
- Entitlement Joule + capability Datasphere **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Datasphere tenant con spaces / data builders configurados.
- Joule integrado en Datasphere UI.

### 1.5 Datos maestros / transaccionales previos
- Modelos de datos (entities, views, business semantics) en Datasphere.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Datasphere (modeler / consumer).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Datasphere + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Datasphere | Datasphere settings | General | Consultor Datasphere | 3 |
| 4 | Asignar roles Datasphere a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas en NL sobre modelos) | Configuración Datasphere | General | Consultor Datasphere | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con modelos reales | Consultor Datasphere | 4 |
| 2 | Documentación para el cliente | Consultor Datasphere | 4 |
| 3 | Transferencia de conocimiento | Consultor Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Calidad de respuesta depende de la riqueza semántica de los modelos.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |

---

## [J305] — Electronic Document Error Handling

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Ofrece explicaciones fáciles de entender para errores de documentos electrónicos con **Joule** en **SAP Document and Reporting Compliance**. SAP indica una reducción del **80% del tiempo** dedicado a entender los detalles del error e identificar la causa raíz.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document and Reporting Compliance** (DRC) activo.
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado (Joule integrado con DRC) **[verificar matriz de productos compatibles vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document and Reporting Compliance**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **DRC** según país / régimen fiscal aplicable — **[verificar el ID exacto en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de **DRC** habilitadas (*eDocument Cockpit* / *Statutory Reporting* según escenario).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Documentos electrónicos generados y procesados por DRC para el país objetivo.
- Errores de validación / transmisión registrados en el log de DRC.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente y disponibilidad por país]**.
- **Edición**: aplica a **SAP S/4HANA Cloud Private Edition** integrado con DRC.
- **Roles**: el usuario debe tener autorización sobre los documentos electrónicos a analizar.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/ae0b823738ee4227b7ec12cc4fbf1b4c/769137a7913747e0b2ad2315dd2e9e4f.html indica prerequisitos relacionados con *Joule Initial Setup* y la integración de Joule con S/4HANA Cloud Private Edition para *Electronic Document Error Handling*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Private Edition y DRC | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Completar el **Joule Initial Setup** para Private Edition | Joule — Initial Setup | General | Consultor BTP + Consultor S/4HANA | 4 |
| 3 | Configurar / verificar la integración Joule ↔ DRC | Integración Joule – DRC | General | Consultor S/4HANA + DRC | 3 |
| 4 | Asignar a los usuarios objetivo los business roles con acceso a DRC y a la capability Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales en Quality (provocar errores controlados en documentos electrónicos y solicitar explicación a Joule) | Configuración funcional DRC | General | Consultor Funcional DRC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con errores reales del cliente (explicaciones sobre errores de varios países / regímenes) | Consultor Funcional DRC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor Funcional DRC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional DRC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las explicaciones son **apoyo a la operación**: el usuario sigue siendo responsable de aplicar la corrección y reenviar el documento conforme a la normativa local.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Confirmar la **disponibilidad por país** dentro de DRC y la cobertura de la capability sobre los regímenes que opera el cliente.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1a1b66db-191d-41e6-b01d-d69b4d645850/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ae0b823738ee4227b7ec12cc4fbf1b4c/769137a7913747e0b2ad2315dd2e9e4f.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J308] — Agent Builder (Joule Studio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite construir agentes de Joule para automatizar procesos de negocio complejos. Los agentes pueden ejecutar flujos adaptativos, razonar, planificar, coordinar procesos de varios pasos, invocar APIs, interactuar con documentos y colaborar con usuarios u otros agentes en sistemas SAP y no SAP. SAP indica: *Aporta eficiencia en escenarios que requieren toma de decisiones experta, manejo de excepciones y orquestación entre sistemas, especialmente donde la automatización determinística no es suficiente.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule Studio** en SAP Business Application Studio / herramienta equivalente vigente.
- **SAP BTP** con entitlement de Joule.
- Acceso a las APIs/skills SAP o de terceros que el agente vaya a orquestar.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement de **Joule Studio / Agent Builder** (Premium) **[verificar AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- N/A (capability de desarrollo/diseño).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Studio UI.
- Conectividad a sistemas backend (S/4HANA, BTP services, etc.) vía destinations.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de skills/APIs disponibles configurado.
- Plantillas de prompt / herramientas base.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Developer / Agent Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement de Joule Studio / Agent Builder | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a sistemas backend | Destinations BTP | Particular (por backend) | Consultor BTP / Integración | 4 |
| 3 | Asignar roles Developer / Agent Designer a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Validar catálogo de skills/APIs disponibles | Configuración Joule Studio | General | Consultor Funcional + Joule | 3 |
| 5 | Construir agente de muestra y desplegarlo | Configuración Agent Builder | Particular (por agente diseñado) | Desarrollador Agent Designer | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del agente con flujos representativos | Agent Designer | 5 |
| 2 | Documentación (catálogo de skills + diagrama del agente) | Agent Designer | 4 |
| 3 | Transferencia de conocimiento | Agent Designer | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- El esfuerzo para construir agentes adicionales **no está incluido** (es por agente diseñado).
- Buenas prácticas: limitar scope inicial, asegurar guardrails y observabilidad.
- Cobertura de skills SAP evoluciona por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 12 |
| **Total** | **29** |

---

## [J313] — Expiring Price Handling

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de Joule en **SAP S/4HANA Cloud Public Edition** que permite a especialistas de precios consultar precios, descuentos o recargos próximos a expirar y crear o actualizar precios mediante interacción conversacional. SAP indica una reducción estimada del **95% del esfuerzo** para detectar y actualizar precios próximos a vencer.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente funcional **SD – Pricing / Condition Management** operativo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule sobre S/4HANA Public **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope item de **Sales Pricing / Condition Management** en S/4HANA Cloud Public Edition — **[verificar el ID exacto en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de mantenimiento de condiciones de precio (*Manage Prices – Sales*, *Manage Prices – Purchasing*, según el escenario) habilitadas.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Tipos de condición, tablas de condición y secuencias de acceso definidos.
- Condiciones de precio actuales cargadas con sus respectivas fechas de validez.
- Catálogo de materiales, clientes y proveedores consistentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización sobre las áreas de organización de ventas y las condiciones de precio a consultar/modificar.

> **Setup oficial SAP**: la página de SAP Help Portal corresponde a la capacidad *Expiring Price Handling* de Joule (https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices). El contenido completo no fue totalmente extractable, por lo que no se agregan prerequisitos no verificados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar configuración de pricing (tipos de condición, tablas, secuencias de acceso) | Configuración SD – Pricing | General | Consultor SD | 3 |
| 3 | Asignar a los usuarios objetivo los business roles de Pricing Specialist con la capability de Joule habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar la capability de Joule para *Expiring Price Handling* | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales en Quality (consultar precios próximos a vencer, crear/actualizar condiciones con prompts) | Configuración funcional SD – Pricing | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (condiciones próximas a expirar, creación masiva conversacional) | Consultor SD | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SD | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Joule responde sobre datos a los que el usuario ya tiene autorización; **no eleva privilegios**: validar la matriz de autorizaciones antes del rollout.
- La capability **crea/modifica datos transaccionales de pricing**: revisar controles de auditoría y aprobaciones internas antes de habilitar.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- SAP Help Portal — Capabilities Guide: https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J326] — Meeting Location Planner Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; pasos de setup pueden no estar todavía completamente documentados públicamente.

**Resumen del caso:** Ayuda a empleados a organizar reuniones offsite sugiriendo ubicaciones que minimizan tiempos de viaje, proponiendo hoteles y mostrando una vista general de costos para planificar dentro del presupuesto. SAP indica: *No se identificó una métrica cuantitativa completa en el contenido accesible de la página de detalle; el valor descrito se concentra en reducir tiempo de planificación y mejorar el control presupuestal de offsites.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con calendar / meeting providers (Microsoft 365 / Google) **[verificar]**.
- (Opcional) Integración con Travel Management / Concur.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible.
- Destinations a calendar / venue providers.

### 1.5 Datos maestros / transaccionales previos
- Calendarios y datos de assistants/executives a soportar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a calendar / venue providers | Destinations | General | Consultor BTP / Integración | 5 |
| 3 | Asignar acceso al agente a executive assistants | Roles / Agent assignment | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Validar políticas (lugares preferidos, presupuestos) | Configuración del agente | Particular (por organización) | Consultor Funcional + Diseñador agente | 4 |
| 5 | Pruebas iniciales con escenarios reales (offsite planning) | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos típicos | Consultor Funcional | 5 |
| 2 | Documentación para el cliente | Consultor Funcional | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Privacidad: el agente accede a calendarios; revisar consentimientos y DLP.
- Resultados dependen del catálogo de venues/políticas disponibles.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |

---

## [J327] — Expense Report Validation Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; puntos de setup pueden no estar plenamente documentados públicamente — marco con **[verificar]** los críticos.

**Resumen del caso:** Agente para ayudar a viajeros de negocio a completar y enviar reportes de gastos, simplificando el proceso de entendimiento y preparación de la información requerida. SAP indica: *Reducción estimada del 30% en el tiempo dedicado a preparar y enviar reportes de gastos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con **SAP Concur Expense** (u otro Travel & Expense del cliente) **[verificar conector]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.
- Suscripción Concur Expense (si aplica).

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible por employees.
- Destination a Concur (API keys / OAuth).

### 1.5 Datos maestros / transaccionales previos
- Políticas de expense (límites, categorías, country specifics).
- Reglas de validación corporativas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant Joule y al proveedor.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a Concur Expense | Destinations BTP | General | Consultor BTP / Integración | 5 |
| 3 | Configurar políticas de validación específicas del cliente | Reglas de validación | Particular (por política / categoría) | Consultor Funcional T&E | 5 |
| 4 | Asignar acceso al agente a employees | Roles / Agent assignment | Particular (por grupo) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con expense reports reales | Configuración funcional T&E | General | Consultor Funcional T&E | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (categorías y excepciones) | Consultor Funcional T&E | 5 |
| 2 | Documentación para el cliente | Consultor Funcional T&E | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional T&E | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- El agente **sugiere/ayuda**; la aprobación final sigue al workflow definido.
- Privacidad: revisar tratamiento de datos personales/financieros.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 12 |
| **Total** | **32** |

---

## [J329] — Semantic Generation (SAP Datasphere)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas. El onboarding semántico toma tablas, contenido y semántica asociada como monedas, unidades, medidas, hechos, dimensiones y asociaciones. SAP indica: *Menor esfuerzo para crear modelos semánticos en SAP Datasphere, mayor velocidad para preparar datos no SAP para consumo analítico y mejor reutilización de información enriquecida semánticamente.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Datasphere + capability AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Datasphere Workspace (Data Builder / Business Builder).

### 1.5 Datos maestros / transaccionales previos
- Fuentes no-SAP conectadas (database, file, etc.).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Modeler.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Datasphere + AI | Tenant Datasphere | General | Consultor Datasphere | 2 |
| 2 | Configurar conexiones a fuentes no-SAP | Conexiones Datasphere | Particular (por fuente) | Consultor Datasphere | 5 |
| 3 | Asignar rol Modeler | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Semantic Generation | Datasphere admin | General | Consultor Datasphere | 2 |
| 5 | Pruebas iniciales (generar semantics sobre tablas/views) | Configuración Datasphere | General | Consultor Datasphere | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datasets reales no-SAP | Consultor Datasphere | 5 |
| 2 | Documentación para el cliente | Consultor Datasphere | 4 |
| 3 | Transferencia de conocimiento | Consultor Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Semántica generada es propuesta; modeler revisa y refina.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J336] — Error Resolution for Cost Accounting

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Ayuda a los contadores de costos a identificar y resolver errores relacionados con contabilidad de costos, ofreciendo orientación asistida para atender incidencias del proceso.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **CO – Controlling / Cost Accounting** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción a S/4HANA Public Edition con CO.
- Entitlement de Joule sobre S/4HANA Public (capability **Base** según AI Foundation Catalog) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items base de Overhead Cost Accounting / Cost Allocation — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de CO donde se generan los mensajes de error (asignaciones, distribuciones, settlements).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Maestros CO (cost centers, internal orders, cost elements, allocation cycles) configurados.
- Documentos / postings que producen los errores a explicar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar matriz de idiomas]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones CO sobre los objetos afectados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración funcional CO (cycles, settlements, distributions) | Configuración CO | General | Consultor CO | 3 |
| 3 | Asignar business roles CO con catálogos de Joule a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar la capability de Joule para Cost Accounting Errors | Joule capability scope | General | Consultor Funcional CO + Joule | 2 |
| 5 | Pruebas iniciales: provocar/replicar errores típicos y validar explicaciones de Joule | Configuración funcional CO | General | Consultor CO | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales de error (allocations, settlements, derivations) | Consultor CO | 4 |
| 2 | Documentación para el cliente | Consultor CO | 4 |
| 3 | Transferencia de conocimiento | Consultor CO | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **explica errores y propone acciones**; la corrección final la decide el usuario en su app destino.
- Respeta autorizaciones; no eleva privilegios.
- Cobertura de tipos de error puede ampliarse en releases sucesivos — revisar **Road Map Explorer**.
- Sin desarrollos custom dentro del alcance estándar.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J342] — Embedded Edition

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP Document AI — Embedded Edition** automatiza tareas de procesamiento documental de punta a punta, ejecución de workflows e integración de canales. SAP indica una reducción del **70% en el tiempo** para procesar documentos, **83% en el tiempo** para mantener plantillas y **40% de reducción** en pérdida de valor por retrasos en procesamiento manual.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document AI** activo (Embedded Edition).
- **SAP Document AI Workspace** configurado.
- Sistema(s) destino que reciben los datos extraídos (típicamente **SAP S/4HANA**) con conectividad operativa.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document AI**.
- Capability **Premium** — activación con **AI Units**.
- **AI Units** asignadas al tenant; pricing por volumen mostrado en *Pricing Details* de Discovery Center **[verificar volumen y costo vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; el escenario funcional (p. ej. *Accounts Payable Invoice Processing*) en el sistema destino tiene su scope item asociado **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Document AI — UI básica / Workspace** disponible para los usuarios objetivo.
- Canales de entrada configurados (p. ej. **buzones de correo**, *upload* manual, integración API).
- Workflows configurados para enrutar el documento extraído hacia el sistema destino.

### 1.5 Datos maestros / transaccionales previos
- Esquemas (predefinidos o personalizados) para los tipos de documento del cliente.
- Datos maestros consistentes en el sistema destino para validar el match de proveedores / clientes / materiales.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción según el modelo subyacente **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos con baja calidad reducen la tasa de extracción correcta.
- **Roles**: administradores de Document AI con permisos para crear schemas y workflows; operadores con acceso al workspace.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_DOCUMENT_AI describe el Initial Setup de SAP Document AI: suscripción, acceso y uso de la UI básica / workspace para Embedded Edition y Premium Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Document AI y AI Units en SAP BTP | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 2 |
| 2 | Aprovisionar AI Units para el volumen estimado | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Aprovisionar el **SAP Document AI Workspace** | Workspace Document AI | General | Consultor SAP Document AI | 3 |
| 4 | Configurar esquemas / plantillas para los tipos de documento del cliente | Schemas Document AI | Particular (por tipo de documento) | Consultor SAP Document AI | 5 |
| 5 | Configurar canales de entrada (correo, API, upload) y workflows hacia el sistema destino | Channels + Workflows Document AI | Particular (por proceso) | Consultor SAP Document AI + Integration Suite | 5 |
| 6 | Asignar a los usuarios objetivo los roles de Document AI | Roles SAP Document AI | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 7 | Pruebas iniciales en Quality con documentos reales del cliente | Configuración funcional Document AI | General | Consultor SAP Document AI | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~23 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (varios tipos, varios proveedores / formatos) | Consultor SAP Document AI | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación / monitoreo) | Consultor SAP Document AI | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica de operación) | Consultor SAP Document AI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units por volumen**: dimensionar con cuidado y planificar el crecimiento.
- La **tasa de extracción** depende de la calidad de los documentos y la cobertura de schemas: planificar un periodo de afinamiento.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza: intervención humana o re-clasificación.
- Considerar **gobernanza / data residency** sobre dónde se procesa el documento y dónde se almacenan los datos extraídos.
- Joule / Document AI respetan las autorizaciones del usuario operador: **no eleva privilegios**.
- Sujeto a la **fair-use policy** y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- SAP Help Portal — SAP Document AI: https://help.sap.com/docs/SAP_DOCUMENT_AI

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 23 |
| Validación + documentación + KT | 11 |
| **Total** | **34** |

---

## [J346] — Note Corrections for Project Billing

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** La función **Smart Notes** en *Manage Project Billing* propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura. SAP indica una **reducción del 50%** del tiempo dedicado a correcciones de notas en postings de Time & Expenses.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **Project Billing / Project Financial Control** operativo (uso de *Manage Project Billing*).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Project Billing / Project Financial Control** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Project Billing** habilitada para los usuarios objetivo.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Proyectos, ítems de Time & Expenses con notas y *project billing requests* abiertos.
- Configuración funcional de Project Billing completada.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: las propuestas de corrección se generan según el modelo subyacente **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener el rol de **Billing Specialist** con acceso a Manage Project Billing.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html describe la configuración de Smart Notes para Project Billing. El procedimiento involucra asignar roles y validar disponibilidad de Smart Notes en *Manage Project Billing*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Asignar a los usuarios objetivo el business role de Billing Specialist con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Validar disponibilidad de Smart Notes dentro de *Manage Project Billing* | Configuración funcional Project Billing | General | Consultor Funcional Project Billing | 2 |
| 5 | Pruebas iniciales con un Billing Specialist piloto (revisión de propuestas de corrección sobre ítems representativos) | Configuración funcional Project Billing | General | Consultor Funcional Project Billing | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (correcciones sobre ítems representativos de varios proyectos) | Consultor Funcional Project Billing | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de revisión de notas) | Consultor Funcional Project Billing | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Project Billing | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- La propuesta es **una sugerencia**: el Billing Specialist debe revisar, editar o descartar cada cambio antes de emitir la factura.
- Considerar el impacto en **cobranza y satisfacción del cliente**: notas claras reducen disputas en factura.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- SAP Help Portal — Smart Notes for Project Billing: https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J355] — Posting Issue Handling for Billing Documents

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Asiste a billing clerks a recuperar y visualizar documentos de facturación con problemas de contabilización según criterios determinados. SAP indica: *65% de reducción en el tiempo para analizar y resolver problemas de contabilización de facturación.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Billing** + **FI-AR** operativos.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Billing & Receivables Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Billing Documents*, *Billing Document Items - Issues*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Maestros de clientes, condiciones, cuentas contables de ingresos.
- Documentos de facturación con issues de posting (incompletos, con error de cuenta, sin pricing, etc.).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD-Billing / FI-AR.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Billing (account determination, pricing, output) | Configuración SD-Billing | General | Consultor SD | 3 |
| 3 | Asignar business roles billing/AR a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Posting Issues | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: provocar/replicar issues típicos y validar resolución asistida | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (account determination fail, pricing missing, etc.) | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **asiste al billing clerk**, no sustituye la decisión funcional.
- Respeta autorizaciones.
- Tipos de issue cubiertos se amplían por wave — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J358] — Processing of Incoming Quality Certificates with SAP Document AI

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition. SAP indica: *La página indica reducción del tiempo de procesamiento de certificados de calidad y protección de ingresos al disminuir retrasos de inspección relacionados con procesamiento documental.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP).
- Componente **QM – Quality Management** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con QM.
- Entitlement de **SAP Document AI** en BTP (capability **Premium** según AI Foundation Catalog) **[verificar pricing vigente]**.
- Entitlement de Joule si la interacción se hace vía copilot.

### 1.3 Scope item relacionado
- Scope items de Quality Management - Inspection (incoming certificates) — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Process Incoming Quality Certificates* / *Quality Inspection Worklist*.
- Communication arrangement S/4HANA Public ↔ Document AI (escenario **SAP_COM_xxxx** — **[verificar]**).

### 1.5 Datos maestros / transaccionales previos
- Maestros de materiales con vista QM, supplier certificate profile, certificate types.
- Quality info records y procurement inspection types configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas soportados por Document AI según matriz vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Formato de documento (PDF / imagen) soportado por Document AI.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar SAP Document AI en BTP y confirmar quotas | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 3 |
| 2 | Configurar el communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al documento QM destino | Mapping Document AI ↔ Quality Certificate | Particular (por tipo de certificado / proveedor) | Consultor QM + Integración | 6 |
| 4 | Asignar business roles QM con catálogos de procesamiento de certificados | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales: ingesta de certificados reales y validación de extracción + posting | Configuración funcional QM | General | Consultor QM | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real de certificados (mínimo 2-3 layouts representativos) | Consultor QM | 6 |
| 2 | Documentación para el cliente | Consultor QM | 4 |
| 3 | Transferencia de conocimiento | Consultor QM | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout del proveedor; podrían necesitarse iteraciones de templates para extracción óptima.
- Volumen de documentos sujeto a cuotas de Document AI.
- Trazabilidad: documentos originales pueden almacenarse adjuntos al documento QM.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |

---

## [J36] — Generation of Full-Stack Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural. Con Joule, la capacidad genera modelos de datos, servicios, datos de ejemplo, anotaciones de UI, lógica de aplicación y pruebas unitarias, dentro de un entorno de desarrollo cloud alineado con SAP Business Application Studio y buenas prácticas de SAP BTP. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor de negocio está en acelerar el ciclo de desarrollo, reducir esfuerzo manual y mejorar la productividad de equipos técnicos que crean extensiones y aplicaciones sobre SAP Build Code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** en BTP.
- Joule integrado (Joule for Developers) **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code con feature Joule (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- Conectividad a backends (CAP / SAP HANA Cloud) si la app integra datos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SAP Build Code + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar conectividad a backends (si aplica) | Destinations / DB | General | Consultor BTP | 4 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar capability Joule Generation | Configuración Build Code | General | Consultor BTP / Dev | 2 |
| 5 | Pruebas iniciales: generar app de muestra con prompts | Configuración Build Code | General | Desarrollador Sr | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Código generado requiere review/refactor humano.
- Seguridad: validar autenticación, autorización, secrets.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J404] — Sales Order Creation from Unstructured Data

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes. Después de cargar el archivo, la información se procesa automáticamente para generar una solicitud de pedido de venta que luego puede convertirse en pedido. SAP indica: *La página indica una reducción del 33% en el esfuerzo manual para crear pedidos de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP) para extracción de datos del input no estructurado (PDF/email/imagen).
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con SD.
- Entitlement de **SAP Document AI** (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management + Document AI integration — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*, *Document Information Extraction Workspace*.
- Communication arrangement S/4HANA ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.
- Tipos de documento de entrada (formato PDF / email parseable / imagen) soportados por Document AI.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Layout del PO del cliente debe ser razonablemente extraíble.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al sales order | Mapping Document AI ↔ SO | Particular (por layout/cliente) | Consultor SD + Integración | 6 |
| 4 | Asignar business roles SD con catálogos de SO + Document AI | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con PDFs reales de PO del cliente | Configuración funcional SD | General | Consultor SD | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real (mínimo 2-3 layouts representativos) | Consultor SD | 6 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout de la fuente; pueden requerirse iteraciones por proveedor/cliente.
- Volumen sujeto a cuotas de Document AI.
- Usuario sigue validando antes de guardar la orden.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |

---

## [J43] — Sales Order Automatic Completion

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Mediante datos históricos y machine learning, la función recomienda valores para completar campos vacíos en órdenes de venta incompletas. SAP indica: *La página indica una reducción del 25% en esfuerzo manual para completar órdenes de venta, ayudando a acelerar el ciclo comercial y reducir errores.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Sales Orders*, *Create Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, plants, sales areas configurados.
- Datos históricos suficientes para que las recomendaciones tengan calidad.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD (sales areas, document types, pricing) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Completion | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: crear sales orders con datos parciales y validar recomendaciones | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Recomendaciones mejoran con volumen / calidad de datos históricos.
- Usuario sigue confirmando antes de guardar.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J45] — Inventory Prompts

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP LeanIX Inventory Prompts** combina la información del inventario LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial mediante una interfaz de lenguaje natural. SAP indica **90% de reducción** del tiempo para generar insights de artefactos del landscape de TI.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo con inventario cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con AI Capabilities habilitadas e *Inventory AI prompts* disponible.

### 1.5 Datos maestros / transaccionales previos
- Inventario LeanIX poblado con datos suficientes (aplicaciones, capacidades, relaciones) para que las consultas devuelvan resultados significativos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: usuario LeanIX con permisos sobre el dominio que va a consultar.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/leanix/ea/ai-capabilities menciona capacidades base de IA, incluyendo Inventory AI prompts. El contenido completo del procedimiento no fue totalmente extractable.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX (incluyendo Inventory AI prompts) | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Inventory Prompts | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 4 | Pruebas iniciales con un usuario piloto (consultas de inventario representativas) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios dominios / niveles de detalle) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad depende **directamente de la calidad y cobertura del inventario** en LeanIX.
- Joule / LeanIX respetan las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** para que la organización aproveche la capability de manera consistente.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J471] — AI-Assisted Calculations

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP for Me). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos, y explicar fórmulas existentes en lenguaje claro. SAP indica una reducción del **60% en el tiempo de creación de cálculos** y **60% en el tiempo de comprensión** de cálculos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).
- Tenant SAC desplegado en un **data center que soporte SAP Business AI** **[verificar matriz de data centers vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Premium** — activación con **AI Units** (consumo registrado y consultable en SAP for Me).
- **AI Units** asignadas al tenant para esta feature **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- No aplica scope item (SAP Analytics Cloud no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias (*stories*) y modelos analíticos donde se vayan a usar los cálculos asistidos.
- Acceso a **SAP for Me** para administradores del tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Modelos y datasets de SAC publicados con métricas, dimensiones y jerarquías necesarias para crear los cálculos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: el diálogo asistido por IA está principalmente en **inglés** **[verificar matriz vigente]**.
- **Disponibilidad regional**: depende del data center del tenant.
- **Roles**: el usuario debe tener permisos para crear/editar cálculos en SAC.

> **Setup oficial SAP**: el procedimiento documentado consiste en:
> 1. Iniciar sesión en **SAP for Me**.
> 2. En el panel de navegación, elegir **Portfolio & Products**.
> 3. Elegir **Business AI**.
> 4. Seleccionar **Request Activation** junto al nombre de la feature.
>
> SAP Support notificará cuando la feature haya sido activada.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar que el tenant SAC está en un data center que soporta SAP Business AI | Tenant SAC | General | Consultor SAC + Consultor BTP | 1 |
| 2 | Confirmar entitlement de AI Units para SAC en el tenant del cliente | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Solicitar la activación de la feature *AI-Assisted Calculations* desde **SAP for Me** → *Portfolio & Products* → *Business AI* → *Request Activation* | SAP for Me — Request Activation | General | Consultor SAC + Cliente Admin | 1 |
| 4 | Esperar notificación de SAP Support sobre la activación | (Solicitud SAP Support) | General | (gestión con SAP Support) | 0 |
| 5 | Asignar a los usuarios los roles SAC con permisos para crear/editar cálculos | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 6 | Pruebas iniciales con un usuario piloto (crear y explicar cálculos en historias representativas) | Configuración funcional SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas (excluyendo tiempo de SAP Support para activar la feature).**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con cálculos reales del cliente (creación y explicación de fórmulas representativas) | Consultor SAC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La activación **no es self-service** dentro del tenant: requiere **solicitud a SAP Support** vía SAP for Me. El tiempo de respuesta de SAP no es controlable por el equipo de implementación.
- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- **Confirmar el data center** del tenant: solo data centers compatibles con SAP Business AI ofrecen la feature.
- Las fórmulas generadas deben ser **validadas funcionalmente** por el usuario antes de usarse en producción: la IA es asistencia, no reemplaza el control de calidad analítico.
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8dcc1f1915b241b3a10c8e5b8a76b062.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J47] — AI-Assisted Texting

> Análisis basado en información públicamente documentada por SAP (SAP LeanIX Help, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que permite crear o mejorar textos analizando contenido y contexto, con opciones para reescribir o resumir información existente (p. ej. generar descripciones para fact sheets). SAP indica hasta un **80% de reducción** en el tiempo para completar descripciones de aplicaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo con fact sheets que se vayan a usar.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** — incluida según el contrato comercial vigente.
- **SAP AI terms** incluidos para nuevos clientes; clientes anteriores deben confirmar con su representante SAP si los términos de IA están firmados.

### 1.3 Scope item relacionado
- No aplica scope item (SAP LeanIX no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con fact sheets / atributos donde se vaya a usar la asistencia textual.
- Roles administrativos LeanIX para activar AI Capabilities **[verificar permisos exactos]**.

### 1.5 Datos maestros / transaccionales previos
- Fact sheets del workspace con suficiente contenido para reformular/resumir.
- Configuración del metamodelo LeanIX vigente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: el usuario debe tener permisos para crear/editar contenido textual en LeanIX.
- **Contractuales**: SAP AI terms firmados.

> **Setup oficial SAP**: la página `https://help.sap.com/docs/leanix/ea/ai-capabilities` identifica la activación de AI Capabilities para SAP LeanIX. El extracto disponible no expone el procedimiento completo paso a paso.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar con representante SAP que los términos de IA de LeanIX están firmados (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asignar a los usuarios objetivo los roles LeanIX con acceso a la funcionalidad de texto asistido | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 4 | Pruebas iniciales con un usuario piloto (reescribir / resumir descripciones de fact sheets) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con contenido real del cliente (descripciones, reescritura, resumen sobre fact sheets representativos) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La habilitación depende de **términos contractuales de IA**: validar antes de planificar la activación.
- Los textos generados deben ser **revisados** por el responsable funcional antes de publicarse: la IA asiste, no reemplaza el control editorial.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J48] — Translation Support

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Traducción asistida por IA en **SAP LeanIX** que permite a administradores agregar y traducir etiquetas y textos de ayuda para atributos nuevos o existentes en la configuración del metamodelo. El valor está en reducir el tiempo requerido para traducir términos del metamodelo y mejorar la accesibilidad del producto.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con acceso al **metamodel administration** del workspace.

### 1.5 Datos maestros / transaccionales previos
- Metamodelo LeanIX del cliente con atributos / labels existentes a traducir.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idiomas soportados**: según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: Workspace Admin / EA Admin con acceso a la configuración del metamodelo.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Identificar atributos / labels del metamodelo objetivo de traducción | Metamodel LeanIX | Particular (por atributo / dominio) | Consultor SAP LeanIX | 3 |
| 4 | Asignar a los usuarios objetivo los roles administrativos LeanIX con acceso al metamodelo | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Workspace Admin (traducir un conjunto representativo de labels) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con traducciones reales del cliente (varios dominios / idiomas) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de traducción) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las traducciones generadas son **borradores**: deben ser revisadas por personas con dominio del idioma destino antes de publicarse, especialmente para términos técnicos.
- Considerar **gobernanza** sobre quién aprueba el cambio en el metamodelo (afecta a todos los usuarios del workspace).
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |

---

## [J54] — Joule with SAP S/4HANA Cloud Private Edition

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Caso "paraguas" que habilita Joule como copilot sobre S/4HANA Cloud Private Edition. Es prerequisito de muchas otras capabilities Joule sobre Private.

**Resumen del caso:** Permite usar lenguaje natural para expresar requerimientos de negocio y acceder a capacidades informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Private Edition. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se centra en productividad, navegación y ejecución de tareas en SAP S/4HANA Cloud Private Edition.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** en release con soporte de Joule **[verificar release mínima vigente]**.
- **SAP Business Technology Platform (BTP)** con tenant en región soportada.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition vigente.
- Entitlement de Joule activado en BTP (capability Base; Premium con addon).

### 1.3 Scope item relacionado
- Scope item de habilitación de Joule sobre S/4HANA Private — **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Launchpad con panel de Joule visible.
- Communication arrangement S/4HANA Private ↔ servicio de Joule en BTP (escenario **SAP_COM_xxxx** — **[verificar]**).
- Identity provider (IAS / corporate IdP) configurado.

### 1.5 Datos maestros / transaccionales previos
- SSO operativo entre S/4HANA Private y BTP.
- Business roles y catálogos asignados a usuarios.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar matriz]**.
- Disponibilidad regional sujeta a tenant.
- Joule respeta autorizaciones del usuario.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar entitlement Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar identity propagation IAS / IdP ↔ S/4HANA Private | Trust / SSO | General | Consultor Basis / Seguridad | 4 |
| 3 | Activar communication scenario de Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Habilitar el panel Joule en el launchpad | Launchpad configuration | Particular (por spaces & pages) | Consultor S/4HANA Private | 4 |
| 5 | Asignar business roles con catálogos Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 4 |
| 6 | Pruebas iniciales end-to-end | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~22 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos por área | Consultor Funcional + key user | 6 |
| 2 | Documentación para el cliente | Consultor Funcional | 5 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 4 |

**Esfuerzo total estimado (validación + entrega): ~15 horas.**

---

## 4. Consideraciones especiales

- **Habilitador transversal** Private: una vez activo, demás capabilities Joule sobre Private requieren típicamente solo enablement adicional.
- En Private aplican consideraciones de upgrade compatibility con la versión del stack ABAP del cliente.
- Trazabilidad / fair-use / cuotas — revisar políticas vigentes.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 22 |
| Validación + documentación + KT | 15 |
| **Total** | **37** |

---

## [J57] — Joule with SAP Business Technology Platform

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se expresa en ahorro de tiempo para consultas administrativas y acceso más rápido a información de BTP.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP BTP** con uno o más subaccounts productivos.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule + capability BTP (Base) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- BTP Cockpit accesible.
- Joule habilitado para usuarios admin / desarrolladores.

### 1.5 Datos maestros / transaccionales previos
- Estructura de global account / directories / subaccounts.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol BTP Admin / Member.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + capability BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Habilitar Joule en BTP Cockpit | Configuración BTP | General | Consultor BTP | 2 |
| 3 | Asignar roles BTP a usuarios | Roles BTP | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Pruebas iniciales (consultar quotas, services, account info) | Configuración BTP | General | Consultor BTP | 3 |

**Esfuerzo total estimado (activación): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos | Consultor BTP | 4 |
| 2 | Documentación para el cliente | Consultor BTP | 3 |
| 3 | Transferencia de conocimiento | Consultor BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Joule consulta; acciones administrativas siguen en BTP Cockpit / CLI.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 10 |
| **Total** | **21** |

---

## [J586] — Project Services

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule incorpora una interfaz conversacional para apoyar actividades rutinarias de gestión de proyectos en SAP S/4HANA Cloud Public Edition. La capacidad ayuda a monitorear cumplimiento de tiempos, resumir cambios de proyecto y ofrecer autoservicio con IA para equipos de proyecto. SAP indica: *La página posiciona la capacidad con una reducción del 60% en esfuerzos de administración de proyectos, acelerando decisiones y mejorando la productividad de los equipos de proyecto.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **PS / Commercial Project Management / Professional Services** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con módulo de Projects.
- Entitlement Joule (**Base**) **[verificar en AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- Scope items de Project Management / Professional Services Delivery — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Projects*, *Project Control*, *Task Management*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Estructuras de proyecto (WBS, tasks, milestones), employees, customers, tipos de proyecto configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones sobre los proyectos consultados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Projects (tipos, profiles, status) | Configuración PS | General | Consultor PS | 3 |
| 3 | Asignar business roles Project Manager / Member a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Project Services | Joule capability scope | General | Consultor Funcional PS + Joule | 2 |
| 5 | Pruebas iniciales conversacionales (consultar, actualizar tareas) | Configuración funcional PS | General | Consultor PS | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (crear/actualizar tareas, consultar estado) | Consultor PS | 4 |
| 2 | Documentación para el cliente | Consultor PS | 4 |
| 3 | Transferencia de conocimiento | Consultor PS | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **gestiona tasks** vía conversación; reportes/analytics se siguen en apps Fiori.
- Respeta autorizaciones por proyecto.
- Cobertura de acciones se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J597] — Back Order Processing

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Road Map Explorer, AI Foundation Catalog). Valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Funcionalidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución y configuración de Back Order Processing mediante interacciones intuitivas basadas en prompts. SAP indica: *Mejora la velocidad y calidad de la ejecución de BOP. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente funcional **SD – Sales** (Back Order Processing — BOP) operativo en el sistema.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción a S/4HANA Cloud Public Edition con módulo SD.
- Entitlement de **Joule** sobre S/4HANA Public; capability incluida como **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope item de Sales Order Management con BOP — **[verificar el ID exacto en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de BOP en S/4HANA Public (*Configure BOP Variants*, *Schedule BOP Run*, *Monitor BOP Runs*).
- Joule habilitado en el Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Materiales, customers, sales orders y ATP / aATP configurados.
- Variantes de BOP definidas y operativas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones Joule principalmente en inglés **[verificar matriz vigente]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario debe contar con autorizaciones SD para BOP.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar que BOP esté correctamente configurado (variantes, segmentos, prioridades) | Configuración BOP | General | Consultor SD | 3 |
| 3 | Asignar business roles SD con catálogos BOP a los usuarios objetivo | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 4 | Habilitar la capability de Joule para BOP (si gating por configuración) | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales con prompts típicos (ejecutar BOP, revisar resultados) en Quality | Configuración funcional SD | General | Consultor SD | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (escenarios típicos: ejecución BOP, redistribución de stock, priorización) | Consultor SD | 4 |
| 2 | Documentación para el cliente (manual de usuario + configuración) | Consultor SD | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **no extiende la lógica funcional de BOP**: ejecuta y consulta apoyado en lo ya configurado.
- Los resultados respetan las autorizaciones del usuario (no eleva privilegios).
- Sujeto a fair-use de Joule **[verificar políticas vigentes]**.
- Sin desarrollos custom: cualquier extensión queda fuera del alcance estándar.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J600] — Joule with SAP Multi-Bank Connectivity

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP AI Roadmap Explorer, SAP Multi-Bank Connectivity product page). Cualquier valor marcado como **[verificar en SAP Help]** debe ser validado contra la documentación oficial vigente antes de la activación en cliente.

**Resumen del caso:** Proporciona respuestas rápidas sobre SAP Multi-Bank Connectivity a partir de documentación del producto en SAP Help Portal, resumidas de forma contextual y clara. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se expresa en ahorro de tiempo de búsqueda, mejor acceso a documentación y mayor satisfacción del usuario.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado (el caso de uso es nativo S/4HANA Public Cloud + Joule).
- **SAP Multi-Bank Connectivity (MBC)** activo en el landscape del cliente. MBC es un servicio gestionado por SAP que enruta mensajes financieros entre S/4HANA y las entidades bancarias vía SWIFT / EBICS.
- **SAP Business Technology Platform (BTP)** — tenant donde se aprovisiona el servicio de Joule.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Multi-Bank Connectivity**.
- **Entitlement de Joule** sobre S/4HANA Cloud Public Edition.
- Este caso aparece como **Premium** en SAP AI Foundation Catalog → requiere addon premium de Joule **[verificar en SAP Help: detalle de pricing/entitlement vigente]**.

### 1.3 Scope item relacionado
- Scope item base de Cash Management / Bank Integration en S/4HANA Cloud Public Edition (familia **J77 – Advanced Cash Operations** / **BFA – Basic Bank Account Management**) — **[verificar el ID exacto del scope item asociado al caso J600 en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori del área **Cash Management** y **Bank Communication Management** (p. ej. *Manage Bank Statements*, *Manage Payment Files*, *Bank Communication Management*).
- Servicio de comunicación y escenario de comunicación con destino **SAP Multi-Bank Connectivity** ya configurado y activo (p. ej. escenarios SAP_COM_0088 / equivalentes vigentes — **[verificar IDs]**).
- Habilitación del asistente **Joule** en el Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- House Banks y Bank Accounts dados de alta en S/4HANA.
- Bank Account Master Data sincronizada con MBC.
- Payment Methods, Payment Method Supplements y Bank Determination configurados.
- Conectividad bancaria operativa (mensajes de prueba de MBC con la entidad bancaria validados).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: Joule, a la fecha, soporta principalmente **inglés** para interacciones de negocio; otros idiomas pueden estar en GA limitada **[verificar matriz de idiomas vigente en SAP Help Portal]**.
- **Edición**: solo S/4HANA Cloud **Public** Edition (este caso J600 está catalogado específicamente bajo MBC + Public Cloud).
- **Roles**: el usuario final debe tener los business roles de tesorería/cash manager con autorización sobre los objetos de MBC.
- **Región / data residency**: disponibilidad del servicio de Joule sujeta a la región del tenant **[verificar]**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule (Premium) y MBC en BTP / Cockpit | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Activar Joule en el tenant de S/4HANA Cloud Public Edition (si no estaba) | Configuración global de Joule | General | Consultor S/4HANA Cloud (Basis/Functional) | 3 |
| 3 | Verificar / activar el escenario de comunicación con SAP Multi-Bank Connectivity | Communication Arrangement / Communication Scenario MBC | General | Consultor Integración S/4HANA | 4 |
| 4 | Asignar a los usuarios objetivo los business roles de tesorería con Joule habilitado | Business Role / Catalog assignment | Particular (por usuario / grupo de usuarios) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar el skill / capability de Joule para MBC en la configuración de Joule de la app | Joule capability scope (MBC) | General | Consultor Funcional Treasury + Joule | 2 |
| 6 | Pruebas de conectividad end-to-end Joule → MBC (consulta de estado de pagos, statements) con un usuario piloto | Configuración funcional Treasury | General | Consultor Funcional Treasury | 3 |

> **Notas**:
> - Los pasos 1–4 son configuración base; si el cliente ya tiene MBC operativo y Joule habilitado, el esfuerzo se concentra en los pasos 5–6.
> - Los IDs específicos de Communication Scenario, Business Catalog y nombre exacto del Joule capability deben confirmarse contra la **Setup Guide oficial de SAP para el caso J600** en el momento de la activación.

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales (consultas Joule sobre estados de pago / extractos MBC en entorno de Quality) | Consultor Funcional Treasury | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Treasury | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Treasury | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- El caso de uso asume que **MBC ya está implantado y productivo**; la activación de Joule sobre MBC **no incluye** el onboarding bancario ni la conexión SWIFT inicial.
- Joule responde sobre datos a los que el usuario ya tiene autorización; **no eleva privilegios**: validar la matriz de autorizaciones antes del rollout.
- Joule puede estar sujeto a **fair-use policy / cuotas de uso**; revisar términos vigentes para evitar throttling en cargas pico **[verificar en condiciones de servicio Joule]**.
- **Trazabilidad / auditoría**: las interacciones con Joule pueden almacenarse para auditoría; revisar políticas de privacidad y data residency aplicables.
- **Roadmap**: SAP amplía periódicamente las skills de Joule sobre MBC. Antes de la activación, revisar el **SAP Road Map Explorer** y release notes de la wave vigente para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos** (extensiones, custom skills); cualquier requerimiento de personalización queda **fuera del alcance estándar**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 11 |
| **Total** | **28** |

---

## [J606] — Anomaly Detection

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Integration Suite** que identifica patrones inusuales o desviaciones en el tráfico de APIs mediante IA, apoyando la detección temprana de anomalías. SAP indica reducción del **costo de resolución de anomalías** de API.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (suscripción activa).
- **API Management** habilitado dentro de SAP Integration Suite.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Integration Suite**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Integration Suite — API Management** con las APIs candidatas publicadas y monitoreadas.

### 1.5 Datos maestros / transaccionales previos
- **APIs publicadas en API Management** con historia de tráfico suficiente para entrenar y aplicar el modelo de anomalías.
- Logs de runtime / métricas de tráfico capturados por API Management.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (la capability trabaja sobre métricas técnicas, no diálogo).
- **Volumen de datos**: requiere historia suficiente; APIs con bajo volumen pueden producir detecciones poco significativas.
- **Roles**: API Admin / API Owner con permisos en Integration Suite.

> **Setup oficial SAP**: el procedimiento es *Configuring APIs for Anomaly Detection* en https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-apis-for-anomaly-detection. La documentación remite a los prerrequisitos de selección de APIs y a habilitar la detección desde Integration Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Integration Suite con API Management activo | Subaccount BTP + entitlement Integration Suite | General | Consultor BTP | 2 |
| 2 | Identificar el conjunto de APIs candidatas con historia de tráfico suficiente | API Management — Catálogo de APIs | Particular (por API) | Consultor Integration Suite | 3 |
| 3 | Habilitar Anomaly Detection sobre las APIs seleccionadas | API Management — Anomaly Detection | Particular (por API seleccionada) | Consultor Integration Suite | 3 |
| 4 | Asignar a los usuarios objetivo los roles con visibilidad de la detección | Roles SAP Integration Suite | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 5 | Pruebas iniciales (monitorear detecciones durante un periodo de observación inicial en Quality / Producción) | Configuración funcional Integration Suite | General | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con tráfico real (provocar anomalías controladas en APIs no críticas y validar detección) | Consultor Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de operación y respuesta a anomalías) | Consultor Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión de respuesta a incidentes) | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La detección depende de **volumen y calidad del tráfico histórico**: APIs nuevas o con bajo tráfico pueden producir falsos positivos / negativos.
- Definir **procesos de respuesta** a anomalías antes del rollout (qué hace el equipo cuando se detecta una desviación).
- Sujeto a las condiciones de servicio vigentes de SAP Integration Suite **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/
- SAP Help Portal — Configuring APIs for Anomaly Detection: https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-apis-for-anomaly-detection

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J638] — Process Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Generation genera artefactos de proceso a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation. SAP indica: *Su valor está en reducir esfuerzo de automatización low-code, acelerar la productividad de desarrolladores y mejorar el time-to-market de soluciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Lobby + Process Editor).

### 1.5 Datos maestros / transaccionales previos
- Conocimiento del proceso a generar (descripción en NL, ejemplos).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales: generar proceso desde prompt y desplegar en QAS | Configuración SBPA | General | Consultor SBPA | 4 |

**Esfuerzo total estimado (activación): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Consultor SBPA | 5 |
| 2 | Documentación para el cliente | Consultor SBPA | 4 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Procesos generados son borradores; refactor humano + tests requeridos.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 12 |
| **Total** | **23** |

---

## [J639] — Process Editing (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Editing ayuda a desarrolladores durante el diseño e implementación de automatizaciones, permitiendo editar artefactos de proceso mediante instrucciones en lenguaje natural. SAP indica: *La capacidad se asocia con reducción del esfuerzo de automatización low-code, mayor productividad de desarrolladores y mejor velocidad de entrega de nuevas aplicaciones o procesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Process Editor).

### 1.5 Datos maestros / transaccionales previos
- Procesos existentes a editar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Editing | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (editar proceso con prompts) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con procesos reales | Consultor SBPA | 4 |
| 2 | Documentación para el cliente | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Edición asistida; revisión humana antes de publicar.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |

---

## [J640] — Process Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que genera resúmenes en lenguaje natural de procesos o artefactos complejos para facilitar comprensión, revisión y transferencia de conocimiento. El valor está en mayor productividad en diseño/implementación low-code y menor esfuerzo de revisión y documentación.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Acceso al entorno con artefactos de proceso o automatizaciones existentes.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con capacidad de generative AI habilitada.

### 1.5 Datos maestros / transaccionales previos
- Procesos / automatizaciones ya modelados en SAP Build Process Automation.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Build Process Automation **[verificar idiomas soportados vigentes]**.
- **Roles**: Developer / Process Owner con permisos sobre los artefactos.

> **Setup oficial SAP**: el enlace https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup describe el Initial Setup general de SAP Build Process Automation. Las capacidades de generative AI se habilitan dentro de ese entorno.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidades de IA generativa | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Validar / habilitar las capacidades de generative AI en el subaccount | Configuración Build Process Automation — Generative AI | General | Consultor BTP / Build | 2 |
| 3 | Asignar a los usuarios objetivo los roles con acceso a la capability | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer / process owner piloto (resúmenes sobre procesos representativos) | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con artefactos reales del cliente (resúmenes sobre procesos representativos) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Los resúmenes son **descriptivos**: el usuario sigue siendo responsable de validar que el resumen represente correctamente el proceso.
- Útil en **handovers, revisiones funcionales y documentación**: definir gobernanza sobre cuándo el resumen reemplaza documentación formal.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J641] — Form Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Genera formularios de automatización de procesos a partir de descripciones en lenguaje natural en SAP Build Process Automation. SAP indica: *Reducción estimada del 30% en esfuerzo de automatización low-code; 10% más rápido el tiempo de productividad para desarrolladores; 10% de mejora en time-to-market para nuevas aplicaciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** activo en BTP.
- Capability AI / Joule integrada **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA con feature AI (Premium si aplica) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Form Designer).

### 1.5 Datos maestros / transaccionales previos
- Datos de proceso de referencia (data types, project).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Form Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (generar forms con prompts) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SBPA | 4 |
| 2 | Documentación para el cliente | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Forms generadas son borradores; revisión humana requerida.
- Buenas prácticas: validar accesibilidad y UX.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |

---

## [J642] — Decision Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Asiste el diseño de procesos al generar artefactos de decisión a partir de descripciones en lenguaje natural de las reglas deseadas. SAP indica: *30% de reducción del esfuerzo de automatización low-code; 10% menor tiempo hasta productividad para desarrolladores; 10% mejora del time-to-market para nuevas aplicaciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** activo en BTP.
- Capability AI / Joule integrada **[verificar AI Foundation Catalog]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA con feature AI habilitada (Premium si aplica) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Lobby, Process/Decision editor).

### 1.5 Datos maestros / transaccionales previos
- Acceso a las fuentes de reglas/datos sobre las que se genera la decisión.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer a usuarios | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar la capability Decision Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (generar decision tables/rules con prompts) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SBPA | 4 |
| 2 | Documentación para el cliente | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Genera artefactos de decisión iniciales; revisión humana sigue siendo necesaria.
- Buenas prácticas: testear cobertura de reglas.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |

---

## [J643] — Decision Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que asiste a los usuarios en el diseño e implementación de automatizaciones al generar resúmenes de negocio de reglas ya modeladas que no tienen documentación. SAP indica **30% de reducción** del esfuerzo de automatización low-code, **10% menor tiempo a productividad** para desarrolladores y **10% mejora en time-to-market** de nuevas aplicaciones low-code.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Acceso al entorno de Build Process Automation del cliente con artefactos de decisión ya modelados.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con módulos de Decision / Workflow activos.
- Capacidades de IA generativa habilitadas en SAP Build Process Automation.

### 1.5 Datos maestros / transaccionales previos
- **Artefactos de decisión** (DMN, reglas de negocio) ya modelados en el entorno del cliente.
- Procesos y workflows existentes para los que se quiera generar resúmenes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Build Process Automation **[verificar idiomas soportados vigentes]**.
- **Roles**: Developer / Process Owner con permisos sobre los artefactos de decisión.

> **Setup oficial SAP**: la página https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai indica que las capacidades de generative AI están disponibles dentro de SAP Build Process Automation para resumir artefactos complejos o reglas de negocio. El contenido extraído no expone pasos administrativos adicionales.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidades de IA generativa | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Habilitar / validar las capacidades de IA generativa en el subaccount del cliente | Configuración de SAP Build Process Automation — Generative AI | General | Consultor BTP / Build | 2 |
| 3 | Asignar a los usuarios objetivo los roles con acceso a la capability | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer / process owner piloto (generar resúmenes sobre artefactos representativos) | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con artefactos reales del cliente (resúmenes sobre reglas de decisión representativas) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Los resúmenes son **descriptivos**: el usuario sigue siendo responsable de validar que el resumen capture correctamente la lógica de la regla.
- Útil principalmente en **handovers y revisiones funcionales**: definir gobernanza sobre cuándo el resumen reemplaza documentación formal.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/
- SAP Help Portal — Generative AI in Build Process Automation: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J644] — Script Task Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite generar código JavaScript ejecutable mediante lenguaje natural dentro de SAP Build Process Automation. La tarea de script integra capacidades de IA generativa para que el desarrollador cree código a partir de prompts y pueda apoyarse en acciones predefinidas alineadas con las restricciones del runtime. SAP indica: *30% de reducción del esfuerzo de automatización low-code; 10% más rapidez para que los desarrolladores alcancen productividad; 10% de mejora en el time-to-market de nuevas aplicaciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Process Editor + Script Task editor).

### 1.5 Datos maestros / transaccionales previos
- Proceso al que se añade el script task.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Script Task Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (generar y probar scripts JS) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Consultor SBPA | 4 |
| 2 | Documentación + buenas prácticas | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Scripts generados requieren review (security, performance).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |

---

## [J650] — Booking Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; la disponibilidad GA, el packaging y los pasos exactos de setup pueden no estar todavía completamente documentados públicamente. Marco con **[verificar en SAP Help]** los puntos clave.

**Resumen del caso:** Agente de Joule en Concur Travel que entrega recomendaciones personalizadas de vuelos y hoteles analizando preferencias del viajero, políticas de viaje de la empresa y restricciones de presupuesto. SAP indica: *Mejora la eficiencia del proceso de booking y el cumplimiento de políticas corporativas. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con sistema de **Travel Management / SAP Concur** o equivalente **[verificar agente disponible/conector]**.
- Email / Calendar provider del usuario (Microsoft 365 / Google) si forma parte del flujo **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium con capabilities Agentic **[verificar AI Foundation Catalog vigente]**.
- Suscripción a Concur u otro Travel Management (si aplica).

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad / endpoint accesible por usuarios target.
- Destinations / API keys a Concur / proveedor de viaje.

### 1.5 Datos maestros / transaccionales previos
- Perfil de viajero, políticas de viaje, métodos de pago corporativos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant Joule y al proveedor de Travel.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a Concur / proveedor Travel | Destinations BTP | General | Consultor BTP / Integración | 5 |
| 3 | Asignar acceso al Booking Agent a usuarios objetivo | Roles / Agent assignment | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 4 | Validar políticas de viaje y catálogo de proveedores | Configuración funcional Travel | General | Consultor Funcional Travel | 4 |
| 5 | Pruebas iniciales con escenarios reales | Configuración base | General | Consultor Funcional Travel | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios típicos | Consultor Funcional Travel | 5 |
| 2 | Documentación para el cliente | Consultor Funcional Travel | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional Travel | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Cumplimiento**: el agente debe respetar políticas de viaje y aprobaciones del cliente.
- **Datos personales**: revisar tratamiento de PII en interacciones.
- Disponibilidad/funcionalidades pueden cambiar — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |

---

## [J652] — Architecture Guidance

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial. SAP no publica un KPI cuantitativo específico en la página consultada; el valor se centra en acelerar la identificación de oportunidades de mejora.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente con inventario de aplicaciones y landscape de TI cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** incluidos para nuevos clientes; clientes anteriores deben confirmar términos con su representante SAP.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture activos.
- Workspace LeanIX configurado con suficiente nivel de detalle para que las recomendaciones sean significativas.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de aplicaciones, componentes técnicos, capacidades de negocio y relaciones en LeanIX.
- Atributos clave (lifecycle, ownership, business criticality) consistentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: Enterprise Architect / EA Admin con acceso a AI Capabilities.
- **Contractuales**: SAP AI terms firmados.

> **Nota**: SAP Discovery Center no publica un enlace de Initial Setup específico para este caso accesible desde la información consultada; aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar con representante SAP que los términos de IA de LeanIX están firmados | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asegurar la calidad mínima del inventario LeanIX (atributos, lifecycle, ownership) | Workspace LeanIX — Inventario | Particular (por dominio / aplicación) | Consultor SAP LeanIX + Enterprise Architect | 4 |
| 4 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Architecture Guidance | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Enterprise Architect piloto (revisión de insights y pasos accionables sugeridos) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con inventario real del cliente (revisión de insights sobre dominios representativos) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación EA) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo de Enterprise Architecture (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad de los insights depende **directamente de la calidad del inventario**: workspaces poco mantenidos producen recomendaciones poco relevantes.
- Las recomendaciones son **apoyo a la decisión** del Enterprise Architect; no reemplazan el análisis humano del contexto del negocio.
- Validar la **gobernanza** sobre quién ejecuta las acciones recomendadas: la capability sugiere, no aprueba ni implementa.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J669] — Insights Description Generator

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio Process Transformation Manager** que ayuda a crear descripciones claras, consistentes y amigables para usuarios de negocio al capturar y colaborar sobre insights de SAP Signavio Process Intelligence. El valor se centra en acelerar el paso de insight a acción.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Transformation Manager** (suscripción activa).
- **SAP Signavio Process Intelligence** con datos cargados (los insights se generan desde allí).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio Process Transformation Manager** con módulo de insights / iniciativas.
- **SAP Signavio Process Intelligence** conectado al Transformation Manager.

### 1.5 Datos maestros / transaccionales previos
- Insights generados o registrados en Process Intelligence / Transformation Manager.
- Modelos / procesos donde se vinculan los insights cargados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Process Analyst / Transformation Lead con permisos sobre los insights.

> **Nota**: el enlace de Initial Setup aparece en Resources pero no fue posible acceder a su contenido exacto desde la herramienta; aplican los prerequisitos generales de SAP Signavio.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Signavio Process Transformation Manager | Workspace Signavio + entitlement | General | Consultor SAP Signavio | 2 |
| 2 | Validar conectividad / integración Transformation Manager ↔ Process Intelligence | Integración Signavio | General | Consultor SAP Signavio | 3 |
| 3 | Asignar a los usuarios objetivo los roles Signavio con acceso a la capability | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 4 | Pruebas iniciales con un Process Analyst piloto (generar descripciones para insights representativos) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con insights reales del cliente (descripciones sobre varios dominios) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las descripciones generadas son un **borrador**: el responsable funcional debe revisar antes de compartirlas con stakeholders.
- La capability acelera la **comunicación de insights**; el análisis del insight sigue siendo responsabilidad del Process Analyst.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0614d66c-4e6d-42bc-b45b-135ba035d843/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J671] — Performance Preparation Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; pasos exactos pueden requerir validación posterior.

**Resumen del caso:** El Performance Preparation Agent automatiza la recopilación de datos, genera talking points personalizados para managers y sugiere próximos pasos accionables para reuniones one-on-one. SAP indica: *70% de reducción en el tiempo del manager dedicado a preparar reuniones de desempeño o one-on-one.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con **SAP SuccessFactors** (Employee Central + Performance & Goals) o equivalente HR **[verificar conector]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.
- Licencia SuccessFactors módulos aplicables.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible para managers.
- Destination a SuccessFactors.

### 1.5 Datos maestros / transaccionales previos
- Datos employees (objectives, performance reviews, feedback histórico).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Cumplimiento data privacy (GDPR / equivalentes).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a SuccessFactors | Destinations / OAuth | General | Consultor BTP / Integración | 5 |
| 3 | Configurar scope de datos visibles al manager (data privacy) | Reglas de visibilidad | Particular (por país / política) | Consultor HR + Compliance | 6 |
| 4 | Asignar acceso al agente a managers | Roles / Agent assignment | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (preparación de 1:1 con datos reales) | Configuración base | General | Consultor HR | 4 |

**Esfuerzo total estimado (activación): ~21 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor HR | 5 |
| 2 | Documentación para el cliente | Consultor HR | 4 |
| 3 | Transferencia de conocimiento | Consultor HR | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Privacidad de datos** crítica: revisar políticas locales y obtener aprobación legal/HR antes del rollout.
- El agente **prepara** insights; la conversación 1:1 sigue siendo responsabilidad del manager.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 21 |
| Validación + documentación + KT | 12 |
| **Total** | **33** |

---

## [J74] — Joule with SAP S/4HANA Cloud Public Edition

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Este es el caso de uso "paraguas" que habilita Joule como copilot transversal sobre S/4HANA Public Edition. Es prerequisito de muchas otras capabilities Joule sobre S/4HANA Public.

**Resumen del caso:** Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se concentra en rapidez de acceso a datos, reducción de pasos manuales y productividad del usuario.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** (release con soporte de Joule — **[verificar release mínima vigente]**).
- **SAP Business Technology Platform (BTP)** con tenant en la misma región (o región soportada).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition vigente.
- Entitlement de **Joule** activado en BTP (capability **Base** incluida; capabilities **Premium** requieren addon).

### 1.3 Scope item relacionado
- Scope item de **habilitación de Joule** sobre S/4HANA Public — **[verificar ID en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Configuración del **launchpad** con el panel de Joule visible.
- Communication arrangement entre S/4HANA Public y el servicio de Joule en BTP (escenario **SAP_COM_xxxx** — **[verificar ID vigente]**).
- Identity provider configurado (SAP IAS / corporate IdP).

### 1.5 Datos maestros / transaccionales previos
- Mapeo de usuarios entre S/4HANA y BTP (single sign-on funcional).
- Roles y catálogos asignados a usuarios target.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: soporte primario inglés; otros idiomas en GA limitada **[verificar matriz]**.
- Disponibilidad regional sujeta a la región del tenant.
- Joule respeta autorizaciones del usuario.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement de Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar identity propagation (IAS / IdP) entre S/4HANA Public y BTP | Trust configuration / SSO | General | Consultor Basis / Seguridad | 4 |
| 3 | Activar el communication scenario de Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Habilitar el panel Joule en el launchpad de los usuarios objetivo | Launchpad configuration | Particular (por usuario / spaces & pages) | Consultor S/4HANA | 4 |
| 5 | Asignar business roles con catálogos Joule a usuarios target | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 4 |
| 6 | Pruebas iniciales end-to-end (consultas informacionales, navegacionales y transaccionales) | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~22 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos por área (Finance, SCM, Sales, HR, etc.) | Consultor Funcional + key user | 6 |
| 2 | Documentación para el cliente (manual usuario + guía de configuración + lista de prompts soportados) | Consultor Funcional | 5 |
| 3 | Transferencia de conocimiento y enablement a usuarios clave | Consultor Funcional | 4 |

**Esfuerzo total estimado (validación + entrega): ~15 horas.**

---

## 4. Consideraciones especiales

- **Habilitador transversal**: una vez activo, las demás capabilities Joule sobre S/4HANA Public requieren típicamente sólo enablement adicional, no el setup completo.
- **Trazabilidad / auditoría**: interacciones pueden almacenarse según política — revisar acuerdos de procesamiento.
- **Fair use / cuotas**: revisar políticas vigentes.
- **Releases**: nuevas capabilities por wave — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 22 |
| Validación + documentación + KT | 15 |
| **Total** | **37** |

---

## [J757] — Supplier Delivery Date Mass Update

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite realizar actualizaciones masivas de fechas de entrega para múltiples pedidos de compra utilizando Joule en SAP S/4HANA Cloud Public Edition. SAP indica: *Mejora la agilidad del proceso de compras y planificación al mantener actualizadas las fechas de entrega de manera más rápida, reduciendo retrasos operativos y reprocesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM-PUR – Purchasing** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Purchase Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori *Manage Purchase Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Purchase orders activos con líneas de delivery schedule.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones MM-PUR.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Purchasing (document types, schedule lines) | Configuración MM-PUR | General | Consultor MM | 3 |
| 3 | Asignar business roles MM-PUR a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Delivery Date Mass Update | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales: actualización masiva de fechas en QAS | Configuración funcional MM | General | Consultor MM | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (volúmenes representativos) | Consultor MM | 4 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Mass update: confirmar volumen máximo recomendado.
- Cambios en fechas pueden disparar reschedulings / ATP recalc — validar impacto previo.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J762] — Joule and Microsoft 365 Copilot

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help / Microsoft Learn]** requieren validación oficial.

**Resumen del caso:** Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365. Permite consultar datos y tareas de SAP desde Copilot y aprovechar información/flujos de Microsoft 365 desde Joule. SAP indica: *No se identificó una métrica cuantitativa explícita de Business Value en la página de detalle consultada; el valor descrito se concentra en productividad, continuidad de trabajo y reducción de fricción entre SAP y Microsoft 365.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Joule** habilitado en BTP.
- **Microsoft 365 Copilot** activo en el tenant Microsoft del cliente.
- **SAP–Microsoft Joule/Copilot integration** (plugin / connector) **[verificar nombre y vehículo de distribución vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule + capability de integración con Copilot **[verificar]**.
- Licencia Microsoft 365 Copilot por usuario.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- SAP Joule endpoint.
- Microsoft 365 (Teams, Outlook, etc.) con Copilot habilitado.

### 1.5 Datos maestros / transaccionales previos
- Mapeo de identidades SAP ↔ Microsoft (typically vía Entra ID / IAS trust).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matrices Joule y Copilot vigentes **[verificar]**.
- Disponibilidad regional.
- Cumplimiento corporativo (data residency, DLP).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + capability Copilot integration | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO entre IAS / Entra ID | Identity federation | General | Consultor Seguridad | 5 |
| 3 | Instalar plugin/connector en M365 Copilot | M365 admin center | General | Admin M365 | 4 |
| 4 | Asignar permisos del plugin a usuarios | Roles / Permissions | Particular (por usuario / grupo) | Admin M365 + Seguridad SAP | 3 |
| 5 | Pruebas iniciales bi-direccionales (consultar SAP desde Copilot y M365 desde Joule) | Configuración base | General | Consultor Funcional + Admin M365 | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Funcional | 5 |
| 2 | Documentación para el cliente | Consultor Funcional | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Multi-vendor**: coordinar con admin Microsoft del cliente.
- **Cumplimiento**: revisar DLP, data residency, retention en ambos lados.
- **Costos**: M365 Copilot tiene licencia per-user separada.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |

---

## [J765] — Behavioral Insights for Contract Accounting

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Feature para **SAP S/4HANA Cloud Private Edition** que ayuda a especialistas de cobranza a predecir y explicar riesgos de pago analizando comportamiento histórico de clientes. SAP indica una reducción de **3.5% en DSO**, **5% en write-offs de cuentas por cobrar** y **1% en costos de facturación / crédito / cobranza**.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** (no aplica a Public Edition).
- Componente **FI-CA – Contract Accounts Receivable and Payable** operativo.
- **SAP BTP** con servicios de IA habilitados.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Private Edition**.
- Capability **Premium** — activación mediante **AI Units** asignadas al tenant.
- **AI Units** requeridas para usar la oferta en el servicio cloud subyacente **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- Scope item de **FI-CA Collections Management / Credit Risk Management** — **[verificar el ID exacto para Private Edition]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de **FI-CA Collections** (*Manage Collection Worklist*, *Collection Specialist Cockpit*, según versión).
- Modelo predictivo desplegado en SAP BTP / S/4HANA con conectividad operativa.
- **Joule** habilitado en el Launchpad (cuando aplique en Private Edition).

### 1.5 Datos maestros / transaccionales previos
- Cuentas de contrato, posiciones abiertas y pagos históricos cargados con consistencia.
- Catálogo de clientes / business partners y datos de comportamiento histórico mínimo.
- Eventos de cobranza y reclamaciones registrados para entrenar/usar el modelo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Private Edition**.
- **Idioma**: interacciones soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: collection specialist / credit manager con autorización sobre cuentas de contrato a analizar.
- **Volumetría**: requiere historia suficiente de comportamiento de pagos para que las predicciones sean significativas.

> **Setup oficial SAP**: el enlace de Initial Setup existe (https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/ebf9f8b183934975b07b0c0ff2484b84.html?version=2023.002) pero el contenido textual completo no fue extractable; no se agregan prerequisitos no verificados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Premium | General | Consultor BTP | 2 |
| 2 | Aprovisionar AI Units para el tenant Private Edition | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Configurar el escenario de predicción de comportamiento en FI-CA (despliegue del modelo + datos de entrenamiento/uso) | Configuración FI-CA + modelo predictivo | General | Consultor Funcional FI-CA + Consultor BTP/Data | 4 |
| 4 | Asignar a los usuarios los business roles de Collection Specialist con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar la capability en las apps de Collections | Capability scope FI-CA | General | Consultor Funcional FI-CA | 2 |
| 6 | Pruebas iniciales en Quality (consultar predicciones para clientes representativos, validar explicaciones) | Configuración funcional FI-CA | General | Consultor Funcional FI-CA | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (predicciones sobre cuentas representativas, validar precisión y explicaciones) | Consultor Funcional FI-CA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional FI-CA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional FI-CA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- **Aplica solo a Private Edition**: confirmar que el cliente está en ese sabor de S/4HANA.
- Las predicciones de riesgo son **apoyo a la decisión**; la decisión final de cobranza/crédito sigue siendo del especialista.
- Considerar implicaciones de **privacidad y regulación crediticia** según el país (GDPR / leyes locales): los análisis de comportamiento sobre clientes pueden requerir consentimientos.
- Sujeto a la **fair-use policy** de Joule / IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/ebf9f8b183934975b07b0c0ff2484b84.html?version=2023.002

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 11 |
| **Total** | **28** |

---

## [J777] — Retrieval of Equipment Information in Service Management

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Los service managers pueden acceder rápidamente a detalles completos del equipo instalado en sitios de cliente, incluyendo garantía, historial de transacciones de servicio y recomendaciones o resúmenes asistidos por IA. SAP indica: *Aporta valor al mejorar supervisión de calendarios de servicio, reducir potenciales tiempos de inactividad y ayudar a mantener el equipo del cliente operando con mayor confiabilidad.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **CS / Service Management** (Equipment, Service Orders, Notifications, History).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Service Management - Equipment & Service History — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de Service Equipment / Service Order Cockpit.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Maestros de equipment, customers, technicians, service history.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones Service.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración de Service Management (equipment categories, history) | Configuración Service | General | Consultor Service | 3 |
| 3 | Asignar business roles Service Manager a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Equipment 360° | Joule capability scope | General | Consultor Funcional Service + Joule | 2 |
| 5 | Pruebas iniciales: consultas sobre equipos y service history | Configuración funcional Service | General | Consultor Service | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (equipos típicos del cliente) | Consultor Service | 4 |
| 2 | Documentación para el cliente | Consultor Service | 4 |
| 3 | Transferencia de conocimiento | Consultor Service | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Vista 360° depende de la calidad/completitud del service history.
- Joule consulta; acciones se ejecutan en apps Service.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J778] — Requirement Generation (SAP Cloud ALM)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Esta función de SAP Cloud ALM permite generar automáticamente requerimientos de negocio de alta calidad a partir de transcripciones o notas de talleres Fit-to-Standard. SAP indica: *El valor se centra en acelerar workshops Fit-to-Standard, aumentar la calidad de los requisitos y reducir esfuerzo administrativo durante fases de implementación.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Cloud ALM** activo (Implementation).
- Capability AI / Joule integrada **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Cloud ALM (incluida con la mayoría de cloud suites SAP).
- Feature AI habilitada **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Cloud ALM Workspace (Project Management, Requirements).

### 1.5 Datos maestros / transaccionales previos
- Proyecto Cloud ALM creado; Fit-to-Standard scope definido.
- Meeting notes / minutas de workshops.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Cloud ALM Project Member.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Cloud ALM + AI | Tenant Cloud ALM | General | Consultor Cloud ALM | 2 |
| 2 | Crear/verificar proyecto Cloud ALM | Configuración Cloud ALM | General | Consultor Cloud ALM | 3 |
| 3 | Asignar roles Cloud ALM a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Requirement Generation | Configuración Cloud ALM | General | Consultor Cloud ALM | 2 |
| 5 | Pruebas iniciales (generar requirements desde meeting notes) | Configuración Cloud ALM | General | Consultor Cloud ALM | 3 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con notas reales de workshops | Consultor Cloud ALM | 4 |
| 2 | Documentación para el cliente | Consultor Cloud ALM | 3 |
| 3 | Transferencia de conocimiento | Consultor Cloud ALM | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Requirements generados son borradores; consultor refina y prioriza.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 10 |
| **Total** | **22** |

---

## [J792] — SAP Joule for Developers, ABAP AI capabilities (S/4HANA Cloud Public Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Existen casos paralelos para Private Edition (J1195) y para SAP BTP ABAP Environment (J162). Este análisis cubre la variante S/4HANA Cloud Public Edition.

**Resumen del caso:** Joule for Developers con capacidades ABAP AI apoya a desarrolladores en SAP S/4HANA Cloud Public Edition para acelerar tareas de desarrollo ABAP mediante asistencia de IA. SAP indica: *La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA y beneficios asociados a mayor eficiencia en desarrollo.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con la **Developer Extensibility (cloud ABAP)** habilitada.
- **ADT (ABAP Development Tools) for Eclipse** actualizado a la versión que soporte Joule for Developers **[verificar versión mínima]**.
- Joule habilitado en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement de Joule para Developers (capability **Premium** según AI Foundation Catalog) **[verificar]**.

### 1.3 Scope item relacionado
- N/A (es capability transversal de desarrollo).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- ADT for Eclipse con la extensión Joule for Developers instalada.
- Communication arrangement / conectividad entre ADT y el tenant.

### 1.5 Datos maestros / transaccionales previos
- Developer Extensibility configurada y proyectos ABAP existentes (paquetes, transports).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Solo aplica al modelo de desarrollo **cloud ABAP** (RAP / ABAP for Cloud Development); no aplica a custom code on-stack clásico.
- Usuario debe contar con rol de desarrollador (Developer Role).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule for Developers | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Habilitar / verificar Developer Extensibility en S/4HANA Public | Configuración Developer Extensibility | General | Consultor S/4HANA Public | 4 |
| 3 | Instalar/actualizar la extensión Joule en ADT for Eclipse | Setup ADT | Particular (por puesto de desarrollador) | Desarrollador ABAP | 2 |
| 4 | Asignar Developer Role + autorizaciones a los desarrolladores | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales: generar clase / behavior / test con prompts representativos | Configuración Developer | General | Desarrollador ABAP Sr | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos (generación de clases, RAP, unit tests) | Desarrollador ABAP Sr | 5 |
| 2 | Documentación para el equipo del cliente (guía de uso + buenas prácticas) | Desarrollador ABAP Sr | 4 |
| 3 | Transferencia de conocimiento al equipo de desarrollo | Desarrollador ABAP Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Joule for Developers **acelera** pero no sustituye la revisión humana del código generado.
- Buenas prácticas: code review obligatorio, ABAP unit tests, naming guidelines.
- Cobertura de capabilities (RAP, CDS, classes, tests) puede ampliarse por wave — revisar **Road Map Explorer**.
- Sujeto a fair-use / cuotas de Joule **[verificar]**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J811] — Supplier Delivery Date Prediction (S/4HANA Cloud Private Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Existe variante para SAP S/4HANA on-premise (J848).

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes del proceso. SAP indica: *Permite planificar con mayor confianza la disponibilidad de materiales y reducir el riesgo operativo asociado a fechas de entrega inciertas o poco confiables.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **MM-PUR – Purchasing** operativo.
- Capability ML / Predictive activa (parte del Joule entitlement o servicio dedicado) **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule + capability predictiva (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Purchase Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Purchase Orders* y vistas de prediction de fechas.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, materials, plants, purchase orders históricos suficientes para entrenar el modelo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Calidad de predicción condicionada por volumen/limpieza del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración MM-PUR (schedule lines, lead times) | Configuración MM-PUR | General | Consultor MM | 3 |
| 3 | Asignar business roles MM-PUR a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability predictiva para delivery date | Joule capability scope | General | Consultor Funcional MM + Joule | 3 |
| 5 | Pruebas iniciales (comparar predicción vs realidad en histórico de prueba) | Configuración funcional MM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios suppliers/materiales) | Consultor MM | 5 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad de predicción depende del histórico (cantidad y limpieza).
- Validar periodicidad de reentrenamiento.
- Usuario sigue tomando la decisión funcional final.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |

---

## [J824] — Resolution of Implausible Meter Readings (IS-U)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** La capacidad se integra en el procesamiento de lecturas de medidor en IS-U para apoyar con machine learning la resolución de lecturas implausibles. SAP indica: *Aporta valor al mejorar la calidad de resolución de excepciones y reducir esfuerzo operativo asociado al análisis manual de lecturas de medidor implausibles.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con **IS-U / Utilities** activo.
- Componentes **DM – Device Management** y **BI – Billing/Invoicing** operativos.
- Joule habilitado (capability ML para meter readings).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition con IS-U.
- Entitlement Joule + capability ML (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Utilities - Meter Reading & Billing — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de Device Management / Meter Reading Workbench.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Maestros IS-U: contracts, devices, registers, profiles de consumo.
- Volumen histórico de meter readings para tener línea base.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Industry-specific: solo aplica a tenants con IS-U.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + capability ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración IS-U (DM, profiles, tolerancias) | Configuración IS-U DM | General | Consultor IS-U | 4 |
| 3 | Asignar business roles IS-U a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability ML para meter readings | Joule capability scope IS-U | General | Consultor Funcional IS-U + Joule | 4 |
| 5 | Pruebas iniciales con readings reales (incluyendo casos implausibles) | Configuración funcional IS-U | General | Consultor IS-U | 4 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios tipos de readings y perfiles) | Consultor IS-U | 6 |
| 2 | Documentación para el cliente | Consultor IS-U | 4 |
| 3 | Transferencia de conocimiento | Consultor IS-U | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- ML mejora con volumen y limpieza histórica.
- Tolerancias funcionales IS-U se respetan.
- Usuario sigue validando casos que escapan al modelo.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 13 |
| **Total** | **30** |

---

## [J825] — Resolution of Outsorted Billing Documents (IS-U)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** La capacidad se integra en el proceso de billing de IS-U para apoyar el procesamiento de documentos de facturación apartados u outsorted. SAP indica: *El valor de negocio está en mejorar eficiencia operativa, acelerar el tratamiento de excepciones de billing y disminuir carga manual en procesos de facturación.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con **IS-U / Utilities** activo.
- Componente **BI – Billing / Invoicing IS-U** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition con IS-U.
- Entitlement Joule (+ capability ML si aplica) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Utilities - Billing Process — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de IS-U Billing Workbench / Outsorted Documents.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Configuración de billing IS-U (procedures, rate categories).
- Volumen histórico de outsorted documents para entrenar/predecir.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Industry-specific: solo IS-U.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración IS-U Billing | Configuración IS-U BI | General | Consultor IS-U | 4 |
| 3 | Asignar business roles IS-U Billing a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Outsorted Billing | Joule capability scope IS-U | General | Consultor Funcional IS-U + Joule | 3 |
| 5 | Pruebas iniciales con documentos outsorted reales | Configuración funcional IS-U | General | Consultor IS-U | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor IS-U | 6 |
| 2 | Documentación para el cliente | Consultor IS-U | 4 |
| 3 | Transferencia de conocimiento | Consultor IS-U | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- Procesamiento ML reduce el backlog manual; usuario sigue validando excepciones.
- Cobertura de motivos de outsorting puede ampliarse — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 13 |
| **Total** | **29** |

---

## [J831] — Sales Order Creation (S/4HANA Cloud Public Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Existen variantes equivalentes para S/4HANA Cloud Private Edition (J832) y SAP S/4HANA on-premise (J846). También existe J404 "Sales Order Creation from Unstructured Data" como variante con extracción de documentos.

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta desde archivos de compra no estructurados en PDF o imágenes; la información se extrae automáticamente y se propone en campos de la solicitud. SAP indica: *La página indica reducción del 25% en el costo de creación de órdenes de venta y acelera el ciclo de ventas gracias a menor tasa de error.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con SD.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing condition records, plants, sales areas, shipping points.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD (document types, pricing, item categories) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Creation | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: crear sales orders con prompts representativos | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Usuario confirma antes de guardar el pedido.
- Respeta autorizaciones SD.
- Para extracción desde documentos no estructurados, ver J404.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J832] — Sales Order Creation (S/4HANA Cloud Private Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante Private del caso. Ver J831 (Public) y J846 (S/4HANA on-prem).

**Resumen del caso:** La capacidad permite crear pedidos de venta a partir de datos no estructurados, como archivos PDF o imágenes de órdenes de compra. El sistema extrae la información del archivo, propone valores para la solicitud de pedido y permite convertirla posteriormente en un pedido de venta. SAP indica: *La página destaca una reducción del 25% en el costo de creación de pedidos de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para SO Creation | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Usuario confirma antes de guardar.
- En Private aplican consideraciones de upgrade compatibility.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J846] — Sales Order Creation (SAP S/4HANA on-premise)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante para SAP S/4HANA on-premise. Ver J831 (Public) y J832 (Private). Joule en on-prem suele requerir bridging vía BTP.

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta a partir de archivos de órdenes de compra en PDF o imagen. El sistema extrae información y propone valores para la solicitud de orden. SAP indica: *El valor se centra en acelerar la creación de órdenes, disminuir errores de procesamiento y reducir el costo asociado a la creación manual de órdenes de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA on-premise** en release con soporte de Joule (vía BTP bridge) **[verificar release mínima]**.
- **SAP BTP** con servicio Joule aprovisionado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia S/4HANA on-premise vigente.
- Entitlement Joule en BTP **[verificar]**.

### 1.3 Scope item relacionado
- Best practice / scope item de Sales Order Management — **[verificar referencia equivalente para on-premise]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Fiori Launchpad on-prem con panel Joule.
- Cloud Connector / RFC conectividad on-prem ↔ BTP.
- Communication arrangement / destination configurados.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Aplica a **on-premise**; algunas capabilities Joule pueden estar limitadas frente a Cloud editions.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar Cloud Connector / destinations on-prem ↔ BTP | Cloud Connector / Destinations | General | Consultor Basis / Integración | 6 |
| 3 | Configurar communication arrangement Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Asignar roles SD + catálogos Joule a usuarios | Roles / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales end-to-end (Joule → SO en on-prem) | Configuración funcional SD | General | Consultor SD | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 5 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **on-premise**: validar firewall / Cloud Connector / latencia.
- Compatibilidad con la versión del stack ABAP del cliente.
- Algunas capabilities Joule pueden no estar disponibles fuera del cloud editions.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |

---

## [J848] — Supplier Delivery Date Prediction (SAP S/4HANA on-premise)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante para SAP S/4HANA on-premise. Ver J811 (Private).

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra con base en datos históricos y múltiples parámetros del proceso de aprovisionamiento. SAP indica: *Incrementa la confiabilidad del abastecimiento, mejora la planeación de materiales y ayuda a reducir impactos por entregas tardías o incertidumbre en fechas de recepción.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA on-premise** en release con soporte de la capability ML / Predictive **[verificar]**.
- Componente **MM-PUR – Purchasing** operativo.
- Servicio predictivo (puede requerir BTP / SAP AI Core) **[verificar arquitectura vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia S/4HANA on-premise vigente.
- Entitlement servicio predictivo (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Best practice / scope item de Purchase Order Management — **[verificar referencia equivalente para on-premise]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Purchase Orders*.
- Conectividad on-prem ↔ BTP / AI Core si aplica.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, materials, plants, POs históricos.
- Volumen / calidad de histórico suficiente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Aplica a **on-premise**.
- Calidad predicción condicionada por histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar servicio predictivo en BTP / AI Core | Subaccount BTP + entitlement | General | Consultor BTP | 4 |
| 2 | Configurar Cloud Connector / destinations on-prem ↔ BTP | Cloud Connector / Destinations | General | Consultor Basis / Integración | 6 |
| 3 | Configurar integración MM-PUR con servicio predictivo | Integración funcional / OData | General | Consultor MM + Integración | 6 |
| 4 | Asignar roles MM-PUR a usuarios | Roles / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (comparar predicción vs realidad) | Configuración funcional MM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~23 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios suppliers) | Consultor MM | 5 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **on-premise**: validar firewall / Cloud Connector / latencia / volumen de datos enviados.
- Periodicidad de reentrenamiento del modelo.
- Usuario sigue decidiendo el ajuste funcional.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 23 |
| Validación + documentación + KT | 12 |
| **Total** | **35** |

---

## [J85] — Joule with Regulatory Change Manager

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento. SAP indica: *85% menos tiempo dedicado a identificar cambios regulatorios, según la métrica mostrada en la página de detalle.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Regulatory Change Manager (RCM)** activo.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción RCM vigente.
- Entitlement Joule + capability RCM **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App RCM (cockpit de regulaciones).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Configuración de jurisdicciones / regulaciones / responsables.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Cobertura jurisdiccional sujeta al catálogo SAP.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement RCM + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar jurisdicciones, regulaciones, owners | Configuración RCM | Particular (por jurisdicción) | Consultor Compliance / RCM | 6 |
| 3 | Asignar roles RCM (Compliance Officer, Reviewer) | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule en RCM | Configuración RCM | General | Consultor RCM + Joule | 2 |
| 5 | Pruebas iniciales: consultar/evaluar regulaciones con Joule | Configuración funcional RCM | General | Consultor Compliance | 4 |

**Esfuerzo total estimado (activación): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varias regulaciones) | Consultor Compliance | 5 |
| 2 | Documentación para el cliente | Consultor Compliance | 4 |
| 3 | Transferencia de conocimiento | Consultor Compliance | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Compliance: decisiones legales requieren revisión humana.
- Cobertura regulatoria evoluciona — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 12 |
| **Total** | **30** |

---

## [J86] — Explanation of Fixed Asset Depreciation Keys

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Explica en lenguaje natural cómo operan las claves de depreciación y la lógica detrás de los cálculos del sistema, comprensible para usuarios de negocio. SAP indica una **reducción del 75%** en el esfuerzo para especificar claves de depreciación durante implementaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **Asset Accounting (FI-AA)** operativo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- Scope items de **Asset Accounting** (Adquisición, Depreciación, Cierre de Periodo) en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Fixed Assets** habilitada para los usuarios objetivo.
- Apps Fiori de configuración / consulta de claves de depreciación.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de activos fijos cargado y consistente.
- **Claves de depreciación**, áreas de valoración y métodos de cálculo configurados.
- Activos fijos con valores históricos y movimientos calculados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener el rol de Asset Accountant o equivalente con acceso a la información de activos a explicar.

> **Setup oficial SAP**: la página de SAP Help Portal corresponde a *AI-Generated Explanation of Depreciation Keys* (https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/17fe86dc95334287b50406d466a26c14.html). El contenido completo de prerequisitos no fue totalmente extractable.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP / Cockpit | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar configuración de Asset Accounting (claves de depreciación, áreas de valoración) | Configuración FI-AA | General | Consultor Funcional Asset Accounting | 3 |
| 4 | Asignar a los usuarios objetivo los business roles de Asset Accountant con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar la capability de Joule para explicación de depreciation keys | Joule capability scope | General | Consultor Funcional Asset Accounting + Joule | 2 |
| 6 | Pruebas iniciales en Quality (solicitar explicación de varias claves representativas) | Configuración funcional FI-AA | General | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre claves de depreciación del negocio) | Consultor Funcional Asset Accounting | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Asset Accounting | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- Las explicaciones son **descriptivas, no normativas**: validar con el equipo de Auditoría/Compliance que el uso sea apropiado en cierre.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/17fe86dc95334287b50406d466a26c14.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J885] — Run Forecasts in Time Series or Line Charts

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de historias. El valor se centra en acelerar el análisis predictivo dentro de dashboards.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias que incluyan gráficos de **serie de tiempo o línea**.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con **dimensión de fecha** y **medidas** con historia suficiente para producir un forecast significativo.
- Datos históricos correctamente cargados y agregados al nivel de granularidad requerido.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (la capability opera sobre datos numéricos / fechas).
- **Roles**: usuario SAC con permisos sobre la historia / modelo.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8f9665dcf53f4f3f90e920995cdd5f05.html describe el uso del forecast predictivo dentro de gráficos compatibles.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar que las historias y modelos incluyan dimensión de fecha y medidas con datos históricos suficientes | Modelos / historias SAC | Particular (por historia / modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (ejecutar forecast en gráficos representativos) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (forecasts sobre series representativas) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad del forecast depende de la **cantidad y consistencia del histórico**: series cortas o con outliers pueden producir resultados poco fiables.
- El forecast es **apoyo a la decisión**: el usuario debe validar supuestos y horizontes con el negocio.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- SAP Help Portal — Forecasts in Charts: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8f9665dcf53f4f3f90e920995cdd5f05.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J886] — Smart Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que analiza desviaciones y puntos de datos dentro del modelo subyacente para entregar explicaciones en texto y visualizaciones asociadas. El valor se centra en acelerar el análisis de causas y desviaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias / modelos publicados sobre los que se aplican los insights.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con métricas y dimensiones suficientes para producir explicaciones significativas.
- Datos consistentes y agregados al nivel de granularidad esperado.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: explicaciones según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: usuario SAC con permisos para consumir / analizar las historias.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html describe las capacidades inteligentes de SAC.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar la calidad y granularidad de los modelos donde se aplicarán Smart Insights | Modelos SAC | Particular (por modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (Smart Insights sobre desviaciones representativas) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre escenarios representativos) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de validar las causas reales con conocimiento del negocio.
- La calidad depende **directamente de la calidad de los modelos** y de la consistencia de la data.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/
- SAP Help Portal — Smart Features in SAC: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

## [J88] — Analytical Business Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog, SAP Road Map Explorer). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente antes de la activación en cliente.

**Resumen del caso:** Panel lateral de IA generativa en *Cost Center Review Booklet* que permite analizar y resumir datos financieros en lenguaje natural y convertirlos en insights accionables. SAP publica beneficios de hasta **50% de reducción del tiempo** para analizar resúmenes y **65% para resumir y documentar** reportes de centros de costo.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente funcional **FI/CO – Cost Center Accounting** operativo en el tenant (app *Cost Center Review Booklet*).
- **SAP BTP** con Generative AI Hub disponible para el tenant del cliente.
- **Intelligent Scenario Lifecycle Management (ISLM)** activo (este caso usa la integración ISLM + Generative AI).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** **[verificar suscripción vigente en SAP Discovery Center]**.
- **AI Units** asignadas al tenant para consumo de la capability (precio bajo solicitud según *Pricing Details* publicado).

### 1.3 Scope item relacionado
- Scope item base de **Cost Center Accounting / Overhead Cost Accounting** en S/4HANA Cloud Public Edition — **[verificar el ID exacto del scope item asociado a J88 en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Cost Center Review Booklet** habilitada para los usuarios objetivo.
- Apps de **Intelligent Scenario Apps** disponibles para administradores ISLM.
- **Generative AI for ISLM** configurado.
- **Service Instance + Service Key de SAP BTP** creados con certificado descargado, según el procedimiento de Initial Setup publicado por SAP.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario final.

### 1.5 Datos maestros / transaccionales previos
- Centros de costo, jerarquías y elementos de costo dados de alta y consistentes.
- Cargas reales/plan de Cost Center Accounting cerradas o vigentes para el periodo a analizar.
- Datos del periodo correctamente publicados en la app *Cost Center Review Booklet*.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: las interacciones de IA generativa de Joule se publican primariamente en **inglés** **[verificar matriz de idiomas vigente en SAP Help]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: usuario final debe tener el business role de Controlling con autorización sobre los centros de costo a analizar.
- **Disponibilidad regional**: sujeta a la región del tenant y a la disponibilidad regional del Generative AI Hub **[verificar]**.

> **Setup oficial SAP**: la página de SAP Help referencia configuración relacionada con *Intelligent Scenario Lifecycle Management*, acceso a *Intelligent Scenario Apps*, *Generative AI for ISLM*, descarga de certificado y creación de SAP BTP Service Instance and Key. Enlace: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP / Cockpit | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Crear **Service Instance + Service Key** de SAP BTP para Generative AI y descargar el certificado | BTP Service Instance/Key + certificado | General | Consultor BTP | 3 |
| 4 | Configurar **Generative AI for ISLM** en S/4HANA Cloud Public Edition | ISLM — Generative AI Configuration | General | Consultor BTP + Consultor Funcional Finanzas | 3 |
| 5 | Habilitar el **Intelligent Scenario** asociado a *Analytical Business Insights* (despliegue del modelo en ISLM) | Intelligent Scenario / ISLM | General | Consultor Funcional Finanzas | 3 |
| 6 | Asignar a los usuarios objetivo el business role de Controlling con catálogo de *Cost Center Review Booklet* y permisos sobre Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 7 | Pruebas iniciales en Quality con un usuario piloto (apertura del panel de Joule en Cost Center Review Booklet, consultas en lenguaje natural) | Configuración funcional FI/CO | General | Consultor Funcional Finanzas | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (resúmenes y análisis sobre centros de costo en entorno de Quality) | Consultor Funcional Finanzas | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración ISLM/BTP) | Consultor Funcional Finanzas | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A sobre uso del panel de Joule) | Consultor Funcional Finanzas | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- La activación implica integrarse con **SAP BTP Generative AI Hub** vía ISLM — no es solo habilitar Joule en el Launchpad, es desplegar un escenario inteligente con certificado y service key.
- Joule responde sobre datos a los que el usuario ya tiene autorización; **no eleva privilegios**: validar la matriz de autorizaciones de Controlling antes del rollout.
- Sujeto a **fair-use policy** de Joule y a las cuotas de AI Units; revisar consumo durante el piloto para dimensionar el volumen anual **[verificar políticas vigentes]**.
- Las interacciones con Joule pueden almacenarse para **auditoría / trazabilidad**; revisar políticas de privacidad y data residency aplicables.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes de la wave vigente para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 11 |
| **Total** | **30** |

---

## [J892] — Smart Grouping

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que agrupa puntos de datos similares en gráficos de dispersión y burbuja mediante clustering basado en centroides. El valor se centra en facilitar el descubrimiento de patrones / segmentos en visualizaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias que incluyan **gráficos de dispersión o burbuja**.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con datos numéricos y dimensiones suficientes para producir clusters significativos en visualizaciones de dispersión / burbuja.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Tipos de gráfico**: la capability aplica únicamente a **scatter y bubble charts**.
- **Roles**: usuario SAC con permisos para crear/editar historias o visualizaciones.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html describe las capacidades inteligentes de SAC.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Preparar el modelo / historia con gráficos de dispersión o burbuja | Modelos / historias SAC | Particular (por historia) | Consultor SAP Analytics Cloud | 2 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (aplicar Smart Grouping en visualizaciones representativas) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (clustering sobre conjuntos representativos) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad del clustering depende del **volumen y dispersión** de los datos: muestras pequeñas o homogéneas reducen el valor de los grupos detectados.
- Es **apoyo visual a la exploración**: la interpretación final de los grupos sigue siendo del analista.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/
- SAP Help Portal — Smart Features in SAC: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J893] — Smart Predict (SAP Analytics Cloud)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite crear modelos predictivos en SAP Analytics Cloud para entregar predicciones aplicables a escenarios de análisis y planificación. SAP indica: *Mejora la anticipación de resultados, acelera el uso de analítica predictiva en decisiones de negocio y reduce dependencia de desarrollos externos para escenarios predictivos básicos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud (SAC)** con capability Smart Predict / Predictive **[verificar plan]**.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia SAC que incluya Smart Predict **[verificar matriz]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Datasets con calidad suficiente para entrenar modelos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI multilenguaje según SAC.
- Calidad de los modelos depende de los datos.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar licencia SAC + Smart Predict | Tenant SAC | General | Consultor SAC | 2 |
| 2 | Verificar datasets / preparar feature engineering | Datasets SAC | General | Consultor SAC / Data | 5 |
| 3 | Asignar roles SAC a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Smart Predict scenarios | Configuración Predict | General | Consultor SAC | 3 |
| 5 | Pruebas iniciales (entrenar/desplegar 1 modelo) | Configuración SAC | General | Consultor SAC | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos (classification/regression/timeseries) | Consultor SAC | 5 |
| 2 | Documentación para el cliente | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Validar bias / explicabilidad antes de adoptar en decisiones críticas.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 12 |
| **Total** | **29** |

---

## [J894] — Predictive Planning (SAP Analytics Cloud)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos. La capacidad ayuda a actualizar previsiones de forma más ágil y a reducir sesgos en los ciclos de planificación. SAP indica: *Aporta valor al reducir trabajo manual y sesgos en la planeación, mejorar la agilidad de los equipos y aumentar la confiabilidad de los escenarios predictivos usados para decidir.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud (SAC)** con módulo Planning activo.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia SAC Planning (incluye capability Predictive) **[verificar matriz vigente]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant SAC con modelos de planning configurados.

### 1.5 Datos maestros / transaccionales previos
- Series temporales históricas con calidad suficiente para forecast.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI multilenguaje según SAC.
- Calidad del forecast depende del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar licencia Planning + Predictive | Tenant SAC | General | Consultor SAC | 2 |
| 2 | Verificar modelo de planning con series temporales | Modelos SAC | General | Consultor SAC | 4 |
| 3 | Asignar roles Planner/Modeler a usuarios | Roles SAC | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Predictive scenarios en SAC | Configuración Predictive | General | Consultor SAC | 3 |
| 5 | Pruebas iniciales (correr predictive scenarios) | Configuración SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (KPIs del cliente) | Consultor SAC | 5 |
| 2 | Documentación para el cliente | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad del forecast mejora con limpieza y volumen del histórico.
- Revisar bias / estacionalidad.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 12 |
| **Total** | **26** |

---

## [J898] — Depreciation Key Explanation

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Explica en lenguaje natural cómo funcionan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema, sobre **SAP S/4HANA Cloud Private Edition**. SAP indica una reducción del **75% en el esfuerzo** para especificar claves de depreciación durante implementaciones y **90% en el esfuerzo** para analizar y responder consultas sobre valores de activos fijos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **Asset Accounting (FI-AA)** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Private Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- Scope items de **Asset Accounting** en S/4HANA Cloud Private Edition — **[verificar IDs en SAP Signavio Process Navigator para Private Edition]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Fixed Assets** habilitada para los usuarios objetivo (cuando aplique en Private Edition).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de activos fijos cargado y consistente.
- **Claves de depreciación**, áreas de valoración y métodos de cálculo configurados.
- Activos fijos con valores históricos y movimientos calculados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Private Edition** (distinguir de J86, que aplica a Public Edition).
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: el usuario debe tener el rol de Asset Accountant con acceso a la información de activos a explicar.

> **Setup oficial SAP**: la página identificada (https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/17fe86dc95334287b50406d466a26c14.html?q=CC05&version=2508.00) referencia la explicación generada por IA para claves de depreciación. El contenido extraído no expone un procedimiento paso a paso completo.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units para Private Edition | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar configuración de Asset Accounting (claves de depreciación, áreas de valoración) | Configuración FI-AA | General | Consultor Funcional Asset Accounting | 3 |
| 4 | Asignar a los usuarios los business roles de Asset Accountant con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar la capability de Joule para explicación de claves de depreciación | Joule capability scope | General | Consultor Funcional Asset Accounting + Joule | 2 |
| 6 | Pruebas iniciales en Quality (solicitar explicación de claves representativas) | Configuración funcional FI-AA | General | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre claves de depreciación del negocio) | Consultor Funcional Asset Accounting | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Asset Accounting | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- **Solo Private Edition**: confirmar que el cliente está en el sabor correcto antes de planificar.
- Las explicaciones son **descriptivas, no normativas**: validar con Auditoría/Compliance que el uso sea apropiado en cierre.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/17fe86dc95334287b50406d466a26c14.html?q=CC05&version=2508.00

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |

---

## [J90] — Smart Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que permite resumir contenido de **object pages basadas en SAP Fiori elements** y generar propuestas de texto para comunicaciones o seguimientos. SAP indica un ahorro estimado del **88% del tiempo** al resumir páginas de objeto.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Apps Fiori elements con **object pages** habilitadas para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item específico; la capability opera transversalmente sobre object pages Fiori elements.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad** del sistema S/4HANA Cloud Public Edition.
- IAM app **SAP Business AI - User Interface Features - Smart Summarization (F7924_SUM_TRAN)** o catálogo equivalente, disponible y asignada al rol de negocio.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales y maestros suficientes en las object pages a resumir.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idiomas**: capability soporta múltiples idiomas para los resúmenes generados **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Tipo de página**: solo aplica a **object pages basadas en SAP Fiori elements**.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html describe el procedimiento: verificar la IAM app **F7924_SUM_TRAN** en *Display IAM Apps* y asignarla al rol de negocio en *Maintain Business Roles*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar la disponibilidad de la **IAM app F7924_SUM_TRAN** en *Display IAM Apps* | IAM App F7924_SUM_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 3 | Asignar la IAM app **F7924_SUM_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Pruebas iniciales con un usuario piloto (abrir object pages representativas, usar *Summarize*, revisar resúmenes en distintos idiomas) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con object pages reales del cliente (varios módulos / idiomas representativos) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **funciona solo sobre object pages basadas en SAP Fiori elements**: validar cobertura sobre las apps clave del cliente.
- Los resúmenes generados deben ser **revisados / editados por el usuario** antes de enviarse por correo o chat — sobre todo en comunicaciones formales.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y tipos de object pages soportados.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/
- SAP Help Portal — Smart Summarization Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |

---

## [J91] — Easy Filter

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que optimiza la experiencia de filtrado en reportes de lista basados en **SAP Fiori elements** mediante lenguaje natural. SAP indica un ahorro estimado del **83% del tiempo** al filtrar reportes de lista.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition**.
- Reportes de lista basados en **SAP Fiori elements** habilitados para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; la capacidad opera transversalmente sobre los reportes Fiori elements.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad** del sistema SAP S/4HANA Cloud Public Edition.
- Apps Fiori elements (list reports) habilitadas en los catálogos de los usuarios.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales del módulo objetivo disponibles para filtrar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: el filtrado por lenguaje natural está disponible principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Tipo de reporte**: solo aplica a **list reports basados en SAP Fiori elements**.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html describe la habilitación de *AI-Assisted Easy Filter*. La activación se realiza por un administrador del SAP Fiori Launchpad del sistema S/4HANA Cloud Public Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Iniciar sesión como administrador en el SAP Fiori Launchpad del sistema S/4HANA Cloud Public Edition | Acceso administrativo | General | Consultor S/4HANA + Cliente Admin | 1 |
| 2 | Habilitar **AI-Assisted Easy Filter** según el procedimiento de la página de SAP Help | Configuración Easy Filter | General | Consultor Funcional S/4HANA | 2 |
| 3 | Asignar a los usuarios objetivo los business roles / catálogos donde se usarán los list reports | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 2 |
| 4 | Pruebas iniciales con un usuario piloto (filtrar list reports representativos por lenguaje natural) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~7 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con list reports reales del cliente (filtros representativos sobre varios módulos) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **funciona solo sobre list reports basados en SAP Fiori elements**: validar la cobertura sobre las apps clave del cliente.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** para que los usuarios aprovechen la capability de manera consistente.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- SAP Help Portal — Easy Filter Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 7 |
| Validación + documentación + KT | 11 |
| **Total** | **18** |

---

## [J924] — Workspace

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP Document AI, Workspace** ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis. El valor se centra en reducir tiempos de procesamiento documental y mejorar la gobernanza de Document AI en entornos empresariales.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document AI** activo (Workspace).
- Sistemas destino que reciben los datos extraídos (p. ej. **SAP S/4HANA**) con conectividad operativa.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document AI**.
- Capability **Premium** — activación con **AI Units**.
- Precio bajo solicitud; duración del contrato disponible bajo solicitud; tiene prerrequisito **[verificar volumen y costo vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; el escenario funcional en el sistema destino tiene su scope item asociado **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Document AI — Workspace** disponible para los administradores.
- Canales de entrada (correo, API, upload) y workflows hacia sistemas destino configurables.

### 1.5 Datos maestros / transaccionales previos
- Esquemas (predefinidos o personalizados) para los tipos de documento a procesar.
- Datos maestros consistentes en sistemas destino para validar matching.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción documentados por SAP **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos con baja calidad reducen la tasa de extracción correcta.
- **Roles**: administradores de Document AI con permisos para configurar schemas, canales, workflows; operadores con acceso al workspace.

> **Nota**: el enlace de Initial Setup está identificado en Resources pero no fue posible acceder a la URL final tras reintentos. Aplican los prerequisitos generales de SAP Document AI documentados en https://help.sap.com/docs/SAP_DOCUMENT_AI.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Document AI Workspace y AI Units en SAP BTP | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 2 |
| 2 | Aprovisionar AI Units para el volumen estimado | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Aprovisionar el **SAP Document AI Workspace** | Workspace Document AI | General | Consultor SAP Document AI | 3 |
| 4 | Configurar esquemas (schemas) para los tipos de documento del cliente | Schemas Document AI | Particular (por tipo de documento) | Consultor SAP Document AI | 5 |
| 5 | Configurar canales de entrada y workflows hacia sistemas destino | Channels + Workflows Document AI | Particular (por proceso) | Consultor SAP Document AI + Integration Suite | 5 |
| 6 | Asignar a los usuarios objetivo los roles administrativos / operativos del workspace | Roles SAP Document AI | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 7 | Habilitar **monitoreo y análisis** en el workspace para los workflows configurados | Monitoring Document AI | General | Consultor SAP Document AI | 2 |
| 8 | Pruebas iniciales en Quality con documentos reales del cliente | Configuración funcional Document AI | General | Consultor SAP Document AI | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~25 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (varios tipos, varios canales) | Consultor SAP Document AI | 4 |
| 2 | Documentación de la activación para el cliente (manual de configuración + manual de operación / monitoreo) | Consultor SAP Document AI | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica de operación) | Consultor SAP Document AI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units por volumen**: dimensionar el consumo y planificar el crecimiento.
- El **monitoreo y análisis** son clave para detectar deriva en la calidad de extracción y para gobernar excepciones.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza.
- Considerar **gobernanza / data residency** sobre dónde se procesa el documento y dónde se almacenan los datos extraídos.
- Sujeto a la **fair-use policy** y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- SAP Help Portal — SAP Document AI: https://help.sap.com/docs/SAP_DOCUMENT_AI

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 25 |
| Validación + documentación + KT | 11 |
| **Total** | **36** |

---

## [J929] — Managing Supplier Invoices

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule ayuda a los contadores a ejecutar acciones estándar sobre facturas de proveedor para acelerar el tiempo de procesamiento. SAP indica: *No se identificó una métrica cuantitativa explícita de Business Value en el contenido accesible de la página de detalle; el valor descrito se centra en acelerar el procesamiento de facturas de proveedor.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM-IV – Invoice Verification / Accounts Payable** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con MM.
- Entitlement Joule (**Base**) **[verificar en AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- Scope items de Accounts Payable / Supplier Invoice Management — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Supplier Invoices*, *Supplier Invoices List*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, POs, GRs, condiciones de pago.
- Workflow de aprobación de facturas operativo (si aplica).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones MM-IV.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración MM-IV (tolerancias, workflows, payment terms) | Configuración MM-IV | General | Consultor MM | 3 |
| 3 | Asignar business roles con catálogos AP a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Supplier Invoices | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales: consultas y acciones básicas vía Joule en QAS | Configuración funcional MM | General | Consultor MM | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (consultar estados, parking, posting) | Consultor MM | 4 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule habilita **acciones básicas** sobre facturas; flujos complejos siguen en las apps Fiori.
- Respeta autorizaciones; no eleva privilegios.
- Cobertura de acciones se amplía por wave — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |

---

## [J92] — Generation of Integrations (SAP Integration Suite)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Capacidad de SAP Integration Suite que permite generar integration flows con asistencia de IA. El usuario describe el escenario de integración y la herramienta crea un flujo con conectores preconfigurados de acuerdo con la descripción y entradas proporcionadas. SAP indica: *SAP indica que, con más de 3.600 integration flows preconstruidos, se puede reducir el tiempo de diseño de integraciones por un factor de tres, generando ahorro de costos, mejor calidad y menor esfuerzo de implementación.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (capability Cloud Integration).
- Capability AI integrada **[verificar AI Foundation Catalog]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Integration Suite con capability AI (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace Integration Suite (Cloud Integration / Integration Designer).

### 1.5 Datos maestros / transaccionales previos
- Catálogo de adaptadores / receivers / senders configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Integration Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Integration Suite + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Integration Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar capability Generation of Integrations | Configuración Integration Suite | General | Consultor Integración | 2 |
| 4 | Pruebas iniciales: generar iFlow base con prompts | Configuración Integration Suite | General | Consultor Integración | 4 |

**Esfuerzo total estimado (activación): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Integración | 5 |
| 2 | Documentación + buenas prácticas | Consultor Integración | 4 |
| 3 | Transferencia de conocimiento | Consultor Integración | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Integraciones generadas son borradores; revisión y hardening (security, performance, error handling) requeridos.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 12 |
| **Total** | **23** |

---

## [J934] — Smart Personalization of My Home for Applications

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a **My Home**. SAP indica una **reducción del 33%** del costo de personalizar la página inicial.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Página **My Home** del SAP Fiori Launchpad disponible para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item específico; la capability opera sobre My Home / Fiori Launchpad.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad — My Home**.
- IAM app **SAP Business AI - My Home - Smart App Finder (F8818_TRAN)** o el catálogo equivalente, asignada a los usuarios objetivo.
- Catálogo de apps Fiori del cliente con metadatos suficientes para que la búsqueda en lenguaje natural funcione correctamente.

### 1.5 Datos maestros / transaccionales previos
- No aplica un dato transaccional específico; la capability opera sobre el catálogo de apps.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario verá únicamente apps a las que tiene autorización (Joule respeta las autorizaciones).

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html describe el procedimiento: verificar la IAM app en *Display IAM Apps*, asignarla al rol de negocio en *Maintain Business Roles* y habilitar el acceso para los usuarios.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar la disponibilidad de la **IAM app F8818_TRAN** en *Display IAM Apps* | IAM App F8818_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 4 | Asignar la IAM app **F8818_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales con un usuario piloto (*Add Content* en My Home → búsqueda en lenguaje natural de apps, revisar resultados y agregarlos) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con usuarios reales (varios perfiles / módulos, búsqueda y adición de apps representativas) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Joule respeta las autorizaciones del usuario: las búsquedas devuelven **únicamente apps a las que el usuario tiene acceso**.
- La calidad de las recomendaciones depende de la **consistencia del catálogo de apps** y de sus metadatos.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- SAP Help Portal — Smart Personalization of My Home: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |

---

## [J966] — Fixed Asset Key Figures Explanation

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones generadas en lenguaje natural, sobre **SAP S/4HANA Cloud Private Edition**. SAP no publica un KPI cuantitativo específico en la página consultada.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **Asset Accounting (FI-AA)** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Private Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Asset Accounting** en S/4HANA Cloud Private Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Fixed Assets** habilitada para los usuarios objetivo (cuando aplique en Private Edition).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de activos fijos cargado y consistente.
- Áreas de valoración, claves de depreciación y movimientos de valor cargados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Private Edition** (distinguir de J288, que aplica a Public Edition).
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: el usuario debe tener autorización sobre el activo fijo cuyas key figures pretende explicar.

> **Nota**: SAP no publica un Initial Setup específico para este caso en Discovery Center; aplican los prerequisitos generales de Joule + Asset Accounting sobre Private Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Private Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar configuración de Asset Accounting (claves, áreas, movimientos) | Configuración FI-AA | General | Consultor Funcional Asset Accounting | 3 |
| 3 | Asignar a los usuarios los business roles de Asset Accountant con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar la capability de Joule para explicación de key figures | Joule capability scope | General | Consultor Funcional Asset Accounting | 2 |
| 5 | Pruebas iniciales en Quality (explicaciones sobre key figures representativas) | Configuración funcional FI-AA | General | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre key figures de activos representativos) | Consultor Funcional Asset Accounting | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Asset Accounting | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- **Solo Private Edition**: confirmar que el cliente está en el sabor correcto.
- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de la interpretación contable y de la decisión.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/780e16a7-74cf-4118-b200-c13484d2f9b5/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |

---

## [J967] — Transformation Advisory, Initiative Builder

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio** que ayuda a identificar oportunidades de transformación alineadas con la estrategia y acelera la ejecución mediante la creación de iniciativas. Conecta estrategia y ejecución, facilitando que oportunidades de transformación se conviertan en planes concretos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio solutions** (suscripción activa).
- Acceso al módulo de Transformation Advisory / Process Transformation Manager dentro de SAP Signavio.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio** con el módulo Transformation Advisory habilitado.

### 1.5 Datos maestros / transaccionales previos
- Definición estratégica del cliente (objetivos, prioridades) cargada o accesible.
- Modelos de procesos relevantes en SAP Signavio.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Transformation Lead / Strategist con permisos sobre el módulo de iniciativas.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de SAP Signavio.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Signavio Transformation Advisory | Workspace Signavio + entitlement | General | Consultor SAP Signavio | 2 |
| 2 | Habilitar el módulo Transformation Advisory en el workspace | Workspace Signavio — Transformation Advisory | General | Consultor SAP Signavio | 2 |
| 3 | Asignar a los usuarios objetivo los roles Signavio con acceso a Transformation Advisory | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 4 | Pruebas iniciales con un Transformation Lead piloto (generar iniciativas a partir de oportunidades representativas) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales del cliente (iniciativas a partir de procesos representativos) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las iniciativas generadas son **borradores**: requieren revisión y priorización por parte del equipo de transformación.
- La utilidad depende de la **calidad y consistencia de la información estratégica y de procesos** disponible en SAP Signavio.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |

---

