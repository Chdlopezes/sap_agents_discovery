# Análisis caso de uso J934 — Smart Personalization of My Home for Applications

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a **My Home**. SAP indica una **reducción del 33%** del costo de personalizar la página inicial.

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
- IAM app **SAP Business AI - My Home - Smart App Finder (F8818_TRAN)** o el catálogo equivalente, asignada a los usuarios objetivo.
- Catálogo de apps Fiori del cliente con metadatos suficientes para que la búsqueda en lenguaje natural funcione correctamente.

### 1.5 Datos maestros / transaccionales previos
- No aplica un dato transaccional específico; la capability opera sobre el catálogo de apps.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de Joule soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario verá únicamente apps a las que tiene autorización (Joule respeta las autorizaciones).

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html describe el procedimiento: verificar la IAM app en *Display IAM Apps*, asignarla al rol de negocio en *Maintain Business Roles* y habilitar el acceso para los usuarios.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule Premium y AI Units en SAP BTP | Subaccount BTP + entitlement Joule Premium for FM | General | Consultor BTP | 2 |
| 2 | Aprovisionar paquete Premium y asignar AI Units al tenant | Joule Premium for Financial Management + AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Verificar la disponibilidad de la **IAM app F8818_TRAN** en *Display IAM Apps* | IAM App F8818_TRAN | General | Consultor Funcional S/4HANA | 1 |
| 4 | Asignar la IAM app **F8818_TRAN** (o catálogo equivalente) a los business roles objetivo en *Maintain Business Roles* | Business Role / Business Catalog | Particular (por rol / grupo) | Consultor Seguridad S/4HANA | 3 |
| 5 | Pruebas iniciales con un usuario piloto (*Add Content* en My Home → búsqueda en lenguaje natural de apps, revisar resultados y agregarlos) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con usuarios reales (varios perfiles / módulos, búsqueda y adición de apps representativas) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- Joule respeta las autorizaciones del usuario: las búsquedas devuelven **únicamente apps a las que el usuario tiene acceso**.
- La calidad de las recomendaciones depende de la **consistencia del catálogo de apps** y de sus metadatos.
- Sujeto a la **fair-use policy** de Joule y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- SAP Help Portal — Smart Personalization of My Home: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |
