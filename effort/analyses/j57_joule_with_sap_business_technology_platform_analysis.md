# Análisis caso de uso J57 — Joule with SAP Business Technology Platform

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J57 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/btp/sap-business-technology-platform/enable-joule-in-sap-btp-cockpit
- AI Feature (SAP Help Portal): https://help.sap.com/docs/btp/sap-business-technology-platform/account-administration-using-joule?ai=true&locale=en-US&version=Cloud
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Business Technology Platform**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have the Administrator role for the global account for which you'd like to enable Joule in the cockpit. Joule is available for your global account (P-/S-users). Make sure you are accessing the cockpit from the SAP default identity provider. This version of Joule is provided free of charge in non-trial BTP Global Accounts and is limited to supporting BTP administration capabilities only within SAP BTP cockpit. Navigate to the global account settings by selecting  (Global Account Settings). After a global account administrator has enabled Joule for the global account, the Joule diamond icon  will become visible in the cockpit tool header for all global account users. A Global Account Administrator must enable Joule in the Global Account settings by accepting the legal Terms and Conditions for Generative AI. Only then will the Joule icon appear in the cockpit tool header. Check out Enable Joule in the Cockpit to learn more.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable Joule in the Cockpit | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |
| 2 | Enable Joule in SAP BTP cockpit to access Generative AI capabilities. | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |
| 3 | Open the global account for which you'd like to enable Joule in SAP BTP cockpit. | Configuración de SAP Business Technology Platform | General | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/btp/sap-business-technology-platform/enable-joule-in-sap-btp-cockpit
- SAP Help Portal — AI Feature: https://help.sap.com/docs/btp/sap-business-technology-platform/account-administration-using-joule?ai=true&locale=en-US&version=Cloud
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
