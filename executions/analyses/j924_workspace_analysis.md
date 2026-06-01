# Análisis caso de uso J924 — Workspace

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J924 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/document-ai/sap-document-ai/subscribing-to-sap-document-ai-workspace-with-identity-authentication-service
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/#pricing

**Resumen del caso:** SAP Document AI, workspace ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document AI**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units para usar esta oferta de IA en el servicio cloud subyacente. El método de activación indicado es “Activate with AI Units”. Precio bajo solicitud; duración del contrato disponible bajo solicitud; tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Service Plans and Metering Subscribing to the SAP Document AI Workspace With the Identity Authentication Service Subscribing to the SAP Document AI Workspace With the Identity Authentication Service You have an SAP BTP global account and a Cloud Foundry or Kyma subaccount. You’re a global account administrator.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable X.509 Authentication | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 2 | Run SAP Document AI in a Multitenant Application | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 3 | Subscribe to the SAP Document AI workspace using the Identity Authentication service to handle authentication and authorization tasks in SAP BTP. | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |
| 4 | Open the SAP BTP cockpit and go to your subaccount. | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 4 |

**Esfuerzo total estimado (activación / configuración): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Document AI / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Document AI / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/document-ai/sap-document-ai/subscribing-to-sap-document-ai-workspace-with-identity-authentication-service
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |
