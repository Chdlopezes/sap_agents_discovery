# Análisis caso de uso J240 — In-house Service Initiation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J240 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/da1c8b47160a49a9820d3a63e1d97c06.html?version=2023.003
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/#pricing

**Resumen del caso:** Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos. El personal de reparación puede escanear o fotografiar documentos entrantes, como órdenes de compra; el sistema extrae datos relevantes y genera objetos de reparación asociados al servicio interno.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units Precio bajo solicitud AI Units requeridas. La oferta solo puede adquirirse como parte del paquete Joule Premium for Supply Chain Management y no está disponible por separado.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You have performed the following steps to set up Intelligent Scenario Lifecycle Management: Configuring Business Roles for the Backend Configuring Business Roles for the Frontend

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open a support ticket on the SAP Support Portal on component CA-S4H-BTPAI. | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

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

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/da1c8b47160a49a9820d3a63e1d97c06.html?version=2023.003
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
