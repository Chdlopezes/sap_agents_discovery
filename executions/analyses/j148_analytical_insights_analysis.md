# Análisis caso de uso J148 — Analytical Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **Joule** que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP, integrándose con **Just Ask** de SAP Analytics Cloud (SAC) dentro de SAP Business Data Cloud (BDC). SAP indica hasta **80% de reducción** en los pasos necesarios para obtener insights analíticos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule** habilitado y operativo.
- **SAP Analytics Cloud (SAC)** o **SAP Business Data Cloud (BDC)** con **Just Ask** configurado.
- **SAP Build Work Zone** desplegado para entregar la experiencia integrada al usuario.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **Joule**.
- Suscripción vigente a **SAP Analytics Cloud** y/o **SAP Business Data Cloud**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **Joule** integrado con SAC / BDC.
- **Just Ask** activado y con datos indexados.
- **SAP Build Work Zone** con tarjetas / launchpad del usuario configurados.
- **Identity Provisioning Service (IPS)** para sincronización de usuarios y roles.

### 1.5 Datos maestros / transaccionales previos
- Modelos / historias de SAC publicadas con datos consistentes.
- Datos indexados en **Just Ask** para que las preguntas en lenguaje natural devuelvan resultados.
- Roles y permisos sincronizados desde el directorio fuente hacia SAP Build Work Zone.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones soportadas principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: usuarios provisionados en SAP Build Work Zone con permisos SAC/BDC adecuados.
- **Integración**: requiere coexistencia funcional entre Joule, SAC/BDC, Just Ask y Work Zone.

> **Setup oficial SAP**: el procedimiento descrito en https://help.sap.com/docs/joule/integrating-joule-with-sap/enable-the-analytical-insights-capability-in-joule consiste en: habilitar la capability *Analytical Insights* en Joule, integrar SAC/BDC con Joule, sincronizar roles y permisos, provisionar usuarios hacia SAP Build Work Zone usando IPS, indexar datos con Just Ask y probar preguntas en lenguaje natural.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule, SAC/BDC y SAP Build Work Zone | Subaccount BTP + entitlements | General | Consultor BTP | 2 |
| 2 | Configurar la integración Joule ↔ SAC / BDC | Joule capability *Analytical Insights* + integración SAC/BDC | General | Consultor BTP + Consultor SAC | 4 |
| 3 | Configurar **SAP Build Work Zone** con las tarjetas / espacios necesarios | SAP Build Work Zone | General | Consultor SAP Build Work Zone | 3 |
| 4 | Sincronizar usuarios y roles vía **Identity Provisioning Service (IPS)** | IPS — Provisioning | Particular (por usuarios / grupos) | Consultor Seguridad / Identity | 3 |
| 5 | Indexar datos en **Just Ask** y validar que las consultas devuelvan resultados | Just Ask — Indexing | General | Consultor SAC | 4 |
| 6 | Asignar a los usuarios objetivo los roles con la capability habilitada | Roles SAC / BDC + Joule | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 7 | Pruebas iniciales end-to-end con un usuario piloto (preguntas desde Joule sobre datos de SAC/BDC) | Configuración funcional integrada | General | Consultor SAC + Consultor Joule | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~21 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria end-to-end con datos reales (preguntas representativas de varios dominios funcionales) | Consultor SAC + Consultor Joule | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración integrada) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + sesión técnica) | Consultor SAC + Consultor BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una integración **multi-producto**: Joule + SAC/BDC + Just Ask + SAP Build Work Zone + IPS. Confirmar disponibilidad y compatibilidad de versiones antes de planificar.
- La calidad de las respuestas depende de **modelos publicados y datos indexados** en Just Ask: invertir en metadatos y semántica.
- Joule respeta las autorizaciones del usuario: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de Joule y a las cuotas vigentes de SAC **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/joule/integrating-joule-with-sap/enable-the-analytical-insights-capability-in-joule

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 21 |
| Validación + documentación + KT | 11 |
| **Total** | **32** |
