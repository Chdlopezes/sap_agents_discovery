# Análisis caso de uso J346 — Note Corrections for Project Billing

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** La función **Smart Notes** en *Manage Project Billing* propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura. SAP indica una **reducción del 50%** del tiempo dedicado a correcciones de notas en postings de Time & Expenses.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **Project Billing / Project Financial Control** operativo (uso de *Manage Project Billing*).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- Scope items de **Project Billing / Project Financial Control** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Project Billing** habilitada para los usuarios objetivo.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Proyectos, ítems de Time & Expenses con notas y *project billing requests* abiertos.
- Configuración funcional de Project Billing completada.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: las propuestas de corrección se generan según el modelo subyacente **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener el rol de **Billing Specialist** con acceso a Manage Project Billing.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html describe la configuración de Smart Notes para Project Billing. El procedimiento involucra asignar roles y validar disponibilidad de Smart Notes en *Manage Project Billing*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Asignar a los usuarios objetivo el business role de Billing Specialist con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Validar disponibilidad de Smart Notes dentro de *Manage Project Billing* | Configuración funcional Project Billing | General | Consultor Funcional Project Billing | 2 |
| 5 | Pruebas iniciales con un Billing Specialist piloto (revisión de propuestas de corrección sobre ítems representativos) | Configuración funcional Project Billing | General | Consultor Funcional Project Billing | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (correcciones sobre ítems representativos de varios proyectos) | Consultor Funcional Project Billing | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de revisión de notas) | Consultor Funcional Project Billing | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Project Billing | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- La propuesta es **una sugerencia**: el Billing Specialist debe revisar, editar o descartar cada cambio antes de emitir la factura.
- Considerar el impacto en **cobranza y satisfacción del cliente**: notas claras reducen disputas en factura.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/
- SAP Help Portal — Smart Notes for Project Billing: https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
