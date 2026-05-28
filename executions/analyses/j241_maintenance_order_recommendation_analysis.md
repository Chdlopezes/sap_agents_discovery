# Análisis caso de uso J241 — Maintenance Order Recommendation

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento. El planificador revisa las recomendaciones y selecciona una orden como referencia para crear una nueva orden de mantenimiento. SAP indica: *40% de aumento en productividad del planificador de mantenimiento; 1% de reducción del downtime no planificado; 5% de aumento en la tasa de resolución en el primer intento de técnicos de mantenimiento.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **PM / EAM – Plant Maintenance / Enterprise Asset Management** operativo.
- Datos históricos suficientes de maintenance orders para entrenar/recomendar.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule (capability puede ser Premium dado el componente ML) **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Plant Maintenance / EAM — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Manage Maintenance Orders*, *Maintenance Planner*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Functional locations, equipment, task lists, maintenance plans, historial de OTs cerradas.
- Volumen de datos históricos suficiente para que las recomendaciones tengan calidad.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones PM.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule + capability ML | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración PM (order types, activity types, task lists) | Configuración PM | General | Consultor PM | 3 |
| 3 | Asignar business roles PM a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Maintenance Recommendation | Joule capability scope | General | Consultor Funcional PM + Joule | 3 |
| 5 | Pruebas iniciales: validar recomendaciones contra historial real | Configuración funcional PM | General | Consultor PM | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (recomendaciones por tipo de equipo) | Consultor PM | 5 |
| 2 | Documentación para el cliente | Consultor PM | 4 |
| 3 | Transferencia de conocimiento | Consultor PM | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad de recomendación depende del volumen y limpieza del histórico.
- Validar periodicidad de reentrenamiento (si aplica).
- Usuario confirma antes de crear la OT.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |
