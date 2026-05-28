# Análisis caso de uso J885 — Run Forecasts in Time Series or Line Charts

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de historias. El valor se centra en acelerar el análisis predictivo dentro de dashboards.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias que incluyan gráficos de **serie de tiempo o línea**.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con **dimensión de fecha** y **medidas** con historia suficiente para producir un forecast significativo.
- Datos históricos correctamente cargados y agregados al nivel de granularidad requerido.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (la capability opera sobre datos numéricos / fechas).
- **Roles**: usuario SAC con permisos sobre la historia / modelo.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8f9665dcf53f4f3f90e920995cdd5f05.html describe el uso del forecast predictivo dentro de gráficos compatibles.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar que las historias y modelos incluyan dimensión de fecha y medidas con datos históricos suficientes | Modelos / historias SAC | Particular (por historia / modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (ejecutar forecast en gráficos representativos) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (forecasts sobre series representativas) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad del forecast depende de la **cantidad y consistencia del histórico**: series cortas o con outliers pueden producir resultados poco fiables.
- El forecast es **apoyo a la decisión**: el usuario debe validar supuestos y horizontes con el negocio.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/
- SAP Help Portal — Forecasts in Charts: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8f9665dcf53f4f3f90e920995cdd5f05.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
