# Análisis caso de uso J74 — Joule with SAP S/4HANA Cloud Public Edition

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J74 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/27d870bda64547febeb48482aeee77d5.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/a955cb79db3c4f5c89ed3f00bb05f080.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): This section describes how to integrate Joule with the technical product SAP S/4HANA Cloud Public Edition. These steps comprise the Joule-specific and product-specific prerequisites and depend on your initial system setup. For example, you must first set up the technical environment, such as the SAP Business Technology Platform (BTP) with the entitlements for Joule and SAP Build Work Zone, standard edition (foundation/standard plan). You are guided through the integration steps with instructions, for example, you run the Joule booster that - among other settings - enables the communication scenario SAP_COM_0882 (SAP Digital Assistant Services) in the background. To access Joule within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your account executive for more information. You fulfill the general Prerequisites for Customer Managed Provisioning for Joule. You have reviewed the Customer Managed Provisioning for Joule and have carried out the necessary steps. To integrate Joule with SAP S/4HANA Cloud Public Edition, you must carry out the following steps:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Register the SAP S/4HANA Cloud Public Edition System | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 4 | Create SAP Build Work Zone Application and Instance | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 5 | Run the Joule Booster | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 6 | Configure Identity Provisioning Service | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 7 | Configure Trusted Domain in SAP BTP | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |
| 8 | Configure Trusted Domains in Identity Authentication | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

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

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/27d870bda64547febeb48482aeee77d5.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/JOULE/82a14f108cfa4d4788244d81371e072b/a955cb79db3c4f5c89ed3f00bb05f080.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |
