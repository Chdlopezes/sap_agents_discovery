# Análisis caso de uso J638 — Process Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J638 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/
- Initial Setup (SAP Help Portal — SAP Build Process Automation, Generative AI): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- AI Feature (SAP Help Portal — Generate Processes): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Genera artefactos de proceso (procesos de negocio, decisiones, formularios y script tasks) a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Process Automation**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (SAP Build Process Automation no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, se debe **habilitar la IA generativa a nivel de tenant** y **aceptar los términos y condiciones**. Tras habilitarla, la función **Generate** queda disponible (aprox. 5 minutos después) en la pantalla Overview del proyecto y en el process editor.
- Según la página **AI Feature** oficial ("Generate Processes"), para usar la generación el usuario debe haber **creado un proyecto** (Business Process Project) y haber **habilitado la IA generativa y aceptado los términos y condiciones** del tenant.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Según la página **AI Feature** oficial: la función *Generate* permite generar únicamente **formularios, procesos y data types**; **no** puede añadir flow controls (branches, go-to steps) ni liberar, desplegar o eliminar un proyecto. El prompt debe tener entre **5 y 1000 caracteres**. Al regenerar un proceso existente, las **variables de proceso (input/output/custom) no se actualizan ni eliminan**, y los inputs de tipo objeto que referencian un data type no están soportados.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Habilitar la **IA generativa a nivel de tenant** en SAP Build Process Automation y aceptar los términos y condiciones | Configuración de tenant (Generative AI) | General | Consultor SAP Build Process Automation | 3 |
| 2 | Verificar (tras ~5 minutos) que la función **Generate** esté disponible en la pantalla Overview del proyecto y en el process editor | Función Generate (process editor) | General | Consultor SAP Build Process Automation | 2 |

**Esfuerzo total estimado (activación / configuración): ~5 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (generar un proceso/decisión/formulario desde lenguaje natural) | Consultor SAP Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La función Generate queda disponible aproximadamente 5 minutos después de habilitar la IA generativa y aceptar los términos y condiciones.
- La IA generativa permite generar procesos de negocio, decisiones, formularios y script tasks.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/
- SAP Help Portal — Initial Setup (SAP Build Process Automation — Generative AI): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US
- SAP Help Portal — AI Feature (Generate Processes): https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generate-process
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 5 |
| Validación + documentación + KT | 11 |
| **Total** | **16** |
