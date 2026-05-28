# Análisis caso de uso J180 — SAP HANA application migration

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Función que automatiza la migración de la capa de servicios **SAP HANA XS/XSA** hacia **SAP CAP** usando GenAI. Convierte artefactos como **XSJSLIB, XSODATA y XSJS** en servicios modernos basados en CAP, alineados con la guía de desarrollo de SAP BTP.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP HANA Cloud** activo.
- Proyecto **SAP HANA XS Advanced (XSA)** o **XS Classic** del cliente a migrar.
- Entorno de desarrollo soportado (típicamente **Visual Studio Code** con la extensión correspondiente).
- Servicios SAP BTP / SAP AI según aplique para la conversión asistida por GenAI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP HANA Cloud**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP HANA Application Migration Assistant** (extensión para Visual Studio Code).
- Acceso a destino BTP (subaccount) para desplegar la aplicación CAP convertida.

### 1.5 Datos maestros / transaccionales previos
- Código fuente XS/XSA del cliente accesible.
- Estructuras de base de datos / datos del proyecto migrable accesibles desde el entorno de desarrollo.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: no aplica (es una herramienta para developers).
- **Cobertura**: la conversión cubre artefactos XSJSLIB, XSODATA y XSJS; lógica muy custom puede requerir reescritura manual.
- **Roles**: developer con acceso a SAP HANA Cloud y a BTP.

> **Setup oficial SAP**: la página https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/migrate-xs-advanced-application-to-sap-cap-and-sap-hana-cloud-with-sap-hana-application-migration-assistant-in-visual-studio-code describe el procedimiento de migración con el Migration Assistant.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP HANA Cloud y subaccount BTP destino | SAP HANA Cloud + Subaccount BTP | General | Consultor BTP / HANA | 2 |
| 2 | Preparar conectividad al sistema origen XS/XSA | Conectividad origen | General | Consultor SAP HANA + Cliente | 3 |
| 3 | Configurar el destino BTP donde se desplegará la aplicación CAP | Destino BTP | General | Consultor BTP | 3 |
| 4 | Crear dev space en Visual Studio Code con la extensión SAP HANA Application Migration Assistant | Dev space VSCode + Extensión | General | Consultor SAP HANA / Developer | 3 |
| 5 | Ejecutar el Migration Assistant sobre los artefactos XSJSLIB / XSODATA / XSJS | Migration Assistant | Particular (por proyecto) | Consultor SAP HANA / Developer | 6 |
| 6 | Validar manualmente la conversión, ajustar lógica y ejecutar pruebas funcionales | Aplicación CAP convertida | Particular (por proyecto) | Consultor SAP HANA / Developer | 8 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~25 horas.**

> **Nota**: el alcance estándar cubre la conversión asistida y un primer ajuste; proyectos con lógica custom extensa requerirán esfuerzo adicional fuera del alcance estándar.

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con escenarios reales del proyecto migrado | Consultor SAP HANA / Developer | 4 |
| 2 | Documentación de la migración para el cliente (diferencias entre el código original y el convertido) | Consultor SAP HANA / Developer | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión técnica) | Consultor SAP HANA / Developer | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Es una **herramienta para developers**: no aplica concepto de Joule capability ni AI Units en el sentido tradicional.
- La conversión es **asistida**: el código resultante debe revisarse, probarse y ajustarse manualmente — no es una migración cero-touch.
- Lógica muy custom o dependencias no soportadas pueden requerir **reescritura manual** fuera del alcance estándar.
- Sujeto a las condiciones de servicio vigentes de SAP HANA Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **acompaña** la modernización técnica; no entrega la aplicación final lista para producción sin trabajo adicional del developer.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/
- SAP Help Portal — Migration Guide: https://help.sap.com/docs/hana-cloud/sap-hana-cloud-migration-guide/migrate-xs-advanced-application-to-sap-cap-and-sap-hana-cloud-with-sap-hana-application-migration-assistant-in-visual-studio-code

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 25 |
| Validación + documentación + KT | 11 |
| **Total** | **36** |
