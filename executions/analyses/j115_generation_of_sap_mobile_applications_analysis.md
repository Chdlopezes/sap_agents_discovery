# Análisis caso de uso J115 — Generation of SAP Mobile Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code. Puede generar componentes a partir de lenguaje natural, incluyendo código, modelos de datos, servicios, lógica de negocio, datos de ejemplo y pruebas unitarias. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar el desarrollo móvil y reducir esfuerzo manual en componentes técnicos repetitivos.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** con Joule.
- **SAP Mobile Services / Mobile Development Kit (MDK)** disponible **[verificar packaging vigente]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code + Joule (Premium) **[verificar]**.
- Entitlement Mobile Services / MDK si requerido.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.
- Mobile Services Cockpit (para despliegue / runtime).

### 1.5 Datos maestros / transaccionales previos
- Backends OData / RAP configurados.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario Mobile Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement Build Code + Joule + Mobile Services | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar Mobile Services (app registration, push) | Mobile Services Cockpit | General | Consultor Mobile | 5 |
| 3 | Asignar rol Mobile Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Mobile App Generation | Configuración Build Code | General | Consultor Mobile / Dev | 2 |
| 5 | Pruebas iniciales: generar app móvil de muestra y desplegar | Configuración Build Code | General | Desarrollador Mobile Sr | 5 |

**Esfuerzo total estimado (activación): ~17 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria en device real (iOS/Android) | Desarrollador Mobile Sr | 6 |
| 2 | Documentación + buenas prácticas | Desarrollador Mobile Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Mobile Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~13 horas.**

---

## 4. Consideraciones especiales

- Considerar offline-first, security (MDM), distribución (stores corporativas).

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 17 |
| Validación + documentación + KT | 13 |
| **Total** | **30** |
