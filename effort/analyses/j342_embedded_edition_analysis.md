# Análisis caso de uso J342 — Embedded Edition

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J342 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_DOCUMENT_AI/5fa7265b9ff64d73bac7cec61ee55ae6/0d68dc0002f0484ba25f85f3170166e0.html?locale=en-US&state=PRODUCTION&version=SHIP
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/#pricing

**Resumen del caso:** Automatiza tareas de procesamiento documental de punta a punta, ejecución de workflows e integración de canales.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Document AI**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Pricing (sección *Pricing Details* de la Detail Page): Activación con AI Units. El detalle de pricing de Discovery Center muestra tarifas por volumen y permite agregar la feature a una estimación. Precio bajo solicitud. Pricing Details muestra: Up to 100,000 = 0.0786; Up to 300,000 = 0.0614; Up to 500,000 = 0.0443; From 500,000 = 0.0364. La unidad exacta no quedó explícita en el texto extraído. Se requieren AI Units para usar esta oferta de IA en el servicio cloud subyacente. La página indica que tiene prerequisito.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Service Plans and Metering You have set up your global account and at least one subaccount on SAP BTP. If you’re working in an enterprise account, you need to add quotas to the services you purchased in your subaccount before they appear in the service marketplace. Otherwise, only default free-of-charge services are listed. Quotas are automatically assigned to the resources available in trial accounts. For more information, see Configure Entitlements and Quotas for Subaccounts. SAP Document AI allows you to move subaccounts between your global accounts. For more information, see Relationship Between Global Accounts, Subaccounts, and Directories.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Enable X.509 Authentication | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 3 |
| 2 | Run SAP Document AI in a Multitenant Application | Configuración de SAP Document AI | General | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~6 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Document AI / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Document AI / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Document AI / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Caso **Premium**: el consumo se factura según el modelo de AI Units / paquete descrito en *Pricing Details* (ver sección 1.2).
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_DOCUMENT_AI/5fa7265b9ff64d73bac7cec61ee55ae6/0d68dc0002f0484ba25f85f3170166e0.html?locale=en-US&state=PRODUCTION&version=SHIP
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 6 |
| Validación + documentación + KT | 11 |
| **Total** | **17** |
