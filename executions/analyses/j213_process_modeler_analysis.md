# Análisis caso de uso J213 — Process Modeler (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio. SAP indica: *La página destaca una reducción del tiempo de modelado de procesos y un menor costo asociado al modelado manual, además de mejorar la colaboración entre negocio y equipos de procesos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Manager** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Manager con feature AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Manager UI.

### 1.5 Datos maestros / transaccionales previos
- Diccionario / glosario, conventions BPMN del cliente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Process Modeler.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Asignar rol Process Modeler | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 3 | Habilitar Process Modeler AI | Signavio admin | General | Consultor Signavio | 2 |
| 4 | Pruebas iniciales (generar BPMN desde texto/imagen) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con descripciones reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Diagrama generado es punto de partida; modeler debe revisar conventions.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 10 |
| **Total** | **19** |
