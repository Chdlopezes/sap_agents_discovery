# Análisis caso de uso J91 — Easy Filter

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J91 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Optimiza la experiencia de filtrado en reportes de lista basados en SAP Fiori elements mediante lenguaje natural.

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
- Según la fuente oficial abierta: Administrators can enable the AI-assisted easy filter in SAP Fiori elements-based applications so users can define filter queries using natural language, instead of applying filters manually. their business users need to have the following business catalog assigned: SAP Business AI - User Interface Features - Easy Filter - Display (SAP_CORE_BC_AIU_FIL_PC). To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Select the role and go to the Business Catalogs tab. Ensure the SAP_CORE_BC_AIU_FIL_PC business catalog is assigned to the role, or click Add to search for it. Select it and click OK. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
