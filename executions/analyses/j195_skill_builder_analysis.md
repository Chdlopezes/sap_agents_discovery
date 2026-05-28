# Análisis caso de uso J195 — Skill Builder

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** **Joule Studio** permite extender Joule mediante **skills** ajustadas a necesidades de negocio. Las skills ejecutan operaciones predefinidas desde la interfaz conversacional de Joule y pueden integrarse con sistemas SAP y no SAP. El valor se centra en reducir el tiempo para desplegar skills personalizadas y disminuir tareas repetitivas mediante automatización conversacional.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado en el tenant del cliente.
- **Joule Studio** (suscripción activa).
- **SAP Build** y, opcionalmente, **SAP Build Process Automation** (según el booster recomendado por SAP).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripciones vigentes a **Joule** y **Joule Studio**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **Joule Studio** desplegado en BTP.
- **SAP Build** / SAP Build Process Automation (cuando se use el booster oficial para conectar Joule).
- Sistemas SAP / no SAP destino con APIs / connectivity disponibles.

### 1.5 Datos maestros / transaccionales previos
- Definición de los escenarios donde se ejecutarán las skills (operaciones, sistemas destino, datos de entrada / salida).
- Conectividad a los sistemas destino configurada (destinations / communication arrangements).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: developers / administradores con permisos sobre Joule Studio y los sistemas destino.

> **Setup oficial SAP**: la página https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html describe los escenarios de setup de Joule Studio. Una opción indicada es ejecutar un **booster** para conectar Joule con SAP Build Process Automation, luego asignar usuarios a roles y preparar capacidades de IA.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlements de Joule y Joule Studio en SAP BTP | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Ejecutar el **booster** oficial para preparar la integración Joule ↔ SAP Build Process Automation (cuando aplique) | Booster BTP | General | Consultor BTP / Joule Studio | 4 |
| 3 | Asignar a los developers los roles administrativos / de developer en Joule Studio | Roles Joule Studio | Particular (por usuario / grupo) | Consultor Seguridad BTP | 2 |
| 4 | Configurar las **destinations** y conectividad a los sistemas destino que usarán las skills | Destinations BTP | Particular (por sistema destino) | Consultor BTP | 4 |
| 5 | Definir y desarrollar las **skills** iniciales para los escenarios objetivo | Skill (Joule Studio) | Particular (por skill) | Consultor Joule Studio / Developer | 8 |
| 6 | Pruebas iniciales end-to-end de las skills desde la UI de Joule | Configuración funcional Joule | General | Consultor Joule Studio + Funcional | 4 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~24 horas.**

> **Nota**: el esfuerzo del paso 5 depende del **número y complejidad** de las skills a desarrollar. La estimación corresponde a un conjunto inicial reducido.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria end-to-end por cada skill desarrollada (incluyendo autorizaciones y manejo de error) | Consultor Joule Studio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual técnico de las skills) | Consultor Joule Studio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica + sesión funcional) | Consultor Joule Studio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability de **desarrollo / extensión**: requiere governance sobre quién define y aprueba skills antes del rollout.
- Las skills **operan sobre datos productivos**: validar autorizaciones y manejo de error antes del go-live.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**, pero las skills deben respetar el principio de mínimo privilegio en sus destinations.
- Considerar **monitorización y auditoría** de skills en producción.
- Sujeto a la **fair-use policy** de Joule **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- El esfuerzo aquí cubre la **activación + un conjunto inicial reducido de skills**; cada skill adicional requiere esfuerzo adicional fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- SAP Help Portal — Joule Studio Setup: https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |
