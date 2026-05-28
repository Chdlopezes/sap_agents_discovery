# Análisis caso de uso J1284 — Document Data Extraction

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Build Process Automation** que extrae y procesa automáticamente información clave de **PDFs e imágenes escaneadas** usando IA, con o sin plantillas. SAP indica beneficios como **500 horas ahorradas por mes**, **70% de facturas procesadas sin intervención manual** y procesamiento de una factura en **menos de 1 minuto** desde la llegada hasta la contabilización.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Process Automation** (suscripción activa).
- Capacidad de extracción documental habilitada para PDFs e imágenes.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Build Process Automation**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Build Process Automation** con módulos de procesos / workflow activos.
- Plantillas de extracción preconfiguradas o personalizadas (según el tipo de documento).

### 1.5 Datos maestros / transaccionales previos
- Documentos representativos de cada tipo a procesar (facturas, órdenes de compra, avisos de pago).
- Si se requiere salida a un sistema destino (p. ej. S/4HANA), conectividad y datos maestros del destino consistentes.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción documentados por SAP **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos escaneados con baja calidad reducen la tasa de extracción correcta.
- **Roles**: roles de Build Process Automation para definir y operar la extracción.

> **Setup oficial SAP**: la página https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai describe el uso de Document Data Extraction desde SAP Build Process Automation. El texto extraído no expone un paso a paso administrativo más detallado.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Build Process Automation con capacidad de extracción documental | Subaccount BTP + entitlement Build Process Automation | General | Consultor BTP | 2 |
| 2 | Habilitar / validar la capacidad de Document Data Extraction en el subaccount | Configuración Build Process Automation — Extracción | General | Consultor BTP / Build | 2 |
| 3 | Configurar plantillas (predefinidas o personalizadas) para los tipos de documento del cliente | Plantillas de extracción | Particular (por tipo de documento) | Consultor Build Process Automation | 4 |
| 4 | Configurar el flujo (workflow / proceso) que consume la extracción y la entrega al sistema destino | Workflow / Proceso Build | Particular (por proceso) | Consultor Build Process Automation | 4 |
| 5 | Asignar a los usuarios objetivo los roles con acceso a la operación | Roles SAP Build Process Automation | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 6 | Pruebas iniciales con documentos reales del cliente en Quality | Configuración funcional Build Process Automation | General | Consultor Build Process Automation | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (facturas, OCs, avisos de pago de varios proveedores/formatos) | Consultor Build Process Automation | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación / monitoreo) | Consultor Build Process Automation | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión de operación) | Consultor Build Process Automation | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La **tasa de extracción correcta** depende de la calidad de los documentos y de la cobertura de plantillas; planificar un periodo de afinamiento.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza: intervención humana o re-clasificación.
- Considerar **gobernanza** sobre dónde se procesa el documento (data residency) y sobre la **retención** de los datos extraídos.
- Sujeto a las condiciones de servicio vigentes de SAP Build Process Automation **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/
- SAP Help Portal — Generative AI in Build Process Automation: https://help.sap.com/docs/build-process-automation/sap-build-process-automation/generative-ai?locale=en-US

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |
