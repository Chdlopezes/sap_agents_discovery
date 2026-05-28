# Análisis caso de uso J643 — Decision Summarization

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que asiste a los usuarios en el diseño e implementación de automatizaciones al generar resúmenes de negocio de reglas ya modeladas que no tienen documentación. SAP indica **30% de reducción** del esfuerzo de automatización low-code, **10% menor tiempo a productividad** para desarrolladores y **10% mejora en time-to-market** de nuevas aplicaciones low-code.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Acceso al entorno de Build Process Automation del cliente con artefactos de decisión ya modelados.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con módulos de Decision / Workflow activos.
- Capacidades de IA generativa habilitadas en SAP Build Process Automation.

### 1.5 Datos maestros / transaccionales previos
- **Artefactos de decisión** (DMN, reglas de negocio) ya modelados en el entorno del cliente.
- Procesos y workflows existentes para los que se quiera generar resúmenes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: capability publicada por SAP Build Process Automation **[verificar idiomas soportados vigentes]**.
- **Roles**: Developer / Process Owner con permisos sobre los artefactos de decisión.

> **Setup oficial SAP**: la página https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai indica que las capacidades de generative AI están disponibles dentro de SAP Build Process Automation para resumir artefactos complejos o reglas de negocio. El contenido extraído no expone pasos administrativos adicionales.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidades de IA generativa | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Habilitar / validar las capacidades de IA generativa en el subaccount del cliente | Configuración de SAP Build Process Automation — Generative AI | General | Consultor BTP / Build | 2 |
| 3 | Asignar a los usuarios objetivo los roles con acceso a la capability | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Pruebas iniciales con un developer / process owner piloto (generar resúmenes sobre artefactos representativos) | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con artefactos reales del cliente (resúmenes sobre reglas de decisión representativas) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Los resúmenes son **descriptivos**: el usuario sigue siendo responsable de validar que el resumen capture correctamente la lógica de la regla.
- Útil principalmente en **handovers y revisiones funcionales**: definir gobernanza sobre cuándo el resumen reemplaza documentación formal.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/
- SAP Help Portal — Generative AI in Build Process Automation: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
