# Análisis caso de uso J892 — Smart Grouping

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
