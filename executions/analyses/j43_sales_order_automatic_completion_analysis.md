# Análisis caso de uso J43 — Sales Order Automatic Completion

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Mediante datos históricos y machine learning, la función recomienda valores para completar campos vacíos en órdenes de venta incompletas. SAP indica: *La página indica una reducción del 25% en esfuerzo manual para completar órdenes de venta, ayudando a acelerar el ciclo comercial y reducir errores.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition.
- Entitlement Joule (**Base**) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Sales Orders*, *Create Sales Orders*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, plants, sales areas configurados.
- Datos históricos suficientes para que las recomendaciones tengan calidad.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario con autorizaciones SD.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración SD (sales areas, document types, pricing) | Configuración SD | General | Consultor SD | 3 |
| 3 | Asignar business roles SD a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Sales Order Completion | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales: crear sales orders con datos parciales y validar recomendaciones | Configuración funcional SD | General | Consultor SD | 3 |

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

- Recomendaciones mejoran con volumen / calidad de datos históricos.
- Usuario sigue confirmando antes de guardar.
- Respeta autorizaciones.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
