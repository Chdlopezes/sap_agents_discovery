# Análisis caso de uso J344 — Permit Management

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J344 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/89944fea-d96d-453c-9684-fe2b2c9cbb51/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Extrae y configura automáticamente permisos de EHS (medio ambiente, salud y seguridad) a partir de documentos PDF que pueden tener desde pocas hasta cientos de páginas. No solo escanea y configura los datos de cabecera del permiso, sino que identifica todos los requisitos y configura las tareas correspondientes (simples, de aviso de mantenimiento, de reporte). El usuario ve en una vista lado a lado las tareas recomendadas mientras revisa las páginas del PDF.

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
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Beta**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/89944fea-d96d-453c-9684-fe2b2c9cbb51/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
