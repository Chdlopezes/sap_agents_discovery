# Análisis caso de uso J404 — Sales Order Creation from Unstructured Data

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes. Después de cargar el archivo, la información se procesa automáticamente para generar una solicitud de pedido de venta que luego puede convertirse en pedido. SAP indica: *La página indica una reducción del 33% en el esfuerzo manual para crear pedidos de venta.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP) para extracción de datos del input no estructurado (PDF/email/imagen).
- Componente **SD – Sales** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con SD.
- Entitlement de **SAP Document AI** (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Sales Order Management + Document AI integration — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Create Sales Orders*, *Manage Sales Orders*, *Document Information Extraction Workspace*.
- Communication arrangement S/4HANA ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Customers, materials, pricing, sales areas configurados.
- Tipos de documento de entrada (formato PDF / email parseable / imagen) soportados por Document AI.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Layout del PO del cliente debe ser razonablemente extraíble.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al sales order | Mapping Document AI ↔ SO | Particular (por layout/cliente) | Consultor SD + Integración | 6 |
| 4 | Asignar business roles SD con catálogos de SO + Document AI | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con PDFs reales de PO del cliente | Configuración funcional SD | General | Consultor SD | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real (mínimo 2-3 layouts representativos) | Consultor SD | 6 |
| 2 | Documentación para el cliente | Consultor SD | 4 |
| 3 | Transferencia de conocimiento | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout de la fuente; pueden requerirse iteraciones por proveedor/cliente.
- Volumen sujeto a cuotas de Document AI.
- Usuario sigue validando antes de guardar la orden.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |
