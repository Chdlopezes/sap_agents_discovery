# Análisis caso de uso J120 — Performance Indicators Recommender

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio** que ayuda a pasar del problema de negocio a un enfoque de medición recomendando KPIs y PPIs relevantes desde un repositorio amplio de indicadores de desempeño de procesos. SAP indica **5% menor erosión de valor** asociada a una selección deficiente de indicadores.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio solutions** (suscripción activa).
- Acceso a procesos / modelos relevantes del cliente en SAP Signavio.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Premium** — activación con **AI Units** según *Pricing Details*.
- **AI Units** asignadas; pricing estimable mediante el AI Estimator de SAP **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio** con modelos de proceso del cliente y acceso al repositorio de PPIs.

### 1.5 Datos maestros / transaccionales previos
- Definición clara del problema de negocio o proceso para el que se buscan indicadores.
- Modelos / event logs disponibles para conectar los indicadores recomendados con datos reales (cuando aplique).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Business Process Analyst / Process Owner.

> **Setup oficial SAP**: la página https://help.sap.com/docs/signavio-process-insights/business-content-reference/process-performance-indicators referencia el catálogo de indicadores. La activación de la capability se realiza mediante AI Units según el Pricing Details.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Premium y AI Units para SAP Signavio | Workspace Signavio + AI Units | General | Consultor SAP Signavio + BTP / Licencias | 2 |
| 2 | Estimar AI Units necesarios para el volumen previsto (AI Estimator) | AI Units — Estimación | General | Consultor SAP Signavio | 2 |
| 3 | Habilitar la capability del Performance Indicators Recommender en el workspace | Workspace Signavio — AI Capabilities | General | Consultor SAP Signavio | 2 |
| 4 | Asignar a los usuarios objetivo los roles Signavio con acceso a la capability | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 5 | Pruebas iniciales con un Process Analyst piloto (recomendaciones sobre procesos representativos) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (procesos / problemas representativos, revisión y adopción de KPIs/PPIs sugeridos) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: estimar el consumo con el AI Estimator de SAP antes del go-live.
- Los indicadores sugeridos son **recomendaciones**: deben validarse con stakeholders y conectarse con datos / event logs para que el marco de medición sea operativo.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/
- SAP Help Portal — Process Performance Indicators: https://help.sap.com/docs/signavio-process-insights/business-content-reference/process-performance-indicators

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |
