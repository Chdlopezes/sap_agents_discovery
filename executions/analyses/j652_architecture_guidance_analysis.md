# Análisis caso de uso J652 — Architecture Guidance

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP LeanIX** que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial. SAP no publica un KPI cuantitativo específico en la página consultada; el valor se centra en acelerar la identificación de oportunidades de mejora.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente con inventario de aplicaciones y landscape de TI cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** incluidos para nuevos clientes; clientes anteriores deben confirmar términos con su representante SAP.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con módulos de Enterprise Architecture activos.
- Workspace LeanIX configurado con suficiente nivel de detalle para que las recomendaciones sean significativas.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de aplicaciones, componentes técnicos, capacidades de negocio y relaciones en LeanIX.
- Atributos clave (lifecycle, ownership, business criticality) consistentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: Enterprise Architect / EA Admin con acceso a AI Capabilities.
- **Contractuales**: SAP AI terms firmados.

> **Nota**: SAP Discovery Center no publica un enlace de Initial Setup específico para este caso accesible desde la información consultada; aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar con representante SAP que los términos de IA de LeanIX están firmados | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asegurar la calidad mínima del inventario LeanIX (atributos, lifecycle, ownership) | Workspace LeanIX — Inventario | Particular (por dominio / aplicación) | Consultor SAP LeanIX + Enterprise Architect | 4 |
| 4 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Architecture Guidance | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Enterprise Architect piloto (revisión de insights y pasos accionables sugeridos) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con inventario real del cliente (revisión de insights sobre dominios representativos) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación EA) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo de Enterprise Architecture (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad de los insights depende **directamente de la calidad del inventario**: workspaces poco mantenidos producen recomendaciones poco relevantes.
- Las recomendaciones son **apoyo a la decisión** del Enterprise Architect; no reemplazan el análisis humano del contexto del negocio.
- Validar la **gobernanza** sobre quién ejecuta las acciones recomendadas: la capability sugiere, no aprueba ni implementa.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
