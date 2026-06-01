# Análisis caso de uso J36 — Generation of Full-Stack Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J36 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural. Con Joule, la capacidad genera modelos de datos, servicios, datos de ejemplo, anotaciones de UI, lógica de aplicación y pruebas unitarias, dentro de un entorno de desarrollo cloud alineado con SAP Business Application Studio y buenas prácticas de SAP BTP.

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
- Según la fuente oficial abierta: You have created a global account in the SAP BTP cockpit. See Getting a Global Account. The correct way to subscribe to SAP Build Code is using the booster and not the manual setup. If you already have a subscription to one or more of the services included in SAP Build Code and you would like to upgrade to the SAP Build Code plan, see Changing Service Plans. Access your global account in the SAP BTP cockpit and choose Boosters from the navigation pane. This booster is relevant for the standard service plan. If you are working in the trial plan, you need to run a different booster. Make sure to select the booster relevant to the plan in which you want to work.

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

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build_code/d0d8f5bfc3d640478854e6f4e7c7584a/07698d7c31284e4db370acdf017cfd14.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
