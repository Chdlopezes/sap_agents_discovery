# Análisis caso de uso J886 — Smart Insights

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que analiza desviaciones y puntos de datos dentro del modelo subyacente para entregar explicaciones en texto y visualizaciones asociadas. El valor se centra en acelerar el análisis de causas y desviaciones.

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
- **SAP Analytics Cloud** con historias / modelos publicados sobre los que se aplican los insights.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con métricas y dimensiones suficientes para producir explicaciones significativas.
- Datos consistentes y agregados al nivel de granularidad esperado.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: explicaciones según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: usuario SAC con permisos para consumir / analizar las historias.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html describe las capacidades inteligentes de SAC.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar la calidad y granularidad de los modelos donde se aplicarán Smart Insights | Modelos SAC | Particular (por modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (Smart Insights sobre desviaciones representativas) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (explicaciones sobre escenarios representativos) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las explicaciones son **descriptivas**: el usuario sigue siendo responsable de validar las causas reales con conocimiento del negocio.
- La calidad depende **directamente de la calidad de los modelos** y de la consistencia de la data.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/
- SAP Help Portal — Smart Features in SAC: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
