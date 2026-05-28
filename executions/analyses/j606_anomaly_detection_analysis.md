# Análisis caso de uso J606 — Anomaly Detection

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Integration Suite** que identifica patrones inusuales o desviaciones en el tráfico de APIs mediante IA, apoyando la detección temprana de anomalías. SAP indica reducción del **costo de resolución de anomalías** de API.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (suscripción activa).
- **API Management** habilitado dentro de SAP Integration Suite.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Integration Suite**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Integration Suite — API Management** con las APIs candidatas publicadas y monitoreadas.

### 1.5 Datos maestros / transaccionales previos
- **APIs publicadas en API Management** con historia de tráfico suficiente para entrenar y aplicar el modelo de anomalías.
- Logs de runtime / métricas de tráfico capturados por API Management.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (la capability trabaja sobre métricas técnicas, no diálogo).
- **Volumen de datos**: requiere historia suficiente; APIs con bajo volumen pueden producir detecciones poco significativas.
- **Roles**: API Admin / API Owner con permisos en Integration Suite.

> **Setup oficial SAP**: el procedimiento es *Configuring APIs for Anomaly Detection* en https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-apis-for-anomaly-detection. La documentación remite a los prerrequisitos de selección de APIs y a habilitar la detección desde Integration Suite.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Integration Suite con API Management activo | Subaccount BTP + entitlement Integration Suite | General | Consultor BTP | 2 |
| 2 | Identificar el conjunto de APIs candidatas con historia de tráfico suficiente | API Management — Catálogo de APIs | Particular (por API) | Consultor Integration Suite | 3 |
| 3 | Habilitar Anomaly Detection sobre las APIs seleccionadas | API Management — Anomaly Detection | Particular (por API seleccionada) | Consultor Integration Suite | 3 |
| 4 | Asignar a los usuarios objetivo los roles con visibilidad de la detección | Roles SAP Integration Suite | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 5 | Pruebas iniciales (monitorear detecciones durante un periodo de observación inicial en Quality / Producción) | Configuración funcional Integration Suite | General | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con tráfico real (provocar anomalías controladas en APIs no críticas y validar detección) | Consultor Integration Suite | 4 |
| 2 | Documentación de la activación para el cliente (manual de operación y respuesta a anomalías) | Consultor Integration Suite | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión de respuesta a incidentes) | Consultor Integration Suite | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La detección depende de **volumen y calidad del tráfico histórico**: APIs nuevas o con bajo tráfico pueden producir falsos positivos / negativos.
- Definir **procesos de respuesta** a anomalías antes del rollout (qué hace el equipo cuando se detecta una desviación).
- Sujeto a las condiciones de servicio vigentes de SAP Integration Suite **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/
- SAP Help Portal — Configuring APIs for Anomaly Detection: https://help.sap.com/docs/integration-suite/sap-integration-suite/enabling-apis-for-anomaly-detection

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
