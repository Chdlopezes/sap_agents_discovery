# Análisis caso de uso J180 — SAP HANA application migration

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J180 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/manually-migrate-xs-classic-application-to-sap-cap-and-sap-hana-cloud-a581b87f52d44d9d9e26b8005cd2ab68
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** La función automatiza la migración de la capa de servicios SAP HANA XS/XSA hacia SAP CAP usando GenAI. Ayuda a convertir artefactos como XSJSLIB, XSODATA y XSJS en servicios modernos basados en CAP, alineados con la guía de desarrollo de SAP BTP.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP HANA Cloud**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- No aplica un paquete Premium.

### 1.3 Scope item relacionado
- No aplica (el producto base no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: You need to provide details of the source instance of SAP HANA on-premise instance which contains the XS advanced applications that you want to migrate. You need access to an SAP BTP sub account where an HTTP destination is defined for the source SAP HANA platform database, which contains the XS advanced applications that you want to migrate. For more information about configuring the required destination, see the steps below. You must have a subscription to SAP Business Application Studio (BAS) or SAP Build. Generative-AI tools are only available in SAP Build plans, which you need to migrate the service layer. To migrate an XS advanced application to SAP CAP, you need to perform the following steps: Connect SAP Cloud Connector to the SAP BTP account where the subscription to SAP Business Application Studio was created.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- No documentado en la fuente oficial.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open the Cloud Connector and navigate to the correct sub account. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 2 | Add a service channel in the category On-premise to Cloud. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 3 | Configure the new On-premise to Cloud service channel as indicated below. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |
| 4 | Configure the mapping between the internal and virtual (Cloud-side) hosts. | Configuración de SAP HANA Cloud | General | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (activación / configuración): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality | Consultor SAP HANA Cloud / BTP | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP HANA Cloud / BTP | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP HANA Cloud / BTP | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/manually-migrate-xs-classic-application-to-sap-cap-and-sap-hana-cloud-a581b87f52d44d9d9e26b8005cd2ab68
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
