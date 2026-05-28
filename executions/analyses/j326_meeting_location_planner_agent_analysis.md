# Análisis caso de uso J326 — Meeting Location Planner Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; pasos de setup pueden no estar todavía completamente documentados públicamente.

**Resumen del caso:** Ayuda a empleados a organizar reuniones offsite sugiriendo ubicaciones que minimizan tiempos de viaje, proponiendo hoteles y mostrando una vista general de costos para planificar dentro del presupuesto. SAP indica: *No se identificó una métrica cuantitativa completa en el contenido accesible de la página de detalle; el valor descrito se concentra en reducir tiempo de planificación y mejorar el control presupuestal de offsites.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con calendar / meeting providers (Microsoft 365 / Google) **[verificar]**.
- (Opcional) Integración con Travel Management / Concur.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible.
- Destinations a calendar / venue providers.

### 1.5 Datos maestros / transaccionales previos
- Calendarios y datos de assistants/executives a soportar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a calendar / venue providers | Destinations | General | Consultor BTP / Integración | 5 |
| 3 | Asignar acceso al agente a executive assistants | Roles / Agent assignment | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Validar políticas (lugares preferidos, presupuestos) | Configuración del agente | Particular (por organización) | Consultor Funcional + Diseñador agente | 4 |
| 5 | Pruebas iniciales con escenarios reales (offsite planning) | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos típicos | Consultor Funcional | 5 |
| 2 | Documentación para el cliente | Consultor Funcional | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Privacidad: el agente accede a calendarios; revisar consentimientos y DLP.
- Resultados dependen del catálogo de venues/políticas disponibles.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |
