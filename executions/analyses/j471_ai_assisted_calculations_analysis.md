# Análisis caso de uso J471 — AI-Assisted Calculations

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J471 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/#pricing

**Resumen del caso:** Permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos de SAP Analytics Cloud, y también explicar fórmulas existentes en lenguaje claro.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Analytics Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activación mediante AI Units. Precio bajo solicitud AI Units requeridas actualmente para usar esta oferta de IA en el servicio cloud subyacente. Tiene prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Your SAP Analytics Cloud tenant is on a data center that supports SAP Business AI. You've purchased the SAP AI Units license. For more information about the SAP AI Units license, contact your Account Executive.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Configure System Settings | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 2 | Enable AI-Assisted Features for SAP Analytics Cloud | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 3 | Configure Data Storage for Planning | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 4 | Enable Bring Your Own Key Encryption with SAP Analytics Cloud and SAP Data Custodian | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 5 | Set Up Third-Party Access with OAuth Clients | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |
| 6 | Configure Email Server | Configuración de SAP Analytics Cloud | General | Consultor SAP Analytics Cloud | 4 |

**Esfuerzo total estimado (activación / configuración): ~24 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/8dcc1f1915b241b3a10c8e5b8a76b062.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 24 |
| Validación + documentación + KT | 11 |
| **Total** | **35** |
