# Análisis caso de uso J811 — Supplier Delivery Date Prediction

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J811 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/
- Initial Setup (SAP Help Portal — Intelligent Scenario Lifecycle Management, Activate Features): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html?locale=en-US
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition** — el caso se apoya en **Intelligent Scenario Lifecycle Management (ISLM)** (Cross Components → Process Management and Integration).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, el caso se gestiona mediante **ISLM**, cuyo framework consta de dos apps SAP Fiori: **Intelligent Scenarios** e **Intelligent Scenario Management**, que ofrecen una interfaz unificada para crear, desplegar, monitorear y activar el modelo a consumir por la aplicación de negocio.
- ISLM integra con **Generative AI Hub, SAP BTP AI services y SAP HANA ML**; un intelligent scenario es una representación ABAP del caso de uso.

### 1.5 Datos maestros / transaccionales previos
- **Datos históricos** de fechas de entrega / posiciones de pedidos de compra para el entrenamiento del modelo (la capacidad usa datos históricos y parámetros relevantes, según la Detail Page).

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para **SAP S/4HANA Cloud Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configurar los prerrequisitos de **ISLM** para el caso (integración con Generative AI Hub / SAP BTP AI services / SAP HANA ML según el intelligent scenario) | ISLM (framework) | General | Consultor Funcional SAP S/4HANA + BTP | 4 |
| 2 | Activar el **intelligent scenario** correspondiente y ejecutar las operaciones de ciclo de vida (entrenamiento/retraining, despliegue y activación del modelo) mediante la app **Intelligent Scenario Management** | Intelligent Scenario / modelo ML | General | Consultor Funcional SAP S/4HANA (ISLM) | 4 |
| 3 | Habilitar el acceso de los usuarios a la feature (asignación de roles/autorizaciones requeridos) | Roles / Autorizaciones | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (predicción de fechas de entrega en posiciones de pedidos de compra) | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (ISLM / Compras) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- ISLM soporta operaciones de ciclo de vida como entrenamiento programado y retraining, además del despliegue y activación del modelo, directamente dentro de SAP S/4HANA (escenarios embedded y side-by-side).
- La predicción usa datos históricos; la calidad del modelo depende de la disponibilidad y calidad de esos datos.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/
- SAP Help Portal — Initial Setup (Intelligent Scenario Lifecycle Management — Activate Features): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/436151b128614f0e84024015136043d3.html?locale=en-US
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |
