# Análisis caso de uso J778 — Requirement Generation (SAP Cloud ALM)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Esta función de SAP Cloud ALM permite generar automáticamente requerimientos de negocio de alta calidad a partir de transcripciones o notas de talleres Fit-to-Standard. SAP indica: *El valor se centra en acelerar workshops Fit-to-Standard, aumentar la calidad de los requisitos y reducir esfuerzo administrativo durante fases de implementación.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Cloud ALM** activo (Implementation).
- Capability AI / Joule integrada **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Cloud ALM (incluida con la mayoría de cloud suites SAP).
- Feature AI habilitada **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Cloud ALM Workspace (Project Management, Requirements).

### 1.5 Datos maestros / transaccionales previos
- Proyecto Cloud ALM creado; Fit-to-Standard scope definido.
- Meeting notes / minutas de workshops.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Usuario con rol Cloud ALM Project Member.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement Cloud ALM + AI | Tenant Cloud ALM | General | Consultor Cloud ALM | 2 |
| 2 | Crear/verificar proyecto Cloud ALM | Configuración Cloud ALM | General | Consultor Cloud ALM | 3 |
| 3 | Asignar roles Cloud ALM a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Requirement Generation | Configuración Cloud ALM | General | Consultor Cloud ALM | 2 |
| 5 | Pruebas iniciales (generar requirements desde meeting notes) | Configuración Cloud ALM | General | Consultor Cloud ALM | 3 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con notas reales de workshops | Consultor Cloud ALM | 4 |
| 2 | Documentación para el cliente | Consultor Cloud ALM | 3 |
| 3 | Transferencia de conocimiento | Consultor Cloud ALM | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Requirements generados son borradores; consultor refina y prioriza.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 10 |
| **Total** | **22** |
