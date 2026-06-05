# Análisis caso de uso J404 — Sales Order Creation from Unstructured Data

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
