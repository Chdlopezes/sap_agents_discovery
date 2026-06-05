# Análisis caso de uso J535 — Central Governance

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J535 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?version=CLOUD
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/30b09a79645d4137a187835e5010e53d.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule embebido en SAP Master Data Governance sobre SAP S/4HANA Cloud Private Edition permite a usuarios de negocio (p. ej. gerentes de ventas y especialistas de compras) operar funciones de MDG mediante lenguaje natural, sin conocimiento técnico extenso. Usa procesamiento de lenguaje natural para interpretar los prompts del usuario contra la estructura de los datos maestros y ejecutar los cambios: buscar, visualizar, crear nuevos business partners o modificar existentes, y consultar el estado de los procesos de gobierno.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud for master data governance, private edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You provision and configure Joule yourself using SAP BTP, with full control over subaccounts, entitlements, and system integrations. You have checked the general prerequisites for provisioning. A global account, subaccounts, and entitlements have been set up by performing administrative actions in the SAP BTP cockpit. Make sure you have completed the configuration steps before you run the Joule booster. Authorization Objects Used by Master Data Governance

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud for master data governance, private edition | Particular (por usuario / rol) | Consultor SAP MDG (S/4HANA) | 4 |
| 3 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 4 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 5 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 6 | Configure Opt-in/Out of Conversation Log Storage | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |
| 7 | Set Up Document Grounding | Configuración de SAP S/4HANA Cloud for master data governance, private edition | General | Consultor SAP MDG (S/4HANA) | 4 |

**Esfuerzo total estimado (activación / configuración): ~28 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP MDG (S/4HANA) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP MDG (S/4HANA) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP MDG (S/4HANA) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?version=CLOUD
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/30b09a79645d4137a187835e5010e53d.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 28 |
| Validación + documentación + KT | 11 |
| **Total** | **39** |
