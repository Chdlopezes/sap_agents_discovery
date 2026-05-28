# Análisis caso de uso J117 — Form Extension in Localization as a Self-Service

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Genera y actualiza automáticamente formularios localizados personalizados según requisitos de negocio, enlaza fuentes de datos y carga los formularios en SAP S/4HANA Cloud Public Edition. SAP indica: *Reducción estimada del 80% en tiempo y costo para crear plantillas de formularios localizados.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Framework de **Form Templates / Localization Toolkit** activo en el tenant.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción a S/4HANA Public Edition.
- Entitlement de Joule; capability **Base** **[verificar en AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- Scope items de localización del país objetivo (output management / forms) — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori *Maintain Form Templates* (o equivalente vigente).
- Output Management / Form determination configurado.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Form templates base por país disponibles y activos.
- Procesos de output que consuman dichos formularios.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- País/localización debe estar soportado por el set de templates vigente.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración de Output Management / Form Templates | Output Management / Forms | General | Consultor Funcional Output | 3 |
| 3 | Asignar business roles con catálogos de Form Templates a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar la capability de Joule para extensión de formularios | Joule capability scope | General | Consultor Funcional + Joule | 2 |
| 5 | Pruebas: extender un template por localización con prompt + validar render del documento | Configuración funcional Output | General | Consultor Funcional | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con templates reales del cliente | Consultor Funcional Output | 4 |
| 2 | Documentación para el cliente | Consultor Funcional Output | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional Output | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Es un **self-service**: el usuario clave (no desarrollador) extiende localizaciones sin código.
- Joule respeta los límites técnicos del framework de Forms; cambios estructurales fuertes pueden requerir extensión clásica.
- Revisar la lista de **localizaciones soportadas** en SAP Help antes del rollout.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
