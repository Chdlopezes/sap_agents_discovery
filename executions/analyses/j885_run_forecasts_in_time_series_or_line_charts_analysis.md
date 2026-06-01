# Análisis caso de uso J885 — Run Forecasts in Time Series or Line Charts

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J885 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/ca67817bec1c4f6582126d5d9dab68bb.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Los analistas de negocio pueden generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de SAP Analytics Cloud.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Creating and Provisioning Your SAP Analytics Cloud Tenant in SAP BTP Cockpit This setting lets you define if creators of calendar events on your tenant can enable the integration of their calendar events with Microsoft tools, like Microsoft Outlook and Microsoft Teams. To turn on this setting, enter the IDs of the application (client) and the directory (tenant) from your Microsoft Azure Active Directory. This setting allows SAP Product Support to create a support user on your tenant during troubleshooting processes without requiring internal user credentials. By default, this setting is disabled. This setting enables you to prevent users from uploading data without permission by an administrator. By default, this setting is disabled until you turn it on.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure System Settings | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 2 | Enable AI-Assisted Features for SAP Analytics Cloud | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 3 | Configure Data Storage for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 4 | Enable Bring Your Own Key Encryption with SAP Analytics Cloud and SAP Data Custodian | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 5 | Set Up Third-Party Access with OAuth Clients | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 6 | Configure Email Server | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/ca67817bec1c4f6582126d5d9dab68bb.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |
