# Análisis caso de uso J25 — Natural Language Query

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Función de IA generativa de **SAP Analytics Cloud (SAC)** que democratiza la analítica permitiendo solicitar datos mediante lenguaje natural. SAP indica una reducción del **80% del tiempo** para acceder a información relevante.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC sin necesidad de paquete Premium adicional **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias / modelos publicados sobre los que se quiera consultar.

### 1.5 Datos maestros / transaccionales previos
- Modelos / datasets de SAC publicados con métricas, dimensiones y jerarquías correctamente configuradas.
- Nombres / descripciones consistentes en el modelo para que la consulta en lenguaje natural funcione correctamente.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: la consulta en lenguaje natural está disponible principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: el usuario debe tener permisos de visualización sobre los modelos / historias consultadas.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de SAP Analytics Cloud.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Verificar la calidad / nomenclatura de los modelos donde se usará la consulta en lenguaje natural | Modelos SAC | Particular (por modelo) | Consultor SAP Analytics Cloud | 3 |
| 3 | Asignar a los usuarios objetivo los roles SAC con permisos sobre los modelos / historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (consultas representativas en lenguaje natural) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (varios dominios / niveles de complejidad) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + buenas prácticas de prompting) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La calidad de las respuestas depende directamente de la **calidad de los modelos**: nomenclatura clara, jerarquías y métricas bien definidas.
- Joule / SAC respetan las autorizaciones del usuario: **no eleva privilegios**.
- Definir **buenas prácticas de prompting** y publicar ejemplos al inicio para acelerar adopción.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas y funcionalidades disponibles.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |
