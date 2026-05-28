# Análisis caso de uso J358 — Processing of Incoming Quality Certificates with SAP Document AI

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition. SAP indica: *La página indica reducción del tiempo de procesamiento de certificados de calidad y protección de ingresos al disminuir retrasos de inspección relacionados con procesamiento documental.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP).
- Componente **QM – Quality Management** operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Public Edition con QM.
- Entitlement de **SAP Document AI** en BTP (capability **Premium** según AI Foundation Catalog) **[verificar pricing vigente]**.
- Entitlement de Joule si la interacción se hace vía copilot.

### 1.3 Scope item relacionado
- Scope items de Quality Management - Inspection (incoming certificates) — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Process Incoming Quality Certificates* / *Quality Inspection Worklist*.
- Communication arrangement S/4HANA Public ↔ Document AI (escenario **SAP_COM_xxxx** — **[verificar]**).

### 1.5 Datos maestros / transaccionales previos
- Maestros de materiales con vista QM, supplier certificate profile, certificate types.
- Quality info records y procurement inspection types configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: idiomas soportados por Document AI según matriz vigente **[verificar]**.
- Solo S/4HANA Cloud **Public** Edition.
- Formato de documento (PDF / imagen) soportado por Document AI.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar SAP Document AI en BTP y confirmar quotas | Subaccount BTP + entitlement Document AI | General | Consultor BTP | 3 |
| 2 | Configurar el communication scenario con Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al documento QM destino | Mapping Document AI ↔ Quality Certificate | Particular (por tipo de certificado / proveedor) | Consultor QM + Integración | 6 |
| 4 | Asignar business roles QM con catálogos de procesamiento de certificados | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales: ingesta de certificados reales y validación de extracción + posting | Configuración funcional QM | General | Consultor QM | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real de certificados (mínimo 2-3 layouts representativos) | Consultor QM | 6 |
| 2 | Documentación para el cliente | Consultor QM | 4 |
| 3 | Transferencia de conocimiento | Consultor QM | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout del proveedor; podrían necesitarse iteraciones de templates para extracción óptima.
- Volumen de documentos sujeto a cuotas de Document AI.
- Trazabilidad: documentos originales pueden almacenarse adjuntos al documento QM.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |
