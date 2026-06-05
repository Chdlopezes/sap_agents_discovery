# Análisis caso de uso J151 — Master Data Governance

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
