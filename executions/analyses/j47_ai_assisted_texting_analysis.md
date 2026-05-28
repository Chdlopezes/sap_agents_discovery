# Análisis caso de uso J47 — AI-Assisted Texting

> Análisis basado en información públicamente documentada por SAP (SAP LeanIX Help, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que permite crear o mejorar textos analizando contenido y contexto, con opciones para reescribir o resumir información existente (p. ej. generar descripciones para fact sheets). SAP indica hasta un **80% de reducción** en el tiempo para completar descripciones de aplicaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo con fact sheets que se vayan a usar.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** — incluida según el contrato comercial vigente.
- **SAP AI terms** incluidos para nuevos clientes; clientes anteriores deben confirmar con su representante SAP si los términos de IA están firmados.

### 1.3 Scope item relacionado
- No aplica scope item (SAP LeanIX no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con fact sheets / atributos donde se vaya a usar la asistencia textual.
- Roles administrativos LeanIX para activar AI Capabilities **[verificar permisos exactos]**.

### 1.5 Datos maestros / transaccionales previos
- Fact sheets del workspace con suficiente contenido para reformular/resumir.
- Configuración del metamodelo LeanIX vigente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: el usuario debe tener permisos para crear/editar contenido textual en LeanIX.
- **Contractuales**: SAP AI terms firmados.

> **Setup oficial SAP**: la página `https://help.sap.com/docs/leanix/ea/ai-capabilities` identifica la activación de AI Capabilities para SAP LeanIX. El extracto disponible no expone el procedimiento completo paso a paso.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar con representante SAP que los términos de IA de LeanIX están firmados (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asignar a los usuarios objetivo los roles LeanIX con acceso a la funcionalidad de texto asistido | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 4 | Pruebas iniciales con un usuario piloto (reescribir / resumir descripciones de fact sheets) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con contenido real del cliente (descripciones, reescritura, resumen sobre fact sheets representativos) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La habilitación depende de **términos contractuales de IA**: validar antes de planificar la activación.
- Los textos generados deben ser **revisados** por el responsable funcional antes de publicarse: la IA asiste, no reemplaza el control editorial.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
