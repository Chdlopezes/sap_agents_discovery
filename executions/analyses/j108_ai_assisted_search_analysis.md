# Análisis caso de uso J108 — AI-Assisted Search

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J108 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- Initial Setup (SAP Help Portal — Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

**Resumen del caso:** Habilita consultas de búsqueda en lenguaje natural directamente en SAP Datasphere (repository explorer, data builder, catalog y data marketplace). La búsqueda aumentada con IA interpreta solicitudes complejas y devuelve resultados sobre los objetos y artefactos del tenant.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): activación mediante **AI Units**; precio bajo solicitud (métrica Flat Fee). Se requieren AI Units para usar la oferta en el servicio cloud subyacente.

### 1.3 Scope item relacionado
- No aplica (SAP Datasphere no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial ("Enable SAP Business AI for SAP Datasphere"), para habilitar SAP Business AI se debe contar con un **rol global** que otorgue los privilegios requeridos; la fuente indica que el rol global **DW Administrator**, por ejemplo, otorga esos privilegios.
- SAP Business AI es un servicio gestionado por SAP; se habilita SAP Business AI y Joule para SAP Datasphere para integrar recomendaciones de contenido de IA.

### 1.5 Datos maestros / transaccionales previos
- Artefactos de datos del tenant (modelos, vistas, objetos, espacios) sobre los que realizar la búsqueda.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asegurar un **rol global** con los privilegios requeridos para habilitar SAP Business AI (p. ej. **DW Administrator**) | Roles globales / privilegios de SAP Datasphere | Particular (por usuario / rol) | Consultor Seguridad SAP Datasphere | 3 |
| 2 | **Habilitar SAP Business AI y Joule para SAP Datasphere** (Enable SAP Business AI for SAP Datasphere) | Configuración del tenant (System → Configuration) | General | Consultor SAP Datasphere | 3 |
| 3 | Confirmar el entitlement de **AI Units** para el tenant | AI Units | General | Consultor BTP / Licencias | 2 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (búsquedas en lenguaje natural sobre artefactos del tenant) | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura por **AI Units** (precio bajo solicitud, métrica Flat Fee), según *Pricing Details*.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- SAP Help Portal — Initial Setup (Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
