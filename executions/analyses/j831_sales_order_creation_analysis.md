# Análisis caso de uso J831 — Sales Order Creation

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
