# Análisis caso de uso J893 — Smart Predict (SAP Analytics Cloud)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite crear modelos predictivos en SAP Analytics Cloud para entregar predicciones aplicables a escenarios de análisis y planificación. SAP indica: *Mejora la anticipación de resultados, acelera el uso de analítica predictiva en decisiones de negocio y reduce dependencia de desarrollos externos para escenarios predictivos básicos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud (SAC)** con capability Smart Predict / Predictive **[verificar plan]**.

### 1.2 Licenciamiento / entitlement / paquete
- Licencia SAC que incluya Smart Predict **[verificar matriz]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Datasets con calidad suficiente para entrenar modelos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: UI multilenguaje según SAC.
- Calidad de los modelos depende de los datos.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar licencia SAC + Smart Predict | Tenant SAC | General | Consultor SAC | 2 |
| 2 | Verificar datasets / preparar feature engineering | Datasets SAC | General | Consultor SAC / Data | 5 |
| 3 | Asignar roles SAC a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Smart Predict scenarios | Configuración Predict | General | Consultor SAC | 3 |
| 5 | Pruebas iniciales (entrenar/desplegar 1 modelo) | Configuración SAC | General | Consultor SAC | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos (classification/regression/timeseries) | Consultor SAC | 5 |
| 2 | Documentación para el cliente | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Validar bias / explicabilidad antes de adoptar en decisiones críticas.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 12 |
| **Total** | **29** |
