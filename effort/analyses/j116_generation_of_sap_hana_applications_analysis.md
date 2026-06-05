# Análisis caso de uso J116 — Generation of SAP HANA Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J116 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código. La capacidad ayuda a crear modelos de datos, servicios, lógica de aplicación y pruebas desde lenguaje natural; además, incluye herramientas generativas para crear sentencias SQL desde prompts.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Build Code**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You have created a global account in the SAP BTP cockpit. See Getting a Global Account. The correct way to subscribe to SAP Build Code is using the booster and not the manual setup. If you already have a subscription to one or more of the services included in SAP Build Code and you would like to upgrade to the SAP Build Code plan, see Changing Service Plans. Access your global account in the SAP BTP cockpit and choose Boosters from the navigation pane. This booster is relevant for the standard service plan. If you are working in the trial plan, you need to run a different booster. Make sure to select the booster relevant to the plan in which you want to work. This option is only available if you are working in the build-code or the build-default plan. See Application Plans.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Subscribe to SAP Build Code | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 2 | Open the booster to see the overview, components, and additional resources. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 3 | Create a Project | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 4 | Select a section of code. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |
| 5 | Open Joule () from the activity bar. | Configuración de SAP Build Code | General | Consultor SAP Build / Desarrollo | 4 |

**Esfuerzo total estimado (activación / configuración): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Build / Desarrollo | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Desarrollo | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Desarrollo | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 11 |
| **Total** | **31** |
