# Análisis caso de uso J294 — Joule with SAP Datasphere

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Con Joule embebido en SAP Datasphere, los usuarios pueden realizar tareas informativas, navegacionales y transaccionales de forma fluida, incluyendo consultas sobre uso del producto y tareas comunes de administración. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se orienta a productividad de usuarios y administradores en SAP Datasphere.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** activo en BTP.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Datasphere.
- Entitlement Joule + capability Datasphere **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Datasphere tenant con spaces / data builders configurados.
- Joule integrado en Datasphere UI.

### 1.5 Datos maestros / transaccionales previos
- Modelos de datos (entities, views, business semantics) en Datasphere.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Datasphere (modeler / consumer).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Datasphere + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Datasphere | Datasphere settings | General | Consultor Datasphere | 3 |
| 4 | Asignar roles Datasphere a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas en NL sobre modelos) | Configuración Datasphere | General | Consultor Datasphere | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con modelos reales | Consultor Datasphere | 4 |
| 2 | Documentación para el cliente | Consultor Datasphere | 4 |
| 3 | Transferencia de conocimiento | Consultor Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Calidad de respuesta depende de la riqueza semántica de los modelos.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |
