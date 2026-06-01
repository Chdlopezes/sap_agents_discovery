# Análisis caso de uso J639 — Process Editing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J639 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/143f1e51-609a-45d9-ab96-bf286e044a03/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
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
- Según la fuente oficial abierta: You can use generative AI in SAP Build Process Automation to generate a business process, decisions, forms, and script tasks. To use the generative AI features you need to enable generative AI at tenant level and agree to the terms and conditions. When you have enabled generative AI, after approximately 5 minutes, the Generate function is available in the Overview screen for the project and in the process editor. To enable generative AI for your tenant, choose Control Tower  Tenant Configuration  Generative AI. Use the toggle to enable generative AI and accept the AI Usage Terms and Conditions.

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

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

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
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
