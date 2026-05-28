# Análisis caso de uso J226 — Smart Personalization of My Home

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que permite personalizar **My Home** agregando **insights cards** mediante lenguaje natural. SAP indica un ahorro estimado del **50% del tiempo** para agregar insights cards a My Home.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Página **My Home** del SAP Fiori Launchpad disponible para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Premium** — requiere el paquete **Joule Premium for Financial Management** (no se vende por separado).
- **AI Units** asignadas al tenant para consumo de la capability **[verificar volumen vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item específico; la capability opera sobre My Home / Fiori Launchpad.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad — My Home**.
- IAM app **SAP Business AI - User Interface Features - Smart Personalization (F8555_TRAN)** o el catálogo equivalente, asignada a los usuarios objetivo.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales disponibles en los módulos sobre los que se generan las insights cards (cuanto más datos relevantes haya, mejores serán las tarjetas propuestas).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario debe tener autorización a las apps cuya información se mostrará en las insights cards (Joule respeta las autorizaciones).

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html describe el procedimiento: abrir *Maintain Business Roles*, asignar la **IAM app F8555_TRAN** al rol de negocio y dejar la capacidad habilitada para los usuarios. Los usuarios pueden usar *Add Content* en My Home → *Insights Cards*.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar la disponibilidad de la **IAM app F8555_TRAN** en *Display IAM Apps* | IAM App F8555_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 4 | Asignar la IAM app **F8555_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales con un usuario piloto (*Add Content* → *Insights Cards*, consulta en lenguaje natural, generar / previsualizar / agregar tarjeta) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con usuarios reales (varios perfiles / módulos, tarjetas representativas) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Joule respeta las autorizaciones del usuario: las **insights cards no exponen datos a los que el usuario no tiene acceso**.
- Definir **buenas prácticas de prompting** para acelerar la adopción.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/
- SAP Help Portal — Smart Personalization of My Home: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |
