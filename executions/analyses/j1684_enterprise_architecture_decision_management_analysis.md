# Análisis caso de uso J1684 — Enterprise Architecture Decision Management

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que analiza y extrae datos relevantes para generar entradas de decisiones de arquitectura con el contexto e información que los stakeholders necesitan para aprobarlas.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente con inventario y landscape cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture / Decision Management activos.

### 1.5 Datos maestros / transaccionales previos
- Inventario de aplicaciones, capacidades de negocio y stakeholders cargados en LeanIX.
- Procesos formales de decisión de arquitectura definidos (qué se decide y quién aprueba).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: Enterprise Architect / EA Admin con permisos sobre decisiones y stakeholders.

> **Nota**: el recurso *Initial Setup* existe en la página de detalle, pero no fue posible extraer texto suficiente desde la herramienta para identificar prerequisitos concretos. Aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Configurar el módulo de **Decision Management** según los procesos del cliente (categorías de decisión, stakeholders, plantillas) | Decision Management — Configuración | Particular (por categoría de decisión) | Consultor SAP LeanIX + Enterprise Architect | 4 |
| 4 | Asignar a los usuarios objetivo los roles LeanIX con acceso a la capability | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Enterprise Architect piloto (generar entradas de decisión asistidas por IA) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con decisiones reales del cliente (varios tipos / dominios) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación EA) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo de Enterprise Architecture | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de las entradas generadas depende **directamente del inventario y datos contextuales** del workspace.
- Las decisiones siguen siendo **responsabilidad de los stakeholders aprobadores**: la IA prepara, los humanos deciden.
- Definir **gobernanza** del flujo: quién revisa, quién aprueba, quién publica.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
