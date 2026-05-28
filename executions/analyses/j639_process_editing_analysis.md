# Análisis caso de uso J639 — Process Editing (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Editing ayuda a desarrolladores durante el diseño e implementación de automatizaciones, permitiendo editar artefactos de proceso mediante instrucciones en lenguaje natural. SAP indica: *La capacidad se asocia con reducción del esfuerzo de automatización low-code, mayor productividad de desarrolladores y mejor velocidad de entrega de nuevas aplicaciones o procesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Process Editor).

### 1.5 Datos maestros / transaccionales previos
- Procesos existentes a editar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles SBPA | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Editing | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (editar proceso con prompts) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con procesos reales | Consultor SBPA | 4 |
| 2 | Documentación para el cliente | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Edición asistida; revisión humana antes de publicar.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |
