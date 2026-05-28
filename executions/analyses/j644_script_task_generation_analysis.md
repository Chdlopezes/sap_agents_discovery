# Análisis caso de uso J644 — Script Task Generation (SAP Build Process Automation)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite generar código JavaScript ejecutable mediante lenguaje natural dentro de SAP Build Process Automation. La tarea de script integra capacidades de IA generativa para que el desarrollador cree código a partir de prompts y pueda apoyarse en acciones predefinidas alineadas con las restricciones del runtime. SAP indica: *30% de reducción del esfuerzo de automatización low-code; 10% más rapidez para que los desarrolladores alcancen productividad; 10% de mejora en el time-to-market de nuevas aplicaciones low-code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation (SBPA)** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SBPA + AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Workspace SBPA (Process Editor + Script Task editor).

### 1.5 Datos maestros / transaccionales previos
- Proceso al que se añade el script task.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Rol Process Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SBPA + AI | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Asignar rol Process Designer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Script Task Generation | Configuración SBPA | General | Consultor SBPA | 2 |
| 4 | Pruebas iniciales (generar y probar scripts JS) | Configuración SBPA | General | Consultor SBPA | 3 |

**Esfuerzo total estimado (activación): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Consultor SBPA | 4 |
| 2 | Documentación + buenas prácticas | Consultor SBPA | 3 |
| 3 | Transferencia de conocimiento | Consultor SBPA | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Scripts generados requieren review (security, performance).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 10 |
| **Total** | **20** |
