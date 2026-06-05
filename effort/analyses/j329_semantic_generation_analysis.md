# Análisis caso de uso J329 — Semantic Generation

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J329 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html
- AI Feature (SAP Help Portal): https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/2fc1d26ebff748e4905d724247d33531.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/#pricing

**Resumen del caso:** Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas. El onboarding semántico toma tablas, contenido y semántica asociada como monedas, unidades, medidas, hechos, dimensiones y asociaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Datasphere**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Requiere AI Units para usar la oferta de IA en el servicio cloud subyacente. El método de activación indicado es “Activate with AI Units”. Precio bajo solicitud; duración de contrato disponible bajo solicitud. Incluye prerrequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): You must complete the following Joule configuration procedures before activating Joule in SAP Datasphere.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Create Your SAP Datasphere Service Instance in SAP BTP | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 2 | Configure the Size of Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 3 | Review and Manage Links to SAP Analytics Cloud and SAP Business Data Cloud Tenants | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 4 | Enable SAP HANA for SQL Data Warehousing on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 5 | Enable the SAP HANA Cloud Script Server on Your SAP Datasphere Tenant | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 6 | Enable SAP Business AI for SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 7 | Enable Choropleth Layers for Geographical Visualizations | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |
| 8 | Create OAuth2.0 Clients to Authenticate Against SAP Datasphere | Configuración de SAP Datasphere | General | Consultor SAP Datasphere | 4 |

**Esfuerzo total estimado (activación / configuración): ~32 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Datasphere | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Datasphere | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Datasphere | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/1b3fe45f38df4db1a9cda97a5a7bcdaf.html
- SAP Help Portal — AI Feature: https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/2fc1d26ebff748e4905d724247d33531.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 32 |
| Validación + documentación + KT | 11 |
| **Total** | **43** |
