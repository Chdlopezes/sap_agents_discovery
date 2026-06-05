# Análisis caso de uso J241 — Maintenance Order Recommendation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J241 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/ff90ad7fa38a41a5a0f3a8faa21189f9.html?locale=en-US
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/46af82ff1a4e47159f6cc00a06b94e91.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/#pricing

**Resumen del caso:** Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento. El planificador revisa las recomendaciones y selecciona una orden como referencia para crear una nueva orden de mantenimiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica que la oferta se adquiere como parte de Joule Premium for Supply Chain Management y no por separado; el precio está disponible bajo solicitud. Las solicitudes adicionales se cobran en bloques de 1.000 por 2 AI Unit(s).

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): As a system administrator, you need to perform some initial setup steps to enable the system to generate order recommendations. Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. Required Users and Authorizations Make sure that you have access to the Intelligent Scenario Management app (F4470), which is included in the business role template for the Analytics Specialist (SAP_BR_ANALYTICS_SPECIALIST). Personalized Recommendation is a service provided on SAP Business Technology Platform (SAP BTP). To use this service, contact SAP to request a service instance for Personalized Recommendation and to be onboarded to the intelligent scenario EAM_MAINTORD_RECMDN. Make sure you have noted down the name of the intelligent scenario, as you will need it later in the setup process. For more information, see Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP). Intelligent Scenario Lifecycle Management

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/ff90ad7fa38a41a5a0f3a8faa21189f9.html?locale=en-US
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e72f747389b340229f7fa343975bfa57/46af82ff1a4e47159f6cc00a06b94e91.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
