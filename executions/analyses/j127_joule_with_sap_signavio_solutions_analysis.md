# Análisis caso de uso J127 — Joule with SAP Signavio solutions

> Análisis construido **únicamente** a partir de las fuentes oficiales de SAP asociadas al AI Feature/Agent J127 en `processed/AI_Features_Data_Enriched.xlsx`. Los campos para los que SAP no publica información aparecen literalmente como "No aplica", "No existe en la fuente oficial" o "No documentado en la fuente oficial". **No se ha completado ningún dato con conocimiento general ni con inferencia desde casos similares.**

**Fuentes oficiales consultadas:**
- Detail Page (SAP Discovery Center): https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/
- Initial Setup (SAP Help Portal — Joule in SAP Signavio solutions): https://help.sap.com/docs/signavio-process-transformation-suite/joule-in-sap-signavio-solutions-dcd44974e9b24ca684923bc484d954c2/joule-in-sap-signavio-solutions
- Pricing Details (SAP Discovery Center): No aplica

**Resumen del caso:** Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural con Joule.

---

## 1. Prerequisitos para la activación

### 1.1 Producto / componente SAP requerido
- **SAP Signavio solutions** (SAP Signavio Process Transformation Suite).

### 1.2 Licenciamiento / entitlement / paquete
- Capability **Base** (clasificación del XLSX).
- La fuente indica que el acceso a Joule en Signavio **puede requerir entitlement y autorización adicionales** (consultar al account executive) y describe modalidades **Base/Premium consumiendo AI Units**.

### 1.3 Scope item relacionado
- No aplica (SAP Signavio no utiliza scope items de SAP S/4HANA).

### 1.4 Aplicaciones / apps Fiori / servicios / componentes técnicos
- Según el Initial Setup oficial, para usar esta capacidad se debe **crear un user group en SAP Cloud Identity Services** y contar con un **rol de administrador en el tenant** conectado a Joule con SAP Signavio.
- La fuente remite al paso 8 del procedimiento **"Integration with SAP Signavio Solutions"**.
- Opcionalmente, para la capacidad de tipo informacional con document grounding, se debe **configurar Document Grounding** (Set Up Document Grounding).

### 1.5 Datos maestros / transaccionales previos
- Contenido de Signavio (diagramas de proceso, diccionario, documentos, métricas) sobre el que operar.

### 1.6 Restricciones funcionales / técnicas / idioma
- El acceso a Joule en SAP Signavio puede requerir entitlement/autorización adicionales.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar el entitlement/autorización para Joule en SAP Signavio (consultar al account executive) | Entitlement / autorización | General | Consultor SAP Signavio | 3 |
| 2 | Crear el user group en **SAP Cloud Identity Services** y asegurar el rol de administrador en el tenant conectado a Joule (procedimiento "Integration with SAP Signavio Solutions", paso 8) | SAP Cloud Identity Services / tenant | General | Consultor SAP Signavio + BTP/Identidad | 4 |
| 3 | (Opcional) Configurar **Document Grounding** para la capacidad informacional que usa documentos propios | Document Grounding | General | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (activación / configuración): ~10 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria del caso de uso con datos reales en entorno de Quality (consultas en lenguaje natural sobre diagramas, diccionario, documentos y métricas) | Consultor SAP Signavio | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + manual de configuración) | Consultor SAP Signavio | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SAP Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- La fuente describe variantes de capacidad **Base/Premium** con consumo de **AI Units**.
- El document grounding es opcional y sirve para añadir contexto propio a las respuestas de Joule.
- Disponibilidad indicada por SAP: **Generally Available**.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/
- SAP Help Portal — Initial Setup (Joule in SAP Signavio solutions): https://help.sap.com/docs/signavio-process-transformation-suite/joule-in-sap-signavio-solutions-dcd44974e9b24ca684923bc484d954c2/joule-in-sap-signavio-solutions
- SAP Discovery Center — Pricing Details: No aplica

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 10 |
| Validación + documentación + KT | 11 |
| **Total** | **21** |
