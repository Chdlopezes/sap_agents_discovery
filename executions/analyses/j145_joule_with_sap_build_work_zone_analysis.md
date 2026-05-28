# Análisis caso de uso J145 — Joule with SAP Build Work Zone

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo. También soporta acceso remoto mediante SAP Mobile Start o sitio móvil. SAP indica: *50% más rapidez en búsquedas informativas; 59% más rapidez en ejecución de tareas de navegación y transaccionales; mayor satisfacción del usuario de negocio.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Work Zone** (standard edition o advanced) en BTP.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Build Work Zone.
- Entitlement Joule + capability Work Zone **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant Work Zone configurado.
- Joule habilitado dentro de Work Zone.

### 1.5 Datos maestros / transaccionales previos
- Aplicaciones integradas en Work Zone con sus destinations/roles.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Catálogo de apps con soporte Joule.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Work Zone + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en Work Zone | Work Zone settings | General | Consultor Work Zone | 3 |
| 4 | Asignar roles a usuarios | Roles | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (interactuar con apps vía Joule en Work Zone) | Configuración Work Zone | General | Consultor Work Zone | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Work Zone | 4 |
| 2 | Documentación para el cliente | Consultor Work Zone | 4 |
| 3 | Transferencia de conocimiento | Consultor Work Zone | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Cobertura de apps con soporte Joule se amplía por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |
