# Análisis caso de uso J91 — Easy Filter

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP S/4HANA Cloud Public Edition** que optimiza la experiencia de filtrado en reportes de lista basados en **SAP Fiori elements** mediante lenguaje natural. SAP indica un ahorro estimado del **83% del tiempo** al filtrar reportes de lista.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition**.
- Reportes de lista basados en **SAP Fiori elements** habilitados para los usuarios objetivo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP S/4HANA Cloud Public Edition**.
- Capability **Base** — incluida con el entitlement estándar de Joule **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; la capacidad opera transversalmente sobre los reportes Fiori elements.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Fiori Launchpad** del sistema SAP S/4HANA Cloud Public Edition.
- Apps Fiori elements (list reports) habilitadas en los catálogos de los usuarios.

### 1.5 Datos maestros / transaccionales previos
- Datos transaccionales del módulo objetivo disponibles para filtrar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: el filtrado por lenguaje natural está disponible principalmente en **inglés** **[verificar matriz vigente]**.
- **Edición**: aplica únicamente a **SAP S/4HANA Cloud Public Edition**.
- **Tipo de reporte**: solo aplica a **list reports basados en SAP Fiori elements**.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html describe la habilitación de *AI-Assisted Easy Filter*. La activación se realiza por un administrador del SAP Fiori Launchpad del sistema S/4HANA Cloud Public Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Iniciar sesión como administrador en el SAP Fiori Launchpad del sistema S/4HANA Cloud Public Edition | Acceso administrativo | General | Consultor S/4HANA + Cliente Admin | 1 |
| 2 | Habilitar **AI-Assisted Easy Filter** según el procedimiento de la página de SAP Help | Configuración Easy Filter | General | Consultor Funcional S/4HANA | 2 |
| 3 | Asignar a los usuarios objetivo los business roles / catálogos donde se usarán los list reports | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad S/4HANA | 2 |
| 4 | Pruebas iniciales con un usuario piloto (filtrar list reports representativos por lenguaje natural) | Configuración funcional S/4HANA | General | Consultor Funcional S/4HANA | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~7 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con list reports reales del cliente (filtros representativos sobre varios módulos) | Consultor Funcional S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor Funcional S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Funcional S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La capability **funciona solo sobre list reports basados en SAP Fiori elements**: validar la cobertura sobre las apps clave del cliente.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** para que los usuarios aprovechen la capability de manera consistente.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/
- SAP Help Portal — Easy Filter Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/e3410abd11404d87b319cb2d63a50a92.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 7 |
| Validación + documentación + KT | 11 |
| **Total** | **18** |
