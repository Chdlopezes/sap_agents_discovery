# Análisis caso de uso J195 — Skill Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J195 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite extender Joule mediante skills ajustadas a necesidades de negocio. Las skills ejecutan operaciones predefinidas desde la interfaz conversacional de Joule y pueden integrarse con sistemas SAP y no SAP.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule Studio**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: An outline of the required subscriptions, licenses, and supported environments for both customers and partners using Joule Studio. Understanding these requirements ensures proper activation and use of SAP Build services and avoids compatibility issues. You have subscribed to SAP Build with the build-default service plan. An active user (developer) license is required to build, test, and deploy your custom Joule skills. For more information about the active user (developer) license for SAP Build, refer to SAP Build - Service Plans and Metering. You have any of the following Joule (base or higher) licenses: Joule Premium (SKU 8019164) (Includes AI Units)

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Set Up Joule Studio | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 2 | Assign Users to Roles | Configuración de Joule Studio | Particular (por usuario / rol) | Consultor SAP Joule Studio / BTP | 3 |
| 3 | Create AI Capabilities | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 4 | Create an Action Project | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |
| 5 | Activate the SAP Build Process Automation service, ensuring you select the build-default plan during setup. | Configuración de Joule Studio | General | Consultor SAP Joule Studio / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP Joule Studio / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Joule Studio / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Joule Studio / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |
