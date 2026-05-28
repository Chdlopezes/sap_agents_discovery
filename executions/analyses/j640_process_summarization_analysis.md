# Análisis caso de uso J640 — Process Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que genera resúmenes en lenguaje natural de procesos o artefactos complejos para facilitar comprensión, revisión y transferencia de conocimiento. El valor está en mayor productividad en diseño/implementación low-code y menor esfuerzo de revisión y documentación.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Acceso al entorno con artefactos de proceso o automatizaciones existentes.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con capacidad de generative AI habilitada.

### 1.5 Datos maestros / transaccionales previos
- Procesos / automatizaciones ya modelados en SAP Build Process Automation.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Build Process Automation **[verificar idiomas soportados vigentes]**.
- **Roles**: Developer / Process Owner con permisos sobre los artefactos.

> **Setup oficial SAP**: el enlace https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup describe el Initial Setup general de SAP Build Process Automation. Las capacidades de generative AI se habilitan dentro de ese entorno.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidades de IA generativa | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Validar / habilitar las capacidades de generative AI en el subaccount | Configuración Build Process Automation — Generative AI | General | Consultor BTP / Build | 2 |
| 3 | Asignar a los usuarios objetivo los roles con acceso a la capability | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer / process owner piloto (resúmenes sobre procesos representativos) | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con artefactos reales del cliente (resúmenes sobre procesos representativos) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Los resúmenes son **descriptivos**: el usuario sigue siendo responsable de validar que el resumen represente correctamente el proceso.
- Útil en **handovers, revisiones funcionales y documentación**: definir gobernanza sobre cuándo el resumen reemplaza documentación formal.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/initial-setup

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
