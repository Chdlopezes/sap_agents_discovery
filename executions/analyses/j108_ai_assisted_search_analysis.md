# Análisis caso de uso J108 — AI-Assisted Search

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Datasphere** que habilita consultas de búsqueda en lenguaje natural directamente en repository explorer, data builder, catalog y data marketplace. SAP indica una reducción del **90% en el tiempo** dedicado a solicitudes complejas de búsqueda de artefactos de datos.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Datasphere** (suscripción activa).
- Tenant de SAP Datasphere en un **landscape que soporte SAP Business AI** **[verificar matriz de landscapes vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Datasphere**.
- Capability **Premium** — activación con **AI Units**.
- Licencia de **AI Units** asignada al tenant **[verificar volumen vigente; precio bajo solicitud, métrica Flat Fee]**.
- Tenant **habilitado para SAP Business AI**.

### 1.3 Scope item relacionado
- No aplica scope item (SAP Datasphere no usa scope items de S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Datasphere** con repository explorer, data builder, catalog y data marketplace activos.
- **Joule** integrado con SAP Datasphere (el botón de Joule aparece en la shell bar para usuarios con privilegio adecuado).

### 1.5 Datos maestros / transaccionales previos
- Artefactos de datos del cliente cargados en el repository (modelos, vistas, tablas, espacios).
- Catalog y/o marketplace con metadatos suficientes para indexar y buscar.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: búsqueda en lenguaje natural principalmente en **inglés** **[verificar matriz vigente]**.
- **Roles**: rol global con privilegios *Data Warehouse General* y *System Information* (p. ej. **DW Administrator**) para configurar; **Data Warehouse AI Consumer** para los usuarios finales.
- **Disponibilidad**: depende del landscape del tenant.

> **Setup oficial SAP**: procedimiento documentado:
> 1. Ir a **System > Configuration**.
> 2. Abrir la pestaña **AI Services**.
> 3. En **AI Features**, marcar las opciones que se quieran usar.
> 4. **Guardar**.
> 5. Asignar a los usuarios el privilegio global **Data Warehouse AI Consumer**.
>
> Los usuarios con el privilegio requerido verán el botón de Joule en la shell bar.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar que el tenant de SAP Datasphere está habilitado para SAP Business AI y en landscape compatible | Tenant Datasphere | General | Consultor SAP Datasphere + BTP | 2 |
| 2 | Confirmar entitlement de AI Units para Datasphere | AI Units | General | Consultor BTP / Licencias | 2 |
| 3 | Habilitar AI Services en **System > Configuration > AI Services** y marcar las features a usar | Datasphere — AI Services | General | Consultor SAP Datasphere | 2 |
| 4 | Asignar el privilegio global **Data Warehouse AI Consumer** a los usuarios objetivo | Roles / Privilegios Datasphere | Particular (por usuario / grupo) | Consultor Seguridad SAP Datasphere | 3 |
| 5 | Pruebas iniciales con un usuario piloto (consultas en repository explorer, data builder, catalog, marketplace) | Configuración funcional Datasphere | General | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con consultas reales del cliente (búsquedas complejas sobre artefactos representativos) | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual breve de operación) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una capability **Premium** que consume **AI Units**: dimensionar el consumo durante el piloto.
- La calidad de la búsqueda depende de la **calidad de los metadatos** del repository/catalog: nombres, descripciones y tags consistentes mejoran los resultados.
- Joule respeta las autorizaciones del usuario en Datasphere: **no eleva privilegios**.
- Sujeto a la **fair-use policy** de IA y al consumo de AI Units **[verificar políticas vigentes]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
