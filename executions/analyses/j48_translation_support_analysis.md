# Análisis caso de uso J48 — Translation Support

> Análisis basado en información públicamente documentada por SAP (SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Traducción asistida por IA en **SAP LeanIX** que permite a administradores agregar y traducir etiquetas y textos de ayuda para atributos nuevos o existentes en la configuración del metamodelo. El valor está en reducir el tiempo requerido para traducir términos del metamodelo y mejorar la accesibilidad del producto.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP LeanIX solutions** (suscripción activa).
- Workspace LeanIX del cliente operativo.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP LeanIX**.
- Capability **Base** **[verificar en AI Foundation Catalog vigente]**.
- **SAP AI terms** firmados.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP LeanIX** con acceso al **metamodel administration** del workspace.

### 1.5 Datos maestros / transaccionales previos
- Metamodelo LeanIX del cliente con atributos / labels existentes a traducir.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idiomas soportados**: según el modelo subyacente **[verificar matriz vigente]**.
- **Roles**: Workspace Admin / EA Admin con acceso a la configuración del metamodelo.

> **Nota**: SAP Discovery Center indica que no existe enlace de Initial Setup específico en la sección Resources. Aplican los prerequisitos generales de AI Capabilities de SAP LeanIX.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Validar términos de IA de LeanIX (contractual) | Términos de IA SAP LeanIX | General | Consultor SAP LeanIX + Cliente Legal | 2 |
| 2 | Habilitar AI Capabilities en el workspace de SAP LeanIX | Workspace LeanIX — AI Capabilities | General | Consultor SAP LeanIX | 2 |
| 3 | Identificar atributos / labels del metamodelo objetivo de traducción | Metamodel LeanIX | Particular (por atributo / dominio) | Consultor SAP LeanIX | 3 |
| 4 | Asignar a los usuarios objetivo los roles administrativos LeanIX con acceso al metamodelo | Roles SAP LeanIX | Particular (por usuario / grupo) | Consultor Seguridad LeanIX | 2 |
| 5 | Pruebas iniciales con un Workspace Admin (traducir un conjunto representativo de labels) | Configuración funcional LeanIX | General | Consultor SAP LeanIX | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~11 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con traducciones reales del cliente (varios dominios / idiomas) | Consultor SAP LeanIX | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario + lineamientos de traducción) | Consultor SAP LeanIX | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP LeanIX | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- Las traducciones generadas son **borradores**: deben ser revisadas por personas con dominio del idioma destino antes de publicarse, especialmente para términos técnicos.
- Considerar **gobernanza** sobre quién aprueba el cambio en el metamodelo (afecta a todos los usuarios del workspace).
- Sujeto a las condiciones de servicio vigentes de SAP LeanIX **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 11 |
| Validación + documentación + KT | 11 |
| **Total** | **22** |
