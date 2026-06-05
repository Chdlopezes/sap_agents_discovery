# Análisis caso de uso J108 — AI-Assisted Search

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J108 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- Initial Setup (SAP Help Portal — Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- AI Feature (SAP Help Portal — Natural Language Search): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/04170c64c1004fc58d7f235aea0e4970.html?locale=en-US&state=PRODUCTION&version=cloud
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

**Resumen del caso:** Habilita consultas de búsqueda en lenguaje natural directamente en SAP Datasphere (repository explorer, data builder, catalog y data marketplace). La búsqueda aumentada con IA interpreta solicitudes complejas y devuelve resultados sobre los objetos y artefactos del tenant.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): activación mediante **AI Units**; precio bajo solicitud (métrica Flat Fee). Se requieren AI Units para usar la oferta en el servicio cloud subyacente.

### 1.3 Scope item relacionado
- No aplica (SAP Datasphere no utiliza scope items de SAP S/4HANA).

- Según el Initial Setup oficial ("Enable SAP Business AI for SAP Datasphere"), para habilitar SAP Business AI se debe contar con un **rol global** que otorgue los privilegios requeridos; la fuente indica que el rol global **DW Administrator**, por ejemplo, otorga esos privilegios.
- SAP Business AI es un servicio gestionado por SAP; se habilita SAP Business AI y Joule para SAP Datasphere para integrar recomendaciones de contenido de IA.
- Según la página **AI Feature** oficial ("Natural Language Search"), para usar la búsqueda en lenguaje natural ésta debe estar habilitada en el tenant (ver *Enable SAP Business AI for SAP Datasphere*) y el usuario debe tener **un rol scoped y un rol global** a la vez:
  - **Rol scoped** con los privilegios *Data Warehouse General (-R------)* —acceder a SAP Datasphere— y *Spaces Files (-R------)* —acceder a objetos de un espacio.
  - **Rol global** con el privilegio *Data Warehouse AI Consumption (----E---)* —usar las funciones de SAP Business AI.
  - Las plantillas **DW Modeler** (scoped) y **DW AI Consumer** (global), aplicadas juntas, otorgan estos privilegios.
- La búsqueda en lenguaje natural está disponible en el **Repository Explorer**, la página de inicio del **Data Builder** y el **Source Browser** (según la página AI Feature).

### 1.5 Datos maestros / transaccionales previos
- Artefactos de datos del tenant (modelos, vistas, objetos, espacios) sobre los que realizar la búsqueda.

### 1.6 Restricciones funcionales / técnicas / idioma
- Según la página **AI Feature** oficial, la búsqueda en lenguaje natural está **soportada solo en inglés** (puede arrojar resultados utilizables en otros idiomas, sin garantía).
- El uso de lenguaje natural depende de la longitud de la cadena: con **una palabra** no se usa; con **dos palabras** se usa solo si la búsqueda estándar no devuelve resultados; con **tres o más palabras** se usa siempre.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Asignar al usuario un **rol scoped** (*DW Modeler*: privilegios Data Warehouse General y Spaces Files) **y un rol global** (*DW AI Consumer*: privilegio Data Warehouse AI Consumption) que habiliten el uso de SAP Business AI | Roles scoped y globales / privilegios de SAP Datasphere | Particular (por usuario / rol) | Consultor Seguridad SAP Datasphere | 3 |
| 2 | **Habilitar SAP Business AI y Joule para SAP Datasphere** (Enable SAP Business AI for SAP Datasphere) | Configuración del tenant (System → Configuration) | General | Consultor SAP Datasphere | 3 |
| 3 | Confirmar el entitlement de **AI Units** para el tenant | AI Units | General | Consultor BTP / Licencias | 2 |

**Esfuerzo total estimado (activación / configuración): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (búsquedas en lenguaje natural sobre artefactos del tenant) | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura por **AI Units** (precio bajo solicitud, métrica Flat Fee), según *Pricing Details*.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/
- SAP Help Portal — Initial Setup (Enable SAP Business AI for SAP Datasphere): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html?locale=en-US
- SAP Help Portal — AI Feature (Natural Language Search): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/04170c64c1004fc58d7f235aea0e4970.html?locale=en-US&state=PRODUCTION&version=cloud
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
