# Análisis caso de uso J641 — Form Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Genera formularios de automatización de procesos a partir de descripciones en lenguaje natural en SAP Build Process Automation. SAP indica: *Reducción estimada del 30% en esfuerzo de automatización low-code; 10% más rápido el tiempo de productividad para desarrolladores; 10% de mejora en time-to-market para nuevas aplicaciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** activo en BTP.
- Capability AI / Joule integrada **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA con feature AI (Premium si aplica) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Form Designer).

### 1.5 Datos maestros / transaccionales previos
- Datos de proceso de referencia (data types, project).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Form Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (generar forms con prompts) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor SBPA | 4 |
| 2 | Documentación para el cliente | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Forms generadas son borradores; revisión humana requerida.
- Buenas prácticas: validar accesibilidad y UX.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |
