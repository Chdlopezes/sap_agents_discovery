# Análisis caso de uso J146 — SAP Joule for Consultants

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J146 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/serviceguide/provisioning-sap-joule-for-consultants
- AI Feature (SAP Help Portal): https://help.sap.com/docs/joule/serviceguide/sap-consulting-capability-for-joule
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/#pricing

**Resumen del caso:** SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud. Está orientado a consultores y equipos de implementación que necesitan acceso guiado a conocimiento, recomendaciones y soporte durante actividades de delivery.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Joule for Consultants**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **SAP Joule for Consultants**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details muestra métrica Requests / usuario-mes para SAP Joule for Consultants. La información visible indica 35 AI Units por métrica, tarifa de EUR 7 por AI Unit y costo por métrica de EUR 245, con cantidad incluida hasta 22.900 solicitudes.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): To start using SAP Joule for Consultants, you must have to following: The SAP AI Units must be assigned to the existing BTP global account where you intend to activate SAP Joule for Consultants. If you do not have a BTP global account, an account will be provisioned free of charge when purchasing SAP AI Units. This account provides sufficient capabilities to enable SAP Joule for Consultants. For a step-by-step guide on how to obtain a BTP global account, please refer to this Learning Journey. BTP global account administrator. SAP Cloud Identity Services administrator.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure the SAP BTP subaccount | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Create a subaccount and select region (i.e. EU10, EU11, US10 or AP10). | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 3 | Add the service plans: | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 4 | Establish Trust with SAP Cloud Identity Services | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 5 | Select the appropriate SAP Cloud Identity Services tenant and establish trust. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 6 | Subscribe to SAP Joule for Consultants | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 7 | Select the service SAP Consulting Capability and the plan standard-ga, click on Next. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |
| 8 | Review the details and click Create. | Configuración de SAP Joule for Consultants | General | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP + Funcional | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP + Funcional | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/serviceguide/provisioning-sap-joule-for-consultants
- SAP Help Portal — AI Feature: https://help.sap.com/docs/joule/serviceguide/sap-consulting-capability-for-joule
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |
