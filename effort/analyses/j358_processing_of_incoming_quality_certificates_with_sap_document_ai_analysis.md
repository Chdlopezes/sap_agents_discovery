# Análisis caso de uso J358 — Processing of Incoming Quality Certificates with SAP Document AI

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J358 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/46a0ffd9c19d4dde88861505889b14b1.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/#pricing

**Resumen del caso:** Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): AI Units requeridos. En Pricing Details se indica activación mediante “Activate with AI Units”; precio disponible bajo solicitud; duración contractual disponible bajo solicitud; tiene prerrequisito. La página también indica que, para activar esta capacidad, se requieren SAP Document AI, embedded edition y un workspace de SAP Document AI, por lo que pueden aplicar sus detalles de pricing.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have configured incoming quality certificates with one or more certificate types for which enhanced certificate processing is enabled. Users have the business catalog QM - Incoming Quality Certificates (SAP_QM_BC_INCG_QLTY_CERT_PC) or the apps Manage Certificate Receipts (F3233), Review Certificate Document Matches (F8537), and Upload Quality Certificate Documents (F8858) assigned to one of their roles. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Review Certificate Document Matches | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

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

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/46a0ffd9c19d4dde88861505889b14b1.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
