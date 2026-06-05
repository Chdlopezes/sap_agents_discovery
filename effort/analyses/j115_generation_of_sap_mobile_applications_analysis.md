# Análisis caso de uso J115 — Generation of SAP Mobile Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J115 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/337848fc83f24738a9f3a15a88f1fa76.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code. Puede generar componentes a partir de lenguaje natural, incluyendo código, modelos de datos, servicios, lógica de negocio, datos de ejemplo y pruebas unitarias.

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/
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
