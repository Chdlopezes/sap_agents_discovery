# Análisis caso de uso J600 — Joule with SAP Multi-Bank Connectivity

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J600 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Proporciona respuestas rápidas sobre SAP Multi-Bank Connectivity a partir de documentación del producto en SAP Help Portal, resumidas de forma contextual y clara.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Multi-Bank Connectivity**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: In this situation, you already have a global account, subaccounts, and entitlements set up. You also have users onboarded and trust set up to support your platform. Since the BTP platform is ready, you simply need to initiate the booster to prepare Joule and then configure the trusted domains. Make sure you Configure Trust to the Identity Authentication Tenant and Configure User Attributes for Joule from the Identity Directory before running the Joule booster. If you haven't set up a BTP platform, then you'll need to set up BTP first. This involves administrative actions in the SAP BTP cockpit. After you set up the platform, you can onboard Joule.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Document Grounding | Configuración de SAP Multi-Bank Connectivity | General | Consultor SAP Multi-Bank Connectivity | 4 |
| 2 | Run the Joule Booster | Configuración de SAP Multi-Bank Connectivity | General | Consultor SAP Multi-Bank Connectivity | 4 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Multi-Bank Connectivity | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Multi-Bank Connectivity | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Multi-Bank Connectivity | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
