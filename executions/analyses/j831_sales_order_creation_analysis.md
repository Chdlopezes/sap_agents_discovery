# Análisis caso de uso J831 — Sales Order Creation (S/4HANA Cloud Public Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Existen variantes equivalentes para S/4HANA Cloud Private Edition (J832) y SAP S/4HANA on-premise (J846). También existe J404 "Sales Order Creation from Unstructured Data" como variante con extracción de documentos.

**Resumen del caso:** Representantes de ventas internos pueden crear órdenes de venta desde archivos de compra no estructurados en PDF o imágenes; la información se extrae automáticamente y se propone en campos de la solicitud. SAP indica: *La página indica reducción del 25% en el costo de creación de órdenes de venta y acelera el ciclo de ventas gracias a menor tasa de error.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con SD.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing condition records, plants, sales areas, shipping points.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD (document types, pricing, item categories) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Creation | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: crear sales orders con prompts representativos | Configuración funcional SD | General | Consultor SD | 3 |

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

- Usuario confirma antes de guardar el pedido.
- Respeta autorizaciones SD.
- Para extracción desde documentos no estructurados, ver J404.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
