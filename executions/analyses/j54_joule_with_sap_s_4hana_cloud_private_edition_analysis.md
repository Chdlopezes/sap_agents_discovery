# Análisis caso de uso J54 — Joule with SAP S/4HANA Cloud Private Edition

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Caso "paraguas" que habilita Joule como copilot sobre S/4HANA Cloud Private Edition. Es prerequisito de muchas otras capabilities Joule sobre Private.

**Resumen del caso:** Permite usar lenguaje natural para expresar requerimientos de negocio y acceder a capacidades informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Private Edition. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se centra en productividad, navegación y ejecución de tareas en SAP S/4HANA Cloud Private Edition.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** en release con soporte de Joule **[verificar release mínima vigente]**.
- **SAP Business Technology Platform (BTP)** con tenant en región soportada.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition vigente.
- Entitlement de Joule activado en BTP (capability Base; Premium con addon).

### 1.3 Scope item relacionado
- Scope item de habilitación de Joule sobre S/4HANA Private — **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Launchpad con panel de Joule visible.
- Communication arrangement S/4HANA Private ↔ servicio de Joule en BTP (escenario **SAP_COM_xxxx** — **[verificar]**).
- Identity provider (IAS / corporate IdP) configurado.

### 1.5 Datos maestros / transaccionales previos
- SSO operativo entre S/4HANA Private y BTP.
- Business roles y catálogos asignados a usuarios.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar matriz]**.
- Disponibilidad regional sujeta a tenant.
- Joule respeta autorizaciones del usuario.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar entitlement Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar identity propagation IAS / IdP ↔ S/4HANA Private | Trust / SSO | General | Consultor Basis / Seguridad | 4 |
| 3 | Activar communication scenario de Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Habilitar el panel Joule en el launchpad | Launchpad configuration | Particular (por spaces & pages) | Consultor S/4HANA Private | 4 |
| 5 | Asignar business roles con catálogos Joule | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 4 |
| 6 | Pruebas iniciales end-to-end | Configuración base | General | Consultor Funcional | 4 |

**Esfuerzo total estimado (activación): ~22 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos por área | Consultor Funcional + key user | 6 |
| 2 | Documentación para el cliente | Consultor Funcional | 5 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 4 |

**Esfuerzo total estimado (validación + entrega): ~15 horas.**

---

## 4. Consideraciones especiales

- **Habilitador transversal** Private: una vez activo, demás capabilities Joule sobre Private requieren típicamente solo enablement adicional.
- En Private aplican consideraciones de upgrade compatibility con la versión del stack ABAP del cliente.
- Trazabilidad / fair-use / cuotas — revisar políticas vigentes.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 22 |
| Validación + documentación + KT | 15 |
| **Total** | **37** |
