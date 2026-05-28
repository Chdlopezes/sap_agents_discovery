# Análisis caso de uso J146 — SAP Joule for Consultants

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud. Está orientado a consultores y equipos de implementación que necesitan acceso guiado a conocimiento, recomendaciones y soporte durante actividades de delivery. SAP indica: *La página posiciona el valor en acelerar la entrega de proyectos SAP, mejorar la productividad del equipo consultor y facilitar el acceso a conocimiento SAP relevante durante transformaciones cloud.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP con capability "for Consultants" **[verificar]**.
- Integración con **SAP Learning** / **SAP Help** / **Cloud ALM** según las funciones cubiertas.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule for Consultants (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible para consultores.

### 1.5 Datos maestros / transaccionales previos
- Cuenta consultor con accesos requeridos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule for Consultants | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO con identidad corporativa | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Asignar acceso a consultores | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Pruebas iniciales (consultas sobre best practices, soluciones) | Configuración base | General | Consultor Sr | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios típicos de proyecto | Consultor Sr | 4 |
| 2 | Documentación para el cliente | Consultor Sr | 3 |
| 3 | Transferencia de conocimiento | Consultor Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Pensado para acelerar consultores, no sustituirles.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 10 |
| **Total** | **23** |
