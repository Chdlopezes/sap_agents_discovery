# Análisis caso de uso J89 — Configuration for US Tax Jurisdictions

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J89 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/
- Initial Setup / AI Feature (SAP Help Portal — *Resources* enlaza ambos a la misma página oficial): https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/eecd222f00914c058e3268c8aed1f112.html
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/#pricing

**Resumen del caso:** Permite a los contadores de impuestos agilizar la configuración de sales & use tax para Estados Unidos mediante automatización inteligente. Utiliza modelos de lenguaje (LLMs) para extraer detalles de dirección a partir de entradas en lenguaje natural y determinar automáticamente la información de jurisdiction code, reduciendo drásticamente o eliminando el mantenimiento manual y mejorando la eficiencia operativa.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Public Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Financial Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Esta oferta de IA solo puede adquirirse como parte del paquete 'Joule Premium for Financial Management' y no está disponible por separado; los precios corresponden al paquete completo. Descripción del paquete: incrementa la eficiencia de los procesos financieros centrales con IA avanzada que acelera el cierre de periodo, mejora la gobernanza de datos maestros y reduce los días de ventas pendientes (DSO), entre otros. Pricing del paquete por métrica 'Users': hasta 39 usuarios → 8 AI Units por métrica (tarifa EUR 7 por AI Unit; EUR 56 por métrica); hasta 200 → 7,2; hasta 550 → 6,5; hasta 1.000 → 5,7; desde 1.000 → 5. Incluye hasta 5.200 requests sin costo adicional; las solicitudes adicionales se cobran en bloques de 1.000 a 2 AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según las fuentes oficiales abiertas (Initial Setup / AI Feature): Within the Upload Tax Rates configuration activity, open the Quick Config tab. In the Address field, enter the address or ZIP code for the location for which you need to configure the sales and use tax jurisdiction information. Based on the street address and/or ZIP code information you provide in the Address field, the AI returns the relevant jurisdiction information for you to review. The Tax Code and Jurisdiction information contains up to three levels of the relevant taxation information, that is, at the state, county, and ZIP code levels, as defined by that state's taxation authority. Once you've verified the location information, manually enter the corresponding tax rates and maintain the validity dates for each level. Then select Configure to save your changes. You can also manually maintain the District (description) and District Jurisdiction (indicator) fields. These together comprise an optional fourth level that is used as an indicator for local special use taxes. Typically, the District Jurisdiction indicator is left unfilled and by default is recorded as "0". In some cases, however, you need to add a character to indicate the special use tax. Examples of such taxes include the Metropolitan Commuter Transportation District surcharge in New York or the Historic Triangle Region sales tax surcharge in Virginia. When you perform any manual tax jurisdiction code maintenance with the AI configuration tool active, you must format the jurisdiction codes according to the SAP default structure. This is a 2-2-5-1 structure, where the first two characters are the state code, the second two characters are the county (or, in some states, independent city), the next 5 characters are the ZIP code, and the final character is a special use tax indicator, if applicable. The state codes are the postal abbreviations for the state (or territory), such as NVfor Nevada or GU for Guam. You can find the state and county codes attached to SAP Note 3613837 . When You Have Jurisdiction Codes in Your System

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Public Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Open this video in a new window | Configuración de SAP S/4HANA Cloud Public Edition | General | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~3 horas.**

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

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/
- SAP Help Portal — Initial Setup / AI Feature (misma página): https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/eecd222f00914c058e3268c8aed1f112.html
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 3 |
| Validación + documentación + KT | 11 |
| **Total** | **14** |
