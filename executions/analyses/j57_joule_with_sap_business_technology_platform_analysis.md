# Análisis caso de uso J57 — Joule with SAP Business Technology Platform

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural. SAP indica: *No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se expresa en ahorro de tiempo para consultas administrativas y acceso más rápido a información de BTP.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP BTP** con uno o más subaccounts productivos.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule + capability BTP (Base) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- BTP Cockpit accesible.
- Joule habilitado para usuarios admin / desarrolladores.

### 1.5 Datos maestros / transaccionales previos
- Estructura de global account / directories / subaccounts.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol BTP Admin / Member.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + capability BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Habilitar Joule en BTP Cockpit | Configuración BTP | General | Consultor BTP | 2 |
| 3 | Asignar roles BTP a usuarios | Roles BTP | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Pruebas iniciales (consultar quotas, services, account info) | Configuración BTP | General | Consultor BTP | 3 |

**Esfuerzo total estimado (activación): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con prompts representativos | Consultor BTP | 4 |
| 2 | Documentación para el cliente | Consultor BTP | 3 |
| 3 | Transferencia de conocimiento | Consultor BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Joule consulta; acciones administrativas siguen en BTP Cockpit / CLI.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 10 |
| **Total** | **21** |
