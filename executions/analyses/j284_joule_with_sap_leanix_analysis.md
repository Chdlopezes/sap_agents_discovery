# Análisis caso de uso J284 — Joule with SAP LeanIX

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto. SAP indica: *50% menos esfuerzo para buscar documentación e información relevante, según la métrica mostrada en la página de detalle.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX** activo (EAM / Architecture suite).
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción LeanIX.
- Entitlement Joule + capability LeanIX **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace LeanIX.
- Joule integrado en LeanIX UI.

### 1.5 Datos maestros / transaccionales previos
- Inventario LeanIX poblado (applications, business capabilities, tech stack).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement LeanIX + Joule capability | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar SSO entre LeanIX e identidad corporativa | Identity / SSO | General | Consultor Seguridad | 4 |
| 3 | Habilitar capability Joule en LeanIX | LeanIX admin | General | Consultor LeanIX | 3 |
| 4 | Asignar roles LeanIX a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales (consultas NL sobre inventario) | Configuración LeanIX | General | Consultor LeanIX | 3 |

**Esfuerzo total estimado (activación): ~16 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con inventario real | Consultor LeanIX | 4 |
| 2 | Documentación para el cliente | Consultor LeanIX | 4 |
| 3 | Transferencia de conocimiento | Consultor LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Calidad depende de la cobertura/limpieza del inventario LeanIX.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 16 |
| Validación + documentación + KT | 11 |
| **Total** | **27** |
