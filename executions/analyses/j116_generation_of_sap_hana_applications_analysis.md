# Análisis caso de uso J116 — Generation of SAP HANA Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código. La capacidad ayuda a crear modelos de datos, servicios, lógica de aplicación y pruebas desde lenguaje natural; además, incluye herramientas generativas para crear sentencias SQL desde prompts. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar extensiones y aplicaciones HANA, mejorar productividad del desarrollador y facilitar un enfoque clean core.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.
- **SAP HANA Cloud** disponible como backend.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.
- Entitlement HANA Cloud.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- HANA Cloud DB provisionada; esquemas / HDI containers configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Developer con permisos HANA Cloud.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule + HANA Cloud | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar conexión HANA Cloud (HDI container, schema) | DB setup | General | Consultor HANA | 4 |
| 3 | Asignar rol Developer + HANA roles | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar HANA App Generation | Configuración Build Code | General | Consultor HANA / Dev | 2 |
| 5 | Pruebas iniciales: generar app CAP+HANA con prompts | Configuración Build Code | General | Desarrollador HANA Sr | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador HANA Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador HANA Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador HANA Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Modelado de datos HANA (CDS, calculation views) merece review especializado.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |
