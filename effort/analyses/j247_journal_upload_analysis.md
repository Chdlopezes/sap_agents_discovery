# Análisis caso de uso J247 — Journal Upload

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J247 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/cab97d8445064be79d3dcb868ccddf94.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/#pricing

**Resumen del caso:** Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition. Mediante una app SAP Fiori con capacidades de IA generativa, permite crear casos de carga, asociar una guía o política de contabilización en lenguaje natural, generar propuestas, validarlas y publicar asientos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta se adquiere como parte de Joule Premium for Financial Management y no por separado; el precio está disponible bajo solicitud. Las solicitudes adicionales se cobran en bloques de 1.000 por 2 AI Unit(s).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. Approval Workflow Integration: You can submit proposals for review, and designated approvers can verify and approve them before posting. To do this, you need to configure and manage approval workflows for journal upload cases. Setting Up the Connection to Intelligent Scenario Lifecycle Management Activating the Intelligent Scenario

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Request Access to SAP Business Technology Platform (SAP BTP) | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/cab97d8445064be79d3dcb868ccddf94.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
