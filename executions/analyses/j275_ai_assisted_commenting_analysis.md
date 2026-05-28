# Análisis caso de uso J275 — AI-Assisted Commenting

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP for Me). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite resumir comentarios existentes y reformular nuevos comentarios durante la autoría. Permite resumir comentarios por celda, agregarlos a lo largo de una jerarquía y recibir traducciones según el idioma del usuario. SAP indica reducciones del **80%** en tiempo para reformular, agregar/traducir descendientes y resumir/traducir comentarios por celda o hilo.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).
- Tenant SAC desplegado en un **data center que soporte SAP Business AI** **[verificar matriz de data centers vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Premium** — activación con **AI Units** (consumo registrado y consultable en SAP for Me).
- **AI Units** asignadas al tenant para esta feature **[verificar volumen vigente en Pricing Details]**.

### 1.3 Scope item relacionado
- No aplica scope item (SAP Analytics Cloud no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias / planning models donde se usen comentarios.
- Acceso a **SAP for Me** para administradores del tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Comentarios existentes (a nivel celda, hilo o jerarquía) en las historias / modelos donde se vaya a usar la capability.
- Configuración de comentarios habilitada en el modelo / historia.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: la capability soporta traducciones; idiomas soportados en función del modelo de IA subyacente **[verificar matriz vigente]**.
- **Disponibilidad regional**: depende del data center del tenant.
- **Roles**: el usuario debe tener permisos para leer/editar comentarios en las historias / modelos.

> **Setup oficial SAP**: el procedimiento documentado es el mismo que para otras features de IA de SAC:
> 1. Iniciar sesión en **SAP for Me**.
> 2. En el panel de navegación, elegir **Portfolio & Products**.
> 3. Elegir **Business AI**.
> 4. Seleccionar **Request Activation** junto al nombre de la feature.
>
> SAP Support notificará cuando la feature haya sido activada.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar que el tenant SAC está en un data center que soporta SAP Business AI | Tenant SAC | General | Consultor SAC + Consultor BTP | 1 |
| 2 | Confirmar entitlement de AI Units para SAC en el tenant del cliente | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Solicitar la activación de la feature *AI-Assisted Commenting* desde **SAP for Me** → *Portfolio & Products* → *Business AI* → *Request Activation* | SAP for Me — Request Activation | General | Consultor SAC + Cliente Admin | 1 |
| 4 | Esperar notificación de SAP Support sobre la activación | (Solicitud SAP Support) | General | (gestión con SAP Support) | 0 |
| 5 | Verificar que la capability de comentarios esté habilitada en las historias / modelos objetivo | Configuración SAC – Comments | Particular (por historia / modelo) | Consultor SAC | 2 |
| 6 | Asignar a los usuarios los roles SAC con permisos sobre comentarios | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 7 | Pruebas iniciales con un usuario piloto (resumir, reformular y traducir comentarios) | Configuración funcional SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas (excluyendo tiempo de SAP Support para activar la feature).**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con comentarios reales del cliente (resumen, reformulación, traducción y agregación por jerarquía) | Consultor SAC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La activación **no es self-service**: requiere **solicitud a SAP Support** vía SAP for Me. El tiempo de respuesta de SAP no es controlable.
- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- **Confirmar el data center** del tenant: solo data centers compatibles con SAP Business AI ofrecen la feature.
- Las traducciones y reformulaciones son **asistencia**: el usuario debe revisar el resultado, especialmente en contextos sensibles (planning narrative, comentarios contractuales).
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar idiomas / funcionalidades disponibles.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8dcc1f1915b241b3a10c8e5b8a76b062.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |
