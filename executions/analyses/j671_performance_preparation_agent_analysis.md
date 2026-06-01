# Análisis caso de uso J671 — Performance Preparation Agent

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
