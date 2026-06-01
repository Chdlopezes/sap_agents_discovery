# Análisis caso de uso J121 — Process Recommender

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J121 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-model
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/#pricing

**Resumen del caso:** Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio.

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
| 1 | Select the  Process AI recommendation service in the top header. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 2 | Select the Find process models prompt. This becomes the prefix for your query. Then, use natural language to complete the query. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |
| 3 | Select View template, to preview the process model. | Configuración de SAP Signavio solutions | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/signavio-process-collaboration-hub/user-guide/using-ai-to-find-best-process-model
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
