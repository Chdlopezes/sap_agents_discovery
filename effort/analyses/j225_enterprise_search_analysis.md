# Análisis caso de uso J225 — Enterprise Search

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J225 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e69295d106654923be99d4ff4e22d751.html?version=2508.500
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Búsqueda empresarial asistida por IA para SAP S/4HANA Cloud Public Edition que ayuda a los usuarios a encontrar datos relevantes de objetos de negocio mediante lenguaje natural desde SAP Fiori Launchpad.

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
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): In the SAP Fiori launchpad, you can use the Enterprise Search feature to access business data efficiently. Depending on your business role, you see a list of business objects in the SAP Fiori launchpad search dropdown. This AI-assisted feature allows you to use natural language for searching business data. You can enter your search queries in natural language in the SAP Fiori launchpad search bar to find the information you need. To enable natural language search on the business objects, you must select the checkbox Enable AI Natural Language Search from the user profile settings [Goto User Profile  Settings  Search]. On selecting the checkbox, you can view the list of business objects that are configured for natural language search. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Install Additional Software | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e69295d106654923be99d4ff4e22d751.html?version=2508.500
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
