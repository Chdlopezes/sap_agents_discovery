# Análisis caso de uso J924 — Workspace

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP Document AI, Workspace** ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis. El valor se centra en reducir tiempos de procesamiento documental y mejorar la gobernanza de Document AI en entornos empresariales.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document AI** activo (Workspace).
- Sistemas destino que reciben los datos extraídos (p. ej. **SAP S/4HANA**) con conectividad operativa.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document AI**.
- Capability **Premium** — activación con **AI Units**.
- Precio bajo solicitud; duración del contrato disponible bajo solicitud; tiene prerrequisito **[verificar volumen y costo vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; el escenario funcional en el sistema destino tiene su scope item asociado **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Document AI — Workspace** disponible para los administradores.
- Canales de entrada (correo, API, upload) y workflows hacia sistemas destino configurables.

### 1.5 Datos maestros / transaccionales previos
- Esquemas (predefinidos o personalizados) para los tipos de documento a procesar.
- Datos maestros consistentes en sistemas destino para validar matching.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción documentados por SAP **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos con baja calidad reducen la tasa de extracción correcta.
- **Roles**: administradores de Document AI con permisos para configurar schemas, canales, workflows; operadores con acceso al workspace.

> **Nota**: el enlace de Initial Setup está identificado en Resources pero no fue posible acceder a la URL final tras reintentos. Aplican los prerequisitos generales de SAP Document AI documentados en https://help.sap.com/docs/SAP_DOCUMENT_AI.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Document AI Workspace y AI Units en SAP BTP | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 2 |
| 2 | Aprovisionar AI Units para el volumen estimado | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Aprovisionar el **SAP Document AI Workspace** | Workspace Document AI | General | Consultor SAP Document AI | 3 |
| 4 | Configurar esquemas (schemas) para los tipos de documento del cliente | Schemas Document AI | Particular (por tipo de documento) | Consultor SAP Document AI | 5 |
| 5 | Configurar canales de entrada y workflows hacia sistemas destino | Channels + Workflows Document AI | Particular (por proceso) | Consultor SAP Document AI + Integration Suite | 5 |
| 6 | Asignar a los usuarios objetivo los roles administrativos / operativos del workspace | Roles SAP Document AI | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 7 | Habilitar **monitoreo y análisis** en el workspace para los workflows configurados | Monitoring Document AI | General | Consultor SAP Document AI | 2 |
| 8 | Pruebas iniciales en Quality con documentos reales del cliente | Configuración funcional Document AI | General | Consultor SAP Document AI | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~25 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (varios tipos, varios canales) | Consultor SAP Document AI | 4 |
| 2 | Documentación de la activación para el cliente (manual de configuración + manual de operación / monitoreo) | Consultor SAP Document AI | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica de operación) | Consultor SAP Document AI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units por volumen**: dimensionar el consumo y planificar el crecimiento.
- El **monitoreo y análisis** son clave para detectar deriva en la calidad de extracción y para gobernar excepciones.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza.
- Considerar **gobernanza / data residency** sobre dónde se procesa el documento y dónde se almacenan los datos extraídos.
- Sujeto a la **fair-use policy** y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/
- SAP Help Portal — SAP Document AI: https://help.sap.com/docs/SAP_DOCUMENT_AI

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 25 |
| Validación + documentación + KT | 11 |
| **Total** | **36** |
