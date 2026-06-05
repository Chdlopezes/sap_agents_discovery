# Análisis caso de uso J597 — Back Order Processing

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J597 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/
- Initial Setup (SAP Help Portal — Joule Capabilities Guide, Executing Backorder Processing (BOP) Run): https://help.sap.com/docs/joule/capabilities-guide/executing-backorder-processing-bop-run?version=CLOUD
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución de Back Order Processing (BOP) mediante interacciones en lenguaje natural.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** con Joule.
- Proceso de **Back Order Processing (BOP)** de Order Fulfillment.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe tener asignado el business catalog **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)**.
- La fuente indica que el rol de negocio **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)** es una de las plantillas que contienen ese business catalog por defecto.
- La fuente referencia el documento **Maintain Business Roles** para comparar/ajustar roles existentes con la última plantilla SAP.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Public Edition** (fuente: Joule Capabilities Guide para Public Edition).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activar SAP Business AI y asignar usuarios a Joule (paso general "Activating Business AI and Assigning Users") | Activación de Business AI / asignación de usuarios | General | Consultor Funcional SAP S/4HANA + Seguridad | 3 |
| 2 | Asignar el business catalog **Order Fulfillment Manager (SAP_BR_ORDER_FULFILLMNT_MNGR)** a los usuarios objetivo (rol de negocio del mismo nombre); si se usan roles existentes, compararlos con la plantilla SAP vigente (Maintain Business Roles) | Business Catalog / Business Role | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (ejecutar un BOP run vía Joule) | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (Order Fulfillment) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente recomienda comparar los roles existentes con la última plantilla SAP y ajustarlos según se requiera para la capability BOP de Joule.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/
- SAP Help Portal — Initial Setup (Joule Capabilities Guide — Executing Backorder Processing (BOP) Run): https://help.sap.com/docs/joule/capabilities-guide/executing-backorder-processing-bop-run?version=CLOUD
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
