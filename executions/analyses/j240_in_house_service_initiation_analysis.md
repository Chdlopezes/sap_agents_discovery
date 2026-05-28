# Análisis caso de uso J240 — In-house Service Initiation

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos. El personal de reparación puede escanear o fotografiar documentos entrantes, como órdenes de compra; el sistema extrae datos relevantes y genera objetos de reparación asociados al servicio interno. SAP indica: *SAP indica aumento de 70% en productividad del trabajador de servicio al preparar órdenes de servicio. El valor está en reducir digitación manual, evitar pérdida de datos y acelerar el procesamiento de reparaciones.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Document AI** (para input papel/PDF).
- Componente **CS / Service Management** (Service Order / Notification) operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Document AI (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Service Management - In-house Repair / Customer Service — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Service Orders*, *Service Notifications*.
- Communication arrangement con Document AI.

### 1.5 Datos maestros / transaccionales previos
- Maestros de equipos, customers, service types, technicians.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Mapping de datos extraídos al service order / notification | Mapping Document AI ↔ Service | Particular (por tipo de service request) | Consultor Service + Integración | 6 |
| 4 | Asignar business roles Service a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con documentos reales | Configuración funcional Service | General | Consultor Service | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real | Consultor Service | 6 |
| 2 | Documentación para el cliente | Consultor Service | 4 |
| 3 | Transferencia de conocimiento | Consultor Service | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- Calidad de extracción depende del layout del documento de entrada.
- Usuario sigue validando antes de crear el service order/notification.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |
