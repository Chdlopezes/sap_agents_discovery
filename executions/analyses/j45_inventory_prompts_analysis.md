# Análisis caso de uso J45 — Inventory Prompts

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J45 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- Initial Setup (SAP Help Portal): https://docs-eam.leanix.net/docs/ai-capabilities
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Inventory Prompts combina la información del inventario SAP LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial. Provee una interfaz de lenguaje natural para consultar datos y obtener insights usando preguntas cotidianas.

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
- Según la fuente oficial abierta: If you haven’t signed your contract and want to activate AI capabilities, contact your SAP Account Executive to sign the SAP AI terms and start the activation process.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Register to use Joule in SAP LeanIX | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

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

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- SAP Help Portal — Initial Setup: https://docs-eam.leanix.net/docs/ai-capabilities
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
