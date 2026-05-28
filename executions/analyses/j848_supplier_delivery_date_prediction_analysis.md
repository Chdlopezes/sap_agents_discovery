# Análisis caso de uso J848 — Supplier Delivery Date Prediction (SAP S/4HANA on-premise)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Variante para SAP S/4HANA on-premise. Ver J811 (Private).

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra con base en datos históricos y múltiples parámetros del proceso de aprovisionamiento. SAP indica: *Incrementa la confiabilidad del abastecimiento, mejora la planeación de materiales y ayuda a reducir impactos por entregas tardías o incertidumbre en fechas de recepción.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA on-premise** en release con soporte de la capability ML / Predictive **[verificar]**.
- Componente **MM-PUR – Purchasing** operativo.
- Servicio predictivo (puede requerir BTP / SAP AI Core) **[verificar arquitectura vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia S/4HANA on-premise vigente.
- Entitlement servicio predictivo (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Best practice / scope item de Purchase Order Management — **[verificar referencia equivalente para on-premise]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Purchase Orders*.
- Conectividad on-prem ↔ BTP / AI Core si aplica.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, materials, plants, POs históricos.
- Volumen / calidad de histórico suficiente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Aplica a **on-premise**.
- Calidad predicción condicionada por histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar servicio predictivo en BTP / AI Core | Subaccount BTP + entitlement | General | Consultor BTP | 4 |
| 2 | Configurar Cloud Connector / destinations on-prem ↔ BTP | Cloud Connector / Destinations | General | Consultor Basis / Integración | 6 |
| 3 | Configurar integración MM-PUR con servicio predictivo | Integración funcional / OData | General | Consultor MM + Integración | 6 |
| 4 | Asignar roles MM-PUR a usuarios | Roles / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (comparar predicción vs realidad) | Configuración funcional MM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~23 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios suppliers) | Consultor MM | 5 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **on-premise**: validar firewall / Cloud Connector / latencia / volumen de datos enviados.
- Periodicidad de reentrenamiento del modelo.
- Usuario sigue decidiendo el ajuste funcional.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 23 |
| Validación + documentación + KT | 12 |
| **Total** | **35** |
