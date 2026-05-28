# Análisis caso de uso J74 — Joule with SAP S/4HANA Cloud Public Edition

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Este es el caso de uso "paraguas" que habilita Joule como copilot transversal sobre S/4HANA Public Edition. Es prerequisito de muchas otras capabilities Joule sobre S/4HANA Public.

**Resumen del caso:** Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se concentra en rapidez de acceso a datos, reducción de pasos manuales y productividad del usuario.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** (release con soporte de Joule — **[verificar release mínima vigente]**).
- **SAP Business Technology Platform (BTP)** con tenant en la misma región (o región soportada).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition vigente.
- Entitlement de **Joule** activado en BTP (capability **Base** incluida; capabilities **Premium** requieren addon).

### 1.3 Scope item relacionado
- Scope item de **habilitación de Joule** sobre S/4HANA Public — **[verificar ID en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Configuración del **launchpad** con el panel de Joule visible.
- Communication arrangement entre S/4HANA Public y el servicio de Joule en BTP (escenario **SAP_COM_xxxx** — **[verificar ID vigente]**).
- Identity provider configurado (SAP IAS / corporate IdP).

### 1.5 Datos maestros / transaccionales previos
- Mapeo de usuarios entre S/4HANA y BTP (single sign-on funcional).
- Roles y catálogos asignados a usuarios target.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: soporte primario inglés; otros idiomas en GA limitada **[verificar matriz]**.
- Disponibilidad regional sujeta a la región del tenant.
- Joule respeta autorizaciones del usuario.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement de Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar identity propagation (IAS / IdP) entre S/4HANA Public y BTP | Trust configuration / SSO | General | Consultor Basis / Seguridad | 4 |
| 3 | Activar el communication scenario de Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Habilitar el panel Joule en el launchpad de los usuarios objetivo | Launchpad configuration | Particular (por usuario / spaces & pages) | Consultor S/4HANA | 4 |
| 5 | Asignar business roles con catálogos Joule a usuarios target | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 4 |
| 6 | Pruebas iniciales end-to-end (consultas informacionales, navegacionales y transaccionales) | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~22 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos por área (Finance, SCM, Sales, HR, etc.) | Consultor Funcional + key user | 6 |
| 2 | Documentación para el cliente (manual usuario + guía de configuración + lista de prompts soportados) | Consultor Funcional | 5 |
| 3 | Transferencia de conocimiento y enablement a usuarios clave | Consultor Funcional | 4 |

**Esfuerzo total estimado (validación + entrega): ~15 horas.**

---

## 4. Consideraciones especiales

- **Habilitador transversal**: una vez activo, las demás capabilities Joule sobre S/4HANA Public requieren típicamente sólo enablement adicional, no el setup completo.
- **Trazabilidad / auditoría**: interacciones pueden almacenarse según política — revisar acuerdos de procesamiento.
- **Fair use / cuotas**: revisar políticas vigentes.
- **Releases**: nuevas capabilities por wave — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 22 |
| Validación + documentación + KT | 15 |
| **Total** | **37** |
