# Análisis caso de uso J225 — Enterprise Search

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center, SAP Help Portal). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Búsqueda empresarial asistida por IA en **SAP S/4HANA Cloud Public Edition** que permite encontrar objetos de negocio mediante lenguaje natural desde el SAP Fiori Launchpad. SAP indica un ahorro estimado del **50% en el tiempo de búsqueda** de objetos de negocio.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **Enterprise Search** habilitado en S/4HANA Cloud Public Edition (índices de búsqueda activos).
- SAP Fiori Launchpad disponible para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule sobre S/4HANA Public **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No se identifica un scope item específico; aplica al motor transversal de Enterprise Search del producto base **[verificar en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Caja de búsqueda del **SAP Fiori Launchpad** activa para el usuario.
- Apps Fiori de los objetos de negocio que se desea buscar (los resultados navegan a las apps correspondientes).
- **Joule** habilitado en el Launchpad del usuario final.

### 1.5 Datos maestros / transaccionales previos
- Objetos de negocio (Business Partners, Materiales, Sales Orders, etc.) cargados y consistentes.
- Índices de Enterprise Search refrescados y operativos para los objetos a consultar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones de búsqueda en lenguaje natural soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Roles**: el usuario sólo verá resultados sobre objetos para los que tiene autorización.

> **Nota**: SAP no publica un Initial Setup específico para este caso en Discovery Center; aplican los prerequisitos generales de Joule + Enterprise Search sobre S/4HANA Cloud Public Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public Edition | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar que **Enterprise Search** esté habilitado y los índices estén operativos | Configuración de Enterprise Search | General | Consultor Funcional S/4HANA + Basis Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los business roles con autorización sobre los objetos a buscar | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 3 |
| 4 | Habilitar el botón / capability de Joule en el Launchpad de los usuarios | Joule capability scope | General | Consultor Funcional S/4HANA | 2 |
| 5 | Pruebas iniciales en Quality con un usuario piloto (consultas en lenguaje natural sobre objetos comunes) | Configuración funcional / Launchpad | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (búsquedas representativas sobre objetos clave del cliente) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Joule respeta las autorizaciones del usuario: **no eleva privilegios**. Los resultados se filtran según el perfil de seguridad.
- La calidad de la búsqueda depende del **estado de los índices de Enterprise Search**; si están desactualizados, los resultados serán incompletos.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y objetos soportados.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
