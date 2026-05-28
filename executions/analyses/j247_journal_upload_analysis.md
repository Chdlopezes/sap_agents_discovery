# Análisis caso de uso J247 — Journal Upload

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition. Mediante una app SAP Fiori con capacidades de IA generativa, permite crear casos de carga, asociar una guía o política de contabilización en lenguaje natural, generar propuestas, validarlas y publicar asientos. SAP indica: *70% de reducción del esfuerzo para preparar journals manuales al cierre de período; 50% de reducción del esfuerzo para cargar y validar journals manuales al cierre.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- Componente **FI-GL – General Ledger** operativo.
- (Opcional) **SAP Document AI** si la entrada es PDF/Excel no estructurado.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement Joule **[verificar]**.
- Si aplica, entitlement Document AI (Premium).

### 1.3 Scope item relacionado
- Scope items de Record-to-Report / Period-End Close — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Post General Journal Entries*, *Upload General Journal Entries*.
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Chart of accounts, document types, periodos abiertos.
- Plantilla de upload (formato Excel SAP).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones FI-GL.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración FI-GL (doc types, posting keys) | Configuración FI-GL | General | Consultor FI | 3 |
| 3 | Asignar business roles FI-GL a usuarios | Business Role / Business Catalog | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para Journal Upload | Joule capability scope | General | Consultor Funcional FI + Joule | 2 |
| 5 | Pruebas iniciales con plantillas reales en QAS | Configuración funcional FI | General | Consultor FI | 3 |

**Esfuerzo total estimado (activación): ~13 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con journals reales del cliente | Consultor FI | 4 |
| 2 | Documentación para el cliente | Consultor FI | 4 |
| 3 | Transferencia de conocimiento | Consultor FI | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Acelera period-end; validar tolerancias y workflows de aprobación.
- Reglas de validación FI siguen aplicando.
- Usuario confirma posting.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 13 |
| Validación + documentación + KT | 11 |
| **Total** | **24** |
