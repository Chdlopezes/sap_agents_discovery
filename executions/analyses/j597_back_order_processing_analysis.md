# Análisis caso de uso J597 — Back Order Processing

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Road Map Explorer, AI Foundation Catalog). Valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Funcionalidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución y configuración de Back Order Processing mediante interacciones intuitivas basadas en prompts. SAP indica: *Mejora la velocidad y calidad de la ejecución de BOP. No se encontró un KPI cuantitativo específico en la página consultada.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP S/4HANA Cloud Public Edition** con Joule habilitado.
- Componente funcional **SD – Sales** (Back Order Processing — BOP) operativo en el sistema.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción a S/4HANA Cloud Public Edition con módulo SD.
- Entitlement de **Joule** sobre S/4HANA Public; capability incluida como **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- Scope item de Sales Order Management con BOP — **[verificar el ID exacto en SAP Signavio Process Navigator]**.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Apps Fiori de BOP en S/4HANA Public (*Configure BOP Variants*, *Schedule BOP Run*, *Monitor BOP Runs*).
- Joule habilitado en el Launchpad del usuario.

### 1.5 Datos maestros / transaccionales previos
- Materiales, customers, sales orders y ATP / aATP configurados.
- Variantes de BOP definidas y operativas.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: interacciones Joule principalmente en inglés **[verificar matriz vigente]**.
- Solo S/4HANA Cloud **Public** Edition.
- Usuario debe contar con autorizaciones SD para BOP.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de Joule sobre S/4HANA Public | Subaccount BTP + entitlement Joule | General | Consultor BTP | 2 |
| 2 | Verificar que BOP esté correctamente configurado (variantes, segmentos, prioridades) | Configuración BOP | General | Consultor SD | 3 |
| 3 | Asignar business roles SD con catálogos BOP a los usuarios objetivo | Business Role / Business Catalog | Particular (por usuario / grupo) | Consultor Seguridad | 3 |
| 4 | Habilitar la capability de Joule para BOP (si gating por configuración) | Joule capability scope | General | Consultor Funcional SD + Joule | 2 |
| 5 | Pruebas iniciales con prompts típicos (ejecutar BOP, revisar resultados) en Quality | Configuración funcional SD | General | Consultor SD | 2 |

**Esfuerzo total estimado (activación): ~12 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales (escenarios típicos: ejecución BOP, redistribución de stock, priorización) | Consultor SD | 4 |
| 2 | Documentación para el cliente (manual de usuario + configuración) | Consultor SD | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente | Consultor SD | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales

- Joule **no extiende la lógica funcional de BOP**: ejecuta y consulta apoyado en lo ya configurado.
- Los resultados respetan las autorizaciones del usuario (no eleva privilegios).
- Sujeto a fair-use de Joule **[verificar políticas vigentes]**.
- Sin desarrollos custom: cualquier extensión queda fuera del alcance estándar.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 12 |
| Validación + documentación + KT | 11 |
| **Total** | **23** |
