# Análisis caso de uso J85 — Joule with Regulatory Change Manager

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento. SAP indica: *85% menos tiempo dedicado a identificar cambios regulatorios, según la métrica mostrada en la página de detalle.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Regulatory Change Manager (RCM)** activo.
- **Joule** habilitado en BTP.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción RCM vigente.
- Entitlement Joule + capability RCM **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- App RCM (cockpit de regulaciones).
- Joule habilitado en el Launchpad.

### 1.5 Datos maestros / transaccionales previos
- Configuración de jurisdicciones / regulaciones / responsables.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Cobertura jurisdiccional sujeta al catálogo SAP.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement RCM + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar jurisdicciones, regulaciones, owners | Configuración RCM | Particular (por jurisdicción) | Consultor Compliance / RCM | 6 |
| 3 | Asignar roles RCM (Compliance Officer, Reviewer) | Roles | Particular (por usuario) | Consultor Seguridad | 3 |
| 4 | Habilitar capability Joule en RCM | Configuración RCM | General | Consultor RCM + Joule | 2 |
| 5 | Pruebas iniciales: consultar/evaluar regulaciones con Joule | Configuración funcional RCM | General | Consultor Compliance | 4 |

**Esfuerzo total estimado (activación): ~18 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales (varias regulaciones) | Consultor Compliance | 5 |
| 2 | Documentación para el cliente | Consultor Compliance | 4 |
| 3 | Transferencia de conocimiento | Consultor Compliance | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Compliance: decisiones legales requieren revisión humana.
- Cobertura regulatoria evoluciona — revisar **Road Map Explorer**.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 18 |
| Validación + documentación + KT | 12 |
| **Total** | **30** |
