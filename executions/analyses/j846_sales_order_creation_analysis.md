# Análisis caso de uso J846 — Sales Order Creation (SAP S/4HANA on-premise)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante para SAP S/4HANA on-premise. Ver J831 (Public) y J832 (Private). Joule en on-prem suele requerir bridging vía BTP.

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta a partir de archivos de órdenes de compra en PDF o imagen. El sistema extrae información y propone valores para la solicitud de orden. SAP indica: *El valor se centra en acelerar la creación de órdenes, disminuir errores de procesamiento y reducir el costo asociado a la creación manual de órdenes de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA on-premise** en release con soporte de Joule (vía BTP bridge) **[verificar release mínima]**.
- **SAP BTP** con servicio Joule aprovisionado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia S/4HANA on-premise vigente.
- Entitlement Joule en BTP **[verificar]**.

### 1.3 Scope item relacionado
- Best practice / scope item de Sales Order Management — **[verificar referencia equivalente para on-premise]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Fiori Launchpad on-prem con panel Joule.
- Cloud Connector / RFC conectividad on-prem ↔ BTP.
- Communication arrangement / destination configurados.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Aplica a **on-premise**; algunas capabilities Joule pueden estar limitadas frente a Cloud editions.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar Cloud Connector / destinations on-prem ↔ BTP | Cloud Connector / Destinations | General | Consultor Basis / Integración | 6 |
| 3 | Configurar communication arrangement Joule | Communication Arrangement | General | Consultor Integración | 3 |
| 4 | Asignar roles SD + catálogos Joule a usuarios | Roles / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales end-to-end (Joule → SO en on-prem) | Configuración funcional SD | General | Consultor SD | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SD | 5 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **on-premise**: validar firewall / Cloud Connector / latencia.
- Compatibilidad con la versión del stack ABAP del cliente.
- Algunas capabilities Joule pueden no estar disponibles fuera del cloud editions.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |
