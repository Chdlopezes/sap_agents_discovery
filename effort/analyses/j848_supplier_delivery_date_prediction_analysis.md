# Análisis caso de uso J848 — Supplier Delivery Date Prediction

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
