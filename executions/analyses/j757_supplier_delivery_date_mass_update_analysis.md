# Análisis caso de uso J757 — Supplier Delivery Date Mass Update

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite realizar actualizaciones masivas de fechas de entrega para múltiples pedidos de compra utilizando Joule en SAP S/4HANA Cloud Public Edition. SAP indica: *Mejora la agilidad del proceso de compras y planificación al mantener actualizadas las fechas de entrega de manera más rápida, reduciendo retrasos operativos y reprocesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **MM-PUR – Purchasing** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Purchase Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App Fiori *Manage Purchase Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Purchase orders activos con líneas de delivery schedule.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones MM-PUR.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración Purchasing (document types, schedule lines) | Configuración MM-PUR | General | Consultor MM | 3 |
| 3 | Asignar business roles MM-PUR a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Delivery Date Mass Update | Joule capability scope | General | Consultor Funcional MM + Joule | 2 |
| 5 | Pruebas iniciales: actualización masiva de fechas en QAS | Configuración funcional MM | General | Consultor MM | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (volúmenes representativos) | Consultor MM | 4 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Mass update: confirmar volumen máximo recomendado.
- Cambios en fechas pueden disparar reschedulings / ATP recalc — validar impacto previo.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
