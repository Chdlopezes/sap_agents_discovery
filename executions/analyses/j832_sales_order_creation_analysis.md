# Análisis caso de uso J832 — Sales Order Creation (S/4HANA Cloud Private Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante Private del caso. Ver J831 (Public) y J846 (S/4HANA on-prem).

**Resumen del caso:** La capacidad permite crear pedidos de venta a partir de datos no estructurados, como archivos PDF o imágenes de órdenes de compra. El sistema extrae la información del archivo, propone valores para la solicitud de pedido y permite convertirla posteriormente en un pedido de venta. SAP indica: *La página destaca una reducción del 25% en el costo de creación de pedidos de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para SO Creation | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales | Configuración funcional SD | General | Consultor SD | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 4 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Usuario confirma antes de guardar.
- En Private aplican consideraciones de upgrade compatibility.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
