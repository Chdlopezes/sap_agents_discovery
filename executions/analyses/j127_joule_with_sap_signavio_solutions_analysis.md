# Análisis caso de uso J127 — Joule with SAP Signavio solutions

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural. SAP indica: *50% más rapidez en búsquedas informativas; 50% más rapidez en ejecución de tareas de navegación y transaccionales; mejor calidad de resultados de búsqueda y experiencia de usuario.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Transformation Suite** (Process Manager, Process Intelligence, Process Insights, etc.) activo.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio (módulos aplicables).
- Entitlement Joule + capability Signavio **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace Signavio.
- Joule integrado en Signavio UI.

### 1.5 Datos maestros / transaccionales previos
- Modelos BPMN, mining de datos, KPI definidos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Signavio.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Signavio + Joule capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO Signavio | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Signavio | Signavio admin | General | Consultor Signavio | 3 |
| 4 | Asignar roles Signavio a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas y acciones sobre procesos) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con modelos/datos reales | Consultor Signavio | 5 |
| 2 | Documentación para el cliente | Consultor Signavio | 4 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Cobertura de capabilities Joule dentro de Signavio se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 12 |
| **Total** | **28** |
