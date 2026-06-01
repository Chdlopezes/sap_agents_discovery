# Análisis caso de uso J346 — Note Corrections for Project Billing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J346 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/#pricing

**Resumen del caso:** La función Smart Notes en Manage Project Billing propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta solo puede comprarse como parte de Joule Premium for Financial Management y no está disponible por separado; precio y duración de contrato bajo solicitud.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: If you use the standard role (SAP_BR_PROJ_BILLG_SPCLST), the following conditions are applicable: If the feature toggle PROJ_BILLG_SMART_NOTE is turned on, the business catalog SAP_PS_BC_BILLG_AI_SNOTE_PC will be added automatically and you can use the Smart Notes feature. Even if the feature toggle is turned off later, the business catalog will still be part of the standard business role. However, you cannot use the Smart Notes feature if the feature toggle PROJ_BILLG_SMART_NOTE is turned off. If the feature toggle PROJ_BILLG_SMART_NOTE is turned on, you have to manually add the Business Catalog SAP_PS_BC_BILLG_AI_SNOTE_PC in order to view and access the Smart Notes feature. If the feature toggle PROJ_BILLG_SMART_NOTE is turned off, you cannot view and access the Smart Notes feature. You will need to manually remove the business catalog.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

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

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
