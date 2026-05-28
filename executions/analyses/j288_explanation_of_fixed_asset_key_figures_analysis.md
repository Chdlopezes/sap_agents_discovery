# Análisis caso de uso J288 — Explanation of Fixed Asset Key Figures

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones en lenguaje natural de cálculos complejos. SAP indica una **reducción de hasta 75%** en el esfuerzo para analizar valores de activos y responder preguntas de usuarios. La funcionalidad se accede desde la sección *Value Display* de la app *Manage Fixed Assets*.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **Asset Accounting (FI-AA)** operativo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- Scope items de **Asset Accounting** en S/4HANA Cloud Public Edition — **[verificar IDs en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Manage Fixed Assets** habilitada para los usuarios objetivo (la funcionalidad se usa desde la sección *Value Display*).
- **Joule** habilitado en el SAP Fiori Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de activos fijos cargado y consistente.
- Áreas de valoración, claves de depreciación y movimientos de valor cargados.
- Periodos contables abiertos / cerrados según necesidad de análisis.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización sobre el activo fijo cuyas key figures pretende explicar.

> **Setup oficial SAP**: la página de SAP Help Portal corresponde a *AI-Generated Explanation of Key Figures* (https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/ee5966f4b7f640ac8edbe3aa26bcc47b.html). El contenido disponible indica el uso en la sección *Value Display* de la app *Manage Fixed Assets*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP / Cockpit | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar configuración de Asset Accounting (áreas de valoración, claves, movimientos) | Configuración FI-AA | General | Consultor Funcional Asset Accounting | 3 |
| 4 | Asignar a los usuarios objetivo los business roles de Asset Accountant con la capability habilitada | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Habilitar la capability de Joule para *Explanation of Key Figures* en *Manage Fixed Assets* | Joule capability scope | General | Consultor Funcional Asset Accounting + Joule | 2 |
| 6 | Pruebas iniciales en Quality (consultas sobre key figures representativas en Value Display) | Configuración funcional FI-AA | General | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre key figures de activos representativos) | Consultor Funcional Asset Accounting | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional Asset Accounting | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional Asset Accounting | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de la interpretación contable y de la decisión.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/ee5966f4b7f640ac8edbe3aa26bcc47b.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |
