# Análisis caso de uso J284 — Joule with SAP LeanIX

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J284 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/
- Initial Setup (SAP Help Portal): Enlace presente en *Resources* pero no accesible tras reintentos (versión/login).
- AI Feature (SAP Help Portal): https://help.sap.com/docs/leanix/ea/joule-in-sap-leanix?locale=en-US&version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Search the inventory by fact sheet name, by applying filters, or using natural language. If you have the required permissions, you can create, update, or archive fact sheets without leaving the conversation. You can update the fact sheet name, description, lifecycle, and quality seal from the conversation. View fact sheet subscribers and their roles, and contact them directly from the conversation. Find users by name or email and see which fact sheets they’re subscribed to.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open a fact sheet to view related to-dos and their status. Create new to-dos without leaving the conversation. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Early Adopter Care (EAC)**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/
- SAP Help Portal — Initial Setup: No accesible tras reintentos
- SAP Help Portal — AI Feature: https://help.sap.com/docs/leanix/ea/joule-in-sap-leanix?locale=en-US&version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
