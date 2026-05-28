# Análisis caso de uso J327 — Expense Report Validation Agent

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

> **Aviso**: agente nuevo; puntos de setup pueden no estar plenamente documentados públicamente — marco con **[verificar]** los críticos.

**Resumen del caso:** Agente para ayudar a viajeros de negocio a completar y enviar reportes de gastos, simplificando el proceso de entendimiento y preparación de la información requerida. SAP indica: *Reducción estimada del 30% en el tiempo dedicado a preparar y enviar reportes de gastos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en BTP (capability Agentic).
- Integración con **SAP Concur Expense** (u otro Travel & Expense del cliente) **[verificar conector]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule Premium + Agentic capability **[verificar]**.
- Suscripción Concur Expense (si aplica).

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Launchpad accesible por employees.
- Destination a Concur (API keys / OAuth).

### 1.5 Datos maestros / transaccionales previos
- Políticas de expense (límites, categorías, country specifics).
- Reglas de validación corporativas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Disponibilidad regional sujeta al tenant Joule y al proveedor.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + Agentic | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destination a Concur Expense | Destinations BTP | General | Consultor BTP / Integración | 5 |
| 3 | Configurar políticas de validación específicas del cliente | Reglas de validación | Particular (por política / categoría) | Consultor Funcional T&E | 5 |
| 4 | Asignar acceso al agente a employees | Roles / Agent assignment | Particular (por grupo) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con expense reports reales | Configuración funcional T&E | General | Consultor Funcional T&E | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (categorías y excepciones) | Consultor Funcional T&E | 5 |
| 2 | Documentación para el cliente | Consultor Funcional T&E | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional T&E | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- El agente **sugiere/ayuda**; la aprobación final sigue al workflow definido.
- Privacidad: revisar tratamiento de datos personales/financieros.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 12 |
| **Total** | **32** |
