# Análisis caso de uso J121 — Process Recommender (SAP Signavio)

> Basado en información públicamente documentada por SAP. Valores marcados como **[verificar en SAP Help]** requieren validación oficial.

**Resumen del caso:** Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio. SAP indica: *La capacidad apunta a mejorar la productividad de recursos BPM, reducir costos de consultoría para mapeo de procesos y disminuir el tiempo de capacitación interna.*

---

## 1. Prerequisitos para la activación

### 1.1 Productos / componentes SAP requeridos
- **SAP Signavio Process Insights** o equivalente con capability AI.

### 1.2 Licenciamiento / entitlement / paquete
- Suscripción Signavio Process Insights / Recommendations **[verificar]**.

### 1.3 Scope item relacionado
- N/A.

### 1.4 Aplicaciones / apps Fiori / servicios requeridos
- Signavio Process Insights UI.

### 1.5 Datos maestros / transaccionales previos
- Process data conectado (S/4HANA / otros sistemas) suficientemente poblado.

### 1.6 Restricciones funcionales / técnicas / idioma
- **Idioma**: inglés primariamente **[verificar]**.
- Rol Process Insights user.

---

## 2. Pasos de activación / configuración estándar

| # | Actividad estándar | Objeto de configuración | Tipo de configuración | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|---|---|
| 1 | Confirmar suscripción Signavio + AI | Tenant Signavio | General | Consultor Signavio | 2 |
| 2 | Conectar data sources (S/4HANA / otros) | Conexiones Signavio | General | Consultor Signavio | 5 |
| 3 | Asignar roles a usuarios | Roles | Particular (por usuario) | Consultor Seguridad | 2 |
| 4 | Habilitar Process Recommender | Signavio admin | General | Consultor Signavio | 2 |
| 5 | Pruebas iniciales (revisar recomendaciones) | Configuración Signavio | General | Consultor Signavio | 3 |

**Esfuerzo total estimado (activación): ~14 horas.**

---

## 3. Pasos adicionales de validación

| # | Actividad | Consultor requerido | Tiempo estimado (h, Medium) |
|---|---|---|---|
| 1 | Prueba unitaria con datos reales | Consultor Signavio | 4 |
| 2 | Documentación para el cliente | Consultor Signavio | 3 |
| 3 | Transferencia de conocimiento | Consultor Signavio | 3 |

**Esfuerzo total estimado (validación + entrega): ~10 horas.**

---

## 4. Consideraciones especiales

- Calidad de recomendaciones depende de la cobertura/volumen de datos del proceso.

---

## Resumen ejecutivo de esfuerzo

| Bloque | Horas |
|---|---|
| Activación / configuración | 14 |
| Validación + documentación + KT | 10 |
| **Total** | **24** |
