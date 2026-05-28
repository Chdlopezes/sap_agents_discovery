# Análisis caso de uso J1310 — Purchase Order Approvals Reminder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **Joule** en **SAP S/4HANA Cloud Public Edition** que ayuda a dar seguimiento a aprobaciones de órdenes de compra, identificar aprobadores y enviar recordatorios automatizados dentro del flujo de procurement. El valor se centra en reducir retrasos en aprobaciones y disminuir el seguimiento manual.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM – Procurement / Purchase Order Workflow** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Operational Procurement / Purchase Order Approval** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori del área **Procurement** (*Manage Purchase Orders*, *My Inbox* / *Manage Workflows*).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.
- Workflow de aprobación de órdenes de compra configurado.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de aprobadores y matriz de responsables definidos en el workflow.
- Órdenes de compra existentes con aprobaciones pendientes para validar la capability.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: Procurement Specialist / Approver con permisos sobre el workflow de aprobación.

> **Setup oficial SAP**: la página https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders sirve como referencia general de Joule capabilities en procurement. La configuración base de Joule debe estar completada antes de habilitar la capability.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Validar configuración base del **workflow de aprobación** de órdenes de compra (responsables, reglas) | Workflow PO Approval | Particular (por escenario / org) | Consultor MM / Procurement | 3 |
| 3 | Asignar a los usuarios objetivo los business roles de Procurement con la capability de Joule habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar la capability *Purchase Order Approvals Reminder* en Joule | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales con un usuario piloto (consultar aprobaciones pendientes, enviar recordatorios) | Configuración funcional MM | General | Consultor MM / Procurement | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (aprobaciones pendientes representativas y recordatorios end-to-end) | Consultor MM / Procurement | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación) | Consultor MM / Procurement | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor MM / Procurement | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **complementa el workflow de aprobación**, no lo reemplaza: si el workflow está mal configurado, los recordatorios irán al destinatario incorrecto.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Considerar **buenas prácticas de comunicación** (frecuencia de recordatorios) para evitar fatiga de notificaciones.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/
- SAP Help Portal — Joule Capabilities Guide (Procurement): https://help.sap.com/docs/joule/capabilities-guide/updating-delivery-dates-for-purchase-orders

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
