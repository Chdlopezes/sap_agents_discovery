# Análisis caso de uso J638 — Process Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Generation genera artefactos de proceso a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation. SAP indica: *Su valor está en reducir esfuerzo de automatización low-code, acelerar la productividad de desarrolladores y mejorar el time-to-market de soluciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Lobby + Process Editor).

### 1.5 Datos maestros / transaccionales previos
- Conocimiento del proceso a generar (descripción en NL, ejemplos).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales: generar proceso desde prompt y desplegar en QAS | Configuración SBPA | General | Consultor SBPA | 4 |

**Esfuerzo total estimado (activación): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Consultor SBPA | 5 |
| 2 | Documentación para el cliente | Consultor SBPA | 4 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Procesos generados son borradores; refactor humano + tests requeridos.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 12 |
| **Total** | **23** |
