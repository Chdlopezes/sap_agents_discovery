# Análisis caso de uso J178 — Inventory Builder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP LeanIX Inventory Builder** acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX. El valor se centra en reducir el esfuerzo manual para construir y mantener inventarios de arquitectura empresarial.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente disponible.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Premium** — activación con **AI Units** **[verificar volumen vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture activos.

### 1.5 Datos maestros / transaccionales previos
- Fuentes de datos a cargar / analizar (planillas, CMDB, exportaciones de otros sistemas) para que el builder pueda procesarlas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Formatos / volumen**: el contenido accesible no detalla límites técnicos exactos **[verificar]**.
- **Roles**: EA Admin / Workspace Admin con acceso a Inventory Builder.

> **Setup oficial SAP**: la página https://help.sap.com/docs/leanix/ea/ai-capabilities describe la activación de AI Capabilities en SAP LeanIX. El contenido completo del procedimiento específico de Inventory Builder no fue totalmente extractable.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Confirmar AI Units asignadas para Inventory Builder | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 4 | Preparar las fuentes de datos (formatos, calidad, mapeos) que va a procesar Inventory Builder | Fuentes de datos | Particular (por fuente) | Consultor SAP LeanIX + Cliente Funcional | 5 |
| 5 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Inventory Builder | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 6 | Pruebas iniciales con datos representativos (cargas controladas y validación de resultados) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (varios formatos / dominios) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Los datos cargados deben pasar por **revisión humana** antes de promoverse a producción: la IA acelera, no reemplaza el control de calidad de datos.
- Considerar **gobernanza** sobre qué fuentes de datos están autorizadas a ingresar al workspace.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 11 |
| **Total** | **28** |
