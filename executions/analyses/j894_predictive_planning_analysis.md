# Análisis caso de uso J894 — Predictive Planning

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J894 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/66eeff9e46334644b43b10e49e2022bf.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos. La capacidad ayuda a actualizar previsiones de forma más ágil y a reducir sesgos en los ciclos de planificación.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

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

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Define the Settings of Time Series Predictive Models for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/66eeff9e46334644b43b10e49e2022bf.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
