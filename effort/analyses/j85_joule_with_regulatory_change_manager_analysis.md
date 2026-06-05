# Análisis caso de uso J85 — Joule with Regulatory Change Manager

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J85 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/REGULATORY_CHANGE_MANAGER/8d691963179a42858de62e51939bafe3/6a2270b857024325a4d643487e1bba6a.html?version=Public
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Regulatory Change Manager**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Only IT Users have access to Joule and are limited to asking 15 questions per week. Once you have asked 10 questions in a week, Joule will notify you about the remaining questions. The quota of 15 questions will be reset every Sunday.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

> **No se registran pasos de activación.** La fuente oficial SAP abierta describe el uso de la capability pero no detalla un procedimiento de activación administrativo explícito. El caso de uso puede venir habilitado por defecto al cumplirse los prerequisitos del producto base.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Regulatory Change Manager | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Regulatory Change Manager | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Regulatory Change Manager | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/REGULATORY_CHANGE_MANAGER/8d691963179a42858de62e51939bafe3/6a2270b857024325a4d643487e1bba6a.html?version=Public
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | No aplica (sin pasos oficialmente documentados) |
| Validación + documentación + KT | 11 |
| **Total** | **11** |
