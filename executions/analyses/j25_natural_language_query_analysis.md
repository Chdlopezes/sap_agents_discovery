# Análisis caso de uso J25 — Natural Language Query

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J25 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/61a8150e7e7944c4848c79d0ec032bd2.html?locale=en-US
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
- Según la fuente oficial abierta: Searching Your Data Using Just Ask Exploring Your Data with Just Ask Use configuration settings to prepare and maintain Just Ask for your system users. A Just Ask administrator can control the following: There are two access points for Just Ask:

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

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

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
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |
