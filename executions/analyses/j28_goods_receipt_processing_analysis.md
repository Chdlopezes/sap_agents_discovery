# Análisis caso de uso J28 — Goods Receipt Processing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J28 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/30d87325d6964ec18da12bd2fe927009.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/#pricing

**Resumen del caso:** Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA. Permite extraer información relevante de documentos de flete en papel, publicarla en el sistema y detectar anomalías que pueden retrasar la validación de freight orders.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units Precio bajo solicitud AI Units requeridas para usar la oferta en el Cloud Service subyacente. Tiene prerrequisito.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. To onboard AI-Assisted Goods Receipt Analysis, you need to request an SAP Business Technology Platform (SAP BTP) service key with the intelligent scenario SCMTMS_DOX_DLV_NOTE for the delivery note and SCMTMS_TMDOX for the shipping document. For more information, see SAP Delivered Document Information Extraction Scenario and Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP).

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

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
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/30d87325d6964ec18da12bd2fe927009.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
