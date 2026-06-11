# Análisis caso de uso J1173 — Deep Research Capability

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1173 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/0cbab727-02fe-47d3-9bf1-ff96d6c2ae62/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La capacidad de deep research en Joule permite a los usuarios buscar, preguntar y acceder al conocimiento e insights que necesitan dentro de su flujo de trabajo. Accediendo a recursos internos y a conocimiento externo —estructurado o no estructurado— Joule entrega información relevante y accionable, asegurando cumplimiento y maximizando la productividad.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You provision and configure Joule yourself using SAP BTP, with full control over subaccounts, entitlements, and system integrations. You have checked the general prerequisites for provisioning. A global account, subaccounts, and entitlements have been set up by performing administrative actions in the SAP BTP cockpit. Make sure you have completed the configuration steps before you run the Joule booster.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure Trust to the Identity Authentication Tenant | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |
| 2 | Configure User Attributes for Joule from the Identity Directory | Configuración de Joule | Particular (por usuario / rol) | Consultor SAP BTP + Funcional | 4 |
| 3 | Run the Joule Booster | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |
| 4 | Configure Trusted Domains in Identity Authentication | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |
| 5 | Configure Trusted Domain in SAP BTP | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |
| 6 | Configure Opt-in/Out of Conversation Log Storage | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |
| 7 | Set Up Document Grounding | Configuración de Joule | General | Consultor SAP BTP + Funcional | 4 |

**Esfuerzo total estimado (activación / configuración): ~28 horas.**

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

- Disponibilidad indicada por SAP: **Beta**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0cbab727-02fe-47d3-9bf1-ff96d6c2ae62/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/initial-setup?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 28 |
| Validación + documentación + KT | 11 |
| **Total** | **39** |
