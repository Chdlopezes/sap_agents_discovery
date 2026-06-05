# Análisis caso de uso J135 — Conversational Planning

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J135 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/
- Initial Setup (SAP Help Portal): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/ae5ea1c82b2f48e2874f94783c6ea0ae.html?locale=en-US
- Pricing Details (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/#pricing

**Resumen del caso:** Apoya a los planificadores en la creación de planes de transporte eficientes, incluyendo cadenas de acciones con múltiples instrucciones, mediante lenguaje natural en el transportation cockpit. El cockpit puede mostrar los requerimientos de planificación y las capacidades disponibles.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP S/4HANA Cloud Private Edition**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Premium**.
- Paquete comercial: **Joule Premium for Supply Chain Management**.
- Pricing (sección *Pricing Details* de la Detail Page): Esta oferta de IA solo puede adquirirse como parte del paquete 'Joule Premium for Supply Chain Management' y no está disponible por separado; los precios corresponden al paquete completo. Descripción del paquete: impulsa la agilidad de la cadena de suministro con IA premium que optimiza la programación de mantenimiento, mitiga disrupciones en planta y acelera la planificación de transporte, entre otros. Pricing del paquete por métrica 'Users': hasta 39 usuarios → 8 AI Units por métrica (tarifa EUR 7 por AI Unit; EUR 56 por métrica); hasta 200 → 7,2; hasta 550 → 6,5; hasta 1.000 → 5,7; desde 1.000 → 5. Incluye hasta 5.200 requests sin costo adicional; las solicitudes adicionales se cobran en bloques de 1.000 a 2 AI Units.

### 1.3 Scope item relacionado
- No documentado en la fuente oficial.

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según la fuente oficial abierta: Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your SAP account executive for more information. You have configured the settings related to Intelligent Scenario Lifecycle Management (ISLM) that are required to use generative AI in Transportation Management (TM). First, you have requested an SAP Business Technology Platform (SAP BTP) service key for the intelligent scenario GENAI_TM_COPL_GPT40. Make sure you have noted down the name of the intelligent scenario, as you will need it later in the setup process. For more information, see Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP). Then you have performed the subsequent steps. For more information, see Customizing for Transportation Management under Basic Functions  Generative Artificial Intelligence. For more information about ISLM setup, see SAP Delivered Generative AI Scenarios. You have defined a generative AI profile of type Conversational Planning (conversational planning profile). In this profile, you have indicated one or several capabilities, that is, planning operations, that you would like to perform in the transportation cockpit using generative AI.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- Disponible para SAP S/4HANA Cloud **Private Edition**.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Select all freight orders going to Spain | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 2 | Select the truck with the highest weight capacity | Configuración de SAP S/4HANA Cloud Private Edition | General | Consultor Funcional SAP S/4HANA | 3 |
| 3 | Assign freight units to freight orders | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 4 | Assign freight units to trucks | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 5 | Assign trucks to freight orders | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |
| 6 | Assign all freight units from New York to the small truck | Configuración de SAP S/4HANA Cloud Private Edition | Particular (por usuario / rol) | Consultor Funcional SAP S/4HANA | 3 |

**Esfuerzo total estimado (activación / configuración): ~18 horas.**

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
- Restringido a SAP S/4HANA Cloud **Private Edition**.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/
- SAP Help Portal — Initial Setup: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/ae5ea1c82b2f48e2874f94783c6ea0ae.html?locale=en-US
- SAP Discovery Center — Pricing Details: https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/#pricing

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 11 |
| **Total** | **29** |
