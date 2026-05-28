# Análisis caso de uso J329 — Semantic Generation (SAP Datasphere)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas. El onboarding semántico toma tablas, contenido y semántica asociada como monedas, unidades, medidas, hechos, dimensiones y asociaciones. SAP indica: *Menor esfuerzo para crear modelos semánticos en SAP Datasphere, mayor velocidad para preparar datos no SAP para consumo analítico y mejor reutilización de información enriquecida semánticamente.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Datasphere + capability AI **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Datasphere Workspace (Data Builder / Business Builder).

### 1.5 Datos maestros / transaccionales previos
- Fuentes no-SAP conectadas (database, file, etc.).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Modeler.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Datasphere + AI | Tenant Datasphere | General | Consultor Datasphere | 2 |
| 2 | Configurar conexiones a fuentes no-SAP | Conexiones Datasphere | Particular (por fuente) | Consultor Datasphere | 5 |
| 3 | Asignar rol Modeler | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Semantic Generation | Datasphere admin | General | Consultor Datasphere | 2 |
| 5 | Pruebas iniciales (generar semantics sobre tablas/views) | Configuración Datasphere | General | Consultor Datasphere | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datasets reales no-SAP | Consultor Datasphere | 5 |
| 2 | Documentación para el cliente | Consultor Datasphere | 4 |
| 3 | Transferencia de conocimiento | Consultor Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Semántica generada es propuesta; modeler revisa y refina.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |
