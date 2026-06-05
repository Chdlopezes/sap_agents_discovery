# Análisis caso de uso J213 — Process Modeler

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J213 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-manager/user-guide/creating-bpmn-diagram-with-ai-assisted-process-modeling
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/#pricing

**Resumen del caso:** Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create a Diagram | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 2 | Open and Save Diagrams | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 3 | Add and Connect Elements | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 4 | Create Subprocesses | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 5 | Add Live Insights | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 6 | Add Links to SAP Signavio Process Insights Content | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

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

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-manager/user-guide/creating-bpmn-diagram-with-ai-assisted-process-modeling
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |
