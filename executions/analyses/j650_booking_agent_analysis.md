# Análisis caso de uso J650 — Booking Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; la disponibilidad GA, el packaging y los pasos exactos de setup pueden no estar todavía completamente documentados públicamente. Marco con **[verificar en SAP Help]** los puntos clave.

**Resumen del caso:** Agente de Joule en Concur Travel que entrega recomendaciones personalizadas de vuelos y hoteles analizando preferencias del viajero, políticas de viaje de la empresa y restricciones de presupuesto. SAP indica: *Mejora la eficiencia del proceso de booking y el cumplimiento de políticas corporativas. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con sistema de **Travel Management / SAP Concur** o equivalente **[verificar agente disponible/conector]**.
- Email / Calendar provider del usuario (Microsoft 365 / Google) si forma parte del flujo **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium con capabilities Agentic **[verificar AI Foundation Catalog vigente]**.
- Suscripción a Concur u otro Travel Management (si aplica).

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad / endpoint accesible por usuarios target.
- Destinations / API keys a Concur / proveedor de viaje.

### 1.5 Datos maestros / transaccionales previos
- Perfil de viajero, políticas de viaje, métodos de pago corporativos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant Joule y al proveedor de Travel.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a Concur / proveedor Travel | Destinations BTP | General | Consultor BTP / Integración | 5 |
| 3 | Asignar acceso al Booking Agent a usuarios objetivo | Roles / Agent assignment | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 4 | Validar políticas de viaje y catálogo de proveedores | Configuración funcional Travel | General | Consultor Funcional Travel | 4 |
| 5 | Pruebas iniciales con escenarios reales | Configuración base | General | Consultor Funcional Travel | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios típicos | Consultor Funcional Travel | 5 |
| 2 | Documentación para el cliente | Consultor Funcional Travel | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional Travel | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Cumplimiento**: el agente debe respetar políticas de viaje y aprobaciones del cliente.
- **Datos personales**: revisar tratamiento de PII en interacciones.
- Disponibilidad/funcionalidades pueden cambiar — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |
