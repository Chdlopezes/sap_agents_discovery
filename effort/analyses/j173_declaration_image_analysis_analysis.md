# Análisis caso de uso J173 — Declaration Image Analysis

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J173 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ef9efdef-7300-4580-9c54-5664e1c99f95/
- Initial Setup (SAP Help Portal): No existe enlace 'Initial Setup' en *Resources*.
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Extrae automáticamente información de declaraciones de distintos formatos sin interacción del usuario y contabiliza los datos de la transacción en SAP Green Token. Elimina la dependencia de mecanismos de extracción propios del cliente y extrae datos con precisión de tipos de documento diversos, donde la información requerida está bien definida pero la estructura y el formato no son uniformes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Green Token**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- No documentado en la fuente oficial.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** Tras consultar el Initial Setup y la página AI Feature enlazados en *Resources*, no fue posible acceder a una página oficial SAP que describa un procedimiento de activación para este caso. No se han fabricado pasos.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional del producto base (producto base) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional del producto base (producto base) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional del producto base (producto base) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Beta**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ef9efdef-7300-4580-9c54-5664e1c99f95/
- SAP Help Portal — Initial Setup: No existe enlace en *Resources*
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
