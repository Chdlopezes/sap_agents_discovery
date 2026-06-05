# Análisis caso de uso J832 — Sales Order Creation

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
