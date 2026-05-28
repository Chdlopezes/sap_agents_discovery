# Análisis caso de uso J471 — AI-Assisted Calculations

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center, SAP for Me). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos, y explicar fórmulas existentes en lenguaje claro. SAP indica una reducción del **60% en el tiempo de creación de cálculos** y **60% en el tiempo de comprensión** de cálculos.

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
- **SAP Analytics Cloud** con historias (*stories*) y modelos analíticos donde se vayan a usar los cálculos asistidos.
- Acceso a **SAP for Me** para administradores del tenant SAC.

### 1.5 Datos maestros / transaccionales previos
- Modelos y datasets de SAC publicados con métricas, dimensiones y jerarquías necesarias para crear los cálculos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: el diálogo asistido por IA está principalmente en **inglés** **[verificar matriz vigente]**.
- **Disponibilidad regional**: depende del data center del tenant.
- **Roles**: el usuario debe tener permisos para crear/editar cálculos en SAC.

> **Setup oficial SAP**: el procedimiento documentado consiste en:
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
| 3 | Solicitar la activación de la feature *AI-Assisted Calculations* desde **SAP for Me** → *Portfolio & Products* → *Business AI* → *Request Activation* | SAP for Me — Request Activation | General | Consultor SAC + Cliente Admin | 1 |
| 4 | Esperar notificación de SAP Support sobre la activación | (Solicitud SAP Support) | General | (gestión con SAP Support) | 0 |
| 5 | Asignar a los usuarios los roles SAC con permisos para crear/editar cálculos | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 6 | Pruebas iniciales con un usuario piloto (crear y explicar cálculos en historias representativas) | Configuración funcional SAC | General | Consultor SAC | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~9 horas (excluyendo tiempo de SAP Support para activar la feature).**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con cálculos reales del cliente (creación y explicación de fórmulas representativas) | Consultor SAC | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAC | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAC | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La activación **no es self-service** dentro del tenant: requiere **solicitud a SAP Support** vía SAP for Me. El tiempo de respuesta de SAP no es controlable por el equipo de implementación.
- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- **Confirmar el data center** del tenant: solo data centers compatibles con SAP Business AI ofrecen la feature.
- Las fórmulas generadas deben ser **validadas funcionalmente** por el usuario antes de usarse en producción: la IA es asistencia, no reemplaza el control de calidad analítico.
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes para confirmar funcionalidades disponibles vs. planificadas.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8dcc1f1915b241b3a10c8e5b8a76b062.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
