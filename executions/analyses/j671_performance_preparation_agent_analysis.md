# Análisis caso de uso J671 — Performance Preparation Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; pasos exactos pueden requerir validación posterior.

**Resumen del caso:** El Performance Preparation Agent automatiza la recopilación de datos, genera talking points personalizados para managers y sugiere próximos pasos accionables para reuniones one-on-one. SAP indica: *70% de reducción en el tiempo del manager dedicado a preparar reuniones de desempeño o one-on-one.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con **SAP SuccessFactors** (Employee Central + Performance & Goals) o equivalente HR **[verificar conector]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.
- Licencia SuccessFactors módulos aplicables.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible para managers.
- Destination a SuccessFactors.

### 1.5 Datos maestros / transaccionales previos
- Datos employees (objectives, performance reviews, feedback histórico).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Cumplimiento data privacy (GDPR / equivalentes).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a SuccessFactors | Destinations / OAuth | General | Consultor BTP / Integración | 5 |
| 3 | Configurar scope de datos visibles al manager (data privacy) | Reglas de visibilidad | Particular (por país / política) | Consultor HR + Compliance | 6 |
| 4 | Asignar acceso al agente a managers | Roles / Agent assignment | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (preparación de 1:1 con datos reales) | Configuración base | General | Consultor HR | 4 |

**Esfuerzo total estimado (activación): ~21 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor HR | 5 |
| 2 | Documentación para el cliente | Consultor HR | 4 |
| 3 | Transferencia de conocimiento | Consultor HR | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Privacidad de datos** crítica: revisar políticas locales y obtener aprobación legal/HR antes del rollout.
- El agente **prepara** insights; la conversación 1:1 sigue siendo responsabilidad del manager.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 21 |
| Validación + documentación + KT | 12 |
| **Total** | **33** |
