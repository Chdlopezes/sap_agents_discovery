# Análisis caso de uso J45 — Inventory Prompts

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP LeanIX Inventory Prompts** combina la información del inventario LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial mediante una interfaz de lenguaje natural. SAP indica **90% de reducción** del tiempo para generar insights de artefactos del landscape de TI.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo con inventario cargado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con AI Capabilities habilitadas e *Inventory AI prompts* disponible.

### 1.5 Datos maestros / transaccionales previos
- Inventario LeanIX poblado con datos suficientes (aplicaciones, capacidades, relaciones) para que las consultas devuelvan resultados significativos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP LeanIX **[verificar idiomas soportados vigentes]**.
- **Roles**: usuario LeanIX con permisos sobre el dominio que va a consultar.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/leanix/ea/ai-capabilities menciona capacidades base de IA, incluyendo Inventory AI prompts. El contenido completo del procedimiento no fue totalmente extractable.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX (incluyendo Inventory AI prompts) | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Asignar a los usuarios objetivo los roles LeanIX con acceso a Inventory Prompts | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 4 | Pruebas iniciales con un usuario piloto (consultas de inventario representativas) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios dominios / niveles de detalle) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad depende **directamente de la calidad y cobertura del inventario** en LeanIX.
- Joule / LeanIX respetan las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** para que la organización aproveche la capability de manera consistente.
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/
- SAP Help Portal — AI Capabilities (LeanIX): https://help.sap.com/docs/leanix/ea/ai-capabilities

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
