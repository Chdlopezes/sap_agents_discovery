# Análisis caso de uso J892 — Smart Grouping

> Análisis basado en información públicamente documentada por SAP (SAP Help Portal, SAP Discovery Center). Los valores marcados como **[verificar en SAP Help]** deben validarse contra la documentación oficial vigente.

**Resumen del caso:** Capacidad de **SAP Analytics Cloud (SAC)** que agrupa puntos de datos similares en gráficos de dispersión y burbuja mediante clustering basado en centroides. El valor se centra en facilitar el descubrimiento de patrones / segmentos en visualizaciones.

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Analytics Cloud** (suscripción activa).

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción vigente a **SAP Analytics Cloud**.
- Capability **Base** — incluida con SAC **[verificar en AI Foundation Catalog vigente]**.

### 1.3 Scope item relacionado
- No aplica scope item.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- **SAP Analytics Cloud** con historias que incluyan **gráficos de dispersión o burbuja**.

### 1.5 Datos maestros / transaccionales previos
- Modelo SAC con datos numéricos y dimensiones suficientes para producir clusters significativos en visualizaciones de dispersión / burbuja.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Tipos de gráfico**: la capability aplica únicamente a **scatter y bubble charts**.
- **Roles**: usuario SAC con permisos para crear/editar historias o visualizaciones.

> **Setup oficial SAP**: la documentación https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html describe las capacidades inteligentes de SAC.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar entitlement de SAP Analytics Cloud en el tenant del cliente | Tenant SAC | General | Consultor SAP Analytics Cloud | 2 |
| 2 | Preparar el modelo / historia con gráficos de dispersión o burbuja | Modelos / historias SAC | Particular (por historia) | Consultor SAP Analytics Cloud | 2 |
| 3 | Asignar a los usuarios objetivo los roles SAC con acceso a las historias | Roles SAC | Particular (por usuario / grupo) | Consultor Seguridad SAC | 2 |
| 4 | Pruebas iniciales con un usuario piloto (aplicar Smart Grouping en visualizaciones representativas) | Configuración funcional SAC | General | Consultor SAP Analytics Cloud | 2 |

**Esfuerzo total estimado (activación estándar, sin necesidades adicionales): ~8 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales del cliente (clustering sobre conjuntos representativos) | Consultor SAP Analytics Cloud | 4 |
| 2 | Documentación de la activación para el cliente (manual de usuario) | Consultor SAP Analytics Cloud | 4 |
| 3 | Transferencia de conocimiento al equipo del cliente (sesión funcional + Q&A) | Consultor SAP Analytics Cloud | 3 |

**Esfuerzo total estimado (validación + entrega): ~11 horas.**

---

## 4. Consideraciones especiales (según guía SAP)

- La utilidad del clustering depende del **volumen y dispersión** de los datos: muestras pequeñas o homogéneas reducen el valor de los grupos detectados.
- Es **apoyo visual a la exploración**: la interpretación final de los grupos sigue siendo del analista.
- Sujeto a las condiciones de servicio vigentes de SAP Analytics Cloud **[verificar]**.
- Antes de la activación, revisar el **SAP Road Map Explorer** y release notes vigentes.
- Este caso de uso **no incluye desarrollos custom**; cualquier extensión queda fuera del alcance estándar.

---

## Referencias oficiales

- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/
- SAP Help Portal — Smart Features in SAC: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/8b9038ca44f547bf8e69b04e5c55eb37.html

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 8 |
| Validación + documentación + KT | 11 |
| **Total** | **19** |
