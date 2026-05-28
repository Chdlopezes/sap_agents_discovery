# Análisis caso de uso J193 — UI Generation from Data (SAP Build Apps)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite generar automáticamente páginas de aplicación a partir de entidades de datos ya integradas en un proyecto de SAP Build Apps, incluyendo operaciones CRUD como punto de partida. SAP indica: *Reduce el tiempo de construcción de aplicaciones, mejora la productividad de equipos low-code y acelera la entrega de extensiones o aplicaciones empresariales basadas en datos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Apps** en BTP con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Apps + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SAP Build Apps.

### 1.5 Datos maestros / transaccionales previos
- Data entities integradas (OData / REST / DB) en Build Apps.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Citizen Developer / Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SAP Build Apps + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar data entities en Build Apps | Build Apps data | Particular (por entidad) | Consultor Build Apps | 5 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar UI Generation from Data | Configuración Build Apps | General | Consultor Build Apps | 2 |
| 5 | Pruebas iniciales (generar páginas desde entidades) | Configuración Build Apps | General | Consultor Build Apps | 4 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Build Apps | 5 |
| 2 | Documentación + buenas prácticas | Consultor Build Apps | 4 |
| 3 | Transferencia de conocimiento | Consultor Build Apps | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Páginas generadas son base; pulir UX, navigation y validations.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |
