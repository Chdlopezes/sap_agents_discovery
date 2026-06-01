# Análisis caso de uso J1284 — Document Data Extraction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J1284 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Extrae y procesa automáticamente información clave de PDFs e imágenes escaneadas usando IA, con o sin plantillas.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Before you can work in SAP Build Process Automation, your SAP BTP account administrator must subscribe your SAP BTP subaccount to the SAP Build Process Automation application. Once subscribed, you can then configure additional product extensions.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Process Automation | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 2 | Configure Automation Capabilities | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 3 | Create a Business Site Using SAP Build Work Zone | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 4 | Configure Product Extensions | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 5 | Enable Notifications | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |
| 6 | Integrate and Connect With Other Services | Configuración de SAP Build Process Automation | General | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |
