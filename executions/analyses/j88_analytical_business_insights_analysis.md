# Análisis caso de uso J88 — Analytical Business Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP AI Foundation Catalog, SAP Road Map Explorer). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente antes de la activación en cliente.

**Resumen del caso:** Panel lateral de IA generativa en *Cost Center Review Booklet* que permite analizar y resumir datos financieros en lenguaje natural y convertirlos en insights accionables. SAP publica beneficios de hasta **50% de reducción del tiempo** para analizar resúmenes y **65% para resumir y documentar** reportes de centros de costo.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente funcional **FI/CO – Cost Center Accounting** operativo en el tenant (app *Cost Center Review Booklet*).
- **SAP BTP** con Generative AI Hub disponible para el tenant del cliente.
- **Intelligent Scenario Lifecycle Management (ISLM)** activo (este caso usa la integración ISLM + Generative AI).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** **[verificar suscripción vigente en SAP Discovery Center]**.
- **AI Units** asignadas al tenant para consumo de la capability (precio bajo solicitud según *Pricing Details* publicado).

### 1.3 Scope item relacionado
- Scope item base de **Cost Center Accounting / Overhead Cost Accounting** en S/4HANA Cloud Public Edition — **[verificar el ID exacto del scope item asociado a J88 en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori **Cost Center Review Booklet** habilitada para los usuarios objetivo.
- Apps de **Intelligent Scenario Apps** disponibles para administradores ISLM.
- **Generative AI for ISLM** configurado.
- **Service Instance + Service Key de SAP BTP** creados con certificado descargado, según el procedimiento de Initial Setup publicado por SAP.
- **Joule** habilitado en el SAP Fiori Launchpad del usuario final.

### 1.5 Datos maestros / transaccionales previos
- Centros de costo, jerarquías y elementos de costo dados de alta y consistentes.
- Cargas reales/plan de Cost Center Accounting cerradas o vigentes para el periodo a analizar.
- Datos del periodo correctamente publicados en la app *Cost Center Review Booklet*.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: las interacciones de IA generativa de Joule se publican primariamente en **inglés** **[verificar matriz de idiomas vigente en SAP Help]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: usuario final debe tener el business role de Controlling con autorización sobre los centros de costo a analizar.
- **Disponibilidad regional**: sujeta a la región del tenant y a la disponibilidad regional del Generative AI Hub **[verificar]**.

> **Setup oficial SAP**: la página de SAP Help referencia configuración relacionada con *Intelligent Scenario Lifecycle Management*, acceso a *Intelligent Scenario Apps*, *Generative AI for ISLM*, descarga de certificado y creación de SAP BTP Service Instance and Key. Enlace: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP / Cockpit | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Crear **Service Instance + Service Key** de SAP BTP para Generative AI y descargar el certificado | BTP Service Instance/Key + certificado | General | Consultor BTP | 3 |
| 4 | Configurar **Generative AI for ISLM** en S/4HANA Cloud Public Edition | ISLM — Generative AI Configuration | General | Consultor BTP + Consultor Funcional Finanzas | 3 |
| 5 | Habilitar el **Intelligent Scenario** asociado a *Analytical Business Insights* (despliegue del modelo en ISLM) | Intelligent Scenario / ISLM | General | Consultor Funcional Finanzas | 3 |
| 6 | Asignar a los usuarios objetivo el business role de Controlling con catálogo de *Cost Center Review Booklet* y permisos sobre Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 7 | Pruebas iniciales en Quality con un usuario piloto (apertura del panel de Joule en Cost Center Review Booklet, consultas en lenguaje natural) | Configuración funcional FI/CO | General | Consultor Funcional Finanzas | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (resúmenes y análisis sobre centros de costo en entorno de Quality) | Consultor Funcional Finanzas | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración ISLM/BTP) | Consultor Funcional Finanzas | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A sobre uso del panel de Joule) | Consultor Funcional Finanzas | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium**: requiere el paquete **Joule Premium for Financial Management** y AI Units suficientes.
- La activación implica integrarse con **SAP BTP Generative AI Hub** vía ISLM — no es solo habilitar Joule en el Launchpad, es desplegar un escenario inteligente con certificado y service key.
- Joule responde sobre datos a los que el usuario ya tiene autorización; **no eleva privilegios**: validar la matriz de autorizaciones de Controlling antes del rollout.
- Sujeto a **fair-use policy** de Joule y a las cuotas de AI Units; revisar consumo durante el piloto para dimensionar el volumen anual **[verificar políticas vigentes]**.
- Las interacciones con Joule pueden almacenarse para **auditoría / trazabilidad**; revisar políticas de privacidad y data residency aplicables.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes de la wave vigente para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/f28304dcfa8c4104a137eb82c75c2ef2.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 11 |
| **Total** | **30** |
