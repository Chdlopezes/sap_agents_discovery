# Análisis caso de uso J36 — Generation of Full-Stack Applications (SAP Build Code)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural. Con Joule, la capacidad genera modelos de datos, servicios, datos de ejemplo, anotaciones de UI, lógica de aplicación y pruebas unitarias, dentro de un entorno de desarrollo cloud alineado con SAP Business Application Studio y buenas prácticas de SAP BTP. SAP indica: *SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor de negocio está en acelerar el ciclo de desarrollo, reducir esfuerzo manual y mejorar la productividad de equipos técnicos que crean extensiones y aplicaciones sobre SAP Build Code.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Build Code** en BTP.
- Joule integrado (Joule for Developers) **[verificar]**.

### 1.2 Licenciamiento / entitlement / paquete
- Entitlement SAP Build Code con feature Joule (Premium) **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- IDE Build Code / Business Application Studio.

### 1.5 Datos maestros / transaccionales previos
- Conectividad a backends (CAP / SAP HANA Cloud) si la app integra datos.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: prompts en inglés primariamente **[verificar]**.
- Usuario con rol Developer.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Aprovisionar entitlement SAP Build Code + Joule | Subaccount BTP + entitlement | General | Consultor BTP | 3 |
| 2 | Configurar conectividad a backends (si aplica) | Destinations / DB | General | Consultor BTP | 4 |
| 3 | Asignar rol Developer | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar capability Joule Generation | Configuración Build Code | General | Consultor BTP / Dev | 2 |
| 5 | Pruebas iniciales: generar app de muestra con prompts | Configuración Build Code | General | Desarrollador Sr | 4 |

**Esfuerzo total estimado (activación): ~15 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con casos representativos | Desarrollador Sr | 5 |
| 2 | Documentación + buenas prácticas | Desarrollador Sr | 4 |
| 3 | Transferencia de conocimiento | Desarrollador Sr | 3 |

**Esfuerzo total estimado (validación + entrega): ~12 horas.**

---

## 4. Consideraciones especiales

- Código generado requiere review/refactor humano.
- Seguridad: validar autenticación, autorización, secrets.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 15 |
| Validación + documentación + KT | 12 |
| **Total** | **27** |
