# Análisis caso de uso J178 — Inventory Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J178 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/inventory-builder
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/#pricing

**Resumen del caso:** SAP LeanIX Inventory Builder acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP LeanIX solutions**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activar con AI Units Precio bajo solicitud AI Units requeridas para usar la oferta en el Cloud Service subyacente. Tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: The inventory builder is a premium AI feature. To use it in production workspaces, you must accept the AI terms and have AI units assigned to your tenant. In some test or demo workspaces, you may be able to try premium AI features without buying AI units. You have accepted the AI terms. You have purchased AI units and they are assigned to your tenant.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open this video in a new window | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |
| 2 | Review the proposed fact sheets and relations. While reviewing, you can make the following changes: | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

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

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/inventory-builder
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
