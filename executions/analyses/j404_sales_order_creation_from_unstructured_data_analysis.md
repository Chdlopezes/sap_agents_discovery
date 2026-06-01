# Análisis caso de uso J404 — Sales Order Creation from Unstructured Data

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J404 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/11193ef55baa4904a5b25bd639e51a0f.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/#pricing

**Resumen del caso:** La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes. Después de cargar el archivo, la información se procesa automáticamente para generar una solicitud de pedido de venta que luego puede convertirse en pedido.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Pricing Details indica que la función puede agregarse al AI Estimator para estimar la cantidad aproximada de AI Units y costos relacionados. No se muestra un importe fijo visible en la información extraída de la sección.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Manage Document AI Schema Registration Subscriptions For the set-up, for every SAP S/4HANA Cloud Public Edition tenant, one central tenant of SAP Document AI, Embedded Edition, can be integrated through scope item 7TC. For every SAP S/4HANA Cloud Public Edition tenant, a separate SAP Document AI tenant must be integrated. The integration includes one communication scenario for the UI integration for SAP Document AI FIORI applications into the SAP S/4HANA Cloud Public Edition launchpad and one communication scenario for the inbound and outbound API integration through technical user communication. To access this generative AI feature within SAP S/4HANA Cloud Public Edition, an additional entitlement and authorization may be required.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Install Additional Software | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Create Sales Orders - AI-Assisted Extraction | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/11193ef55baa4904a5b25bd639e51a0f.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
