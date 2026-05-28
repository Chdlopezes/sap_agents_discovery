# Análisis caso de uso J1104 — Processing of Payment Advices with SAP Document AI

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Processing of Payment Advices with SAP Document AI automatiza el procesamiento multilingüe de avisos de pago mediante extracción y lectura asistida por IA. SAP indica: *La capacidad busca reducir tiempos de procesamiento documental, disminuir correcciones manuales y mejorar la eficiencia del equipo de cuentas por cobrar.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP).
- Componente **FI-AR – Accounts Receivable** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con FI.
- Entitlement de **SAP Document AI** (capability Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Accounts Receivable - Incoming Payments / Payment Advice — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Payment Advices*, *Post Incoming Payments*.
- Communication arrangement S/4HANA ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Maestros de clientes con configuración de payment advice.
- Open items en AR pendientes de clearing.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas soportados por Document AI según matriz vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Formato del payment advice (PDF / email parseable) soportado.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar SAP Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de payment advice extraído al documento de clearing AR | Mapping Document AI ↔ Payment Advice | Particular (por layout/cliente) | Consultor FI + Integración | 6 |
| 4 | Asignar business roles AR con catálogos de payment advice a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales: cargar payment advices reales y validar matching + clearing | Configuración funcional FI-AR | General | Consultor FI | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real de payment advices (varios layouts) | Consultor FI | 6 |
| 2 | Documentación para el cliente | Consultor FI | 4 |
| 3 | Transferencia de conocimiento | Consultor FI | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de matching** depende del payment advice y del estado de los open items.
- Volumen sujeto a cuotas de Document AI.
- El usuario sigue validando casos no automáticos antes del clearing.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |
