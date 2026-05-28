# Análisis caso de uso J1047 — Sales Order Status Check

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule permite a los representantes de ventas comprobar si el cumplimiento de un pedido está en curso y detectar problemas que bloquean su finalización. La experiencia se orienta a consultar estado, causas y posibles acciones desde un flujo conversacional. SAP indica: *Aporta valor al reducir el tiempo de análisis manual del estado de pedidos y al facilitar acciones tempranas sobre problemas que podrían retrasar el cumplimiento.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo (incluyendo Delivery & Billing).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Fulfillment / Order to Cash — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Sales Order Fulfillment - Analyze and Resolve Issues*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Sales orders activos con deliveries, billing, ATP info.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Order Fulfillment (status profiles, blocks) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Status | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales (consultas estado, identificación de bloqueos) | Configuración funcional SD | General | Consultor SD | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (consultar status, bloqueos, predicciones de entrega) | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **consulta y diagnostica**; la resolución se ejecuta en las apps SD.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
