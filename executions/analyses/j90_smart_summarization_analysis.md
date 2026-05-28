# Análisis caso de uso J90 — Smart Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que permite resumir contenido de **object pages basadas en SAP Fiori elements** y generar propuestas de texto para comunicaciones o seguimientos. SAP indica un ahorro estimado del **88% del tiempo** al resumir páginas de objeto.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Apps Fiori elements con **object pages** habilitadas para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item específico; la capability opera transversalmente sobre object pages Fiori elements.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad** del sistema S/4HANA Cloud Public Edition.
- IAM app **SAP Business AI - User Interface Features - Smart Summarization (F7924_SUM_TRAN)** o catálogo equivalente, disponible y asignada al rol de negocio.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales y maestros suficientes en las object pages a resumir.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idiomas**: capability soporta múltiples idiomas para los resúmenes generados **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Tipo de página**: solo aplica a **object pages basadas en SAP Fiori elements**.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html describe el procedimiento: verificar la IAM app **F7924_SUM_TRAN** en *Display IAM Apps* y asignarla al rol de negocio en *Maintain Business Roles*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar la disponibilidad de la **IAM app F7924_SUM_TRAN** en *Display IAM Apps* | IAM App F7924_SUM_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 3 | Asignar la IAM app **F7924_SUM_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Pruebas iniciales con un usuario piloto (abrir object pages representativas, usar *Summarize*, revisar resúmenes en distintos idiomas) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con object pages reales del cliente (varios módulos / idiomas representativos) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **funciona solo sobre object pages basadas en SAP Fiori elements**: validar cobertura sobre las apps clave del cliente.
- Los resúmenes generados deben ser **revisados / editados por el usuario** antes de enviarse por correo o chat — sobre todo en comunicaciones formales.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y tipos de object pages soportados.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/
- SAP Help Portal — Smart Summarization Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/4a69b2cc611a40c4bf5afb42fa016e0e.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
