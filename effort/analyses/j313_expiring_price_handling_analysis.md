# Análisis caso de uso J313 — Expiring Price Handling

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J313 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- Initial Setup (SAP Help Portal — Joule Capabilities Guide, Expiring Price Handling): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Capacidad de Joule para SAP S/4HANA Cloud Public Edition que permite a un especialista de precios gestionar la expiración de precios de forma más eficiente. El usuario puede pedir a Joule que recupere precios (condition records de pricing en ventas) próximos a expirar y los renueve extendiendo su periodo de validez y ajustando los importes o ratios de las condiciones.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition** con Joule.
- Funcionalidad de pricing en ventas (condition records); la fuente cita la app **Manage Prices - Sales** para abrir precios y detalles del job.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe tener asignado el business catalog **Master Data - Prices (SAP_SD_BC_PRICE_MANAGE_MC)**.
- La fuente indica que el rol de negocio **Pricing Specialist (SAP_BR_PRICING_SPECIALIST)** es una de las plantillas que contienen ese business catalog por defecto.
- App referenciada por la fuente: **Manage Prices - Sales**.

### 1.5 Datos maestros / transaccionales previos
- Condition records de pricing en ventas existentes (precios con periodos de validez), según la definición de "expiring prices" de la fuente.

### 1.6 Restricciones funcionales / técnicas / idioma
- Aplica a **SAP S/4HANA Cloud Public Edition** (la fuente es la Joule Capabilities Guide para Public Edition).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Activar SAP Business AI y asignar usuarios a Joule (paso general "Activating Business AI and Assigning Users" referenciado por la Joule Capabilities Guide) | Activación de Business AI / asignación de usuarios | General | Consultor Funcional SAP S/4HANA + Seguridad | 3 |
| 2 | Asignar el business catalog **Master Data - Prices (SAP_SD_BC_PRICE_MANAGE_MC)** a los usuarios objetivo (p. ej. mediante el rol **Pricing Specialist — SAP_BR_PRICING_SPECIALIST**) | Business Catalog / Business Role | Particular (por usuario / rol) | Consultor Seguridad SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (consultar precios por expirar, extender validez, ajustar importes, crear condition records, seguir el job) | Consultor Funcional SAP S/4HANA (SD / Pricing) | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA (SD / Pricing) | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA (SD / Pricing) | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente describe la capacidad como un flujo conversacional secuencial: mostrar precios por expirar (con criterios como condition type o sales organization), extender valid-to, ajustar importes/ratios y crear los nuevos condition records en un único job, con seguimiento del progreso.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/
- SAP Help Portal — Initial Setup (Joule Capabilities Guide — Expiring Price Handling): https://help.sap.com/docs/joule/capabilities-guide/renew-expiring-prices
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
