# Análisis caso de uso J652 — Architecture Guidance

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J652 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/leanix/ea/ai-assisted-architecture-guidance
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de SAP LeanIX que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial.

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
- Según la fuente oficial abierta: Confirm that the relevant AI terms have been signed. Contact your customer success manager if you have questions. If insights are already available, they appear as tiles on the Architecture Guidance page. If you've just activated the feature, it can take some time before insights are displayed.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activate AI Assisted Architecture Guidance under Administration  Optional Features & Early Access. | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |
| 2 | Add new applications and business capabilities to your inventory, for example, look into a new department or line of business, see Define the Scope of Your Application Portfolio Assessment | Configuración de SAP LeanIX solutions | General | Consultor SAP LeanIX | 3 |

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

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/leanix/ea/ai-assisted-architecture-guidance
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
