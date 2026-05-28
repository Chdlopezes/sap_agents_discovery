# Análisis caso de uso J114 — Generation of SAP Fiori Elements and SAPUI5 Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Project Accelerator simplifica el desarrollo convirtiendo requerimientos de negocio desde texto, imágenes o ambos en un proyecto full-stack con una aplicación SAP Fiori elements funcional. Se puede acceder desde el panel de SAP Fiori o mediante un comando en Joule. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar el desarrollo de aplicaciones Fiori/SAPUI5 y permitir que el equipo se enfoque en aspectos más complejos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- OData / RAP services back-end donde se generan las apps Fiori.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a backends OData/RAP | Destinations | Particular (por backend) | Consultor BTP | 3 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Fiori Elements/UI5 Generation | Configuración Build Code | General | Consultor BTP / Dev | 2 |
| 5 | Pruebas iniciales: generar app Fiori Elements | Configuración Build Code | General | Desarrollador Fiori | 4 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador Fiori | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador Fiori | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Fiori | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Código generado requiere review (annotations, navegación, performance).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 12 |
| **Total** | **26** |
