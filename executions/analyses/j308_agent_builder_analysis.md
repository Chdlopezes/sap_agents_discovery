# Análisis caso de uso J308 — Agent Builder

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J308 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/
- Initial Setup (SAP Help Portal — Joule Studio, Initial Setup and Prerequisites): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite construir agentes de Joule (en Joule Studio) para automatizar procesos de negocio complejos. Los agentes pueden ejecutar flujos adaptativos, razonar, planificar y coordinar procesos.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **Joule Studio** (parte de SAP Build).
- La fuente describe la integración de Joule Studio con **SAP Build**.

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base**.
- La fuente exige una licencia de Joule (base o superior): **Joule Base (SKU 8019544)** o **Joule Premium (SKU 8019164)** (este último incluye AI Units).
- No aplica un paquete Premium específico para este caso (clasificado como Base).

### 1.3 Scope item relacionado
- No aplica (el producto base — Joule Studio / SAP Build — no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial (Prerequisites for Customers):
  - Suscripción a **SAP Build** con el service plan **build-default**.
  - **Licencia de usuario activo (developer)** para construir, probar y desplegar las skills/agentes propios de Joule.
  - Modelo comercial unificado de SAP Build, disponible en cuatro modalidades: **Subscription, BTPEA (BTP Enterprise Agreement), PAYG (Pay As You Go), CPEA (Cloud Platform Enterprise Agreement)**.

### 1.5 Datos maestros / transaccionales previos
- No documentado en la fuente oficial.

### 1.6 Restricciones funcionales / técnicas / idioma
- La fuente distingue prerrequisitos para **clientes** y para **partners**; este análisis recoge la vía de cliente.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar la suscripción a SAP Build (service plan build-default), la licencia de usuario developer y la licencia de Joule (Base SKU 8019544 o Premium SKU 8019164) | Suscripción / entitlement SAP Build + Joule | General | Consultor SAP BTP / Licencias | 4 |
| 2 | Configurar Joule Studio según el escenario aplicable ("Setup Scenarios for Joule Studio" → "Set Up Joule Studio") | Joule Studio (SAP Build) | General | Consultor SAP Build / Joule Studio | 4 |
| 3 | Asignar usuarios a los roles ("Assign Users to Roles") | Roles de SAP Build / Joule Studio | Particular (por usuario / rol) | Consultor Seguridad / SAP Build | 3 |
| 4 | Crear AI capabilities y/o un Action Project ("Create AI Capabilities" / "Create an Action Project") como base para construir los agentes | AI Capabilities / Action Project en Joule Studio | General | Consultor SAP Build / Joule Studio | 4 |

**Esfuerzo total estimado (activación / configuración): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (construir, probar y monitorear una capability/agente) | Consultor SAP Build / Joule Studio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Build / Joule Studio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Build / Joule Studio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente advierte (Caution) sobre la correcta combinación de suscripciones y licencias para evitar problemas de compatibilidad al activar y usar los servicios de SAP Build.
- La documentación de Joule Studio incluye además los bloques "Building Capabilities for Joule", "Managing Joule Studio Projects", "Monitor AI Capabilities" y "Security" como parte del ciclo de vida del agente.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/
- SAP Help Portal — Initial Setup (Joule Studio — Initial Setup and Prerequisites): https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/b323c5a639a5428eb05fdafcca9bc9df.html
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 11 |
| **Total** | **26** |
