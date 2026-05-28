# Análisis caso de uso J28 — Goods Receipt Processing

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA. Permite extraer información relevante de documentos de flete en papel, publicarla en el sistema y detectar anomalías que pueden retrasar la validación de freight orders. SAP indica: *El valor está en reducir trabajo manual y errores durante la recepción de mercancía, acelerar validaciones y mejorar eficiencia operacional en transporte/logística.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Document AI** (servicio en BTP) para extracción de delivery notes.
- Componente **MM-IM – Inventory Management** + **MM-PUR – Purchasing** operativos.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition.
- Entitlement **Document AI** (Premium) **[verificar]**.
- Entitlement Joule.

### 1.3 Scope item relacionado
- Scope items de Procure-to-Pay / Goods Receipt — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori *Post Goods Receipt for Purchase Order*, *Goods Receipt Reversal*.
- Communication arrangement S/4HANA Private ↔ Document AI.

### 1.5 Datos maestros / transaccionales previos
- Materials, suppliers, purchase orders abiertos.
- Tipos de delivery notes (papel/PDF) soportados por Document AI.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matriz Document AI vigente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Layout del documento debe ser razonablemente extraíble.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Provisionar Document AI en BTP | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar communication scenario S/4HANA Private ↔ Document AI | Communication Arrangement | General | Consultor Integración | 4 |
| 3 | Configurar mapping de campos extraídos al goods receipt | Mapping Document AI ↔ GR | Particular (por layout/proveedor) | Consultor MM + Integración | 6 |
| 4 | Asignar business roles Warehouse / Inventory a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 5 | Pruebas iniciales con delivery notes reales | Configuración funcional MM-IM | General | Consultor MM | 4 |

**Esfuerzo total estimado (activación): ~20 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con muestra real (varios layouts de proveedores) | Consultor MM | 6 |
| 2 | Documentación para el cliente | Consultor MM | 4 |
| 3 | Transferencia de conocimiento | Consultor MM | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- **Calidad de extracción** depende del layout del delivery note.
- Reglas de tolerancia y discrepancias siguen aplicando.
- Usuario sigue confirmando posting cuando hay discrepancias.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 20 |
| Validación + documentación + KT | 13 |
| **Total** | **33** |
