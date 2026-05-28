# Análisis caso de uso J112 — Process Analyzer, Text to Insight

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio Process Intelligence** que permite consultar datos de procesos mediante lenguaje natural y obtener insights inmediatos. Posicionada como una forma de reducir el tiempo para descubrir insights clave de procesos y ampliar el acceso organizacional al process mining.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Intelligence** (suscripción activa).
- Datos de proceso cargados (event logs) en Process Intelligence.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio Process Intelligence — Process Analyzer**.

### 1.5 Datos maestros / transaccionales previos
- Event logs y modelos de proceso cargados y consistentes en Process Intelligence.
- Buenas prácticas de naming en variantes / actividades para mejorar la calidad de las preguntas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: consultas soportadas según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: Process Analyst con permisos sobre los process logs a consultar.

> **Setup oficial SAP**: la página https://help.sap.com/docs/signavio-process-transformation-suite/sap-signavio-process-transformation-suite-administration-guide/activate-embedded-ai-capabilities?version=1.0 documenta la activación de capacidades de IA embebidas en SAP Signavio Process Transformation Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Signavio Process Intelligence | Workspace Signavio + entitlement | General | Consultor SAP Signavio | 2 |
| 2 | Activar las capacidades de IA embebidas en la administración de Process Transformation Suite | Configuración Embedded AI | General | Consultor SAP Signavio | 2 |
| 3 | Verificar que los event logs y modelos de proceso estén cargados y consistentes | Process Intelligence — Datos | Particular (por proceso) | Consultor SAP Signavio | 3 |
| 4 | Asignar a los usuarios objetivo los roles Signavio con acceso a Process Analyzer | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 5 | Pruebas iniciales con un Process Analyst piloto (preguntas representativas) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios procesos / niveles de detalle) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + buenas prácticas de prompting) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de los insights depende **directamente de la calidad de los event logs** y de la nomenclatura de actividades.
- Definir **buenas prácticas de prompting** para que la organización aproveche la capability de manera consistente.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/
- SAP Help Portal — Activate Embedded AI Capabilities: https://help.sap.com/docs/signavio-process-transformation-suite/sap-signavio-process-transformation-suite-administration-guide/activate-embedded-ai-capabilities?version=1.0

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
