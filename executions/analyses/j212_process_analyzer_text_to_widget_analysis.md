# Análisis caso de uso J212 — Process Analyzer, Text To Widget (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Analyzer, Text to Widget permite crear widgets de dashboard a partir de consultas en lenguaje natural sobre datos de procesos. SAP indica: *El valor se centra en acelerar el time-to-value de los dashboards de procesos, mejorar la autonomía de usuarios de negocio y reducir dependencia de equipos técnicos para análisis básicos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Intelligence** activo.
- Capability AI / Joule integrada en Signavio **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Intelligence con feature AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Analyzer.

### 1.5 Datos maestros / transaccionales previos
- Investigations / process data sources cargados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Process Analyst.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Asignar rol Process Analyst | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Text To Widget | Signavio admin | General | Consultor Signavio | 2 |
| 4 | Pruebas iniciales: generar widgets a partir de prompts | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con investigations reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Resultados dependen de la riqueza del modelo de datos cargado en Signavio.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 10 |
| **Total** | **19** |
