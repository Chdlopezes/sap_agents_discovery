# Análisis caso de uso J762 — Joule and Microsoft 365 Copilot

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help / Microsoft Learn]** requieren validación oficial.

**Resumen del caso:** Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365. Permite consultar datos y tareas de SAP desde Copilot y aprovechar información/flujos de Microsoft 365 desde Joule. SAP indica: *No se identificó una métrica cuantitativa explícita de Business Value en la página de detalle consultada; el valor descrito se concentra en productividad, continuidad de trabajo y reducción de fricción entre SAP y Microsoft 365.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Joule** habilitado en BTP.
- **Microsoft 365 Copilot** activo en el tenant Microsoft del cliente.
- **SAP–Microsoft Joule/Copilot integration** (plugin / connector) **[verificar nombre y vehículo de distribución vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement Joule + capability de integración con Copilot **[verificar]**.
- Licencia Microsoft 365 Copilot por usuario.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- SAP Joule endpoint.
- Microsoft 365 (Teams, Outlook, etc.) con Copilot habilitado.

### 1.5 Datos maestros / transaccionales previos
- Mapeo de identidades SAP ↔ Microsoft (typically vía Entra ID / IAS trust).

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: matrices Joule y Copilot vigentes **[verificar]**.
- Disponibilidad regional.
- Cumplimiento corporativo (data residency, DLP).

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Joule + capability Copilot integration | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar trust / SSO entre IAS / Entra ID | Identity federation | General | Consultor Seguridad | 5 |
| 3 | Instalar plugin/connector en M365 Copilot | M365 admin center | General | Admin M365 | 4 |
| 4 | Asignar permisos del plugin a usuarios | Roles / Permissions | Particular (por usuario / grupo) | Admin M365 + Seguridad SAP | 3 |
| 5 | Pruebas iniciales bi-direccionales (consultar SAP desde Copilot y M365 desde Joule) | Configuración base | General | Consultor Funcional + Admin M365 | 4 |

**Esfuerzo total estimado (activación): ~19 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales | Consultor Funcional | 5 |
| 2 | Documentación para el cliente | Consultor Funcional | 4 |
| 3 | Transferencia de conocimiento | Consultor Funcional | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- **Multi-vendor**: coordinar con admin Microsoft del cliente.
- **Cumplimiento**: revisar DLP, data residency, retention en ambos lados.
- **Costos**: M365 Copilot tiene licencia per-user separada.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 19 |
| Validación + documentación + KT | 12 |
| **Total** | **31** |
