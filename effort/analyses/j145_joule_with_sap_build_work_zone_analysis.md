# Análisis caso de uso J145 — Joule with SAP Build Work Zone

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J145 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/integration-with-joule
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo. También soporta acceso remoto mediante SAP Mobile Start o sitio móvil.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Work Zone**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Service Plans and Metering New subscriptions in SAP Build Work Zone, standard edition created after 20th March, 2025 are directly connected to Identity Authentication by default. If your subscription was created before this date, and you aren't connected to Identity Authentication, you need to switch over. For more information, see Switching to SAP Cloud Identity Services - Identity Authentication Joule requires a trust configuration of type OpenID Connect with your Identity Authentication tenant. SAML based trust is not supported. Before completing the Joule onboarding tasks, you'll need to ensure that you've met the required prerequisites for both SAP Build Work Zone, standard edition and for Joule. For a list of these prerequisites, please refer to: Prerequisites. To integrate Joule with both the standard and advanced editions, you can create an additional subscription to Joule in another subaccount and use one edition per subaccount.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Work Zone | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Work Zone | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Work Zone | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/integration-with-joule
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
