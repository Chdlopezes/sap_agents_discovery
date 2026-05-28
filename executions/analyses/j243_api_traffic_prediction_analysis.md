# Análisis caso de uso J243 — API traffic prediction (SAP Integration Suite)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Funcionalidad de SAP Integration Suite que identifica tendencias en llamadas API y predice volúmenes futuros de tráfico para apoyar decisiones sobre capacidad, carga y estrategia API. SAP indica: *Mejora la planificación de recursos, la gestión de carga del sistema y la toma de decisiones sobre estrategia API. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Integration Suite** (capability API Management).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Integration Suite con plan que incluya API Management.
- Capability AI activada **[verificar AI Foundation Catalog]**.

### 1.3 Scope item relacionado
- N/A (capability de la plataforma).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Subaccount BTP con Integration Suite habilitado.
- API Management con proxies productivos y métricas habilitadas.

### 1.5 Datos maestros / transaccionales previos
- Histórico de tráfico de APIs por proxy / API Product (idealmente varias semanas).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI en inglés primariamente **[verificar]**.
- Calidad de predicción depende del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Integration Suite + capability AI | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Habilitar capability AI en API Management | API Management settings | General | Consultor Integración | 3 |
| 3 | Asignar roles API Admin / Analyst a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Validar histórico mínimo de tráfico para activación útil | Configuración API Management | General | Consultor Integración | 2 |
| 5 | Pruebas iniciales (revisar predicciones contra histórico) | Configuración AI | General | Consultor Integración | 3 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con APIs reales del cliente | Consultor Integración | 4 |
| 2 | Documentación para el cliente | Consultor Integración | 3 |
| 3 | Transferencia de conocimiento | Consultor Integración | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Útil para capacity planning y SLA management.
- Calidad mejora con volumen/estabilidad del tráfico.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 10 |
| **Total** | **22** |
