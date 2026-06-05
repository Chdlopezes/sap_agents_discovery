# Análisis caso de uso J934 — Smart Personalization of My Home for Applications

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J934 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html?version=2602.500
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/2ae43f58ee664e288374b59db9b95bc9.html?version=2602.500
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/#pricing

**Resumen del caso:** Ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a My Home para acceso directo desde la página inicial.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units. La oferta solo puede adquirirse como parte del paquete Joule Premium for Financial Management y no está disponible por separado; el paquete se adquiere mediante AI Units. Precio bajo solicitud; duración de contrato disponible bajo solicitud.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Administrators can enable the AI-assisted smart personalization of My Home for applications. Users can then enter their queries in natural language to find and add applications and insights tiles to the My Home in SAP S/4HANA Cloud Public Edition. Their business users need to have the following business catalog assigned: SAP Business AI - My Home - Smart App Finder – Display (SAP_CORE_BC_AIU_PRO_PC) To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required. Please consult your SAP account executive for more information. Log on as an administrator to SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system. To assign the IAM app to the business role, proceed as follows:

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Display IAM Apps app. | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Open the Maintain Business Roles app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Open the Business Catalogs app. | Configuración de SAP S/4HANA Cloud Public Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~9 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor Funcional SAP S/4HANA | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor Funcional SAP S/4HANA | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Aplica a SAP S/4HANA Cloud **Public Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/3b78db8727f541ab88e59f9c44f4c377.html?version=2602.500
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/2ae43f58ee664e288374b59db9b95bc9.html?version=2602.500
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 9 |
| Validación + documentación + KT | 11 |
| **Total** | **20** |
