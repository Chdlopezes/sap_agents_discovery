# Análisis caso de uso J1143 — BPMN Simulation Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1143 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-modeler/user-guide/using-ai-assisted-bpmn-simulation-insights?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/#pricing

**Resumen del caso:** Feature de SAP Signavio que integra simulaciones BPMN directamente en diagramas de proceso y convierte métricas como costos, tiempos de ciclo y uso de recursos en insights impulsados por IA.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Detalle de pricing: No documentado en la fuente oficial.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have an SAP Signavio Process Modeler license and write access to the workspace that stores the BPMN model. Your workspace administrator has Joule integrated with SAP Signavio solutions. For more information, see Integration with SAP Signavio Solutions. Your workspace administrator created an SAP for Me ticket with the BPI-SIG-PM-MOD-SIM label to request the AI capability to be enabled. Once enabled, your workspace administrator must activate this capability for the users. For more information, see Activate Embedded AI Capabilities and Assign Users. Access to these features depends on your license and access rights.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Las fuentes oficiales SAP abiertas (Initial Setup y/o AI Feature) describen el uso de la capability pero no detallan un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-modeler/user-guide/using-ai-assisted-bpmn-simulation-insights?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/signavio-process-modeler/user-guide/simulating-bpmn-diagrams?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
