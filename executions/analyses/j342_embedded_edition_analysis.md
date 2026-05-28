# Análisis caso de uso J342 — Embedded Edition

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **SAP Document AI — Embedded Edition** automatiza tareas de procesamiento documental de punta a punta, ejecución de workflows e integración de canales. SAP indica una reducción del **70% en el tiempo** para procesar documentos, **83% en el tiempo** para mantener plantillas y **40% de reducción** en pérdida de valor por retrasos en procesamiento manual.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Document AI** activo (Embedded Edition).
- **SAP Document AI Workspace** configurado.
- Sistema(s) destino que reciben los datos extraídos (típicamente **SAP S/4HANA**) con conectividad operativa.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Document AI**.
- Capability **Premium** — activación con **AI Units**.
- **AI Units** asignadas al tenant; pricing por volumen mostrado en *Pricing Details* de Discovery Center **[verificar volumen y costo vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item directamente; el escenario funcional (p. ej. *Accounts Payable Invoice Processing*) en el sistema destino tiene su scope item asociado **[verificar]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Document AI — UI básica / Workspace** disponible para los usuarios objetivo.
- Canales de entrada configurados (p. ej. **buzones de correo**, *upload* manual, integración API).
- Workflows configurados para enrutar el documento extraído hacia el sistema destino.

### 1.5 Datos maestros / transaccionales previos
- Esquemas (predefinidos o personalizados) para los tipos de documento del cliente.
- Datos maestros consistentes en el sistema destino para validar el match de proveedores / clientes / materiales.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas de OCR / extracción según el modelo subyacente **[verificar matriz vigente]**.
- **Calidad de documentos**: documentos con baja calidad reducen la tasa de extracción correcta.
- **Roles**: administradores de Document AI con permisos para crear schemas y workflows; operadores con acceso al workspace.

> **Setup oficial SAP**: la página https://help.sap.com/docs/SAP_DOCUMENT_AI describe el Initial Setup de SAP Document AI: suscripción, acceso y uso de la UI básica / workspace para Embedded Edition y Premium Edition.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Document AI y AI Units en SAP BTP | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 2 |
| 2 | Aprovisionar AI Units para el volumen estimado | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Aprovisionar el **SAP Document AI Workspace** | Workspace Document AI | General | Consultor SAP Document AI | 3 |
| 4 | Configurar esquemas / plantillas para los tipos de documento del cliente | Schemas Document AI | Particular (por tipo de documento) | Consultor SAP Document AI | 5 |
| 5 | Configurar canales de entrada (correo, API, upload) y workflows hacia el sistema destino | Channels + Workflows Document AI | Particular (por proceso) | Consultor SAP Document AI + Integration Suite | 5 |
| 6 | Asignar a los usuarios objetivo los roles de Document AI | Roles SAP Document AI | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 7 | Pruebas iniciales en Quality con documentos reales del cliente | Configuración funcional Document AI | General | Consultor SAP Document AI | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~23 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con documentos reales del cliente (varios tipos, varios proveedores / formatos) | Consultor SAP Document AI | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de operación / monitoreo) | Consultor SAP Document AI | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica de operación) | Consultor SAP Document AI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units por volumen**: dimensionar con cuidado y planificar el crecimiento.
- La **tasa de extracción** depende de la calidad de los documentos y la cobertura de schemas: planificar un periodo de afinamiento.
- Definir **flujo de excepción** cuando la extracción no alcanza el umbral de confianza: intervención humana o re-clasificación.
- Considerar **gobernanza / data residency** sobre dónde se procesa el documento y dónde se almacenan los datos extraídos.
- Joule / Document AI respetan las autorizaciones del usuario operador: **no eleva privilegios**.
- Sujeto a la **fair-use policy** y consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- SAP Help Portal — SAP Document AI: https://help.sap.com/docs/SAP_DOCUMENT_AI

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 23 |
| Validación + documentación + KT | 11 |
| **Total** | **34** |
