# Análisis caso de uso J762 — Joule and Microsoft 365 Copilot

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J762 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/joule/integrating-joule-with-sap/integrating-joule-with-microsoft-365-copilot?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365. Permite consultar datos y tareas de SAP desde Copilot y aprovechar información/flujos de Microsoft 365 desde Joule.

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
- Según la fuente oficial abierta: You have at least one SAP business tenant (Such as SAP S/4HANA Private Cloud, SAP SuccessFactors) integrated with Joule. You have set up trust between Entra and SAP Cloud Identity Services – Identity Authentication, registering Entra as the Corporate IdP based on OIDC. For more information, see Configuring SAP Cloud Identity Services and Microsoft Entra ID for Joule. You have a Microsoft M365 Copilot license and have rolled out M365 Copilot to the intended user base. For more information, see Getting Started with Microsoft 365 Copilot. Joule maintains a 1:1 relationship with a Microsoft Entra ID tenant. Hence, a single Entra ID tenant cannot be used for configuring multiple Joule environments. In which case, your development and production tenants cannot use the same Microsoft Entra ID tenant. Therefore, to establish a testing environment for the Microsoft 365 Copilot integration, it is recommended to utilize a dedicated M365 tenant for testing purposes. Note down your Microsoft M365 Tenant Id corresponding to your productive Microsoft M365 Copilot/Teams deployment. You'll need to provide this during the Joule landscape setup.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Document Grounding | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Install the SAP Joule app via the Microsoft 365 Admin Center. | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

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

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/integrating-joule-with-microsoft-365-copilot?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
