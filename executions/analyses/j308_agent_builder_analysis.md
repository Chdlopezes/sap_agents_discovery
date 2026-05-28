# Análisis caso de uso J308 — Agent Builder (Joule Studio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite construir agentes de Joule para automatizar procesos de negocio complejos. Los agentes pueden ejecutar flujos adaptativos, razonar, planificar, coordinar procesos de varios pasos, invocar APIs, interactuar con documentos y colaborar con usuarios u otros agentes en sistemas SAP y no SAP. SAP indica: *Aporta eficiencia en escenarios que requieren toma de decisiones experta, manejo de excepciones y orquestación entre sistemas, especialmente donde la automatización determinística no es suficiente.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **Joule Studio** en SAP Business Application Studio / herramienta equivalente vigente.
- **SAP BTP** con entitlement de Joule.
- Acceso a las APIs/skills SAP o de terceros que el agente vaya a orquestar.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement de **Joule Studio / Agent Builder** (Premium) **[verificar AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- N/A (capability de desarrollo/diseño).

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Joule Studio UI.
- Conectividad a sistemas backend (S/4HANA, BTP services, etc.) vía destinations.

### 1.5 Datos maestros / transaccionales previos
- Catálogo de skills/APIs disponibles configurado.
- Plantillas de prompt / herramientas base.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Developer / Agent Designer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement de Joule Studio / Agent Builder | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar destinations a sistemas backend | Destinations BTP | Particular (por backend) | Consultor BTP / Integración | 4 |
| 3 | Asignar roles Developer / Agent Designer a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Validar catálogo de skills/APIs disponibles | Configuración Joule Studio | General | Consultor Funcional + Joule | 3 |
| 5 | Construir agente de muestra y desplegarlo | Configuración Agent Builder | Particular (por agente diseñado) | Desarrollador Agent Designer | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del agente con flujos representativos | Agent Designer | 5 |
| 2 | Documentación (catálogo de skills + diagrama del agente) | Agent Designer | 4 |
| 3 | Transferencia de conocimiento | Agent Designer | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- El esfuerzo para construir agentes adicionales **no está incluido** (es por agente diseñado).
- Buenas prácticas: limitar scope inicial, asegurar guardrails y observabilidad.
- Cobertura de skills SAP evoluciona por wave.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 12 |
| **Total** | **29** |
