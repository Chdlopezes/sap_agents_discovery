# Análisis caso de uso J147 — Script Optimization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Integration Suite** que ayuda a optimizar scripts personalizados en Cloud Integration. SAP indica que la función está disponible como **promoción gratuita hasta septiembre de 2026** y posteriormente pasará a ser una función **Premium**.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (suscripción activa).
- **Cloud Integration** dentro de SAP Integration Suite con iFlows que contengan scripts personalizados.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Integration Suite**.
- Capability **Base** **hasta septiembre de 2026** (promoción gratuita); posteriormente pasa a **Premium** **[verificar fecha exacta de transición vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Integration Suite — Cloud Integration** con capacidades de IA habilitadas.

### 1.5 Datos maestros / transaccionales previos
- iFlows del cliente con scripts personalizados (Groovy / JavaScript) a optimizar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Lenguajes soportados**: principalmente Groovy y JavaScript según lo permitido por Cloud Integration **[verificar matriz vigente]**.
- **Roles**: Integration Developer con acceso a Cloud Integration y a artefactos de integración.

> **Setup oficial SAP**: la página https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence describe las capacidades de IA disponibles en SAP Integration Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Integration Suite con Cloud Integration | Subaccount BTP + entitlement Integration Suite | General | Consultor BTP | 2 |
| 2 | Habilitar / validar las capacidades de IA en SAP Integration Suite | Configuración Integration Suite — AI | General | Consultor Integration Suite | 2 |
| 3 | Asignar a los developers los roles con acceso a la capability | Roles SAP Integration Suite | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer piloto (optimizar scripts representativos) | Configuración funcional Integration Suite | General | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con scripts reales del cliente (revisión de recomendaciones y validación de comportamiento del iFlow tras los cambios) | Consultor Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de scripting) | Consultor Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica) | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Después de **septiembre de 2026** la función deja de ser gratuita: **planificar el modelo de costos** para uso continuo bajo el esquema Premium.
- Las recomendaciones son **sugerencias**: el developer debe revisar cada cambio antes de aplicarlo a un iFlow productivo.
- Definir un **proceso de control** sobre cuándo y quién aplica optimizaciones a iFlows productivos.
- Sujeto a las condiciones de servicio vigentes de SAP Integration Suite **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/
- SAP Help Portal — Artificial Intelligence in Integration Suite: https://help.sap.com/docs/integration-suite/sap-integration-suite/artificial-intelligence

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
