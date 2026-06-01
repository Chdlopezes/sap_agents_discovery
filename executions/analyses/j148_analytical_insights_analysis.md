# Análisis caso de uso J148 — Analytical Insights

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J148 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/3d8afae09f1e48e79aac5b2102b2aa7b.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP. Se integra con Just Ask de SAP Analytics Cloud dentro de SAP Business Data Cloud.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Index Your Data Using Just Ask and Test Your Integration The Joule 2506 release has introduced a change that affects Joule analytical insights. SAP Build Work Zone is now required as part of the integration to provision and sync users and roles from SAP Analytics Cloud to SAP Build Work Zone. If you have activated analytical insights in Joule before the 2506 release, you need to redo the setup using the instructions found in this guide. You must be an SAP BTP global account administrator to follow the steps in this guide and set up the capability. You must have appropriate Joule entitlements. You must have SAP Build Work Zone as part of the integration to provision and sync users and roles from SAP Analytics Cloud to SAP Build Work Zone.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable the Analytical Insights Capability in Joule | Configuración de Joule | General | Consultor SAP BTP + Funcional | 3 |
| 2 | Provision Users from SAP Analytics Cloud to SAP Build Work Zone Using IPS | Configuración de Joule | Particular (por usuario / rol) | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP BTP + Funcional | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP BTP + Funcional | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP BTP + Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/JOULE/6189c8655c484916bb8eb767126a653a/3d8afae09f1e48e79aac5b2102b2aa7b.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
