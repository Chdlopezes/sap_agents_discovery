# Análisis caso de uso J151 — Master Data Governance

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite usar lenguaje natural para crear y actualizar solicitudes de cambio de datos maestros dentro de procesos de Master Data Governance en SAP S/4HANA Cloud Private Edition. SAP indica: *60% de reducción del esfuerzo para crear solicitudes de cambio de datos maestros; 20% de reducción del esfuerzo para revisar solicitudes de cambio; la página también indica una reducción adicional del 5% en un indicador que aparece truncado en el contenido accesible.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Private Edition** con Joule habilitado.
- **SAP Master Data Governance (MDG)** activo (data domain aplicable: customers, suppliers, materials, finance, etc.).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción S/4HANA Cloud Private Edition con MDG.
- Entitlement Joule **[verificar]**.

### 1.3 Scope item relacionado
- Scope items de Master Data Governance por dominio — **[verificar IDs]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori MDG (*Manage Change Requests*, *Process Change Requests*).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Configuración MDG por dominio: data models, workflows, validation rules.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Solo S/4HANA Cloud **Private** Edition.
- Usuario con autorizaciones MDG (requestor / processor / approver).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule | Subaccount BTP + entitlement | General | Consultor BTP | 2 |
| 2 | Verificar configuración MDG (workflows, change request types) | Configuración MDG | General | Consultor MDG | 4 |
| 3 | Asignar business roles MDG a usuarios | Business Role / Authorizations | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule para creación de CRs y summaries | Joule capability scope | General | Consultor Funcional MDG + Joule | 3 |
| 5 | Pruebas iniciales: crear CR vía Joule + generar summary | Configuración funcional MDG | General | Consultor MDG | 3 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (CRs por dominio + summaries) | Consultor MDG | 5 |
| 2 | Documentación para el cliente | Consultor MDG | 4 |
| 3 | Transferencia de conocimiento | Consultor MDG | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Joule asiste, no sustituye al governance flow (approval levels siguen aplicando).
- Cobertura por dominio puede variar — revisar **Road Map Explorer**.
- Respeta autorizaciones MDG.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |
