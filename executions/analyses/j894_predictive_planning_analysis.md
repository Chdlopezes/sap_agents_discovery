# Análisis caso de uso J894 — Predictive Planning (SAP Analytics Cloud)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos. La capacidad ayuda a actualizar previsiones de forma más ágil y a reducir sesgos en los ciclos de planificación. SAP indica: *Aporta valor al reducir trabajo manual y sesgos en la planeación, mejorar la agilidad de los equipos y aumentar la confiabilidad de los escenarios predictivos usados para decidir.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud (SAC)** con módulo Planning activo.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia SAC Planning (incluye capability Predictive) **[verificar matriz vigente]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant SAC con modelos de planning configurados.

### 1.5 Datos maestros / transaccionales previos
- Series temporales históricas con calidad suficiente para forecast.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI multilenguaje según SAC.
- Calidad del forecast depende del histórico.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar licencia Planning + Predictive | Tenant SAC | General | Consultor SAC | 2 |
| 2 | Verificar modelo de planning con series temporales | Modelos SAC | General | Consultor SAC | 4 |
| 3 | Asignar roles Planner/Modeler a usuarios | Roles SAC | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Predictive scenarios en SAC | Configuración Predictive | General | Consultor SAC | 3 |
| 5 | Pruebas iniciales (correr predictive scenarios) | Configuración SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (KPIs del cliente) | Consultor SAC | 5 |
| 2 | Documentación para el cliente | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Calidad del forecast mejora con limpieza y volumen del histórico.
- Revisar bias / estacionalidad.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 12 |
| **Total** | **26** |
