# Análisis caso de uso J967 — Transformation Advisory, Initiative Builder

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Signavio** que ayuda a identificar oportunidades de transformación alineadas con la estrategia y acelera la ejecución mediante la creación de iniciativas. Conecta estrategia y ejecución, facilitando que oportunidades de transformación se conviertan en planes concretos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio solutions** (suscripción activa).
- Acceso al módulo de Transformation Advisory / Process Transformation Manager dentro de SAP Signavio.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Signavio solutions**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Signavio** con el módulo Transformation Advisory habilitado.

### 1.5 Datos maestros / transaccionales previos
- Definición estratégica del cliente (objetivos, prioridades) cargada o accesible.
- Modelos de procesos relevantes en SAP Signavio.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Signavio **[verificar idiomas soportados vigentes]**.
- **Roles**: Transformation Lead / Strategist con permisos sobre el módulo de iniciativas.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de SAP Signavio.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Signavio Transformation Advisory | Workspace Signavio + entitlement | General | Consultor SAP Signavio | 2 |
| 2 | Habilitar el módulo Transformation Advisory en el workspace | Workspace Signavio — Transformation Advisory | General | Consultor SAP Signavio | 2 |
| 3 | Asignar a los usuarios objetivo los roles Signavio con acceso a Transformation Advisory | Roles SAP Signavio | Particular (por usuario / grupo) | Consultor Seguridad Signavio | 2 |
| 4 | Pruebas iniciales con un Transformation Lead piloto (generar iniciativas a partir de oportunidades representativas) | Configuración funcional Signavio | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales del cliente (iniciativas a partir de procesos representativos) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las iniciativas generadas son **borradores**: requieren revisión y priorización por parte del equipo de transformación.
- La utilidad depende de la **calidad y consistencia de la información estratégica y de procesos** disponible en SAP Signavio.
- Sujeto a las condiciones de servicio vigentes de SAP Signavio **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
