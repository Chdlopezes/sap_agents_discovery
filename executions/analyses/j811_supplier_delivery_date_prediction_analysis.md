# Análisis caso de uso J811 — Supplier Delivery Date Prediction (S/4HANA Cloud Private Edition)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Nota**: Existe variante para SAP S/4HANA on-premise (J848).

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes del proceso. SAP indica: *Permite planificar con mayor confianza la disponibilidad de materiales y reducir el riesgo operativo asociado a fechas de entrega inciertas o poco confiables.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **MM-PUR – Purchasing** operativo.
- Capability ML / Predictive activa (parte del Joule entitlement o servicio dedicado) **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule + capability predictiva (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Purchase Order Management — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Purchase Orders* y vistas de prediction de fechas.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Suppliers, materials, plants, purchase orders históricos suficientes para entrenar el modelo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Calidad de predicción condicionada por volumen/limpieza del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración MM-PUR (schedule lines, lead times) | Configuración MM-PUR | General | Consultor MM | 3 |
| 3 | Asignar business roles MM-PUR a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability predictiva para delivery date | Joule capability scope | General | Consultor Funcional MM + Joule | 3 |
| 5 | Pruebas iniciales (comparar predicción vs realidad en histórico de prueba) | Configuración funcional MM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varios suppliers/materiales) | Consultor MM | 5 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad de predicción depende del histórico (cantidad y limpieza).
- Validar periodicidad de reentrenamiento.
- Usuario sigue tomando la decisión funcional final.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |
