# SAP Business AI — Fichas Descriptivas de AI Features (Corpus RAG)

> **Última actualización:** 2026-06-11T15:45:47+00:00
> **Fichas incluidas:** 161

## Qué contiene este documento

Este archivo es la **concatenación canónica** de las fichas explicativas de los
casos de uso de IA del catálogo **SAP Business AI**. A diferencia del corpus de
*esfuerzo de activación* (`effort/`), aquí el foco es **entender qué hace cada
AI Feature y cómo se usa**, no estimar su esfuerzo.

Cada ficha, identificada por su código `JNNN` y nombre oficial, contiene:

1. **En una frase** — síntesis ultra-breve.
2. **¿Qué es?** — Overview tomado de la Detail Page de SAP Discovery Center.
3. **Beneficios** y **Valor de negocio** — publicados por SAP.
4. **¿Cómo funciona?** — flujo de uso de la capability.
5. **Casos de uso (ilustrativos)** — escenarios de ejemplo (no oficiales) para
   facilitar la comprensión.
6. **¿Cuándo usarla?** y **Datos clave**.

## Reglas de la fuente

- El Overview, Beneficios y Valor de negocio provienen de la **Detail Page**
  oficial de SAP Discovery Center (contenido vivo).
- Los **casos de uso** marcados como *ilustrativos* son ejemplos redactados para
  facilitar la comprensión y **no** son escenarios oficiales de SAP.
- Las fichas están escritas en **español**.

## Cómo está estructurado este archivo

- Cada ficha es una sección de nivel 2 con el formato `## [JNNN] — Nombre`,
  separada por una línea horizontal `---`.

> Para cargar este corpus en un sistema RAG: trocea por sección de nivel 2
> (`##`) y trata el texto bajo cada encabezado como una unidad semántica.

---

## [J1003] — Allocation Run Results

## En una frase
Funcionalidad de Joule para analistas de negocio y contadores de costos que permite consultar montos asignados entre objetos como centros de costo, objetos de rentabilidad o centros de beneficio, y navegar rápidamente al job y al reporte detallado de la corrida de asignación.

## ¿Qué es?
Funcionalidad de Joule para analistas de negocio y contadores de costos que permite consultar montos asignados entre objetos como centros de costo, objetos de rentabilidad o centros de beneficio, y navegar rápidamente al job y al reporte detallado de la corrida de asignación. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Acceso inmediato al flujo de costos y al impacto en clientes
- menor esfuerzo de síntesis de datos entre distintas fuentes
- insights rápidos sobre asignaciones de costos
- navegación directa a detalles de contabilizaciones relacionadas

## Valor de negocio
70% de reducción del tiempo dedicado al análisis de resultados de asignación y 40% de resolución más rápida de problemas de asignación.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Acceso inmediato al flujo de costos y al impacto en clientes_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1003 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | FIN-UA-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/58e5fdf9-b00a-414b-97ef-74c65c21b10b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/58e5fdf9-b00a-414b-97ef-74c65c21b10b/

---

## [J1043] — Dispute Resolution Agent

## En una frase
Automatiza el análisis de causa raíz y sugiere soluciones accionables: revisa rápidamente facturas, pedidos de venta, registros de entrega, acuerdos de precios, reglas de impuestos y datos históricos para identificar las causas de la disputa.

## ¿Qué es?
Automatiza el análisis de causa raíz y sugiere soluciones accionables: revisa rápidamente facturas, pedidos de venta, registros de entrega, acuerdos de precios, reglas de impuestos y datos históricos para identificar las causas de la disputa. Ofrece recomendaciones conformes y a medida, reduciendo el tiempo y el esfuerzo de resolución y avanzando hacia una gestión de disputas automatizada, más rápida y alineada con la regulación. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition‚ Joule.

## Beneficios
- Escanea facturas y contratos en busca de errores automáticamente
- detecta cargos incorrectos y sugiere correcciones como la creación de notas de crédito
- mejora la confianza y las relaciones con resolución de disputas más rápida

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Escanea facturas y contratos en busca de errores automáticamente_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1043 |
| Producto | SAP S/4HANA Cloud Public Edition‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FI-FIO-AR-TRA-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d3a94887-d357-4620-98d5-784a035f9e41/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d3a94887-d357-4620-98d5-784a035f9e41/

---

## [J1047] — Sales Order Status Check

## En una frase
Joule permite a los representantes de ventas comprobar si el cumplimiento de un pedido está en curso y detectar problemas que bloquean su finalización.

## ¿Qué es?
Joule permite a los representantes de ventas comprobar si el cumplimiento de un pedido está en curso y detectar problemas que bloquean su finalización. La experiencia se orienta a consultar estado, causas y posibles acciones desde un flujo conversacional. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Permite entender rápidamente el estado real de fulfillment de un pedido y mejora la eficiencia al resolver incidencias de forma más intuitiva

## Valor de negocio
Aporta valor al reducir el tiempo de análisis manual del estado de pedidos y al facilitar acciones tempranas sobre problemas que podrían retrasar el cumplimiento.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Permite entender rápidamente el estado real de fulfillment de un pedido y mejora la eficiencia al resolver incidencias de forma más intuitiva_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1047 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | SD-FIO-HBA-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8e12da05-b0e4-490f-9cf4-0cc2a9482f71/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8e12da05-b0e4-490f-9cf4-0cc2a9482f71/

---

## [J1088] — Joule with SAP Order Management Services

## En una frase
La integración de Joule con SAP Order Management Services permite a los operations managers acceder a los datos del servicio mediante consultas conversacionales, con guía operativa en tiempo real basada en rol, cubriendo múltiples dominios: procesamiento de pedidos, orquestación, sourcing, disponibilidad, devoluciones y flujos.

## ¿Qué es?
La integración de Joule con SAP Order Management Services permite a los operations managers acceder a los datos del servicio mediante consultas conversacionales, con guía operativa en tiempo real basada en rol, cubriendo múltiples dominios: procesamiento de pedidos, orquestación, sourcing, disponibilidad, devoluciones y flujos. Es una capacidad de IA **Base** de SAP Order Management Services.

## Beneficios
- Ahorra tiempo y dinero actuando antes de que ocurran los problemas
- el acceso rápido a transacciones mejora la velocidad y la capacidad de respuesta
- los insights en tiempo real previenen incidencias
- datos instantáneos y precisos habilitan decisiones más inteligentes y rápidas

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Order Management Services.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Order Management Services sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Ahorra tiempo y dinero actuando antes de que ocurran los problemas_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Order Management Services y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Order Management Services** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1088 |
| Producto | SAP Order Management Services |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CEC-BAF-DOM-JOULE |
| Industrias aplicables | Retail |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/b9498c45-6944-48e3-bb0e-902c71bef176/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b9498c45-6944-48e3-bb0e-902c71bef176/

---

## [J108] — AI-Assisted Search

## En una frase
Habilita **búsqueda en lenguaje natural** dentro de **SAP Datasphere**, para encontrar objetos y artefactos de datos sin tener que aplicar filtros manualmente.

## ¿Qué es?
Es una capacidad **Premium** que lleva la IA generativa al buscador de SAP Datasphere (repository explorer, data builder, catalog y data marketplace). El usuario escribe una petición en lenguaje natural —de complejidad arbitraria— y la búsqueda aumentada con IA **interpreta la intención** y devuelve los resultados correctos del conjunto de objetos y artefactos disponibles en el tenant de SAP Datasphere. Así se elimina la necesidad de seleccionar filtros manualmente y revisar cientos de objetos uno a uno.

## Beneficios
- Agiliza el **descubrimiento de artefactos de datos** permitiendo buscar en lenguaje natural, haciendo el proceso más preciso y rápido.

## Valor de negocio
- **90% de reducción del tiempo** dedicado a búsquedas complejas de artefactos de datos (cifra publicada por SAP).

## ¿Cómo funciona?
1. **Entrada en lenguaje natural:** el usuario describe lo que busca (p. ej. *"tablas de ventas por región del último año"*) en el buscador de SAP Datasphere.
2. **Comprensión con IA generativa:** el motor de búsqueda aumentado interpreta la consulta, incluso si es ambigua o compleja.
3. **Resultados relevantes:** devuelve los objetos y artefactos coincidentes del tenant (modelos, tablas, vistas, productos de datos del marketplace, etc.) sin aplicar filtros manuales.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un analista nuevo no conoce la convención de nombres del tenant y necesita encontrar el modelo de datos de inventario. **Cómo ayuda la feature:** escribe "datos de inventario por almacén" y la búsqueda IA le lleva directo a los artefactos relevantes, sin adivinar nombres técnicos ni recorrer filtros.
2. **Escenario:** Un data steward quiere localizar todos los productos de datos relacionados con clientes publicados en el catálogo. **Cómo ayuda la feature:** una consulta en lenguaje natural recupera de una vez los artefactos pertinentes dispersos por explorer, catalog y marketplace.

## ¿Cuándo usarla?
- Cuando el tenant de SAP Datasphere tiene **muchos objetos** y el descubrimiento manual por filtros es lento o propenso a omisiones.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver pricing).
- Aporta más a usuarios que conocen el dominio de negocio pero no necesariamente la estructura técnica/nombres internos del tenant.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J108 |
| Producto | SAP Datasphere |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | Por **AI Units**: Requests en bloques de 100 → 0,7 AI Units (≈ EUR 7 por bloque, según AI Estimator) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/68658ffa-898f-4e8d-888f-b48e3be618f5/

---

## [J1104] — Processing of Payment Advices with SAP Document AI

## En una frase
Processing of Payment Advices with SAP Document AI automatiza el procesamiento multilingüe de avisos de pago mediante extracción y lectura asistida por IA.

## ¿Qué es?
Processing of Payment Advices with SAP Document AI automatiza el procesamiento multilingüe de avisos de pago mediante extracción y lectura asistida por IA. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Disminuye el esfuerzo manual de cuentas por cobrar, reduce errores de captura y permite procesar documentos de pago con mayor consistencia

## Valor de negocio
La capacidad busca reducir tiempos de procesamiento documental, disminuir correcciones manuales y mejorar la eficiencia del equipo de cuentas por cobrar.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Disminuye el esfuerzo manual de cuentas por cobrar_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1104 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-FIO-AR-2CL |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/988b6b7c-ac4f-4c5f-be46-0366c7dc5a2e/

---

## [J1114] — Supplier Confirmation Mass Creation

## En una frase
Permite crear de forma masiva varias confirmaciones de proveedor mediante Joule en SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Permite crear de forma masiva varias confirmaciones de proveedor mediante Joule en SAP S/4HANA Cloud Public Edition. El comprador puede ingresar varios pedidos de compra y apoyarse en Joule para acelerar la creación de confirmaciones. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el esfuerzo manual de crear confirmaciones una por una
- agiliza el trabajo del comprador en procesos de procurement
- ayuda a tratar varios pedidos en una sola interacción conversacional

## Valor de negocio
Aporta eficiencia operativa en compras al reducir tiempos de procesamiento, disminuir tareas repetitivas y mejorar la oportunidad con la que se registran confirmaciones de proveedor.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el esfuerzo manual de crear confirmaciones una por una_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1114 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | MM-PUR-CNF-JOU-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/b8dfd079-2d74-417a-ad38-8a5251110a4d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b8dfd079-2d74-417a-ad38-8a5251110a4d/

---

## [J1122] — Process Analyzer‚ Automated Mapping

## En una frase
Con el mapeo automatizado, los analistas de procesos pueden vincular automáticamente actividades de modelos BPMN con eventos sin necesidad de coincidencias exactas de nombre.

## ¿Qué es?
Con el mapeo automatizado, los analistas de procesos pueden vincular automáticamente actividades de modelos BPMN con eventos sin necesidad de coincidencias exactas de nombre. Interpreta el contexto de forma inteligente, permitiendo mapear acciones —eventos, actividades, mejores prácticas, bloqueadores o acciones de texto libre— aunque aparezcan en distintos idiomas, contengan abreviaturas o errores tipográficos. Los mapeos se reutilizan en análisis futuros. Es una capacidad de IA **Base** de SAP Signavio Process Intelligence.

## Beneficios
- Mejora las tareas con verificación de conformidad
- amplía las capacidades de mapeo más allá de los límites actuales del auto-mapeo
- ahorra costos significativos
- ofrece un servicio de mapeo universal aplicable en dashboards, generación de reglas y PCAI

## Valor de negocio
90% de reducción del tiempo de mapear event logs reales a un modelo BPMN.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Signavio Process Intelligence.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Signavio Process Intelligence sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Mejora las tareas con verificación de conformidad_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Intelligence y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Intelligence** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1122 |
| Producto | SAP Signavio Process Intelligence |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIC-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/6c6eb8d1-764c-4727-b8d5-4911607f89b8/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6c6eb8d1-764c-4727-b8d5-4911607f89b8/

---

## [J1129] — Workspace Administration Agent

## En una frase
Automatiza el onboarding de usuarios y la gestión del workspace, permitiendo a expertos de proceso y usuarios de negocio empezar a usar SAP Signavio el doble de rápido.

## ¿Qué es?
Automatiza el onboarding de usuarios y la gestión del workspace, permitiendo a expertos de proceso y usuarios de negocio empezar a usar SAP Signavio el doble de rápido. Agiliza la inscripción para modelado y minería de procesos creando múltiples usuarios, asignando los roles, licencias y derechos de acceso correctos, e inscribiéndolos en los procesos relevantes, asegurando que cada nuevo usuario tenga los permisos adecuados desde el primer día. Es una capacidad de IA **Base** de SAP Signavio Process Collaboration Hub‚ Joule.

## Beneficios
- Automatiza el onboarding masivo de usuarios con roles y licencias
- habilita acceso inmediato a dashboards y análisis
- asegura gobernanza y cumplimiento consistentes
- reduce el esfuerzo administrativo repetitivo
- acelera la adopción de usuarios de process mining

## Valor de negocio
90% de reducción del tiempo de otorgar derechos de acceso a usuarios de SAP Signavio.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Signavio Process Collaboration Hub‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Automatiza el onboarding masivo de usuarios con roles y licencias_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Collaboration Hub‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Collaboration Hub‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1129 |
| Producto | SAP Signavio Process Collaboration Hub‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d8e34c50-6983-4129-aa44-3356bf2fb4bf/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d8e34c50-6983-4129-aa44-3356bf2fb4bf/

---

## [J112] — Process Analyzer, Text to Insight

## En una frase
Permite a cualquier usuario de negocio **hacer preguntas en lenguaje natural sobre sus procesos** en SAP Signavio y recibir insights inmediatos de process mining, sin necesidad de perfil técnico.

## ¿Qué es?
Es una capacidad **Base** de **SAP Signavio solutions** que democratiza el process mining. En lugar de requerir analistas expertos, cualquier usuario —con cualquier nivel de habilidad— puede formular preguntas en lenguaje natural ("prompt to discover insights") y obtener de inmediato hallazgos sobre el comportamiento de sus procesos que sirven para tomar decisiones de negocio.

## Beneficios
- **Detección de correlaciones y anomalías** consumible por usuarios de negocio.
- Enfoque **democratizado** del process mining.
- Mayor **precisión y relevancia** del análisis, guiado por los prompts del usuario de negocio.
- Empodera a usuarios no técnicos para realizar análisis profundos y obtener conocimiento accionable.

## Valor de negocio
- **50% de reducción del tiempo** para acceder a insights.
- **Time-to-productivity más rápido** para nuevas incorporaciones.

## ¿Cómo funciona?
1. **Pregunta en lenguaje natural:** el usuario escribe lo que quiere entender de su proceso (p. ej. *"¿dónde se concentran los retrasos en el proceso de compras?"*).
2. **Análisis asistido por IA:** la capability traduce el prompt en una consulta de process mining sobre los datos del proceso e identifica correlaciones y anomalías.
3. **Insight inmediato:** devuelve el hallazgo en un formato comprensible para negocio, listo para informar una decisión, sin construir manualmente la métrica.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable de operaciones sospecha cuellos de botella en order-to-cash pero no domina las herramientas de mining. **Cómo ayuda la feature:** pregunta "muéstrame los pasos con mayor tiempo de espera en order-to-cash" y obtiene de inmediato las etapas críticas y sus anomalías.
2. **Escenario:** Un analista recién contratado debe ponerse al día con un proceso complejo. **Cómo ayuda la feature:** mediante prompts sucesivos explora el proceso conversacionalmente y reduce drásticamente su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando se busca **extender el process mining más allá del equipo técnico** hacia usuarios de negocio.
- Ideal para exploración ágil de procesos y descubrimiento de anomalías sin construir análisis a mano.
- Requiere SAP Signavio solutions con el módulo de process intelligence correspondiente.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J112 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | Actualmente **no requiere AI Units** para usar esta oferta en el Cloud Service subyacente (sujeto a cambio) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6dde1d9-6da4-443f-874a-e6eb183e2bd5/

---

## [J1130] — Screen Guide Agent

## En una frase
Transforma pantallas complejas y ricas en funciones en comprensión clara y accionable: reconoce dinámicamente la pantalla que ve el usuario, explica su propósito, guía sobre las acciones disponibles y resalta los datos y controles más relevantes.

## ¿Qué es?
Transforma pantallas complejas y ricas en funciones en comprensión clara y accionable: reconoce dinámicamente la pantalla que ve el usuario, explica su propósito, guía sobre las acciones disponibles y resalta los datos y controles más relevantes. Integrado en SAP Signavio, entrega explicaciones en lenguaje natural, resaltados visuales y tips por rol. Es una capacidad de IA **Base** de SAP Signavio Process Collaboration Hub‚ Joule.

## Beneficios
- Simplifica pantallas complejas con explicaciones claras y accionables
- resalta secciones, métricas y controles clave
- contextualiza funciones para mostrar propósito y relevancia
- ofrece insights guiados en lenguaje natural y recomendaciones del siguiente paso
- acelera el onboarding y el uso confiado de la plataforma

## Valor de negocio
30% de reducción del tiempo de interpretar una página de SAP Signavio; 50% de reducción del costo de onboarding y formación de nuevos usuarios.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Signavio Process Collaboration Hub‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Simplifica pantallas complejas con explicaciones claras y accionables_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Collaboration Hub‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Collaboration Hub‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1130 |
| Producto | SAP Signavio Process Collaboration Hub‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/1be89884-5087-4293-9b9e-da35987fe9bc/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1be89884-5087-4293-9b9e-da35987fe9bc/

---

## [J1131] — Value Case Creation Agent

## En una frase
Ayuda a las organizaciones a traducir insights de procesos en valor de negocio tangible: identifica automáticamente ineficiencias (retrabajos, demoras) y las vincula con oportunidades de mejora (automatización, estandarización).

## ¿Qué es?
Ayuda a las organizaciones a traducir insights de procesos en valor de negocio tangible: identifica automáticamente ineficiencias (retrabajos, demoras) y las vincula con oportunidades de mejora (automatización, estandarización). Estimando el impacto financiero potencial con parámetros configurables de costo y esfuerzo, permite crear value cases basados en datos sin requerir experiencia analítica profunda. Entrega borradores editables (resumen del problema, causas raíz, beneficios esperados). Es una capacidad de IA **Base** de SAP Signavio Process Intelligence‚ Joule.

## Beneficios
- Identifica automáticamente ineficiencias de proceso y cuantifica el impacto financiero
- genera value cases basados en datos al instante desde insights de process mining
- sugiere iniciativas de mejora dirigidas a maximizar el ROI
- habilita decisiones basadas en evidencia
- simplifica la colaboración con borradores editables generados por IA

## Valor de negocio
70% de reducción del tiempo de crear un value case centrado en procesos; 5% de reducción de la erosión de valor por inacción ante ineficiencias de proceso.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Signavio Process Intelligence‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Identifica automáticamente ineficiencias de proceso y cuantifica el impacto financiero_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Intelligence‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Intelligence‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1131 |
| Producto | SAP Signavio Process Intelligence‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e5f8f643-4dc9-46d4-96e6-15d73187869a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e5f8f643-4dc9-46d4-96e6-15d73187869a/

---

## [J1132] — Dashboard Analyzer Agent

## En una frase
Transforma datos complejos de process mining en insights claros y accionables: interpreta de forma autónoma event logs y KPIs, identifica ineficiencias y desviaciones, y recomienda próximas mejores acciones, convirtiendo dashboards estáticos en herramientas prescriptivas.

## ¿Qué es?
Transforma datos complejos de process mining en insights claros y accionables: interpreta de forma autónoma event logs y KPIs, identifica ineficiencias y desviaciones, y recomienda próximas mejores acciones, convirtiendo dashboards estáticos en herramientas prescriptivas. Integrado en SAP Signavio, entrega resúmenes en lenguaje natural que explican qué ocurre, por qué importa y cómo mejorar. Es una capacidad de IA **Base** de SAP Signavio Process Intelligence‚ Joule.

## Beneficios
- Simplifica dashboards y KPIs con explicaciones claras y accionables
- detecta ineficiencias, anomalías y desviaciones de rendimiento
- contextualiza y correlaciona KPIs para revelar causas raíz
- genera recomendaciones prescriptivas e insights en lenguaje natural
- acelera decisiones basadas en datos

## Valor de negocio
80% de reducción del tiempo para acceder a insights de process mining; 5% de reducción de la erosión de valor por mala interpretación de los insights.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Signavio Process Intelligence‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Simplifica dashboards y KPIs con explicaciones claras y accionables_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Intelligence‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Intelligence‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1132 |
| Producto | SAP Signavio Process Intelligence‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/251eb6f4-4565-4ac7-8e6c-f5eb6df7d210/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/251eb6f4-4565-4ac7-8e6c-f5eb6df7d210/

---

## [J1137] — Electronic Document Error Handling

## En una frase
Ofrece explicaciones en lenguaje natural para errores técnicos o complejos de documentos electrónicos con Joule.

## ¿Qué es?
Ofrece explicaciones en lenguaje natural para errores técnicos o complejos de documentos electrónicos con Joule. Es una capacidad de IA **Base** de SAP Document and Reporting Compliance.

## Beneficios
- Ayuda a los usuarios a comprender errores sin revisar formatos técnicos complejos
- acelera el procesamiento y la identificación de causa raíz

## Valor de negocio
80% de reducción del tiempo, de 150 minutos a aproximadamente 30 minutos, dedicado a entender el error e identificar la causa raíz.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Document and Reporting Compliance.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Document and Reporting Compliance sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Ayuda a los usuarios a comprender errores sin revisar formatos técnicos complejos_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Document and Reporting Compliance y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Document and Reporting Compliance** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1137 |
| Producto | SAP Document and Reporting Compliance |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-GTF-CSC-EDO-DCC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d755130d-328a-4e41-b5b8-b0f507ee396c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d755130d-328a-4e41-b5b8-b0f507ee396c/

---

## [J1143] — BPMN Simulation Insights

## En una frase
Feature de SAP Signavio que integra simulaciones BPMN directamente en diagramas de proceso y convierte métricas como costos, tiempos de ciclo y uso de recursos en insights impulsados por IA.

## ¿Qué es?
Feature de SAP Signavio que integra simulaciones BPMN directamente en diagramas de proceso y convierte métricas como costos, tiempos de ciclo y uso de recursos en insights impulsados por IA. Es una capacidad de IA **Premium** de SAP Signavio solutions.

## Beneficios
- Facilita interpretar resultados de simulación
- ayuda a analizar costos, tiempos, recursos y potenciales cuellos de botella
- acelera decisiones de mejora de procesos

## Valor de negocio
Acelera el análisis de simulaciones BPMN y la toma de decisiones sobre mejora de procesos. No se encontró un KPI cuantitativo específico en la página consultada.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Signavio solutions.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Signavio solutions sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Facilita interpretar resultados de simulación_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1143 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-PM-MOD-SIM |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/45016b64-67d3-457e-a836-9ac08b193722/

---

## [J114] — Generation of SAP Fiori Elements and SAPUI5 Applications

## En una frase
Convierte **requisitos de negocio expresados en texto y/o imágenes** en una **aplicación full-stack SAP Fiori elements funcional** dentro de SAP Build Code, usando IA generativa.

## ¿Qué es?
Es una capacidad **Base** de **SAP Build Code** —el "Project Accelerator"— que simplifica el desarrollo convirtiendo requisitos de negocio (texto, imágenes o ambos) en un proyecto full-stack con una aplicación SAP Fiori elements totalmente operativa. Se accede desde el panel de SAP Fiori o mediante un comando en **Joule**, y emplea una vista especializada de SAP Fiori tools que aplica IA generativa para transformar los requisitos en artefactos técnicos a través de una interfaz sencilla.

## Beneficios
- Genera apps de UI SAP Fiori, **convierte mockups en aplicaciones ejecutables** con IA, automatiza tareas de codificación e integra las buenas prácticas de SAP Build Code.
- Acelera el desarrollo, permitiendo concentrar el esfuerzo en los aspectos complejos.

## Valor de negocio
- Forma **eficiente y "code-free"** de generar aplicaciones.
- **30% menos de costos** de desarrollo de aplicaciones.

## ¿Cómo funciona?
1. **Especificar requisitos:** el desarrollador describe lo que necesita en texto, sube una imagen/mockup, o ambos.
2. **Generación con IA:** desde el panel de SAP Fiori o vía comando en Joule, el Project Accelerator usa IA generativa para convertir esos requisitos en artefactos técnicos (modelo de datos, servicio, app Fiori elements).
3. **Proyecto full-stack funcional:** se obtiene un proyecto completo con una app Fiori elements operativa, alineada con las mejores prácticas de SAP Build Code, listo para refinar.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita un prototipo de app de gestión de pedidos para una demo en pocos días. **Cómo ayuda la feature:** a partir de una descripción textual y un boceto de pantalla, genera la app Fiori elements full-stack funcional, eliminando el andamiaje manual.
2. **Escenario:** Un consultor funcional con poca experiencia en código debe entregar una app CRUD sobre una entidad de negocio. **Cómo ayuda la feature:** describe la entidad y los campos en lenguaje natural y obtiene la aplicación generada, enfocándose solo en ajustar la lógica específica.

## ¿Cuándo usarla?
- Para **acelerar el arranque** de aplicaciones SAP Fiori elements/SAPUI5 y reducir el trabajo repetitivo de scaffolding.
- Útil tanto para perfiles pro-code (acelerar) como para perfiles de bajo código (habilitar).
- Requiere **SAP Build Code** y una suscripción a **Joule Base** o AI Units (la oferta se incluye con Joule Base sin costo adicional).

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J114 |
| Producto | SAP Build Code |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD |
| Industrias aplicables | Cross-Industry |
| Pricing | Incluida con **Joule Base** sin costo adicional; requiere suscripción a Joule Base o AI Units |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/08cc63b7-8fd7-4535-a9d6-f66a9030174c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/08cc63b7-8fd7-4535-a9d6-f66a9030174c/

---

## [J115] — Generation of SAP Mobile Applications

## En una frase
Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code.

## ¿Qué es?
Joule aporta capacidades de IA para desarrollo móvil en SAP Build Code. Puede generar componentes a partir de lenguaje natural, incluyendo código, modelos de datos, servicios, lógica de negocio, datos de ejemplo y pruebas unitarias. Es una capacidad de IA **Base** de SAP Build Code.

## Beneficios
- Generación de aplicaciones móviles desde lenguaje natural
- aumento de productividad del desarrollador
- mejora de calidad
- alineación con mejores prácticas SAP
- aprovechamiento de herramientas como SAP Mobile Development Kit y SAP BTP SDK for iOS

## Valor de negocio
SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar el desarrollo móvil y reducir esfuerzo manual en componentes técnicos repetitivos.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Build Code.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Build Code sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Generación de aplicaciones móviles desde lenguaje natural_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Code y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Code** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J115 |
| Producto | SAP Build Code |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9cd6bb5e-4178-44c2-b5b3-325c561273e4/

---

## [J1164] — Task Automation

## En una frase
La automatización de tareas asistida por IA permite a los usuarios de negocio crear procesos automatizados en apps SAP Fiori de SAP Cloud ERP.

## ¿Qué es?
La automatización de tareas asistida por IA permite a los usuarios de negocio crear procesos automatizados en apps SAP Fiori de SAP Cloud ERP. Los expertos de proceso los crean mediante instrucciones en lenguaje natural y documentos de grounding opcionales; la IA los analiza y mapea a las aplicaciones y herramientas requeridas, que el usuario revisa y aprueba. Los procesos se inician desde My Home o una app dedicada, con monitoreo y aprobación de cambios. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Automatiza tareas repetitivas en apps SAP Fiori de SAP Cloud ERP manteniendo al usuario en control
- permite a los expertos de negocio crear automatización con simples instrucciones en lenguaje natural, sin programar
- soporta toda la funcionalidad de UI
- escala la automatización con despliegue controlado por TI

## Valor de negocio
5% de reducción del tiempo medio de analizar, diseñar, modelar y monitorear un proceso (en días); 93% de reducción del tiempo medio de aprobar un reporte (en minutos); 5% de reducción de costos de calidad de datos.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Automatiza tareas repetitivas en apps SAP Fiori de SAP Cloud ERP manteniendo al usuario en control_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1164 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-FLP-EXT-IAU |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/0d089203-038a-4f68-a7e0-79078e26eae4/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0d089203-038a-4f68-a7e0-79078e26eae4/

---

## [J116] — Generation of SAP HANA Applications

## En una frase
SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código.

## ¿Qué es?
SAP Build Code usa Joule para potenciar el desarrollo de SAP HANA y la generación de código. La capacidad ayuda a crear modelos de datos, servicios, lógica de aplicación y pruebas desde lenguaje natural; además, incluye herramientas generativas para crear sentencias SQL desde prompts. Es una capacidad de IA **Base** de SAP Build Code.

## Beneficios
- Aceleración del desarrollo SAP HANA
- generación de código, modelos, servicios y pruebas
- soporte a extensiones clean core
- generación de SQL desde lenguaje natural
- desarrollo más eficiente y con menor esfuerzo manual

## Valor de negocio
SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor está en acelerar extensiones y aplicaciones HANA, mejorar productividad del desarrollador y facilitar un enfoque clean core.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Build Code.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Build Code sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Aceleración del desarrollo SAP HANA_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Code y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Code** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J116 |
| Producto | SAP Build Code |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7ee277ac-20af-4458-bb5a-8836d6a51899/

---

## [J1173] — Deep Research Capability

## En una frase
La capacidad de deep research en Joule permite a los usuarios buscar, preguntar y acceder al conocimiento e insights que necesitan dentro de su flujo de trabajo.

## ¿Qué es?
La capacidad de deep research en Joule permite a los usuarios buscar, preguntar y acceder al conocimiento e insights que necesitan dentro de su flujo de trabajo. Accediendo a recursos internos y a conocimiento externo —estructurado o no estructurado— Joule entrega información relevante y accionable, asegurando cumplimiento y maximizando la productividad. Es una capacidad de IA **Base** de Joule.

## Beneficios
- Reduce el tiempo dedicado manualmente a tareas intensivas en investigación
- evita salir del flujo de trabajo para investigar
- las preguntas aclaratorias mejoran el prompting y los resultados de la investigación

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el tiempo dedicado manualmente a tareas intensivas en investigación_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1173 |
| Producto | Joule |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-JDR |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/0cbab727-02fe-47d3-9bf1-ff96d6c2ae62/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0cbab727-02fe-47d3-9bf1-ff96d6c2ae62/

---

## [J117] — Form Extension in Localization as a Self-Service

## En una frase
Genera y actualiza automáticamente formularios localizados personalizados según requisitos de negocio, enlaza fuentes de datos y carga los formularios en SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Genera y actualiza automáticamente formularios localizados personalizados según requisitos de negocio, enlaza fuentes de datos y carga los formularios en SAP S/4HANA Cloud Public Edition. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Acelera la creación o actualización de formularios localizados
- reduce esfuerzo y costo
- ayuda a responder a requerimientos locales de negocio con mayor rapidez

## Valor de negocio
Reducción estimada del 80% en tiempo y costo para crear plantillas de formularios localizados.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera la creación o actualización de formularios localizados_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J117 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-LOC-MFT |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f5f33f40-36d4-4265-b709-461c0c151587/

---

## [J1182] — Settlement Rule Proposal for Asset Capitalization

## En una frase
Propone reglas de liquidación para la capitalización de activos en medidas de inversión.

## ¿Qué es?
Propone reglas de liquidación para la capitalización de activos en medidas de inversión. La funcionalidad asiste la creación de reglas completas y ayuda a determinar receptores de liquidación mediante IA generativa. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Reduce el trabajo manual al crear reglas de liquidación
- permite generar, revisar y editar propuestas antes de aplicarlas
- aporta mayor consistencia al tratamiento de medidas de inversión

## Valor de negocio
Ahorro de tiempo en procesos de Asset Accounting y Project/Investment Management, menor riesgo de errores manuales en reglas de liquidación y mayor trazabilidad en la revisión de propuestas.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce el trabajo manual al crear reglas de liquidación_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1182 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | IM-FA |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/43cfa9f3-485c-4021-8dd1-e1349f471bea/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/43cfa9f3-485c-4021-8dd1-e1349f471bea/

---

## [J1195] — SAP Joule for Developers‚ ABAP AI capabilities

## En una frase
Joule for Developers con capacidades ABAP AI apoya el desarrollo ABAP en SAP S/4HANA Cloud Private Edition, ayudando a desarrolladores con asistencia generativa dentro del ciclo de desarrollo.

## ¿Qué es?
Joule for Developers con capacidades ABAP AI apoya el desarrollo ABAP en SAP S/4HANA Cloud Private Edition, ayudando a desarrolladores con asistencia generativa dentro del ciclo de desarrollo. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Incrementa la productividad del desarrollador, facilita el trabajo diario y contribuye a acelerar tareas de codificación y soporte técnico ABAP

## Valor de negocio
La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA y beneficios de eficiencia en desarrollo.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Private Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Incrementa la productividad del desarrollador_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1195 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-AI-GEN-HUB |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/795cf9fa-d0cc-42b0-a3d7-52e8067e847d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/795cf9fa-d0cc-42b0-a3d7-52e8067e847d/

---

## [J120] — Performance Indicators Recommender

## En una frase
Ayuda a pasar del problema de negocio a un enfoque de medición recomendando KPIs y PPIs relevantes desde un repositorio amplio de indicadores de desempeño de procesos.

## ¿Qué es?
Ayuda a pasar del problema de negocio a un enfoque de medición recomendando KPIs y PPIs relevantes desde un repositorio amplio de indicadores de desempeño de procesos. Es una capacidad de IA **Premium** de SAP Signavio solutions.

## Beneficios
- Entrega recomendaciones rápidas basadas en buenas prácticas
- conecta problema, proceso e indicador
- facilita un enfoque self-service para definir un marco inicial de monitoreo de desempeño

## Valor de negocio
5% menor erosión de valor asociada a una selección deficiente de indicadores de desempeño de proceso.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP Signavio solutions.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP Signavio solutions que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Entrega recomendaciones rápidas basadas en buenas prácticas_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J120 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4be4b091-a23d-4f59-975e-65cb6a4a8fc5/

---

## [J121] — Process Recommender

## En una frase
Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio.

## ¿Qué es?
Process Recommender ofrece recomendaciones de mejores prácticas y modelos de proceso preconfigurados basados en la base de conocimiento de SAP Signavio. Es una capacidad de IA **Premium** de SAP Signavio solutions.

## Beneficios
- Ayuda a partir de modelos recomendados en vez de diseñar desde cero, reduce talleres extensos de levantamiento y facilita seleccionar procesos alineados con mejores prácticas

## Valor de negocio
La capacidad apunta a mejorar la productividad de recursos BPM, reducir costos de consultoría para mapeo de procesos y disminuir el tiempo de capacitación interna.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP Signavio solutions.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP Signavio solutions que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Ayuda a partir de modelos recomendados en vez de diseñar desde cero_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J121 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0568e3e9-bef3-46d5-8b51-f519d8838320/

---

## [J127] — Joule with SAP Signavio solutions

## En una frase
Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural.

## ¿Qué es?
Permite navegar y consultar diagramas de procesos, elementos de diccionario, documentos y métricas en SAP Signavio mediante búsqueda y comandos en lenguaje natural. Es una capacidad de IA **Base** de SAP Signavio solutions.

## Beneficios
- Reduce tiempo y esfuerzo para encontrar información
- facilita decisiones y mejoras de proceso basadas en datos
- mejora la experiencia y engagement de usuarios de negocio

## Valor de negocio
50% más rapidez en búsquedas informativas; 50% más rapidez en ejecución de tareas de navegación y transaccionales; mejor calidad de resultados de búsqueda y experiencia de usuario.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Signavio solutions.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Signavio solutions sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce tiempo y esfuerzo para encontrar información_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J127 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1ed93ca-2efd-4096-8300-613adf55cfef/

---

## [J1284] — Document Data Extraction

## En una frase
Extrae y procesa automáticamente información clave de PDFs e imágenes escaneadas usando IA, con o sin plantillas.

## ¿Qué es?
Extrae y procesa automáticamente información clave de PDFs e imágenes escaneadas usando IA, con o sin plantillas. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Reduce la entrada manual de datos
- soporta documentos estándar como facturas, órdenes de compra y avisos de pago
- permite extracción desde documentos estructurados y no estructurados mediante plantillas preconfiguradas o personalizadas

## Valor de negocio
500 horas ahorradas por mes; 70% de facturas procesadas mediante automatización sin intervención manual; menos de 1 minuto para procesar una factura desde la llegada hasta la contabilización.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Build Process Automation, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Build Process Automation y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce la entrada manual de datos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1284 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577af53b-83ac-4c49-8b02-72114d45ceb6/

---

## [J1310] — Purchase Order Approvals Reminder

## En una frase
La capacidad ayuda a dar seguimiento a aprobaciones de órdenes de compra, identificar aprobadores y enviar recordatorios automatizados dentro del flujo de trabajo de compras.

## ¿Qué es?
La capacidad ayuda a dar seguimiento a aprobaciones de órdenes de compra, identificar aprobadores y enviar recordatorios automatizados dentro del flujo de trabajo de compras. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Mejora la productividad al reducir navegación manual, acelerar el envío de recordatorios y facilitar el seguimiento de aprobaciones pendientes

## Valor de negocio
Aporta valor al disminuir retrasos en aprobaciones de compra, reducir seguimiento manual y mejorar la continuidad de los procesos de procurement.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Mejora la productividad al reducir navegación manual_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1310 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | MM-PUR-PO-WFL-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/13b68daa-1ba2-4bfa-b7d3-4f65f4900d07/

---

## [J1325] — Project Billing Price Verification Agent

## En una frase
En la app Manage Project Billing de SAP S/4HANA Cloud Public Edition, ayuda a los especialistas de facturación a identificar rápidamente discrepancias entre precios acordados y montos facturados.

## ¿Qué es?
En la app Manage Project Billing de SAP S/4HANA Cloud Public Edition, ayuda a los especialistas de facturación a identificar rápidamente discrepancias entre precios acordados y montos facturados. Identifica los contratos y Statements of Work (SoW) del proyecto del cliente, extrae datos clave de precios y los compara con los valores de la Project Billing Request, resaltando discrepancias, aportando contexto y sugiriendo acciones correctivas. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Mejora la exactitud de la facturación
- mejora la productividad reduciendo la revisión manual de datos de precio
- mejora la transparencia (si no existe contrato, el especialista decide si facturar)
- reduce demoras en la facturación

## Valor de negocio
75% de reducción del tiempo de resolver discrepancias de precio; 75% de reducción de la fuga de ingresos por facturación incorrecta no detectada; mejor flujo de caja y menor DSO por menos demoras en el ciclo de facturación.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Mejora la exactitud de la facturación_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1325 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | PPM-SCL-BIL-FIO |
| Industrias aplicables | Professional Services |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/540eb523-953a-43eb-8f93-525ee99d57fd/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/540eb523-953a-43eb-8f93-525ee99d57fd/

---

## [J135] — Conversational Planning

## En una frase
Apoya a los planificadores en la creación de planes de transporte eficientes, incluyendo cadenas de acciones con múltiples instrucciones, mediante lenguaje natural en el transportation cockpit.

## ¿Qué es?
Apoya a los planificadores en la creación de planes de transporte eficientes, incluyendo cadenas de acciones con múltiples instrucciones, mediante lenguaje natural en el transportation cockpit. El cockpit puede mostrar los requerimientos de planificación y las capacidades disponibles. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Mejora la eficiencia en la planificación de transporte
- mejora la experiencia del usuario

## Valor de negocio
50% de mejora en la productividad de los planificadores de transporte en la planificación y programación de rutas.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Private Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Mejora la eficiencia en la planificación de transporte_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J135 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BC-SRV-BUM |
| Industrias aplicables | Consumer Products |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Supply Chain Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/54d5a00e-2519-46da-88fa-b58b4f8ff4dc/

---

## [J1394] — Document Summary

## En una frase
Permite resumir documentación de SAP Cloud ALM mediante capacidades de IA dentro de la aplicación de documentos.

## ¿Qué es?
Permite resumir documentación de SAP Cloud ALM mediante capacidades de IA dentro de la aplicación de documentos. Es una capacidad de IA **Base** de SAP Cloud ALM.

## Beneficios
- Ayuda a comprender más rápido el contenido de documentos seleccionados y reduce el esfuerzo de lectura manual

## Valor de negocio
No disponible en la página consultada.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Cloud ALM, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Cloud ALM y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Ayuda a comprender más rápido el contenido de documentos seleccionados y reduce el esfuerzo de lectura manual_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Cloud ALM y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Cloud ALM** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1394 |
| Producto | SAP Cloud ALM |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | SV-CLM-IMP-DOC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/111df0da-5177-4769-88ea-6a200ecae091/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/111df0da-5177-4769-88ea-6a200ecae091/

---

## [J139] — Chart Summary

## En una frase
Genera automáticamente un **resumen de texto de tres viñetas** de un gráfico de SAP Analytics Cloud y lo inserta como comentario editable en **Microsoft PowerPoint**.

## ¿Qué es?
Es una capacidad **Premium** del **add-in de SAP Analytics Cloud para Microsoft PowerPoint**. Con IA generativa produce un resumen de texto (tres viñetas) correspondiente a un gráfico de SAP Analytics Cloud y lo inserta en la presentación como un **comentario de texto editable**. El resumen puede **regenerarse bajo demanda** para reflejar cualquier cambio en los valores de datos del gráfico asociado.

## Beneficios
- Reduce el tiempo necesario para **escribir y actualizar** el resumen de un gráfico.
- Mejora la **accesibilidad y la comprensión** del gráfico.

## Valor de negocio
- **96% de reducción del tiempo** para escribir y actualizar el resumen de un gráfico (cifra publicada por SAP).

## ¿Cómo funciona?
1. **Gráfico en PowerPoint:** el usuario tiene un gráfico de SAP Analytics Cloud insertado en una diapositiva mediante el add-in.
2. **Generación del resumen:** invoca la función de chart summary; la IA generativa analiza el gráfico y produce un resumen de **tres viñetas**.
3. **Inserción editable:** el resumen se añade a la presentación como comentario de texto que el usuario puede editar.
4. **Regeneración bajo demanda:** si cambian los datos del gráfico, se regenera el resumen para mantenerlo alineado.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un controller prepara la presentación mensual de resultados con varios gráficos de SAC. **Cómo ayuda la feature:** en lugar de redactar manualmente el comentario de cada gráfico, genera los resúmenes de tres viñetas y solo los ajusta, ahorrando tiempo en cada cierre.
2. **Escenario:** Los datos de un KPI se actualizan poco antes de la reunión. **Cómo ayuda la feature:** regenera el resumen del gráfico afectado con un clic, evitando inconsistencias entre el texto y las cifras mostradas.

## ¿Cuándo usarla?
- Cuando se construyen **presentaciones recurrentes en PowerPoint** a partir de gráficos de SAP Analytics Cloud.
- Requiere el **add-in de SAP Analytics Cloud para Microsoft PowerPoint**.
- Es **Premium**: su consumo se factura por **AI Units** (ver pricing).

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J139 |
| Producto | SAP Analytics Cloud (add-in para Microsoft PowerPoint) |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-OF-PPA |
| Industrias aplicables | Cross-Industry |
| Pricing | Por **AI Units**: 1 Request → 0,06 AI Units (≈ EUR 7 por bloque de referencia, según AI Estimator) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/825764c4-6de1-4789-bd0c-74243c60854b/

---

## [J145] — Joule with SAP Build Work Zone

## En una frase
Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo.

## ¿Qué es?
Permite interactuar con SAP apps y SAP Build Work Zone mediante lenguaje natural, obteniendo insights y acciones dentro del espacio de trabajo. También soporta acceso remoto mediante SAP Mobile Start o sitio móvil. Es una capacidad de IA **Base** de SAP Build Work Zone.

## Beneficios
- Interacción natural con Work Zone
- acceso instantáneo a insights, apps y contenido de sistemas SAP conectados
- navegación centrada en el workspace sin abandonar el entorno de trabajo

## Valor de negocio
50% más rapidez en búsquedas informativas; 59% más rapidez en ejecución de tareas de navegación y transaccionales; mayor satisfacción del usuario de negocio.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Build Work Zone.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Build Work Zone sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Interacción natural con Work Zone_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Work Zone y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Work Zone** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J145 |
| Producto | SAP Build Work Zone |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8be96d98-f16d-41b4-968c-c295043c1d73/

---

## [J146] — SAP Joule for Consultants

## En una frase
SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud.

## ¿Qué es?
SAP Joule for Consultants proporciona asistencia de IA para acelerar proyectos SAP y transformaciones cloud. Está orientado a consultores y equipos de implementación que necesitan acceso guiado a conocimiento, recomendaciones y soporte durante actividades de delivery. Es una capacidad de IA **Premium** de SAP Joule for Consultants.

## Beneficios
- Reduce el tiempo de búsqueda de información, ayuda a estructurar respuestas y recomendaciones, y mejora la productividad de consultores en tareas de análisis, documentación y soporte de implementación

## Valor de negocio
La página posiciona el valor en acelerar la entrega de proyectos SAP, mejorar la productividad del equipo consultor y facilitar el acceso a conocimiento SAP relevante durante transformaciones cloud.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Joule for Consultants sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el tiempo de búsqueda de información_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Joule for Consultants y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J146 |
| Producto | SAP Joule for Consultants |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-GAIF-SCC |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package SAP Joule for Consultants and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3c3c6f7d-7310-47a9-ae52-d7ddd2f0c2f2/

---

## [J147] — Script Optimization

## En una frase
Script Optimization en SAP Integration Suite ayuda a optimizar scripts personalizados.

## ¿Qué es?
Script Optimization en SAP Integration Suite ayuda a optimizar scripts personalizados. La página indica que la función está disponible como promoción gratuita hasta septiembre de 2026 y posteriormente pasará a ser una función Premium. Es una capacidad de IA **Base** de SAP Integration Suite.

## Beneficios
- Mitiga riesgos asociados a scripts personalizados, ayuda a mejorar calidad y mantenibilidad, y apoya la alineación con buenas prácticas en scripts de integración

## Valor de negocio
Aporta valor al reducir esfuerzo de revisión manual de scripts y al mejorar confiabilidad, calidad y eficiencia técnica en integraciones de SAP Integration Suite.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP Integration Suite.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP Integration Suite con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Mitiga riesgos asociados a scripts personalizados_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Integration Suite y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Integration Suite** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J147 |
| Producto | SAP Integration Suite |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-HCI-PI-RC-SO |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/99357ead-1ee2-4b9d-9b2f-f74d10f09262/

---

## [J148] — Analytical Insights

## En una frase
Capacidad de Joule que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP.

## ¿Qué es?
Capacidad de Joule que permite obtener insights analíticos mediante preguntas en lenguaje natural desde aplicaciones de SAP. Se integra con Just Ask de SAP Analytics Cloud dentro de SAP Business Data Cloud. Es una capacidad de IA **Base** de Joule.

## Beneficios
- Permite obtener insights desde Joule sin navegar dashboards
- entrega información contextualizada para aplicaciones SAP
- ayuda a empleados a tomar decisiones más rápidas
- ofrece una experiencia de usuario más fluida

## Valor de negocio
Hasta 80% de reducción en los pasos necesarios para obtener insights analíticos.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Permite obtener insights desde Joule sin navegar dashboards_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J148 |
| Producto | Joule |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD_ANA_JOU |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b354ca6f-3bbc-43d0-9c83-b3140b925962/

---

## [J151] — Master Data Governance

## En una frase
Permite usar lenguaje natural para crear y actualizar solicitudes de cambio de datos maestros dentro de procesos de Master Data Governance en SAP S/4HANA Cloud Private Edition.

## ¿Qué es?
Permite usar lenguaje natural para crear y actualizar solicitudes de cambio de datos maestros dentro de procesos de Master Data Governance en SAP S/4HANA Cloud Private Edition. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Ahorra tiempo al solicitar cambios de datos maestros
- simplifica la interacción de negocio con MDG
- reduce trabajo manual de creación y revisión de change requests
- ayuda a disminuir el riesgo de omitir información crítica

## Valor de negocio
60% de reducción del esfuerzo para crear solicitudes de cambio de datos maestros; 20% de reducción del esfuerzo para revisar solicitudes de cambio; la página también indica una reducción adicional del 5% en un indicador que aparece truncado en el contenido accesible.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Ahorra tiempo al solicitar cambios de datos maestros_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J151 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-MDG-AF |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4cb78833-492a-43db-abb2-01747e7e4335/

---

## [J162] — SAP Joule for Developers‚ ABAP AI capabilities

## En una frase
Joule for Developers con capacidades ABAP AI ayuda a acelerar el desarrollo ABAP en SAP BTP, ABAP environment mediante asistencia generativa para tareas de desarrollo.

## ¿Qué es?
Joule for Developers con capacidades ABAP AI ayuda a acelerar el desarrollo ABAP en SAP BTP, ABAP environment mediante asistencia generativa para tareas de desarrollo. Es una capacidad de IA **Base** de SAP BTP‚ ABAP environment.

## Beneficios
- Impulsa la productividad del desarrollador, apoya el trabajo diario y facilita la creación, comprensión y mejora de artefactos ABAP

## Valor de negocio
La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA, junto con mejoras de productividad en actividades de desarrollo.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP BTP‚ ABAP environment.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP BTP‚ ABAP environment sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Impulsa la productividad del desarrollador_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP BTP‚ ABAP environment y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP BTP‚ ABAP environment** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J162 |
| Producto | SAP BTP‚ ABAP environment |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-CP-ABA |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/7f373198-9a41-4416-9eed-bdfca445d37a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7f373198-9a41-4416-9eed-bdfca445d37a/

---

## [J1684] — Enterprise Architecture Decision Management

## En una frase
Asiste a los arquitectos empresariales en la **redacción de decisiones de arquitectura** dentro de SAP LeanIX, generando la entrada de decisión a partir del contexto que el arquitecto proporciona (p. ej. un diagrama de transformación).

## ¿Qué es?
Es una capacidad **Base** de **SAP LeanIX solutions** que aplica IA a la creación de **architecture decisions** —los registros con los que las organizaciones documentan, siguen y alinean sus decisiones de arquitectura empresarial directamente en SAP LeanIX. En vez de redactarlas manualmente, el arquitecto aporta el contexto de la decisión deseada (por ejemplo, un diagrama empresarial que detalla una transformación propuesta) y la IA **genera la entrada de la decisión** con el contexto y la información relevantes que los stakeholders necesitan para aprobarla.

## Beneficios
- Mejora la **productividad del arquitecto**, ahorrando tiempo y reduciendo la extracción manual de datos.
- Facilita la **colaboración** para revisar y aprobar decisiones de arquitectura.
- Mejora la **eficiencia general del flujo de trabajo**.
- Asegura que las decisiones de arquitectura se **creen y concluyan a tiempo**, elevando la eficiencia operativa de la arquitectura.

## Valor de negocio
- (La Detail Page no publica una métrica cuantitativa de Business Value para este caso; el valor se expresa en los beneficios de productividad y colaboración listados arriba.)

## ¿Cómo funciona?
1. **Aportar contexto:** el arquitecto proporciona a la IA el contexto de la decisión deseada, como un diagrama de empresa que describe una transformación propuesta.
2. **Generación de la decisión:** la IA redacta la **architecture decision** con la información y el contexto relevantes para los stakeholders.
3. **Revisión y aprobación:** la entrada generada se comparte para revisión colaborativa y aprobación dentro de SAP LeanIX, acelerando el cierre de la decisión.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un arquitecto propone migrar un conjunto de aplicaciones legadas a SAP BTP y debe documentar formalmente la decisión. **Cómo ayuda la feature:** a partir del diagrama de la transformación, la IA genera el borrador de la decisión con contexto, alternativas e implicaciones, listo para que los stakeholders lo revisen.
2. **Escenario:** El comité de arquitectura tiene un backlog de decisiones sin documentar que frena las aprobaciones. **Cómo ayuda la feature:** acelera la creación de las entradas de decisión y reduce el tiempo hasta su conclusión y aprobación.

## ¿Cuándo usarla?
- Cuando se gestiona **architecture decision management** en SAP LeanIX y la redacción manual de decisiones ralentiza las aprobaciones.
- Aporta más cuando existe contexto estructurado (diagramas, inventario) que la IA pueda aprovechar.
- Requiere SAP LeanIX solutions.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J1684 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | Actualmente **no requiere AI Units** para usar esta oferta en el Cloud Service subyacente (sujeto a cambio) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e9e98379-9c5f-4f4a-84f6-12a772c66ae2/

---

## [J169] — Sales Order Fulfillment Monitoring

## En una frase
La capacidad ayuda a los equipos de ventas a monitorear y resolver problemas de cumplimiento de pedidos mediante IA.

## ¿Qué es?
La capacidad ayuda a los equipos de ventas a monitorear y resolver problemas de cumplimiento de pedidos mediante IA. Los pedidos se resumen a nivel de cabecera e ítem en lenguaje natural, se identifican problemas de fulfillment y se facilita la navegación hacia acciones correctivas. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Mejora la precisión de pedidos, incrementa la satisfacción del cliente y apoya a los equipos comerciales con una resolución más rápida de bloqueos o demoras en el cumplimiento

## Valor de negocio
La página destaca un 30% más de productividad del personal en consultas de pedidos de venta y una reducción del 10% en churn de clientes asociado a retrasos en fulfillment.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Private Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Private Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Mejora la precisión de pedidos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J169 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/16fe0c99-25ff-48e2-81e5-f100d4c64767/

---

## [J172] — 2D Hotspot Creation

## En una frase
Permite a los usuarios de SAP Integrated Product Development crear automáticamente hotspots en planos 2D y asociarlos con datos de negocio del back-end, agilizando la transformación digital de los planos heredados (legacy).

## ¿Qué es?
Permite a los usuarios de SAP Integrated Product Development crear automáticamente hotspots en planos 2D y asociarlos con datos de negocio del back-end, agilizando la transformación digital de los planos heredados (legacy). Es una capacidad de IA **Base** de SAP Integrated Product Development.

## Beneficios
- Mejora significativamente la eficiencia de la creación de hotspots y el mapeo de datos de negocio
- reduce errores humanos del proceso manual
- permite aprovechar planos digitalizados para catálogos interactivos de repuestos o gestión de activos

## Valor de negocio
2% de aumento en la tasa de resolución a la primera; 1% de reducción de downtime no planificado; 10% de mejora en la productividad del técnico de servicio de campo; digitalización acelerada de planos de producto heredados.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Integrated Product Development.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Integrated Product Development para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Mejora significativamente la eficiencia de la creación de hotspots y el mapeo de datos de negocio_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Integrated Product Development y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Integrated Product Development** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J172 |
| Producto | SAP Integrated Product Development |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c523c267-0a3d-4430-9cba-e75df8caac1b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c523c267-0a3d-4430-9cba-e75df8caac1b/

---

## [J173] — Declaration Image Analysis

## En una frase
Extrae automáticamente información de declaraciones de distintos formatos sin interacción del usuario y contabiliza los datos de la transacción en SAP Green Token.

## ¿Qué es?
Extrae automáticamente información de declaraciones de distintos formatos sin interacción del usuario y contabiliza los datos de la transacción en SAP Green Token. Elimina la dependencia de mecanismos de extracción propios del cliente y extrae datos con precisión de tipos de documento diversos, donde la información requerida está bien definida pero la estructura y el formato no son uniformes. Es una capacidad de IA **Base** de SAP Green Token.

## Beneficios
- Reduce el esfuerzo manual de extracción de datos
- reduce el esfuerzo y costo de mantener mecanismos de extracción internos a medida

## Valor de negocio
100% de reducción del costo de la herramienta de extracción de datos; 93% de reducción del tiempo de revisar, interpretar y contabilizar datos en SAP Green Token; 100% de reducción del tiempo de búsqueda de declaraciones.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Green Token, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Green Token y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el esfuerzo manual de extracción de datos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Green Token y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Green Token** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J173 |
| Producto | SAP Green Token |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | SUS-GT |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ef9efdef-7300-4580-9c54-5664e1c99f95/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ef9efdef-7300-4580-9c54-5664e1c99f95/

---

## [J178] — Inventory Builder

## En una frase
SAP LeanIX Inventory Builder acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX.

## ¿Qué es?
SAP LeanIX Inventory Builder acelera el onboarding inicial de clientes, el mantenimiento de inventario y otras tareas de edición de datos dentro de SAP LeanIX. Es una capacidad de IA **Premium** de SAP LeanIX solutions.

## Beneficios
- Acelera onboarding y mantenimiento de inventario
- apoya tareas de edición de datos
- ayuda a mejorar productividad en la gestión de inventarios de arquitectura empresarial

## Valor de negocio
El valor está en reducir esfuerzo manual para construir y mantener inventarios de arquitectura empresarial, facilitando una base de datos más completa y útil para análisis y decisiones.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP LeanIX solutions, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP LeanIX solutions y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Acelera onboarding y mantenimiento de inventario_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J178 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3b4cd740-d09d-4e79-9efc-69bf49221e83/

---

## [J180] — SAP HANA application migration

## En una frase
La función automatiza la migración de la capa de servicios SAP HANA XS/XSA hacia SAP CAP usando GenAI.

## ¿Qué es?
La función automatiza la migración de la capa de servicios SAP HANA XS/XSA hacia SAP CAP usando GenAI. Ayuda a convertir artefactos como XSJSLIB, XSODATA y XSJS en servicios modernos basados en CAP, alineados con la guía de desarrollo de SAP BTP. Es una capacidad de IA **Base** de SAP HANA Cloud.

## Beneficios
- Acelera la migración hacia CAP, reduce esfuerzo manual en la conversión de servicios y facilita la transformación cloud-native de aplicaciones SAP HANA

## Valor de negocio
El valor se centra en acelerar la modernización técnica de aplicaciones SAP HANA y reducir el esfuerzo requerido para migrar capas de servicio legadas a una arquitectura CAP.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP HANA Cloud.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP HANA Cloud con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Acelera la migración hacia CAP_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP HANA Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP HANA Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J180 |
| Producto | SAP HANA Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-XS-TLS-MIG |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/14bbef6b-5d85-4221-bd0e-342f569ef628/

---

## [J181] — Smart Solution for Situations in My Home

## En una frase
Ahorra tiempo ayudando a los usuarios de negocio a identificar los elementos que requieren su atención inmediata desde su último inicio de sesión.

## ¿Qué es?
Ahorra tiempo ayudando a los usuarios de negocio a identificar los elementos que requieren su atención inmediata desde su último inicio de sesión. Permite a los usuarios de SAP S/4HANA Cloud Public Edition gestionar y priorizar tareas e información de forma eficiente, ofreciendo en la página de entrada un resumen completo de los elementos y actualizaciones clave realizados desde la última sesión. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Permite enfocarse en lo importante identificando y actuando rápidamente sobre elementos de alta prioridad
- acelera el acceso a insights esenciales y accionables sin visitar múltiples fuentes
- aumenta la productividad mostrando la información que más importa
- logra ahorros de tiempo significativos simplificando las tareas diarias

## Valor de negocio
46% de reducción del tiempo de resolver situaciones.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP S/4HANA Cloud Public Edition.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP S/4HANA Cloud Public Edition que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Permite enfocarse en lo importante identificando y actuando rápidamente sobre elementos de alta prioridad_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J181 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-UX-MY |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5a6f7a49-1bbf-4e9b-b2e0-57aad5f2de6d/

---

## [J193] — UI Generation from Data

## En una frase
Permite generar automáticamente páginas de aplicación a partir de entidades de datos ya integradas en un proyecto de SAP Build Apps, incluyendo operaciones CRUD como punto de partida.

## ¿Qué es?
Permite generar automáticamente páginas de aplicación a partir de entidades de datos ya integradas en un proyecto de SAP Build Apps, incluyendo operaciones CRUD como punto de partida. Es una capacidad de IA **Base** de SAP Build Apps.

## Beneficios
- Acelera el desarrollo low-code
- reduce el trabajo manual de creación de pantallas
- ofrece una base inicial que los desarrolladores pueden adaptar y extender rápidamente

## Valor de negocio
Reduce el tiempo de construcción de aplicaciones, mejora la productividad de equipos low-code y acelera la entrega de extensiones o aplicaciones empresariales basadas en datos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Apps.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Apps para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera el desarrollo low-code_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Apps y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Apps** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J193 |
| Producto | SAP Build Apps |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-LCA-ACP |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/691b7e82-b4ee-41f2-aae3-43b5b81be6f6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/691b7e82-b4ee-41f2-aae3-43b5b81be6f6/

---

## [J195] — Skill Builder

## En una frase
Permite extender Joule mediante skills ajustadas a necesidades de negocio.

## ¿Qué es?
Permite extender Joule mediante skills ajustadas a necesidades de negocio. Las skills ejecutan operaciones predefinidas desde la interfaz conversacional de Joule y pueden integrarse con sistemas SAP y no SAP. Es una capacidad de IA **Base** de Joule Studio.

## Beneficios
- Facilita automatizar tareas frecuentes con skills contextuales
- permite recuperar datos o ejecutar transacciones desde Joule
- conecta procesos y sistemas empresariales con una experiencia conversacional

## Valor de negocio
Reducción del tiempo para desplegar skills personalizadas de Joule y disminución del tiempo dedicado a tareas de negocio repetitivas mediante automatización conversacional.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule Studio sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Facilita automatizar tareas frecuentes con skills contextuales_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule Studio y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule Studio** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J195 |
| Producto | Joule Studio |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD-JLE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e93aa292-e7f4-449d-9586-f1a8510d5ab6/

---

## [J202] — Content Creation and Summary

## En una frase
Ayuda a los usuarios de negocio de SAP Build Work Zone a crear y refinar contenido directamente en las workpages.

## ¿Qué es?
Ayuda a los usuarios de negocio de SAP Build Work Zone a crear y refinar contenido directamente en las workpages. Genera texto a partir de los prompts del usuario y resume contenido existente en formatos claros y concisos, integrando la asistencia de IA en el proceso de autoría para producir contenido de alta calidad con rapidez y mantener claridad entre páginas. Es una capacidad de IA **Base** de SAP Build Work Zone, advanced edition.

## Beneficios
- Aumenta la productividad con escritura asistida por IA para crear contenido de alta calidad rápidamente
- resume textos extensos en formatos claros y concisos para facilitar la lectura y comprensión

## Valor de negocio
Aumenta la productividad del usuario de negocio reduciendo el tiempo dedicado a cada blog de cara al exterior de 6 horas a 1 hora.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Work Zone, advanced edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Work Zone, advanced edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Aumenta la productividad con escritura asistida por IA para crear contenido de alta calidad rápidamente_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Work Zone, advanced edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Work Zone, advanced edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J202 |
| Producto | SAP Build Work Zone, advanced edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-SF-SWZ |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/39ef0f64-fc3b-4420-92ee-fa5e052d486b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/39ef0f64-fc3b-4420-92ee-fa5e052d486b/

---

## [J212] — Process Analyzer‚ Text To Widget

## En una frase
Process Analyzer, Text to Widget permite crear widgets de dashboard a partir de consultas en lenguaje natural sobre datos de procesos.

## ¿Qué es?
Process Analyzer, Text to Widget permite crear widgets de dashboard a partir de consultas en lenguaje natural sobre datos de procesos. Es una capacidad de IA **Base** de SAP Signavio solutions.

## Beneficios
- Acelera la creación de visualizaciones, facilita el análisis diario para usuarios no técnicos y libera a los analistas para tareas de mayor complejidad

## Valor de negocio
El valor se centra en acelerar el time-to-value de los dashboards de procesos, mejorar la autonomía de usuarios de negocio y reducir dependencia de equipos técnicos para análisis básicos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Signavio solutions.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Signavio solutions para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera la creación de visualizaciones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J212 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/6d74c5e9-32c1-443c-be23-c7ebbc51d573/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6d74c5e9-32c1-443c-be23-c7ebbc51d573/

---

## [J213] — Process Modeler

## En una frase
Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio.

## ¿Qué es?
Process Modeler convierte una descripción textual de un proceso de negocio en un diagrama BPMN inicial dentro de SAP Signavio. Es una capacidad de IA **Premium** de SAP Signavio solutions.

## Beneficios
- Acelera el modelado de procesos, permite que usuarios no técnicos contribuyan con descripciones en texto y reduce el trabajo manual requerido para crear diagramas base

## Valor de negocio
La página destaca una reducción del tiempo de modelado de procesos y un menor costo asociado al modelado manual, además de mejorar la colaboración entre negocio y equipos de procesos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Signavio solutions.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Signavio solutions para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera el modelado de procesos_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J213 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-AI-T2P |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/84eb743d-acdb-48ff-b933-ec51fe9f5f12/

---

## [J214] — Database Administration

## En una frase
Ofrece una nueva experiencia de usuario para administradores de base de datos potenciada por IA generativa: navegación por aplicaciones, conversión de lenguaje natural a SQL, resúmenes de alertas, aprovisionamiento de nuevas instancias y respuesta a preguntas sobre SAP HANA Cloud.

## ¿Qué es?
Ofrece una nueva experiencia de usuario para administradores de base de datos potenciada por IA generativa: navegación por aplicaciones, conversión de lenguaje natural a SQL, resúmenes de alertas, aprovisionamiento de nuevas instancias y respuesta a preguntas sobre SAP HANA Cloud. Mejora la eficiencia operativa simplificando tareas complejas. Es una capacidad de IA **Base** de SAP HANA Cloud.

## Beneficios
- Genera el resumen de cualquier incidencia
- navega a una app específica
- genera un resumen de alertas
- genera sentencias SQL a partir de texto plano
- responde cualquier pregunta sobre SAP HANA Cloud

## Valor de negocio
20% menos esfuerzo para diagnosticar y resolver incidencias de HANA Cloud; 10% menor pérdida de ingreso operativo por downtime de HANA Cloud; mayor rapidez de productividad para administradores de SAP HANA recién contratados.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP HANA Cloud.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP HANA Cloud. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Genera el resumen de cualquier incidencia_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP HANA Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP HANA Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J214 |
| Producto | SAP HANA Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | HAN-CLS-CPT |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/28b14ec8-e7be-4966-b33e-787021b2d05d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/28b14ec8-e7be-4966-b33e-787021b2d05d/

---

## [J224] — Content Generation for Catalog

## En una frase
Ayuda a los data stewards a automatizar la generación de descripciones de negocio, términos de negocio y KPIs.

## ¿Qué es?
Ayuda a los data stewards a automatizar la generación de descripciones de negocio, términos de negocio y KPIs. Genera descripciones de negocio precisas, contextuales y completas para el activo (automatización de descripción de activos) y automatiza la clasificación de datos con etiquetas apropiadas derivadas de una lista jerárquica de tags (auto-tagging de activos). Es una capacidad de IA **Premium** de SAP Datasphere.

## Beneficios
- Mejora la comprensión de los datos de negocio para modeladores y consumidores a medida que crece el volumen y la complejidad de los activos
- simplifica la documentación y clasificación de activos del catálogo de SAP Datasphere sin necesidad de conocer estructuras, objetos y semántica de datos SAP complejos
- mejora la experiencia de usuario y acelera la adopción del catálogo
- facilita un uso más efectivo y eficiente de los datos, mejorando la productividad y la toma de decisiones

## Valor de negocio
87% de reducción del tiempo para mantener los metadatos de los activos del catálogo.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Datasphere.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Datasphere para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Mejora la comprensión de los datos de negocio para modeladores y consumidores a medida que crece el volumen y la complejidad de los activos_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Datasphere y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J224 |
| Producto | SAP Datasphere |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/15213c47-7c33-4787-a97b-d28f3a031c5a/

---

## [J225] — Enterprise Search

## En una frase
Búsqueda empresarial asistida por IA para SAP S/4HANA Cloud Public Edition que ayuda a los usuarios a encontrar datos relevantes de objetos de negocio mediante lenguaje natural desde SAP Fiori Launchpad.

## ¿Qué es?
Búsqueda empresarial asistida por IA para SAP S/4HANA Cloud Public Edition que ayuda a los usuarios a encontrar datos relevantes de objetos de negocio mediante lenguaje natural desde SAP Fiori Launchpad. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Facilita encontrar objetos de negocio sin conocer exactamente la aplicación o transacción
- reduce la curva de aprendizaje para nuevos usuarios
- mejora la experiencia de búsqueda para usuarios existentes

## Valor de negocio
Ahorro de tiempo estimado del 50% al buscar objetos de negocio mediante lenguaje natural.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP S/4HANA Cloud Public Edition.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP S/4HANA Cloud Public Edition sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Facilita encontrar objetos de negocio sin conocer exactamente la aplicación o transacción_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J225 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-EIM-ESH |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ce1359ae-1f44-48ce-b9d8-6d2e73b23402/

---

## [J226] — Smart Personalization of My Home

## En una frase
Permite personalizar My Home en SAP S/4HANA Cloud Public Edition agregando insights cards mediante lenguaje natural.

## ¿Qué es?
Permite personalizar My Home en SAP S/4HANA Cloud Public Edition agregando insights cards mediante lenguaje natural. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Permite acceder a datos requeridos de forma más intuitiva sin entrar a aplicaciones específicas
- reduce la curva de aprendizaje de nuevos usuarios
- aumenta la satisfacción de usuarios existentes

## Valor de negocio
50% de ahorro de tiempo al agregar insights cards a My Home mediante lenguaje natural; mayor eficiencia en el acceso a información relevante desde la página inicial.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP S/4HANA Cloud Public Edition.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP S/4HANA Cloud Public Edition sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Permite acceder a datos requeridos de forma más intuitiva sin entrar a aplicaciones específicas_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J226 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-UX-MY |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5205d1ac-b2a1-413b-8d5c-a01e22311cad/

---

## [J227] — Error Explanation

## En una frase
Genera descripciones y recomendaciones de resolución en lenguaje natural para errores en SAP S/4HANA Cloud Public Edition, ayudando a usuarios de distintos niveles de experiencia a entender el problema y continuar con el proceso.

## ¿Qué es?
Genera descripciones y recomendaciones de resolución en lenguaje natural para errores en SAP S/4HANA Cloud Public Edition, ayudando a usuarios de distintos niveles de experiencia a entender el problema y continuar con el proceso. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce tiempos de inactividad por errores de captura
- disminuye el tiempo de entrenamiento gracias a explicaciones fáciles de entender
- mejora la calidad de datos mediante orientación descriptiva e instructiva

## Valor de negocio
No disponible en la página consultada.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce tiempos de inactividad por errores de captura_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J227 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BC-SRV-APS-AI-UIS |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a6e21835-397b-402d-be1a-e92846dcc47d/

---

## [J240] — In-house Service Initiation

## En una frase
Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos.

## ¿Qué es?
Capacidad de SAP S/4HANA Cloud Private Edition para iniciar servicios internos a partir de documentos. El personal de reparación puede escanear o fotografiar documentos entrantes, como órdenes de compra; el sistema extrae datos relevantes y genera objetos de reparación asociados al servicio interno. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Automatización de extracción de datos desde formularios
- creación más rápida de repair objects
- reducción de errores humanos
- mejora de eficiencia de proceso
- identificación automática de equipos existentes

## Valor de negocio
SAP indica aumento de 70% en productividad del trabajador de servicio al preparar órdenes de servicio. El valor está en reducir digitación manual, evitar pérdida de datos y acelerar el procesamiento de reparaciones.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Private Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Private Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Automatización de extracción de datos desde formularios_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J240 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CRM-S4-IHR |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Supply Chain Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/df0164e9-75f2-4547-80d3-586619709246/

---

## [J241] — Maintenance Order Recommendation

## En una frase
Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento.

## ¿Qué es?
Recomienda órdenes de mantenimiento que resolvieron incidentes similares a partir del historial de mantenimiento. El planificador revisa las recomendaciones y selecciona una orden como referencia para crear una nueva orden de mantenimiento. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Reduce el esfuerzo manual de creación de órdenes
- apoya decisiones con recomendaciones basadas en casos históricos
- ayuda a minimizar tiempos de inactividad y a mejorar la resolución inicial de incidentes

## Valor de negocio
40% de aumento en productividad del planificador de mantenimiento; 1% de reducción del downtime no planificado; 5% de aumento en la tasa de resolución en el primer intento de técnicos de mantenimiento.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce el esfuerzo manual de creación de órdenes_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J241 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | PM-WOC-MO |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Supply Chain Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d2a47a4f-3ea2-4f5b-9bdf-43fc2a3d95f2/

---

## [J243] — API traffic prediction

## En una frase
Funcionalidad de SAP Integration Suite que identifica tendencias en llamadas API y predice volúmenes futuros de tráfico para apoyar decisiones sobre capacidad, carga y estrategia API.

## ¿Qué es?
Funcionalidad de SAP Integration Suite que identifica tendencias en llamadas API y predice volúmenes futuros de tráfico para apoyar decisiones sobre capacidad, carga y estrategia API. Es una capacidad de IA **Base** de SAP Integration Suite.

## Beneficios
- Dashboard para optimizar tráfico API
- selección configurable de proxies API
- configuración de duración de predicción y frecuencia según preferencias

## Valor de negocio
Mejora la planificación de recursos, la gestión de carga del sistema y la toma de decisiones sobre estrategia API. No se encontró un KPI cuantitativo específico en la página consultada.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Integration Suite.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Integration Suite sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Dashboard para optimizar tráfico API_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Integration Suite y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Integration Suite** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J243 |
| Producto | SAP Integration Suite |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | OPU-API-OD-AN |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f74d29df-40d1-498f-905d-90b7af685799/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f74d29df-40d1-498f-905d-90b7af685799/

---

## [J247] — Journal Upload

## En una frase
Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition.

## ¿Qué es?
Acelera las entradas manuales de cierre de período en SAP S/4HANA Cloud Private Edition. Mediante una app SAP Fiori con capacidades de IA generativa, permite crear casos de carga, asociar una guía o política de contabilización en lenguaje natural, generar propuestas, validarlas y publicar asientos. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Automatiza la generación de asientos de cierre alineados con políticas internas
- reduce el esfuerzo de preparar archivos de carga
- mejora la calidad mediante generación y validación asistida
- mantiene trazabilidad para control y auditoría

## Valor de negocio
70% de reducción del esfuerzo para preparar journals manuales al cierre de período; 50% de reducción del esfuerzo para cargar y validar journals manuales al cierre.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Private Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Private Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Automatiza la generación de asientos de cierre alineados con políticas internas_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J247 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-GL-AI-IJU |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/be5c57fd-4b09-436f-8a63-16362fce5547/

---

## [J25] — Natural Language Query

## En una frase
Natural Language Query es una función de IA generativa de SAP Analytics Cloud diseñada para democratizar la analítica, permitiendo solicitar datos mediante lenguaje natural.

## ¿Qué es?
Natural Language Query es una función de IA generativa de SAP Analytics Cloud diseñada para democratizar la analítica, permitiendo solicitar datos mediante lenguaje natural. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Permite obtener respuestas sin saber dónde reside el dato
- reduce dependencia de consultas técnicas
- facilita el acceso rápido a insights para usuarios de negocio

## Valor de negocio
80% de reducción del tiempo para acceder a información relevante.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Analytics Cloud.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Analytics Cloud sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Permite obtener respuestas sin saber dónde reside el dato_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J25 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-ASK |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6a655660-1f00-4b22-a6e4-b79167b527ec/

---

## [J275] — AI-Assisted Commenting

## En una frase
Permite resumir comentarios existentes y reformular nuevos comentarios durante la autoría.

## ¿Qué es?
Permite resumir comentarios existentes y reformular nuevos comentarios durante la autoría. Los analistas de negocio pueden resumir comentarios por celda, agregarlos a lo largo de una jerarquía y recibir traducciones según la preferencia de idioma del usuario. Es una capacidad de IA **Premium** de SAP Analytics Cloud.

## Beneficios
- Mejora el consumo de comentarios para apoyar la toma de decisiones
- reduce actividades manuales poco prácticas para usuarios de negocio
- ayuda a resumir, agregar, traducir y reformular comentarios

## Valor de negocio
SAP indica una reducción del 80% en el tiempo para reformular comentarios, del 80% para agregar y traducir comentarios descendientes, y del 80% para resumir y traducir comentarios por celda o hilo.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Mejora el consumo de comentarios para apoyar la toma de decisiones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J275 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-CMT |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3a0d3a44-e0c6-42e9-b489-cbbd0c1d1030/

---

## [J281] — Easy Fill

## En una frase
Permite a los usuarios de SAP S/4HANA Cloud Public Edition poblar los campos de un objeto de negocio mediante entrada en lenguaje natural, agilizando la captura de datos y mejorando su exactitud, al permitir introducir actualizaciones en un formato relevante para el proceso de negocio y asegurando que los campos requeridos se completen.

## ¿Qué es?
Permite a los usuarios de SAP S/4HANA Cloud Public Edition poblar los campos de un objeto de negocio mediante entrada en lenguaje natural, agilizando la captura de datos y mejorando su exactitud, al permitir introducir actualizaciones en un formato relevante para el proceso de negocio y asegurando que los campos requeridos se completen. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Mayor exactitud de datos al consolidar las entradas del usuario en un único campo unificado
- menor complejidad del proceso de negocio y menor tiempo de formación

## Valor de negocio
83% de reducción del tiempo de captura de entradas en la aplicación.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Mayor exactitud de datos al consolidar las entradas del usuario en un único campo unificado_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J281 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BC-SRV-APS-AI-UIS |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/b054b110-d555-49ef-b233-e16be1a13eed/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b054b110-d555-49ef-b233-e16be1a13eed/

---

## [J284] — Joule with SAP LeanIX

## En una frase
Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto.

## ¿Qué es?
Permite buscar diagramas, reportes, inventario de fact sheets y respuestas sobre SAP LeanIX usando consultas en lenguaje natural; Joule responde con base en la información disponible del producto. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Búsqueda más sencilla de documentación y activos de arquitectura
- acceso más rápido a reportes y fact sheets
- reducción del esfuerzo para encontrar información relevante

## Valor de negocio
50% menos esfuerzo para buscar documentación e información relevante, según la métrica mostrada en la página de detalle.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP LeanIX solutions.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP LeanIX solutions sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Búsqueda más sencilla de documentación y activos de arquitectura_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J284 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Early Adopter Care (EAC) |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Early Adopter Care (EAC). Pricing is not available at this time. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/afef2f21-b812-4548-ab8a-cec5f8fedb10/

---

## [J288] — Explanation of Fixed Asset Key Figures

## En una frase
Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones en lenguaje natural de cálculos complejos.

## ¿Qué es?
Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones en lenguaje natural de cálculos complejos. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Acelera la respuesta a preguntas sobre key figures
- mejora la comprensión de valores de activos
- apoya decisiones de valoración y planificación financiera

## Valor de negocio
Reducción estimada de hasta 75% en el esfuerzo para analizar valores de activos y responder preguntas de usuarios.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera la respuesta a preguntas sobre key figures_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J288 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-AA-AA-B-2L |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8658cb4d-fc45-4db1-b5e3-68a63a255955/

---

## [J28] — Goods Receipt Processing

## En una frase
Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA.

## ¿Qué es?
Capacidad para revisar automáticamente documentos de entrega y notas de entrega/shipping documents con IA. Permite extraer información relevante de documentos de flete en papel, publicarla en el sistema y detectar anomalías que pueden retrasar la validación de freight orders. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Automatiza procesamiento de goods receipts
- reduce errores de digitación
- procesa múltiples layouts de documentos sin entrenamiento
- acelera tiempos de procesamiento
- ayuda a detectar anomalías en documentos de entrega

## Valor de negocio
El valor está en reducir trabajo manual y errores durante la recepción de mercancía, acelerar validaciones y mejorar eficiencia operacional en transporte/logística.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Private Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Private Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Automatiza procesamiento de goods receipts_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J28 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | BC-SRV-BUM |
| Industrias aplicables | Consumer Products |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8d54e237-4ae9-427d-859a-c3e1cd694127/

---

## [J291] — Joule with SAP Business Accelerator Hub

## En una frase
Ayuda a los usuarios a encontrar el contenido adecuado mediante búsqueda conversacional basada en contexto.

## ¿Qué es?
Ayuda a los usuarios a encontrar el contenido adecuado mediante búsqueda conversacional basada en contexto. El descubrimiento con Joule guía la búsqueda de distintos artefactos y su acceso según el contexto específico, acelerando el descubrimiento. Es una capacidad de IA **Base** de SAP Business Accelerator Hub.

## Beneficios
- Mejor descubrimiento de contenido
- menor time-to-productivity
- experiencia de usuario atractiva

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Business Accelerator Hub.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Business Accelerator Hub sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Mejor descubrimiento de contenido_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Business Accelerator Hub y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Business Accelerator Hub** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J291 |
| Producto | SAP Business Accelerator Hub |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | LOD-CHB-CNT |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5b1c80e7-ae6a-45eb-89cf-cf7114bb00d4/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b1c80e7-ae6a-45eb-89cf-cf7114bb00d4/

---

## [J294] — Joule with SAP Datasphere

## En una frase
Con Joule embebido en SAP Datasphere, los usuarios pueden realizar tareas informativas, navegacionales y transaccionales de forma fluida, incluyendo consultas sobre uso del producto y tareas comunes de administración.

## ¿Qué es?
Con Joule embebido en SAP Datasphere, los usuarios pueden realizar tareas informativas, navegacionales y transaccionales de forma fluida, incluyendo consultas sobre uso del producto y tareas comunes de administración. Es una capacidad de IA **Base** de SAP Datasphere.

## Beneficios
- Ayuda contextual dentro de SAP Datasphere
- acceso natural a información y acciones
- apoyo en tareas como espacios, usuarios, roles y navegación a aplicaciones de gestión relevantes

## Valor de negocio
No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se orienta a productividad de usuarios y administradores en SAP Datasphere.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Datasphere.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Datasphere sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Ayuda contextual dentro de SAP Datasphere_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Datasphere y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Datasphere** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J294 |
| Producto | SAP Datasphere |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Early Adopter Care (EAC) |
| Support Component | CA-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Early Adopter Care (EAC). Pricing is not available at this time. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/a2bc2dd0-4f0b-4d82-9f94-c3baaac6c83b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a2bc2dd0-4f0b-4d82-9f94-c3baaac6c83b/

---

## [J298] — Creation of Fixed Asset Master Data

## En una frase
La solución agiliza la creación de datos maestros de activos fijos a través de una interfaz conversacional (Joule).

## ¿Qué es?
La solución agiliza la creación de datos maestros de activos fijos a través de una interfaz conversacional (Joule). Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Facilita la creación de datos maestros de activos fijos con una interfaz conversacional
- mejora la productividad general acelerando el onboarding de nuevos activos
- mejora la precisión y la gobernanza de los datos maestros de activos fijos

## Valor de negocio
Hasta 75% de reducción del tiempo para crear datos maestros de activos fijos.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Facilita la creación de datos maestros de activos fijos con una interfaz conversacional_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J298 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | FI-FIO-AA-MD-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/095edf47-cb36-48d8-bd8f-9a4bc9517991/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/095edf47-cb36-48d8-bd8f-9a4bc9517991/

---

## [J305] — Electronic Document Error Handling

## En una frase
Ofrece explicaciones fáciles de entender para errores de documentos electrónicos con Joule en SAP Document and Reporting Compliance.

## ¿Qué es?
Ofrece explicaciones fáciles de entender para errores de documentos electrónicos con Joule en SAP Document and Reporting Compliance. Es una capacidad de IA **Base** de SAP Document and Reporting Compliance.

## Beneficios
- Entrega explicaciones conversacionales de errores complejos, ayuda a descubrir la causa raíz más rápido y mejora la eficiencia en la resolución

## Valor de negocio
80% de reducción del tiempo dedicado a entender los detalles del error e identificar la causa raíz.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Document and Reporting Compliance.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Document and Reporting Compliance sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Entrega explicaciones conversacionales de errores complejos_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Document and Reporting Compliance y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Document and Reporting Compliance** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J305 |
| Producto | SAP Document and Reporting Compliance |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-GTF-CSC-EDO-DCC |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/1a1b66db-191d-41e6-b01d-d69b4d645850/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1a1b66db-191d-41e6-b01d-d69b4d645850/

---

## [J308] — Agent Builder

## En una frase
Permite construir agentes de Joule para automatizar procesos de negocio complejos.

## ¿Qué es?
Permite construir agentes de Joule para automatizar procesos de negocio complejos. Los agentes pueden ejecutar flujos adaptativos, razonar, planificar, coordinar procesos de varios pasos, invocar APIs, interactuar con documentos y colaborar con usuarios u otros agentes en sistemas SAP y no SAP. Es una capacidad de IA **Base** de Joule Studio.

## Beneficios
- Desarrollo confiable de agentes al fundamentarlos con datos y procesos de negocio
- integración con aplicaciones SAP, aplicaciones de terceros y otros agentes
- gestión centralizada de skills y agentes con visibilidad de ejecución y controles de privacidad de datos

## Valor de negocio
Aporta eficiencia en escenarios que requieren toma de decisiones experta, manejo de excepciones y orquestación entre sistemas, especialmente donde la automatización determinística no es suficiente.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule Studio sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Desarrollo confiable de agentes al fundamentarlos con datos y procesos de negocio_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule Studio y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule Studio** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J308 |
| Producto | Joule Studio |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD-JLE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c95490eb-95c3-4b0a-b9ea-08144355d482/

---

## [J313] — Expiring Price Handling

## En una frase
Permite a los especialistas de precios **detectar y actualizar precios, descuentos y recargos próximos a vencer** conversando en lenguaje natural con **Joule**, dentro de SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Es una capacidad de **Joule con SAP S/4HANA Cloud Public Edition** orientada a la gestión de precios. El especialista puede preguntarle a Joule si existen precios, descuentos o recargos que estén por expirar en un horizonte determinado (días, meses, años) y, en la misma conversación, **crear nuevos elementos de precio** definiendo el nuevo período de validez y el importe. Todo el flujo ocurre de forma conversacional, sin navegar manualmente por las transacciones de pricing.

## Beneficios
- Evita correcciones de precios costosas en tiempo, al detectar precios, descuentos o recargos por vencer **antes** de que dejen de ser válidos.
- Permite a los especialistas de precios **crear nuevos elementos de precio en segundos** usando lenguaje natural.

## Valor de negocio
- **95% de reducción del esfuerzo** para detectar y actualizar precios por vencer (cifra publicada por SAP).

## ¿Cómo funciona?
1. **Consulta en lenguaje natural:** el especialista pregunta a Joule, p. ej. *"¿Qué descuentos vencen el próximo mes?"*.
2. **Detección asistida por IA:** Joule interpreta la intención y consulta el sistema de pricing de S/4HANA para devolver los elementos (precios/descuentos/recargos) próximos a expirar.
3. **Acción conversacional:** en el mismo diálogo, el usuario decide crear nuevos elementos de precio, fijando el **período de validez** y el **importe** nuevos.
4. **Registro en el sistema:** Joule ejecuta la creación contra S/4HANA, evitando navegar manualmente por las apps de condiciones de precio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Cierre de trimestre en una empresa de manufactura; el equipo comercial teme que varios descuentos por volumen caduquen sin renovarse. **Cómo ayuda la feature:** el especialista pide a Joule "muéstrame los descuentos que vencen este mes" y, sobre la lista devuelta, extiende la validez y ajusta importes en minutos, sin abrir transacción por transacción.
2. **Escenario:** Lanzamiento de una campaña promocional con recargos temporales que deben terminar en una fecha exacta. **Cómo ayuda la feature:** el usuario verifica con Joule qué recargos están por expirar y crea los nuevos con el período y monto correctos directamente desde la conversación.

## ¿Cuándo usarla?
- Cuando hay **gestión recurrente de condiciones de precio** (precios, descuentos, recargos) con vigencias que deben mantenerse al día.
- Requiere **Joule con SAP S/4HANA Cloud Public Edition** activo (es un "Required Asset" de esta oferta).
- No sustituye una estrategia de pricing: es un acelerador operativo para detectar vencimientos y crear/renovar elementos de precio puntuales.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J313 |
| Producto | SAP S/4HANA Cloud Public Edition (con Joule) |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | Incluida con **Joule Base** sin costo adicional; requiere suscripción a Joule Base o AI Units |
| Required Asset | Joule con SAP S/4HANA Cloud Public Edition |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/577815a8-947e-4a06-a961-1307ddc49242/

---

## [J326] — Meeting Location Planner Agent

## En una frase
Ayuda a empleados a organizar reuniones offsite sugiriendo ubicaciones que minimizan tiempos de viaje, proponiendo hoteles y mostrando una vista general de costos para planificar dentro del presupuesto.

## ¿Qué es?
Ayuda a empleados a organizar reuniones offsite sugiriendo ubicaciones que minimizan tiempos de viaje, proponiendo hoteles y mostrando una vista general de costos para planificar dentro del presupuesto. Es una capacidad de IA **Base** de el producto SAP.

## Beneficios
- Reduce la comparación manual de ubicaciones, rutas, hoteles y costos
- facilita decisiones de sede más rápidas
- apoya la planificación de offsites con una visión de viaje y presupuesto en un solo flujo

## Valor de negocio
No se identificó una métrica cuantitativa completa en el contenido accesible de la página de detalle; el valor descrito se concentra en reducir tiempo de planificación y mejorar el control presupuestal de offsites.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de el producto SAP.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en el producto SAP sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce la comparación manual de ubicaciones_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de el producto SAP y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **el producto SAP** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J326 |
| Producto | el producto SAP |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Early Adopter Care (EAC) |
| Support Component | Queue - TRV - Core Travel |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI solution is available only with the purchase of the relevant Concur subscription and is not available via AI Units. For more information, please contact your Concur Account Executive or Account Manager. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/65b25edc-21cc-4b54-8f3c-eb4524ab3117/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/65b25edc-21cc-4b54-8f3c-eb4524ab3117/

---

## [J327] — Expense Report Validation Agent

## En una frase
Agente para ayudar a viajeros de negocio a completar y enviar reportes de gastos, simplificando el proceso de entendimiento y preparación de la información requerida.

## ¿Qué es?
Agente para ayudar a viajeros de negocio a completar y enviar reportes de gastos, simplificando el proceso de entendimiento y preparación de la información requerida. Es una capacidad de IA **Base** de el producto SAP.

## Beneficios
- Simplifica la preparación y envío de reportes de gastos
- mejora la satisfacción del empleado
- reduce el tiempo dedicado a tareas administrativas

## Valor de negocio
Reducción estimada del 30% en el tiempo dedicado a preparar y enviar reportes de gastos.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de el producto SAP.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en el producto SAP con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Simplifica la preparación y envío de reportes de gastos_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de el producto SAP y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **el producto SAP** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J327 |
| Producto | el producto SAP |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Early Adopter Care (EAC) |
| Support Component | Concur - Spend - Joule |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI solution is available only with the purchase of the relevant Concur subscription and is not available via AI Units. For more information, please contact your Concur Account Executive or Account Manager. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ba618aac-87c8-485d-8d3c-3338f6a8658a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ba618aac-87c8-485d-8d3c-3338f6a8658a/

---

## [J329] — Semantic Generation

## En una frase
Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas.

## ¿Qué es?
Ayuda a analistas de datos a generar semántica de negocio para fuentes no SAP, evitando reconstruir manualmente definiciones semánticas. El onboarding semántico toma tablas, contenido y semántica asociada como monedas, unidades, medidas, hechos, dimensiones y asociaciones. Es una capacidad de IA **Premium** de SAP Datasphere.

## Beneficios
- Reduce el tiempo de creación de semántica para entidades no SAP
- disminuye costos asociados a modelado semántico
- mejora el valor semántico de los datos y simplifica el trabajo de modelado

## Valor de negocio
Menor esfuerzo para crear modelos semánticos en SAP Datasphere, mayor velocidad para preparar datos no SAP para consumo analítico y mejor reutilización de información enriquecida semánticamente.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Datasphere.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Datasphere para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce el tiempo de creación de semántica para entidades no SAP_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Datasphere y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J329 |
| Producto | SAP Datasphere |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | DS-MD |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d22ae902-3e3d-4c78-9f8e-a656ecd2686d/

---

## [J331] — Role-based Process Overview

## En una frase
“My Process Overview” ofrece a los usuarios una vista personalizada de procesos, contenido y herramientas relevantes para su rol, eliminando la búsqueda manual.

## ¿Qué es?
“My Process Overview” ofrece a los usuarios una vista personalizada de procesos, contenido y herramientas relevantes para su rol, eliminando la búsqueda manual. Ayuda a usuarios sin experiencia profunda en procesos a construir conocimiento y entender sus responsabilidades; ideal para onboarding. Un asistente de configuración con IA adapta las recomendaciones según los detalles del puesto. Es una capacidad de IA **Base** de SAP Signavio Process Collaboration Hub.

## Beneficios
- Permite ver contenido adaptado a su rol sin buscar ni filtrar manualmente
- reduce la carga administrativa con menos configuración manual de vistas y rutas de acceso por rol

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP Signavio Process Collaboration Hub.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP Signavio Process Collaboration Hub con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Permite ver contenido adaptado a su rol sin buscar ni filtrar manualmente_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Collaboration Hub y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Collaboration Hub** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J331 |
| Producto | SAP Signavio Process Collaboration Hub |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e4b92ea3-f81d-4f95-9afd-368b563700ad/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e4b92ea3-f81d-4f95-9afd-368b563700ad/

---

## [J336] — Error Resolution for Cost Accounting

## En una frase
Ayuda a los contadores de costos a identificar y resolver errores relacionados con contabilidad de costos, ofreciendo orientación asistida para atender incidencias del proceso.

## ¿Qué es?
Ayuda a los contadores de costos a identificar y resolver errores relacionados con contabilidad de costos, ofreciendo orientación asistida para atender incidencias del proceso. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el esfuerzo manual de análisis
- facilita la resolución de errores operativos
- apoya la continuidad de procesos financieros

## Valor de negocio
No disponible en la página consultada.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el esfuerzo manual de análisis_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J336 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CO-PC-OBJ-ORD-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/56d1e4d0-5c07-4aa8-b226-64c8dd99750d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/56d1e4d0-5c07-4aa8-b226-64c8dd99750d/

---

## [J342] — Embedded Edition (SAP Document AI)

## En una frase
**Automatiza el procesamiento de documentos de extremo a extremo** —extracción de información, ejecución de workflows e integración de canales— y conecta el flujo documental directamente con sistemas SAP como SAP S/4HANA.

## ¿Qué es?
Es la capacidad **Premium** "embedded edition" de **SAP Document AI**. Optimiza y automatiza las tareas relacionadas con documentos dentro de los procesos empresariales: una sola petición habilita el **procesamiento inteligente** de una página de documento, como la **extracción de información según un esquema predefinido**. Además, facilita **ejecuciones por canal**: leer desde fuentes como buzones de correo y procesar automáticamente los documentos entrantes en el sistema destino (p. ej. SAP S/4HANA).

## Beneficios
- Acelera el manejo de documentos, mejora la **exactitud de los datos** y conecta de forma fluida los flujos documentales con procesos de negocio más amplios.
- Aumenta la productividad asegurando **integración escalable** con diversos canales de comunicación y workflows automatizados dentro de los entornos SAP existentes.

## Valor de negocio
- **70% de reducción** del tiempo para procesar documentos.
- **83% de reducción** del tiempo para mantener plantillas de documentos.
- **40% de reducción** de la pérdida de valor por demoras en el procesamiento manual de documentos.

## ¿Cómo funciona?
1. **Ingesta por canal:** la solución lee documentos desde la fuente (p. ej. una bandeja de correo) o recibe una página a procesar.
2. **Extracción inteligente:** con una sola petición, aplica IA para extraer la información de la página según un **esquema predefinido**.
3. **Ejecución y entrega:** procesa automáticamente el documento y lo integra en el sistema destino (p. ej. SAP S/4HANA), encadenando el resultado con el workflow de negocio correspondiente.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Cuentas por pagar recibe cientos de facturas de proveedor por correo cada día. **Cómo ayuda la feature:** lee el buzón, extrae los campos clave de cada factura según el esquema y los inyecta en SAP S/4HANA para su contabilización, reduciendo la captura manual.
2. **Escenario:** Una empresa debe procesar formularios estandarizados (p. ej. certificados o formularios oficiales) a gran volumen. **Cómo ayuda la feature:** automatiza la extracción estructurada y el enrutamiento al proceso destino, con menos mantenimiento de plantillas.

## ¿Cuándo usarla?
- Cuando hay **alto volumen de documentos** que alimentan procesos SAP y la captura/validación manual es un cuello de botella.
- Aporta especialmente cuando se requiere **integración de canales** (correo u otras fuentes) y entrega automatizada al sistema destino.
- Es **Premium**: su consumo se factura por **AI Units** con tarifa escalonada por volumen (ver pricing).

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J342 |
| Producto | SAP Document AI |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-ML-BDP |
| Industrias aplicables | Cross-Industry |
| Pricing | Por **AI Units** (Requests), tarifa escalonada: hasta 50.000 → 0,1 AI Units/req; hasta 100.000 → 0,0786; hasta 300.000 → 0,0614; hasta 500.000 → 0,0443; desde 500.000 → 0,0364 (≈ EUR 7 por AI Unit) |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9000cc5-4a1a-4c59-9dcd-a343c167d75d/

---

## [J344] — Permit Management

## En una frase
Extrae y configura automáticamente permisos de EHS (medio ambiente, salud y seguridad) a partir de documentos PDF que pueden tener desde pocas hasta cientos de páginas.

## ¿Qué es?
Extrae y configura automáticamente permisos de EHS (medio ambiente, salud y seguridad) a partir de documentos PDF que pueden tener desde pocas hasta cientos de páginas. No solo escanea y configura los datos de cabecera del permiso, sino que identifica todos los requisitos y configura las tareas correspondientes (simples, de aviso de mantenimiento, de reporte). El usuario ve en una vista lado a lado las tareas recomendadas mientras revisa las páginas del PDF. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el esfuerzo manual de extracción de datos
- aumenta la eficiencia con tareas propuestas
- ahorra tiempo buscando datos relevantes en el documento
- mejora la auditabilidad
- mejora la usabilidad con vista lado a lado

## Valor de negocio
65% de reducción del costo de gestión de permisos ambientales; 80% de reducción de sanciones y multas de gestión ambiental; 100% de evitación de costo de una solución de OCR.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el esfuerzo manual de extracción de datos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J344 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Industrias aplicables | Show More |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/89944fea-d96d-453c-9684-fe2b2c9cbb51/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/89944fea-d96d-453c-9684-fe2b2c9cbb51/

---

## [J345] — Compliance Information Processing

## En una frase
Permite a los especialistas de datos maestros procesar automáticamente la información de cumplimiento (compliance) de proveedores —regulaciones, estado y datos de proveedores upstream— y mapearla a los requisitos de compliance en SAP S/4HANA Cloud Public Edition para product compliance, mejorando la eficiencia y precisión del análisis y reduciendo errores que afectan la seguridad y el cumplimiento.

## ¿Qué es?
Permite a los especialistas de datos maestros procesar automáticamente la información de cumplimiento (compliance) de proveedores —regulaciones, estado y datos de proveedores upstream— y mapearla a los requisitos de compliance en SAP S/4HANA Cloud Public Edition para product compliance, mejorando la eficiencia y precisión del análisis y reduciendo errores que afectan la seguridad y el cumplimiento. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Automatiza el procesamiento y análisis de las divulgaciones de compliance en el sistema y su mapeo a los requisitos de cumplimiento
- mejora la precisión para minimizar errores que pueden derivar en multas y sanciones

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Automatiza el procesamiento y análisis de las divulgaciones de compliance en el sistema y su mapeo a los requisitos de cumplimiento_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J345 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Industrias aplicables | Show More |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/57f00cc9-d292-4fd6-baec-cb4a6336c70c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/57f00cc9-d292-4fd6-baec-cb4a6336c70c/

---

## [J346] — Note Corrections for Project Billing

## En una frase
La función Smart Notes en Manage Project Billing propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura.

## ¿Qué es?
La función Smart Notes en Manage Project Billing propone notas gramaticalmente corregidas para ítems de Time & Expenses con notas, para que el especialista de facturación revise y decida los cambios antes de la salida de factura. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce correcciones manuales
- mejora la precisión de la factura
- acelera la generación de facturas
- puede favorecer el cobro al disminuir errores en notas incluidas en la facturación del proyecto

## Valor de negocio
50% de reducción del tiempo dedicado a correcciones de notas de postings de Time & Expenses.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP S/4HANA Cloud Public Edition.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP S/4HANA Cloud Public Edition que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Reduce correcciones manuales_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J346 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | PPM-SCL-BIL-FIO |
| Industrias aplicables | Professional Services |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cab0dc5c-6c85-4d8e-963a-cad7a64e012a/

---

## [J355] — Posting Issue Handling for Billing Documents

## En una frase
Asiste a billing clerks a recuperar y visualizar documentos de facturación con problemas de contabilización según criterios determinados.

## ¿Qué es?
Asiste a billing clerks a recuperar y visualizar documentos de facturación con problemas de contabilización según criterios determinados. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Soporta la resolución de issues de contabilización, incluyendo errores por período contable no abierto
- ayuda a gestionar documentos válidos para contabilización y modificaciones necesarias de fecha de facturación

## Valor de negocio
65% de reducción en el tiempo para analizar y resolver problemas de contabilización de facturación.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Soporta la resolución de issues de contabilización_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J355 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | SD-BIL-GF |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f558354e-8de3-4b95-ae75-4cc5055cf911/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f558354e-8de3-4b95-ae75-4cc5055cf911/

---

## [J358] — Processing of Incoming Quality Certificates with SAP Document AI

## En una frase
Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Processing of Incoming Quality Certificates with SAP Document AI automatiza el procesamiento de certificados de calidad entrantes mediante extracción de datos y vinculación con objetos relevantes en SAP S/4HANA Cloud Public Edition. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el trabajo manual de técnicos de calidad, acelera la confirmación de certificados y ayuda a evitar que documentos se pierdan u omitan durante el proceso

## Valor de negocio
La página indica reducción del tiempo de procesamiento de certificados de calidad y protección de ingresos al disminuir retrasos de inspección relacionados con procesamiento documental.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el trabajo manual de técnicos de calidad_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J358 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | QM-QC-RE |
| Industrias aplicables | Healthcare |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3fd5ea00-34fa-487e-a76a-be112a71220a/

---

## [J36] — Generation of Full-Stack Applications

## En una frase
SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural.

## ¿Qué es?
SAP Build Code permite generar aplicaciones full-stack a partir de lenguaje natural. Con Joule, la capacidad genera modelos de datos, servicios, datos de ejemplo, anotaciones de UI, lógica de aplicación y pruebas unitarias, dentro de un entorno de desarrollo cloud alineado con SAP Business Application Studio y buenas prácticas de SAP BTP. Es una capacidad de IA **Base** de SAP Build Code.

## Beneficios
- Generación de aplicaciones desde prompts
- creación automática de modelos, servicios, datos de ejemplo y anotaciones de UI
- generación de pruebas unitarias
- entorno de desarrollo asistido por IA
- desarrollo más eficiente y con menor necesidad de codificación manual

## Valor de negocio
SAP indica una reducción de 30% en costos de desarrollo de aplicaciones. El valor de negocio está en acelerar el ciclo de desarrollo, reducir esfuerzo manual y mejorar la productividad de equipos técnicos que crean extensiones y aplicaciones sobre SAP Build Code.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Build Code.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Build Code sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Generación de aplicaciones desde prompts_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Code y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Code** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J36 |
| Producto | SAP Build Code |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-BLD |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/98319fdc-fd0d-4887-bba2-a3d6a15f31ed/

---

## [J375] — Payment Exception Analysis

## En una frase
Proporciona a los contables de cuentas por pagar (AP) análisis asistido por IA de las excepciones de la propuesta de pago, con registros de log detallados y resoluciones sugeridas, ayudando a agilizar y acelerar el manejo de excepciones.

## ¿Qué es?
Proporciona a los contables de cuentas por pagar (AP) análisis asistido por IA de las excepciones de la propuesta de pago, con registros de log detallados y resoluciones sugeridas, ayudando a agilizar y acelerar el manejo de excepciones. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Aumenta la tasa media de pagos puntuales
- mejora la identificación de la causa raíz de la excepción buscando partidas abiertas en el log y analizando el contexto de logs adicionales
- aumenta la transparencia con un historial de cambios en las propuestas de pago para usuarios y auditores

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP S/4HANA Cloud Public Edition.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP S/4HANA Cloud Public Edition que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Aumenta la tasa media de pagos puntuales_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J375 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FI-FIO-AP-PAY-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/016c719c-5363-47ff-945f-cdddd5241871/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/016c719c-5363-47ff-945f-cdddd5241871/

---

## [J383] — Production Planning and Operations Agent

## En una frase
Acelera el order-to-delivery ahorrando a los planificadores el tiempo de liberación de órdenes.

## ¿Qué es?
Acelera el order-to-delivery ahorrando a los planificadores el tiempo de liberación de órdenes. Automatiza las verificaciones previas para liberar órdenes de producción —disponibilidad de material, capacidad y programación—, marca faltantes de material y sugiere soluciones (componentes alternativos, ajustes de programación). Cuando se cumplen todos los criterios, el planificador aprueba y el agente completa la liberación de la orden. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition‚ Joule.

## Beneficios
- Reduce el trabajo manual con validación automática de disponibilidad de material, capacidad y programación
- mantiene la producción en marcha con soluciones recomendadas ante conflictos de material y programación
- aumenta el throughput reduciendo demoras de procesamiento de órdenes

## Valor de negocio
50% de mayor productividad del supervisor de producción al buscar información de liberación de órdenes; 2% de menores pérdidas por downtime de producción.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el trabajo manual con validación automática de disponibilidad de material_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J383 |
| Producto | SAP S/4HANA Cloud Public Edition‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | PP-FIO-SFC-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/2bac78a3-811f-456f-b950-a4fb3e7d2ac5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2bac78a3-811f-456f-b950-a4fb3e7d2ac5/

---

## [J404] — Sales Order Creation from Unstructured Data

## En una frase
La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes.

## ¿Qué es?
La función permite a representantes de ventas crear pedidos de venta desde documentos no estructurados, como archivos PDF o imágenes. Después de cargar el archivo, la información se procesa automáticamente para generar una solicitud de pedido de venta que luego puede convertirse en pedido. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce la captura manual de datos, disminuye errores al procesar órdenes de compra y acelera la conversión de solicitudes de cliente en documentos comerciales dentro de SAP S/4HANA Cloud Public Edition

## Valor de negocio
La página indica una reducción del 33% en el esfuerzo manual para crear pedidos de venta.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce la captura manual de datos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J404 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | SD-SLS-IMP-DOX-2CL |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ffd1d0b2-76fc-4e1f-b1fd-523ec82bae54/

---

## [J415] — Sourcing Agent

## En una frase
Run smarter sourcing events faster and with less effort.

## ¿Qué es?
Run smarter sourcing events faster and with less effort. Es una capacidad de IA **Base** de SAP Ariba Sourcing‚ Joule.

## Beneficios
- No disponible en la página Detail Page

## Valor de negocio
No disponible en la página Detail Page.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Ariba Sourcing‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _No disponible en la página Detail Page_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Ariba Sourcing‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Ariba Sourcing‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J415 |
| Producto | SAP Ariba Sourcing‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/944d71fe-90ad-4ef9-894c-878a4a326893/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/944d71fe-90ad-4ef9-894c-878a4a326893/

---

## [J424] — Maintenance Event Planning Agent

## En una frase
Ayuda a los planificadores de mantenimiento a gestionar y priorizar una lista creciente de tareas asegurando la fiabilidad del equipo y minimizando el downtime.

## ¿Qué es?
Ayuda a los planificadores de mantenimiento a gestionar y priorizar una lista creciente de tareas asegurando la fiabilidad del equipo y minimizando el downtime. En colaboración con el planificador, el agente analiza continuamente datos en tiempo real y sugiere ajustes al programa de mantenimiento, repriorizando tareas y mejorando la salud de los activos. Es una capacidad de IA **Base** de Joule‚ SAP S/4HANA Cloud Private Edition.

## Beneficios
- Genera backlogs de eventos de mantenimiento de forma más rápida y eficiente
- agiliza los backlogs reduciendo el downtime al permitir identificar y atender incidencias de mantenimiento rápidamente

## Valor de negocio
40% de aumento de la productividad del planificador de mantenimiento; 1% de reducción del downtime no planificado.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule‚ SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Genera backlogs de eventos de mantenimiento de forma más rápida y eficiente_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule‚ SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule‚ SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J424 |
| Producto | Joule‚ SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-FLP-EXT-PCE-JOU |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8b3daa3f-7a07-4a62-8d23-20e13d00aea4/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8b3daa3f-7a07-4a62-8d23-20e13d00aea4/

---

## [J425] — Cash Positioning Agent

## En una frase
Ayuda a los gestores de tesorería a ahorrar tiempo y aumentar el rendimiento de intereses mediante un agente que automatiza conciliaciones y propone optimizaciones de caja.

## ¿Qué es?
Ayuda a los gestores de tesorería a ahorrar tiempo y aumentar el rendimiento de intereses mediante un agente que automatiza conciliaciones y propone optimizaciones de caja. Procesa con exactitud los extractos bancarios, agrega saldos iniciales y considera los flujos de caja esperados; propone transferencias para optimizar la caja operativa identificando déficits y superávits, que el gestor revisa y aprueba. Es una capacidad de IA **Base** de Joule‚ SAP S/4HANA Cloud Private Edition.

## Beneficios
- Asegura exactitud al procesar y conciliar extractos y saldos bancarios diarios
- optimiza el flujo de caja con identificación automática de déficits y superávits
- mejora el rendimiento de intereses con recomendaciones de transferencia accionables

## Valor de negocio
70% de reducción del esfuerzo de gestión de caja.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule‚ SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Asegura exactitud al procesar y conciliar extractos y saldos bancarios diarios_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule‚ SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule‚ SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J425 |
| Producto | Joule‚ SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FIN-FSCM-CLM |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/61f9300e-11e0-4ca2-acee-ace35c44fae0/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/61f9300e-11e0-4ca2-acee-ace35c44fae0/

---

## [J43] — Sales Order Automatic Completion

## En una frase
Mediante datos históricos y machine learning, la función recomienda valores para completar campos vacíos en órdenes de venta incompletas.

## ¿Qué es?
Mediante datos históricos y machine learning, la función recomienda valores para completar campos vacíos en órdenes de venta incompletas. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Aumenta la productividad comercial, ofrece flexibilidad para continuar tareas aunque la solicitud esté incompleta y reduce costos de gestión de datos y operación

## Valor de negocio
La página indica una reducción del 25% en esfuerzo manual para completar órdenes de venta, ayudando a acelerar el ciclo comercial y reducir errores.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP S/4HANA Cloud Public Edition.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP S/4HANA Cloud Public Edition que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Aumenta la productividad comercial_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J43 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | SD-SLS-SO |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/39a49e49-3ab6-46f5-889d-2035d9378cab/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/39a49e49-3ab6-46f5-889d-2035d9378cab/

---

## [J45] — Inventory Prompts

## En una frase
Inventory Prompts combina la información del inventario SAP LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial.

## ¿Qué es?
Inventory Prompts combina la información del inventario SAP LeanIX con IA generativa para hacer más accesible y accionable la información de arquitectura empresarial. Provee una interfaz de lenguaje natural para consultar datos y obtener insights usando preguntas cotidianas. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Consultas en lenguaje natural sobre el repositorio de arquitectura
- uso de prompts predefinidos o propios
- mejores decisiones con datos más completos
- generación más rápida de insights sobre el landscape de TI

## Valor de negocio
SAP indica 90% de reducción del tiempo para generar insights de artefactos del landscape de TI. El valor está en acelerar análisis de arquitectura empresarial y mejorar toma de decisiones basada en inventario.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP LeanIX solutions.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP LeanIX solutions sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Consultas en lenguaje natural sobre el repositorio de arquitectura_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J45 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e3e00a83-6fc7-4ec4-9763-5d62f942e193/

---

## [J467] — Accounts Receivable Agent

## En una frase
Transforma la gestión de cuentas por cobrar (AR) aportando inteligencia, automatización y foco estratégico.

## ¿Qué es?
Transforma la gestión de cuentas por cobrar (AR) aportando inteligencia, automatización y foco estratégico. Automatiza el análisis de datos de cuentas por cobrar —saldos de clientes, historial de dunning y partidas en disputa— para ofrecer insights y recomendaciones basadas en datos. Ayuda a reducir el DSO priorizando el cierre de partidas abiertas y anticipando riesgos con próximas mejores acciones. Es una capacidad de IA **Base** de Joule‚ SAP S/4HANA Cloud Private Edition.

## Beneficios
- Reduce el tiempo de conciliación y gestión de cuentas por cobrar automatizando la agregación de datos y priorizando lo importante
- reduce el DSO (Days Sales Outstanding) con priorización inteligente
- disminuye los castigos por incobrables al dar visibilidad temprana de disputas o cuentas en riesgo

## Valor de negocio
75% de reducción del esfuerzo de análisis y conciliación de partidas AR abiertas; 1% de reducción del DSO; 2% de reducción de castigos por incobrables.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule‚ SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el tiempo de conciliación y gestión de cuentas por cobrar automatizando la agregación de datos y priorizando lo importante_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule‚ SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule‚ SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J467 |
| Producto | Joule‚ SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FLP-EXT-PCE-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ecd030e9-59b3-43b4-85cf-260d498912dd/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ecd030e9-59b3-43b4-85cf-260d498912dd/

---

## [J468] — Field Service Dispatcher Agent

## En una frase
Permite a los dispatchers planificar y optimizar órdenes de servicio aprovechando datos en tiempo real, la disponibilidad de técnicos y recomendaciones inteligentes.

## ¿Qué es?
Permite a los dispatchers planificar y optimizar órdenes de servicio aprovechando datos en tiempo real, la disponibilidad de técnicos y recomendaciones inteligentes. Propone el técnico adecuado para el trabajo adecuado en el momento y lugar óptimos, reduciendo el esfuerzo manual; cada propuesta la verifica un dispatcher (human-in-the-loop), manteniendo el control humano y la confianza. Es una capacidad de IA **Base** de SAP Field Service Management‚ Joule.

## Beneficios
- Aumenta la productividad del dispatcher reduciendo tareas manuales, minimizando errores y permitiendo decisiones más rápidas y eficientes
- optimiza la asignación de recursos analizando datos en tiempo real y reduciendo asignaciones erróneas

## Valor de negocio
50% de aumento de la productividad del dispatcher de servicio de campo; 8% de reducción de asignaciones erróneas de recursos de servicio.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Field Service Management‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Aumenta la productividad del dispatcher reduciendo tareas manuales_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Field Service Management‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Field Service Management‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J468 |
| Producto | SAP Field Service Management‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CEC-SRV-FSM-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9c354ba9-b021-470a-b75d-b6e7bf4405de/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9c354ba9-b021-470a-b75d-b6e7bf4405de/

---

## [J46] — Context Generation

## En una frase
El contexto generado por IA aporta información e insights adicionales analizando los datos y el contexto existentes, ayudando a los usuarios a comprender mejor las tareas o solicitudes y a tomar decisiones informadas.

## ¿Qué es?
El contexto generado por IA aporta información e insights adicionales analizando los datos y el contexto existentes, ayudando a los usuarios a comprender mejor las tareas o solicitudes y a tomar decisiones informadas. Forma parte de las Base AI capabilities de SAP LeanIX, embebidas en la interfaz del inventory y del workspace. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Incrementa la productividad del responsable (assignee) de los to-dos

## Valor de negocio
50% de reducción del tiempo requerido para completar los to-dos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP LeanIX solutions.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP LeanIX solutions para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Incrementa la productividad del responsable (assignee) de los to-dos_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J46 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/fa2762c1-5080-480b-bf93-103933a0af11/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/fa2762c1-5080-480b-bf93-103933a0af11/

---

## [J470] — Data Actions

## En una frase
Proporciona a los usuarios profesionales de planificación herramientas para generar scripts de Advanced Formulas de SAP Analytics Cloud o comentarios.

## ¿Qué es?
Proporciona a los usuarios profesionales de planificación herramientas para generar scripts de Advanced Formulas de SAP Analytics Cloud o comentarios. También permite generar comentarios de negocio a partir de un Advanced Formulas Script existente para apoyar la documentación y la transferencia de conocimiento, y generar fácilmente una descripción para una data action, incluyendo sus pasos. Es una capacidad de IA **Premium** de SAP Analytics Cloud.

## Beneficios
- Reduce el tiempo para escribir scripts de Advanced Formula mediante un comentario en lenguaje natural
- reduce el tiempo para generar comentarios de negocio a partir de un script existente (documentación o transferencia de conocimiento)
- reduce el tiempo para crear una descripción concisa de una data action

## Valor de negocio
75% de reducción del tiempo para escribir scripts; 75% de reducción del tiempo para crear scripts totalmente documentados; 88% de reducción del tiempo para crear la descripción de una data action.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Analytics Cloud, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Analytics Cloud y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el tiempo para escribir scripts de Advanced Formula mediante un comentario en lenguaje natural_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J470 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PL-AF |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/8e974edb-5d3e-4500-bc00-8549fbf8edd6/

---

## [J471] — AI-Assisted Calculations

## En una frase
Permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos de SAP Analytics Cloud, y también explicar fórmulas existentes en lenguaje claro.

## ¿Qué es?
Permite generar fórmulas de cálculo complejas usando lenguaje natural dentro del diálogo de cálculos de SAP Analytics Cloud, y también explicar fórmulas existentes en lenguaje claro. Es una capacidad de IA **Premium** de SAP Analytics Cloud.

## Beneficios
- Creación de cálculos por lenguaje natural
- explicación de cálculos existentes
- mejor experiencia de usuario para crear y entender cálculos con apoyo de IA

## Valor de negocio
SAP indica una reducción del 60% en el tiempo de creación de cálculos y una reducción del 60% en el tiempo necesario para entender cálculos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Creación de cálculos por lenguaje natural_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J471 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-DAN |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/b0112bf9-3bff-4991-b029-44248df82479/

---

## [J47] — AI-Assisted Texting

## En una frase
Permite crear o mejorar textos analizando contenido y contexto, con opciones para reescribir o resumir información existente.

## ¿Qué es?
Permite crear o mejorar textos analizando contenido y contexto, con opciones para reescribir o resumir información existente. Un ejemplo indicado es generar descripciones concisas y precisas para fact sheets. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Automatiza la generación de descripciones informativas, ahorra tiempo y esfuerzo, y mejora la productividad de los propietarios de aplicaciones

## Valor de negocio
SAP indica hasta un 80% de reducción en el tiempo requerido para completar descripciones de aplicaciones.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP LeanIX solutions.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP LeanIX solutions para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Automatiza la generación de descripciones informativas_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J47 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/86968b11-6426-4749-90c5-39d6711514a7/

---

## [J48] — Translation Support

## En una frase
La traducción asistida por IA permite a administradores agregar y traducir etiquetas y textos de ayuda para atributos nuevos o existentes en la configuración del metamodelo de SAP LeanIX.

## ¿Qué es?
La traducción asistida por IA permite a administradores agregar y traducir etiquetas y textos de ayuda para atributos nuevos o existentes en la configuración del metamodelo de SAP LeanIX. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Ahorra tiempo y esfuerzo en traducciones
- mejora la consistencia del contenido traducido
- amplía la accesibilidad del producto para usuarios con diferentes preferencias de idioma

## Valor de negocio
Reduce el tiempo requerido para traducir términos del metamodelo, mejora la comprensión de la arquitectura empresarial y facilita una experiencia más inclusiva para usuarios globales.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP LeanIX solutions.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP LeanIX solutions para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Ahorra tiempo y esfuerzo en traducciones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J48 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6719d6d7-fda7-4ea9-b0dd-43b99fbab6b6/

---

## [J535] — Central Governance

## En una frase
Joule embebido en SAP Master Data Governance sobre SAP S/4HANA Cloud Private Edition permite a usuarios de negocio (p.

## ¿Qué es?
Joule embebido en SAP Master Data Governance sobre SAP S/4HANA Cloud Private Edition permite a usuarios de negocio (p. ej. gerentes de ventas y especialistas de compras) operar funciones de MDG mediante lenguaje natural, sin conocimiento técnico extenso. Usa procesamiento de lenguaje natural para interpretar los prompts del usuario contra la estructura de los datos maestros y ejecutar los cambios: buscar, visualizar, crear nuevos business partners o modificar existentes, y consultar el estado de los procesos de gobierno. Es una capacidad de IA **Base** de SAP S/4HANA Cloud for master data governance, private edition.

## Beneficios
- Aumenta la flexibilidad y facilidad en la captura y gobierno de datos de business partner
- habilita a usuarios de negocio a usar funciones de SAP Master Data Governance sin herramientas ni capacitación adicionales

## Valor de negocio
85% de reducción del esfuerzo/tiempo dedicado cada vez a gestionar datos maestros; 10% de reducción de la pérdida anual de ingreso operativo por actualizaciones de datos maestros tardías o erróneas.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud for master data governance, private edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud for master data governance, private edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Aumenta la flexibilidad y facilidad en la captura y gobierno de datos de business partner_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud for master data governance, private edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud for master data governance, private edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J535 |
| Producto | SAP S/4HANA Cloud for master data governance, private edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-MDG-CMP-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a0399e7f-e105-40a9-9169-d63e768735b8/

---

## [J54] — Joule with SAP S/4HANA Cloud Private Edition

## En una frase
Permite usar lenguaje natural para expresar requerimientos de negocio y acceder a capacidades informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Private Edition.

## ¿Qué es?
Permite usar lenguaje natural para expresar requerimientos de negocio y acceder a capacidades informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Private Edition. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Navegación hacia aplicaciones de finanzas, ventas, compras, servicios y otros procesos
- ejecución más fluida de tareas
- acceso conversacional a información del negocio

## Valor de negocio
No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se centra en productividad, navegación y ejecución de tareas en SAP S/4HANA Cloud Private Edition.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Private Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Navegación hacia aplicaciones de finanzas_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J54 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-FLP-EXT-PCE-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/98ee8608-82bb-49c3-b4ca-805bd6594314/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/98ee8608-82bb-49c3-b4ca-805bd6594314/

---

## [J57] — Joule with SAP Business Technology Platform

## En una frase
Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural.

## ¿Qué es?
Integra Joule en SAP BTP para que administradores/plataforma consulten información sobre recursos de SAP BTP, usuarios, runtime y cuentas mediante lenguaje natural. Es una capacidad de IA **Base** de SAP Business Technology Platform.

## Beneficios
- Acelera la consulta de recursos y administración de BTP
- reduce navegación manual en cockpit/documentación
- facilita respuestas contextuales para tareas de administración

## Valor de negocio
No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se expresa en ahorro de tiempo para consultas administrativas y acceso más rápido a información de BTP.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Business Technology Platform.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Business Technology Platform sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Acelera la consulta de recursos y administración de BTP_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Business Technology Platform y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Business Technology Platform** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J57 |
| Producto | SAP Business Technology Platform |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-CP-CPT-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9c079680-7938-4ddd-83c4-3d89a7943311/

---

## [J585] — Cash Positioning Agent

## En una frase
Entrega a los gestores de tesorería una visión actualizada de la posición de caja en todas las cuentas bancarias: recopila saldos iniciales y flujos de caja esperados, calcula saldos finales esperados e identifica automáticamente déficits y superávits según la política de tesorería.

## ¿Qué es?
Entrega a los gestores de tesorería una visión actualizada de la posición de caja en todas las cuentas bancarias: recopila saldos iniciales y flujos de caja esperados, calcula saldos finales esperados e identifica automáticamente déficits y superávits según la política de tesorería. Con base en ello, Joule propone asignaciones de caja eficientes mediante transferencias bancarias. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition‚ Joule.

## Beneficios
- Optimiza el flujo de caja con identificación automática de déficits y superávits
- mejora la liquidez con recomendaciones y propuestas de transferencia accionables

## Valor de negocio
70% de reducción del esfuerzo de gestión de caja.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Optimiza el flujo de caja con identificación automática de déficits y superávits_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J585 |
| Producto | SAP S/4HANA Cloud Public Edition‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FIN-FSCM-CLM-COP-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/cd99c7b2-f716-46ab-8fe5-640f9aa02613/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cd99c7b2-f716-46ab-8fe5-640f9aa02613/

---

## [J586] — Project Services

## En una frase
Joule incorpora una interfaz conversacional para apoyar actividades rutinarias de gestión de proyectos en SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Joule incorpora una interfaz conversacional para apoyar actividades rutinarias de gestión de proyectos en SAP S/4HANA Cloud Public Edition. La capacidad ayuda a monitorear cumplimiento de tiempos, resumir cambios de proyecto y ofrecer autoservicio con IA para equipos de proyecto. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce carga administrativa, permite acceso inmediato a insights críticos del proyecto y disminuye la dependencia de soporte back-office mediante capacidades de autoservicio impulsadas por IA

## Valor de negocio
La página posiciona la capacidad con una reducción del 60% en esfuerzos de administración de proyectos, acelerando decisiones y mejorando la productividad de los equipos de proyecto.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce carga administrativa_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J586 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | PPM-SCL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/bccabd59-564e-4a4d-84b3-67d6933348cd/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/bccabd59-564e-4a4d-84b3-67d6933348cd/

---

## [J596] — Safety Observation Reporting

## En una frase
Ayuda a operadores de producción e higienistas industriales a reportar observaciones de seguridad en lenguaje natural.

## ¿Qué es?
Ayuda a operadores de producción e higienistas industriales a reportar observaciones de seguridad en lenguaje natural. El sistema procesa la entrada, detecta detalles críticos faltantes, guía al usuario con preguntas de seguimiento contextuales, y estructura y registra automáticamente los datos en un registro formal de observación de seguridad. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Permite a los operadores reportar peligros en segundos con guía intuitiva, sin romper el flujo de trabajo ni llenar formularios
- permite al higienista industrial capturar datos de observación estandarizados y accionables de los trabajadores de primera línea, acelerando la priorización de riesgos y la acción preventiva

## Valor de negocio
71% de reducción del costo de reporte de observaciones de seguridad; 5% de evitación de costo por pérdida de tiempo debida a incidentes.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Permite a los operadores reportar peligros en segundos con guía intuitiva_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J596 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | EHS-SUS-IM |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c3691d08-1455-4c6a-8cea-e524489e5b69/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c3691d08-1455-4c6a-8cea-e524489e5b69/

---

## [J597] — Back Order Processing

## En una frase
Funcionalidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución y configuración de Back Order Processing mediante interacciones intuitivas basadas en prompts.

## ¿Qué es?
Funcionalidad de Joule para SAP S/4HANA Cloud Public Edition que asiste la ejecución y configuración de Back Order Processing mediante interacciones intuitivas basadas en prompts. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce esfuerzo manual en BOP
- acelera la toma de decisiones con automatización y guía inteligente
- facilita priorizar requerimientos de disponibilidad según criterios de negocio

## Valor de negocio
Mejora la velocidad y calidad de la ejecución de BOP. No se encontró un KPI cuantitativo específico en la página consultada.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce esfuerzo manual en BOP_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J597 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-ATP-AI-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/88bf4617-8a77-4dfb-8950-fc00a67cc01d/

---

## [J600] — Joule with SAP Multi-Bank Connectivity

## En una frase
Proporciona respuestas rápidas sobre SAP Multi-Bank Connectivity a partir de documentación del producto en SAP Help Portal, resumidas de forma contextual y clara.

## ¿Qué es?
Proporciona respuestas rápidas sobre SAP Multi-Bank Connectivity a partir de documentación del producto en SAP Help Portal, resumidas de forma contextual y clara. Es una capacidad de IA **Base** de SAP Multi-Bank Connectivity.

## Beneficios
- Expresión de necesidades de negocio en lenguaje natural
- acceso más rápido a contenido de enablement
- ahorro de tiempo al evitar revisar largas listas de resultados o múltiples temas de documentación

## Valor de negocio
No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se expresa en ahorro de tiempo de búsqueda, mejor acceso a documentación y mayor satisfacción del usuario.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP Multi-Bank Connectivity.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP Multi-Bank Connectivity sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Expresión de necesidades de negocio en lenguaje natural_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Multi-Bank Connectivity y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Multi-Bank Connectivity** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J600 |
| Producto | SAP Multi-Bank Connectivity |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-JOULE-QNA |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5cd6a2a6-c3ba-4bf6-9111-5e2f95757a69/

---

## [J606] — Anomaly Detection

## En una frase
Capacidad de SAP Integration Suite para identificar patrones inusuales o desviaciones en el tráfico de APIs mediante IA, apoyando la detección temprana de anomalías.

## ¿Qué es?
Capacidad de SAP Integration Suite para identificar patrones inusuales o desviaciones en el tráfico de APIs mediante IA, apoyando la detección temprana de anomalías. Es una capacidad de IA **Base** de SAP Integration Suite.

## Beneficios
- Ayuda a API owners a detectar desviaciones relevantes
- permite reaccionar ante comportamiento anómalo de APIs
- mejora el monitoreo operativo del tráfico API

## Valor de negocio
La página consultada indica reducción del costo de resolución de anomalías de API. No se extrajo un segundo indicador cuantitativo completo de la página consultada.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Integration Suite.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Integration Suite sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Ayuda a API owners a detectar desviaciones relevantes_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Integration Suite y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Integration Suite** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J606 |
| Producto | SAP Integration Suite |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | OPU-API-OD-AN |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c1bf4c86-b2bc-4101-b51d-bc5904ff5924/

---

## [J638] — Process Generation

## En una frase
Process Generation genera artefactos de proceso a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation.

## ¿Qué es?
Process Generation genera artefactos de proceso a partir de descripciones en lenguaje natural para apoyar el diseño de automatizaciones en SAP Build Process Automation. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Permite pasar de una descripción de negocio a un artefacto inicial de automatización, reduce tiempo de arranque y mejora la colaboración entre negocio y desarrollo

## Valor de negocio
Su valor está en reducir esfuerzo de automatización low-code, acelerar la productividad de desarrolladores y mejorar el time-to-market de soluciones low-code.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Process Automation.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Process Automation para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Permite pasar de una descripción de negocio a un artefacto inicial de automatización_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J638 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-PA-PRC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/50a434ab-f63c-4f3f-a5d2-c661b5d461f2/

---

## [J639] — Process Editing

## En una frase
Process Editing ayuda a desarrolladores durante el diseño e implementación de automatizaciones, permitiendo editar artefactos de proceso mediante instrucciones en lenguaje natural.

## ¿Qué es?
Process Editing ayuda a desarrolladores durante el diseño e implementación de automatizaciones, permitiendo editar artefactos de proceso mediante instrucciones en lenguaje natural. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Reduce el esfuerzo de edición manual, acelera iteraciones sobre procesos y mejora la productividad en el diseño low-code de automatizaciones

## Valor de negocio
La capacidad se asocia con reducción del esfuerzo de automatización low-code, mayor productividad de desarrolladores y mejor velocidad de entrega de nuevas aplicaciones o procesos.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP Build Process Automation.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP Build Process Automation con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Reduce el esfuerzo de edición manual_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J639 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-PA-PRC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/143f1e51-609a-45d9-ab96-bf286e044a03/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/143f1e51-609a-45d9-ab96-bf286e044a03/

---

## [J640] — Process Summarization

## En una frase
Process Summarization genera resúmenes en lenguaje natural de procesos o artefactos complejos para facilitar la comprensión, revisión y transferencia de conocimiento.

## ¿Qué es?
Process Summarization genera resúmenes en lenguaje natural de procesos o artefactos complejos para facilitar la comprensión, revisión y transferencia de conocimiento. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Reduce el tiempo requerido para entender procesos existentes, apoya handovers y mejora la documentación funcional de automatizaciones

## Valor de negocio
El valor se relaciona con mayor productividad en diseño e implementación de automatizaciones low-code y con menor esfuerzo de revisión/documentación.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Build Process Automation, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Build Process Automation y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el tiempo requerido para entender procesos existentes_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J640 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-PA-PRC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/69b0874a-e8a6-49e3-b66c-4a6c5b1fd77f/

---

## [J641] — Form Generation

## En una frase
Genera formularios de automatización de procesos a partir de descripciones en lenguaje natural en SAP Build Process Automation.

## ¿Qué es?
Genera formularios de automatización de procesos a partir de descripciones en lenguaje natural en SAP Build Process Automation. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Soporta a desarrolladores durante el diseño e implementación de automatizaciones
- permite generar artefactos de formulario de manera más rápida
- incrementa productividad en escenarios low-code

## Valor de negocio
Reducción estimada del 30% en esfuerzo de automatización low-code; 10% más rápido el tiempo de productividad para desarrolladores; 10% de mejora en time-to-market para nuevas aplicaciones low-code.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Process Automation.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Process Automation para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Soporta a desarrolladores durante el diseño e implementación de automatizaciones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J641 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-PA-FRM |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/ff9ca9a1-b443-405d-95bd-9b53a8a503db/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/ff9ca9a1-b443-405d-95bd-9b53a8a503db/

---

## [J642] — Decision Generation

## En una frase
Asiste el diseño de procesos al generar artefactos de decisión a partir de descripciones en lenguaje natural de las reglas deseadas.

## ¿Qué es?
Asiste el diseño de procesos al generar artefactos de decisión a partir de descripciones en lenguaje natural de las reglas deseadas. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Permite construir y automatizar procesos usando lenguaje natural, con mayor productividad de desarrolladores, mejor calidad e innovación
- también facilita el trabajo con procesos y artefactos complejos

## Valor de negocio
30% de reducción del esfuerzo de automatización low-code; 10% menor tiempo hasta productividad para desarrolladores; 10% mejora del time-to-market para nuevas aplicaciones low-code.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Process Automation.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Process Automation para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Permite construir y automatizar procesos usando lenguaje natural_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J642 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-BPM-RUL |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/0517fabc-df67-4042-9015-a57c1a9079ba/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0517fabc-df67-4042-9015-a57c1a9079ba/

---

## [J643] — Decision Summarization

## En una frase
Asiste a los usuarios en el diseño e implementación de automatizaciones al generar resúmenes de negocio de reglas ya modeladas que no tienen documentación.

## ¿Qué es?
Asiste a los usuarios en el diseño e implementación de automatizaciones al generar resúmenes de negocio de reglas ya modeladas que no tienen documentación. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Facilita la comprensión de artefactos de decisión, acelera el handover y reduce el tiempo necesario para entender procesos o reglas complejas

## Valor de negocio
30% de reducción del esfuerzo de automatización low-code; 10% menor tiempo hasta productividad para desarrolladores; 10% mejora del time-to-market para nuevas aplicaciones low-code.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Build Process Automation, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Build Process Automation y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Facilita la comprensión de artefactos de decisión_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J643 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-BPM-RUL |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d9b9af67-e0a9-49cc-b79b-a8eddde1731b/

---

## [J644] — Script Task Generation

## En una frase
Permite generar código JavaScript ejecutable mediante lenguaje natural dentro de SAP Build Process Automation.

## ¿Qué es?
Permite generar código JavaScript ejecutable mediante lenguaje natural dentro de SAP Build Process Automation. La tarea de script integra capacidades de IA generativa para que el desarrollador cree código a partir de prompts y pueda apoyarse en acciones predefinidas alineadas con las restricciones del runtime. Es una capacidad de IA **Base** de SAP Build Process Automation.

## Beneficios
- Acelera la construcción de procesos y automatizaciones a partir de lenguaje natural
- facilita la generación y adaptación de artefactos complejos
- ayuda a los desarrolladores a crear scripts más rápido, incluyendo tareas como remover paquetes de terceros o ajustar código a ECMAScript 5.1

## Valor de negocio
30% de reducción del esfuerzo de automatización low-code; 10% más rapidez para que los desarrolladores alcancen productividad; 10% de mejora en el time-to-market de nuevas aplicaciones low-code.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Build Process Automation.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Build Process Automation para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera la construcción de procesos y automatizaciones a partir de lenguaje natural_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Build Process Automation y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Build Process Automation** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J644 |
| Producto | SAP Build Process Automation |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-PA-PRC |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f2310927-98ed-410a-86bb-1ca9ece68e21/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f2310927-98ed-410a-86bb-1ca9ece68e21/

---

## [J648] — International Trade Classification Agent

## En una frase
Ayuda a los especialistas de clasificación de productos a clasificar mercancías para envíos internacionales: razona sobre las características del producto y las regulaciones comerciales, recomienda números de arancel aduanero y commodity codes, y aporta la justificación para una revisión y aprobación sencillas, ayudando a asegurar el cumplimiento de las regulaciones de comercio global con un proceso auditable.

## ¿Qué es?
Ayuda a los especialistas de clasificación de productos a clasificar mercancías para envíos internacionales: razona sobre las características del producto y las regulaciones comerciales, recomienda números de arancel aduanero y commodity codes, y aporta la justificación para una revisión y aprobación sencillas, ayudando a asegurar el cumplimiento de las regulaciones de comercio global con un proceso auditable. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Ahorra tiempo con la clasificación automática de mercancías para envío internacional
- asegura el cumplimiento con recomendaciones razonadas desde características del producto y regulaciones
- reduce el riesgo eliminando errores manuales con un proceso de decisión auditable

## Valor de negocio
50% de reducción del esfuerzo de clasificar productos de comercio internacional.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Ahorra tiempo con la clasificación automática de mercancías para envío internacional_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J648 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FT-ITR-CLS |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/cb3aa823-c475-4f81-9730-d35d85bd55c7/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/cb3aa823-c475-4f81-9730-d35d85bd55c7/

---

## [J650] — Booking Agent

## En una frase
Agente de Joule en Concur Travel que entrega recomendaciones personalizadas de vuelos y hoteles analizando preferencias del viajero, políticas de viaje de la empresa y restricciones de presupuesto.

## ¿Qué es?
Agente de Joule en Concur Travel que entrega recomendaciones personalizadas de vuelos y hoteles analizando preferencias del viajero, políticas de viaje de la empresa y restricciones de presupuesto. Es una capacidad de IA **Base** de el producto SAP.

## Beneficios
- Reduce búsqueda manual
- aumenta cumplimiento de políticas
- mejora la experiencia de reserva para viajeros
- da a la organización mayor visibilidad y control sobre el gasto de viaje

## Valor de negocio
Mejora la eficiencia del proceso de booking y el cumplimiento de políticas corporativas. No se encontró un KPI cuantitativo específico en la página consultada.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de el producto SAP.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en el producto SAP sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce búsqueda manual_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de el producto SAP y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **el producto SAP** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J650 |
| Producto | el producto SAP |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | Queue - TRV - Core Travel |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/47844870-d3f6-4ffd-abdf-945d6bc20ae7/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/47844870-d3f6-4ffd-abdf-945d6bc20ae7/

---

## [J652] — Architecture Guidance

## En una frase
Capacidad de SAP LeanIX que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial.

## ¿Qué es?
Capacidad de SAP LeanIX que analiza el landscape de TI y ofrece insights personalizados y pasos accionables para optimizar la arquitectura empresarial. Es una capacidad de IA **Base** de SAP LeanIX solutions.

## Beneficios
- Ayuda a descubrir oportunidades de transformación, identificar posibles acciones sobre aplicaciones y acelerar la toma de decisiones de arquitectura con soporte de IA

## Valor de negocio
Acelera el descubrimiento de oportunidades de mejora y reduce el esfuerzo manual de análisis de arquitectura. No se encontró un KPI cuantitativo específico en la página consultada.

## ¿Cómo funciona?
1. **Análisis del contexto:** la IA evalúa los datos relevantes del proceso en SAP LeanIX solutions.
2. **Generación de la propuesta:** produce la recomendación o propuesta con su justificación.
3. **Decisión humana:** el usuario revisa, ajusta y confirma; la IA acelera la decisión sin reemplazar el criterio del responsable.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un especialista enfrenta una decisión repetitiva en SAP LeanIX solutions que consume tiempo de análisis manual. **Cómo ayuda la feature:** la IA le propone una opción con su justificación y el especialista solo valida y confirma. Apoya en: _Ayuda a descubrir oportunidades de transformación_.
2. **Escenario:** Existe un backlog de casos pendientes que frena el proceso. **Cómo ayuda la feature:** las propuestas asistidas aceleran la resolución y reducen el tiempo de ciclo, manteniendo el control humano.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP LeanIX solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP LeanIX solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J652 |
| Producto | SAP LeanIX solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LIX |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5b68ce3e-c6d7-4e5d-a2cd-e137adb01d33/

---

## [J669] — Insights Description Generator

## En una frase
Capacidad de SAP Signavio Process Transformation Manager que ayuda a crear descripciones claras, consistentes y amigables para usuarios de negocio al capturar y colaborar sobre insights de SAP Signavio Process Intelligence.

## ¿Qué es?
Capacidad de SAP Signavio Process Transformation Manager que ayuda a crear descripciones claras, consistentes y amigables para usuarios de negocio al capturar y colaborar sobre insights de SAP Signavio Process Intelligence. Es una capacidad de IA **Base** de SAP Signavio Process Transformation Manager.

## Beneficios
- Acelera la creación de descripciones de insights
- mejora claridad y consistencia
- facilita alineación entre usuarios de negocio y analistas
- ayuda a convertir insights en información accionable

## Valor de negocio
El valor está en acelerar el paso de insight a acción con mayor claridad y estructura, mejorando la alineación y toma de decisiones durante iniciativas de transformación.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP Signavio Process Transformation Manager.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP Signavio Process Transformation Manager. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Acelera la creación de descripciones de insights_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio Process Transformation Manager y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio Process Transformation Manager** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J669 |
| Producto | SAP Signavio Process Transformation Manager |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-CA-II |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/0614d66c-4e6d-42bc-b45b-135ba035d843/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/0614d66c-4e6d-42bc-b45b-135ba035d843/

---

## [J671] — Performance Preparation Agent

## En una frase
El Performance Preparation Agent automatiza la recopilación de datos, genera talking points personalizados para managers y sugiere próximos pasos accionables para reuniones one-on-one.

## ¿Qué es?
El Performance Preparation Agent automatiza la recopilación de datos, genera talking points personalizados para managers y sugiere próximos pasos accionables para reuniones one-on-one. Es una capacidad de IA **Base** de el producto SAP.

## Beneficios
- Da acceso inmediato a insights data-driven de empleados
- reduce preparación manual del manager
- mejora foco y consistencia de conversaciones de desempeño

## Valor de negocio
70% de reducción en el tiempo del manager dedicado a preparar reuniones de desempeño o one-on-one.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en el producto SAP.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en el producto SAP para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Da acceso inmediato a insights data-driven de empleados_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de el producto SAP y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **el producto SAP** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J671 |
| Producto | el producto SAP |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-SF-PLT-GAI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/761a2305-b0a2-4262-b9a3-abd4945ad314/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/761a2305-b0a2-4262-b9a3-abd4945ad314/

---

## [J741] — Catalog Optimization Agent

## En una frase
Permite a los product managers de e-commerce optimizar su catálogo de SAP Commerce Cloud: revisa de forma continua descripciones, atributos y traducciones de producto contra los estándares de calidad de la empresa, detecta brechas de merchandising y ofrece recomendaciones accionables para mejorar la calidad del catálogo, la consistencia multilingüe y la descubribilidad del producto.

## ¿Qué es?
Permite a los product managers de e-commerce optimizar su catálogo de SAP Commerce Cloud: revisa de forma continua descripciones, atributos y traducciones de producto contra los estándares de calidad de la empresa, detecta brechas de merchandising y ofrece recomendaciones accionables para mejorar la calidad del catálogo, la consistencia multilingüe y la descubribilidad del producto. Es una capacidad de IA **Base** de SAP CX AI Toolkit.

## Beneficios
- Mantiene altos estándares de merchandising
- mejora la calidad del catálogo y la descubribilidad del producto
- impulsa mayores tasas de conversión con información de producto profesional y completa

## Valor de negocio
70% de reducción del tiempo de traducir datos del catálogo; 5% de reducción del costo de calidad de datos; 65% de reducción del tiempo de añadir descripción por activo del catálogo.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP CX AI Toolkit.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP CX AI Toolkit con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Mantiene altos estándares de merchandising_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP CX AI Toolkit y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP CX AI Toolkit** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J741 |
| Producto | SAP CX AI Toolkit |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CEC-AIT-HCS |
| Industrias aplicables | Consumer Products |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/28593981-f647-4d1b-bb1f-709783df1fa6/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/28593981-f647-4d1b-bb1f-709783df1fa6/

---

## [J74] — Joule with SAP S/4HANA Cloud Public Edition

## En una frase
Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes.

## ¿Qué es?
Permite obtener insights rápidos sobre datos de negocio, por ejemplo órdenes de compra o entregas salientes, sin tener que buscar y abrir manualmente las aplicaciones correspondientes. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Acceso rápido a información operacional
- menor navegación entre aplicaciones
- soporte para tareas informativas, navegacionales y transaccionales en SAP S/4HANA Cloud Public Edition

## Valor de negocio
No se identificó una métrica cuantitativa explícita en la página de detalle consultada; el valor se concentra en rapidez de acceso a datos, reducción de pasos manuales y productividad del usuario.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Acceso rápido a información operacional_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J74 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-FLP-EXT-JOU |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/59d61974-9d59-4e32-9026-189462bbf54f/

---

## [J756] — Safety Instruction Generation

## En una frase
Genera automáticamente instrucciones de seguridad claras, estructuradas y fáciles de entender, adaptadas a equipos específicos, directamente a partir de las últimas evaluaciones de riesgo y análisis de peligros del trabajo (JHA).

## ¿Qué es?
Genera automáticamente instrucciones de seguridad claras, estructuradas y fáciles de entender, adaptadas a equipos específicos, directamente a partir de las últimas evaluaciones de riesgo y análisis de peligros del trabajo (JHA). Reduce drásticamente el tiempo y el esfuerzo manual transformando datos de evaluación complejos en guía precisa y actualizada, asegurando claridad, cumplimiento y consistencia. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el tiempo y esfuerzo manual de revisar la evaluación de riesgo o JHA para preparar instrucciones de seguridad
- auto-propone pautas estructuradas y fáciles de entender
- adaptadas a equipos específicos
- protege a los trabajadores y mantiene las operaciones seguras

## Valor de negocio
No publicado en la página Detail Page.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce el tiempo y esfuerzo manual de revisar la evaluación de riesgo o JHA para preparar instrucciones de seguridad_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J756 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | EHS-SUS-HS |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/76d64fc7-204e-4a1f-979c-2a75a7a4ce29/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/76d64fc7-204e-4a1f-979c-2a75a7a4ce29/

---

## [J757] — Supplier Delivery Date Mass Update

## En una frase
Permite realizar actualizaciones masivas de fechas de entrega para múltiples pedidos de compra utilizando Joule en SAP S/4HANA Cloud Public Edition.

## ¿Qué es?
Permite realizar actualizaciones masivas de fechas de entrega para múltiples pedidos de compra utilizando Joule en SAP S/4HANA Cloud Public Edition. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Disminuye el trabajo manual asociado al cambio de fechas en múltiples órdenes
- facilita ajustes rápidos ante cambios del proveedor
- mejora la experiencia del comprador mediante una interacción guiada por Joule

## Valor de negocio
Mejora la agilidad del proceso de compras y planificación al mantener actualizadas las fechas de entrega de manera más rápida, reduciendo retrasos operativos y reprocesos.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Disminuye el trabajo manual asociado al cambio de fechas en múltiples órdenes_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J757 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/d7b65dad-4fa1-4430-a860-6c8eba5ff8e1/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/d7b65dad-4fa1-4430-a860-6c8eba5ff8e1/

---

## [J762] — Joule and Microsoft 365 Copilot

## En una frase
Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365.

## ¿Qué es?
Integra de forma bidireccional Joule y Microsoft 365 Copilot para que el usuario trabaje desde el entorno donde ya está: SAP o Microsoft 365. Permite consultar datos y tareas de SAP desde Copilot y aprovechar información/flujos de Microsoft 365 desde Joule. Es una capacidad de IA **Base** de Joule.

## Beneficios
- Flexibilidad para trabajar en el entorno más efectivo según la tarea
- acceso más eficiente a información y workflows de SAP y Microsoft 365
- menor cambio de contexto entre aplicaciones

## Valor de negocio
No se identificó una métrica cuantitativa explícita de Business Value en la página de detalle consultada; el valor descrito se concentra en productividad, continuidad de trabajo y reducción de fricción entre SAP y Microsoft 365.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Flexibilidad para trabajar en el entorno más efectivo según la tarea_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J762 |
| Producto | Joule |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | CA-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4dfa3fea-c5d2-40e3-959d-317b07b6b64e/

---

## [J765] — Behavioral Insights for Contract Accounting

## En una frase
Feature para SAP S/4HANA Cloud Private Edition que ayuda a especialistas de cobranza a predecir y explicar riesgos de pago analizando comportamiento histórico de clientes.

## ¿Qué es?
Feature para SAP S/4HANA Cloud Private Edition que ayuda a especialistas de cobranza a predecir y explicar riesgos de pago analizando comportamiento histórico de clientes. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Identificación rápida de cuentas de alto riesgo
- optimización de estrategias de cobranza
- reducción de deuda pendiente
- ahorro de tiempo y mejores resultados operativos

## Valor de negocio
3.5% de reducción en días de ventas pendientes de cobro (DSO), 5% de reducción de incobrables/write-offs de cuentas por cobrar y 1% de reducción de costos de facturación, crédito y cobranza.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP S/4HANA Cloud Private Edition.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP S/4HANA Cloud Private Edition. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Identificación rápida de cuentas de alto riesgo_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J765 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | IS-PS-BEI |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9b9439fc-3681-446c-989e-2540e2897331/

---

## [J777] — Retrieval of Equipment Information in Service Management

## En una frase
Los service managers pueden acceder rápidamente a detalles completos del equipo instalado en sitios de cliente, incluyendo garantía, historial de transacciones de servicio y recomendaciones o resúmenes asistidos por IA.

## ¿Qué es?
Los service managers pueden acceder rápidamente a detalles completos del equipo instalado en sitios de cliente, incluyendo garantía, historial de transacciones de servicio y recomendaciones o resúmenes asistidos por IA. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Ofrece una vista 360° del equipo, acceso instantáneo a historial y estado de garantía, y apoyo para coordinar mejor actividades de servicio

## Valor de negocio
Aporta valor al mejorar supervisión de calendarios de servicio, reducir potenciales tiempos de inactividad y ayudar a mantener el equipo del cliente operando con mayor confiabilidad.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Ofrece una vista 360° del equipo_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J777 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CRM-S4-MD-EQM |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Supply Chain Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3de36a16-73ca-4df6-94d2-ccd0dc806192/

---

## [J778] — Requirement Generation

## En una frase
Esta función de SAP Cloud ALM permite generar automáticamente requerimientos de negocio de alta calidad a partir de transcripciones o notas de talleres Fit-to-Standard.

## ¿Qué es?
Esta función de SAP Cloud ALM permite generar automáticamente requerimientos de negocio de alta calidad a partir de transcripciones o notas de talleres Fit-to-Standard. Es una capacidad de IA **Premium** de SAP Cloud ALM.

## Beneficios
- Reduce el tiempo dedicado a la creación manual de requerimientos, mejora la consistencia de la documentación y ayuda a capturar resultados de workshops con mayor rapidez

## Valor de negocio
El valor se centra en acelerar workshops Fit-to-Standard, aumentar la calidad de los requisitos y reducir esfuerzo administrativo durante fases de implementación.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Cloud ALM, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Cloud ALM y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el tiempo dedicado a la creación manual de requerimientos_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Cloud ALM y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J778 |
| Producto | SAP Cloud ALM |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | SV-CLM-IMP-TSK |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e5701d25-2615-49ad-acf3-4f2a6363a206/

---

## [J779] — Content Search

## En una frase
SAP Signavio Process Insights ofrece miles de métricas, recomendaciones y guías de referencia; la búsqueda semántica basada en IA permite a los usuarios —especialmente a los expertos en procesos de negocio— descubrir contenido relevante de forma más intuitiva y eficiente.

## ¿Qué es?
SAP Signavio Process Insights ofrece miles de métricas, recomendaciones y guías de referencia; la búsqueda semántica basada en IA permite a los usuarios —especialmente a los expertos en procesos de negocio— descubrir contenido relevante de forma más intuitiva y eficiente. A diferencia de la búsqueda por palabras clave, entiende el contexto y el significado de los términos de búsqueda. Es una capacidad de IA **Base** de SAP Signavio solutions.

## Beneficios
- Ahorra tiempo aclarando preguntas específicas con resultados de búsqueda precisos
- localiza contenido y páginas relevantes sin esfuerzo en las tareas diarias y en el análisis de procesos
- descubre áreas adicionales de investigación con sugerencias más amplias y contextualmente relevantes

## Valor de negocio
82% de reducción del tiempo para obtener insights; 40% de aumento en la adopción de usuarios internos.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Signavio solutions.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Signavio solutions sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Ahorra tiempo aclarando preguntas específicas con resultados de búsqueda precisos_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J779 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-PI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/31657cef-3bb1-4d61-b7b6-0d7b36a328be/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/31657cef-3bb1-4d61-b7b6-0d7b36a328be/

---

## [J787] — Accounting Accruals Agent

## En una frase
Acelera el cierre de fin de periodo: el agente ayuda a los contadores a automatizar la preparación de asientos de devengos (accruals) analizando datos históricos y documentos de política contable.

## ¿Qué es?
Acelera el cierre de fin de periodo: el agente ayuda a los contadores a automatizar la preparación de asientos de devengos (accruals) analizando datos históricos y documentos de política contable. Calcula importes precisos y entrega una lista pre-poblada de asientos para revisión y confirmación, aumentando la productividad y asegurando un cierre mensual oportuno. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el trabajo manual con preparación automática de asientos de devengo
- aumenta la precisión con análisis de datos históricos y patrones financieros mediante IA
- acelera el cierre de periodo y libera tiempo para actividades de mayor valor

## Valor de negocio
80% de reducción del tiempo de cálculo de importes de devengos/diferimientos; 50% de reducción del tiempo de revisión y contabilización de asientos; menor tiempo de cierre de libros.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Public Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Public Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Reduce el trabajo manual con preparación automática de asientos de devengo_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J787 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FI-FIO-GL-TRA-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/2ba6ab3e-ff22-4cb6-b3b4-20613ae8f6e3/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2ba6ab3e-ff22-4cb6-b3b4-20613ae8f6e3/

---

## [J788] — Change Record Management Agent

## En una frase
Reduce costos y acelera el time-to-market: apoya a product managers e ingenieros de diseño encontrando change records similares que afectan al mismo producto y proponiendo la creación de un nuevo borrador de change record.

## ¿Qué es?
Reduce costos y acelera el time-to-market: apoya a product managers e ingenieros de diseño encontrando change records similares que afectan al mismo producto y proponiendo la creación de un nuevo borrador de change record. Acelera decisiones e inicia el proceso de cambio, reduciendo retrasos por datos de cambio fragmentados y mejorando la gobernanza y la trazabilidad. Es una capacidad de IA **Base** de Joule‚ SAP S/4HANA Cloud Private Edition.

## Beneficios
- Reduce el trabajo manual de verificar change records similares, evitando solapamientos y apoyando la decisión de crear uno nuevo o reutilizar el existente
- acelera decisiones entre equipos de ingeniería y manufactura con el siguiente paso recomendado

## Valor de negocio
20% de reducción del tiempo de creación de change requests; 1% de reducción del time-to-market de nuevos productos; 2% de reducción del costo de cambios de ingeniería.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule‚ SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Reduce el trabajo manual de verificar change records similares_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule‚ SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule‚ SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J788 |
| Producto | Joule‚ SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/905534ac-4ede-4c01-a815-476a1643ac7c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/905534ac-4ede-4c01-a815-476a1643ac7c/

---

## [J792] — SAP Joule for Developers‚ ABAP AI capabilities

## En una frase
Joule for Developers con capacidades ABAP AI apoya a desarrolladores en SAP S/4HANA Cloud Public Edition para acelerar tareas de desarrollo ABAP mediante asistencia de IA.

## ¿Qué es?
Joule for Developers con capacidades ABAP AI apoya a desarrolladores en SAP S/4HANA Cloud Public Edition para acelerar tareas de desarrollo ABAP mediante asistencia de IA. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Aumenta la productividad del desarrollador, mejora el soporte en tareas cotidianas y facilita actividades de codificación, explicación o generación de artefactos ABAP

## Valor de negocio
La página indica una reducción del 20% en tiempo y esfuerzo para escribir código ABAP/JAVA y beneficios asociados a mayor eficiencia en desarrollo.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Aumenta la productividad del desarrollador_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J792 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-CP-ABA |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3c06a28b-576b-47ba-a2be-de0588391d6a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3c06a28b-576b-47ba-a2be-de0588391d6a/

---

## [J811] — Supplier Delivery Date Prediction

## En una frase
Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes del proceso.

## ¿Qué es?
Predice fechas de entrega para posiciones de pedidos de compra en SAP S/4HANA Cloud Private Edition utilizando datos históricos y parámetros relevantes del proceso. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Mejora la precisión de las fechas previstas
- aporta soporte predictivo al comprador
- facilita una mejor coordinación con proveedores y planificación interna

## Valor de negocio
Permite planificar con mayor confianza la disponibilidad de materiales y reducir el riesgo operativo asociado a fechas de entrega inciertas o poco confiables.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP S/4HANA Cloud Private Edition.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP S/4HANA Cloud Private Edition sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Mejora la precisión de las fechas previstas_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J811 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/c264b09d-42ca-4256-8d8e-0da5af6c838a/

---

## [J824] — Resolution of Implausible Meter Readings

## En una frase
La capacidad se integra en el procesamiento de lecturas de medidor en IS-U para apoyar con machine learning la resolución de lecturas implausibles.

## ¿Qué es?
La capacidad se integra en el procesamiento de lecturas de medidor en IS-U para apoyar con machine learning la resolución de lecturas implausibles. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Reduce trabajo manual, mejora la eficiencia del procesamiento y ayuda a los equipos de utilities a gestionar excepciones de lectura con mayor calidad

## Valor de negocio
Aporta valor al mejorar la calidad de resolución de excepciones y reducir esfuerzo operativo asociado al análisis manual de lecturas de medidor implausibles.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Private Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Private Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Reduce trabajo manual_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J824 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/4d67f2b1-6f72-4c6f-bce3-e6d4c0e89b1c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/4d67f2b1-6f72-4c6f-bce3-e6d4c0e89b1c/

---

## [J825] — Resolution of Outsorted Billing Documents

## En una frase
La capacidad se integra en el proceso de billing de IS-U para apoyar el procesamiento de documentos de facturación apartados u outsorted.

## ¿Qué es?
La capacidad se integra en el proceso de billing de IS-U para apoyar el procesamiento de documentos de facturación apartados u outsorted. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Incrementa la calidad en la resolución de excepciones y reduce el trabajo manual del especialista de facturación en escenarios de Utilities

## Valor de negocio
El valor de negocio está en mejorar eficiencia operativa, acelerar el tratamiento de excepciones de billing y disminuir carga manual en procesos de facturación.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP S/4HANA Cloud Private Edition, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP S/4HANA Cloud Private Edition y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Incrementa la calidad en la resolución de excepciones y reduce el trabajo manual del especialista de facturación en escenarios de Utilities_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J825 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/f9a4201e-955f-4aaf-b41a-d2479fb13ed1/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/f9a4201e-955f-4aaf-b41a-d2479fb13ed1/

---

## [J831] — Sales Order Creation

## En una frase
Representantes de ventas internos pueden crear órdenes de venta desde archivos de compra no estructurados en PDF o imágenes; la información se extrae automáticamente y se propone en campos de la solicitud.

## ¿Qué es?
Representantes de ventas internos pueden crear órdenes de venta desde archivos de compra no estructurados en PDF o imágenes; la información se extrae automáticamente y se propone en campos de la solicitud. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Automatiza la preparación de solicitudes de pedido, reduce trabajo intensivo manual y disminuye errores durante el procesamiento de documentos de compra

## Valor de negocio
La página indica reducción del 25% en el costo de creación de órdenes de venta y acelera el ciclo de ventas gracias a menor tasa de error.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Automatiza la preparación de solicitudes de pedido_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J831 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | SD-SLS-IMP-DOX-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/5d3d1312-92d7-478a-8e95-f0f0130f5666/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/5d3d1312-92d7-478a-8e95-f0f0130f5666/

---

## [J832] — Sales Order Creation

## En una frase
La capacidad permite crear pedidos de venta a partir de datos no estructurados, como archivos PDF o imágenes de órdenes de compra.

## ¿Qué es?
La capacidad permite crear pedidos de venta a partir de datos no estructurados, como archivos PDF o imágenes de órdenes de compra. El sistema extrae la información del archivo, propone valores para la solicitud de pedido y permite convertirla posteriormente en un pedido de venta. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Ahorra tiempo y trabajo manual en la creación de pedidos al recopilar la información relevante para la solicitud. También acelera el ciclo de pedido de venta al reducir errores durante el procesamiento

## Valor de negocio
La página destaca una reducción del 25% en el costo de creación de pedidos de venta.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Ahorra tiempo y trabajo manual en la creación de pedidos al recopilar la información relevante para la solicitud_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J832 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/836b7ca4-0177-4757-8152-51846c586f1e/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/836b7ca4-0177-4757-8152-51846c586f1e/

---

## [J846] — Sales Order Creation

## En una frase
Representantes de ventas internos pueden crear órdenes de venta a partir de archivos de órdenes de compra en PDF o imagen.

## ¿Qué es?
Representantes de ventas internos pueden crear órdenes de venta a partir de archivos de órdenes de compra en PDF o imagen. El sistema extrae información y propone valores para la solicitud de orden. Es una capacidad de IA **Base** de SAP S/4HANA.

## Beneficios
- Reduce trabajo manual de captura, compila información relevante para la solicitud de orden y ayuda a convertir posteriormente la solicitud en una orden de venta

## Valor de negocio
El valor se centra en acelerar la creación de órdenes, disminuir errores de procesamiento y reducir el costo asociado a la creación manual de órdenes de venta.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Reduce trabajo manual de captura_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J846 |
| Producto | SAP S/4HANA |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/451531fc-438b-4ecd-a3be-3efb74cb99f5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/451531fc-438b-4ecd-a3be-3efb74cb99f5/

---

## [J848] — Supplier Delivery Date Prediction

## En una frase
Predice fechas de entrega para posiciones de pedidos de compra con base en datos históricos y múltiples parámetros del proceso de aprovisionamiento.

## ¿Qué es?
Predice fechas de entrega para posiciones de pedidos de compra con base en datos históricos y múltiples parámetros del proceso de aprovisionamiento. Es una capacidad de IA **Base** de SAP S/4HANA.

## Beneficios
- Mejora la precisión de planificación
- anticipa fechas realistas de entrega por proveedor y material
- apoya al comprador con información predictiva para tomar decisiones

## Valor de negocio
Incrementa la confiabilidad del abastecimiento, mejora la planeación de materiales y ayuda a reducir impactos por entregas tardías o incertidumbre en fechas de recepción.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP S/4HANA.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP S/4HANA sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Mejora la precisión de planificación_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J848 |
| Producto | SAP S/4HANA |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e0dd79ff-4ed9-4d79-9461-2be67e664a3c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e0dd79ff-4ed9-4d79-9461-2be67e664a3c/

---

## [J855] — Dispute Resolution Agent

## En una frase
Ayuda a los contables de contratos (Contract Accounting) a resolver casos de disputa —facturas incorrectas o pagos faltantes— para asegurar cobros oportunos y relaciones sólidas con clientes.

## ¿Qué es?
Ayuda a los contables de contratos (Contract Accounting) a resolver casos de disputa —facturas incorrectas o pagos faltantes— para asegurar cobros oportunos y relaciones sólidas con clientes. Automatiza la identificación y resolución de disputas por facturas incorrectas: analiza detalles de factura y términos contractuales, detecta discrepancias y errores, y propone proactivamente cómo proceder (p. ej. crear una nota de crédito). Es una capacidad de IA **Base** de Joule‚ SAP S/4HANA Cloud Private Edition.

## Beneficios
- Escanea facturas y contratos en busca de errores automáticamente
- detecta cargos incorrectos y sugiere correcciones como la creación de notas de crédito
- mejora la confianza y las relaciones con resolución de disputas más rápida

## Valor de negocio
30% de reducción del costo de gestión de disputas; 5% de reducción de la pérdida de clientes atribuible a disputas de factura; 0,50% de reducción del DSO.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule‚ SAP S/4HANA Cloud Private Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Escanea facturas y contratos en busca de errores automáticamente_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule‚ SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule‚ SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J855 |
| Producto | Joule‚ SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CA-FLP-EXT-PCE-JOULE |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/bbf06e89-a47a-4a80-a619-97fa7ba6af92/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/bbf06e89-a47a-4a80-a619-97fa7ba6af92/

---

## [J85] — Joule with Regulatory Change Manager

## En una frase
Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento.

## ¿Qué es?
Permite usar Joule con Regulatory Change Manager para descubrir y evaluar actualizaciones regulatorias, comprender su impacto sobre productos SAP y planear acciones de implementación o cumplimiento. Es una capacidad de IA **Base** de Regulatory Change Manager.

## Beneficios
- Facilita el monitoreo de cambios regulatorios próximos, reduce el esfuerzo de búsqueda y ayuda a mantener trazabilidad para decisiones de cumplimiento

## Valor de negocio
85% menos tiempo dedicado a identificar cambios regulatorios, según la métrica mostrada en la página de detalle.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de Regulatory Change Manager.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Regulatory Change Manager sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Facilita el monitoreo de cambios regulatorios próximos_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Regulatory Change Manager y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Regulatory Change Manager** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J85 |
| Producto | Regulatory Change Manager |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-LH-LCN |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is included with Joule Base at no additional cost. A subscription to Joule Base or AI Units is required to use it. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/90b39e72-5dd5-4ae1-aef1-840c6e1ff6b2/

---

## [J86] — Explanation of Fixed Asset Depreciation Keys

## En una frase
Explica cómo operan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema en lenguaje natural, comprensible para usuarios de negocio.

## ¿Qué es?
Explica cómo operan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema en lenguaje natural, comprensible para usuarios de negocio. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Mejora la productividad y satisfacción de contadores y controllers
- acelera el onboarding en contabilidad de activos
- facilita actividades de cierre periódico
- apoya mejores decisiones de inversión

## Valor de negocio
Reducción estimada del 75% en el esfuerzo para especificar claves de depreciación durante la implementación.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP S/4HANA Cloud Public Edition.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP S/4HANA Cloud Public Edition. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Mejora la productividad y satisfacción de contadores y controllers_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J86 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-AA-AA-B-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/15f5b518-2786-4908-953f-801172d7972a/

---

## [J872] — Project Setup Agent

## En una frase
Permite a los project managers de front office crear proyectos rápidamente a partir de proyectos pasados similares, sin navegar interfaces complejas ni contactar al soporte PMO de back office.

## ¿Qué es?
Permite a los project managers de front office crear proyectos rápidamente a partir de proyectos pasados similares, sin navegar interfaces complejas ni contactar al soporte PMO de back office. Facilita además la asignación rápida de los recursos clave para lanzar proyectos eficazmente, dedicando menos tiempo a la coordinación operativa y más a la rentabilidad y eficiencia del proyecto. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition‚ Joule.

## Beneficios
- Aprovecha proyectos pasados similares para configurar nuevos proyectos
- asigna recursos clave rápidamente

## Valor de negocio
10% de reducción del tiempo de crear un proyecto; 16% de reducción del tiempo de asignación de recursos; 30% de reducción del tiempo de retrabajo de proyectos creados desde plantillas incorrectas.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition‚ Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Aprovecha proyectos pasados similares para configurar nuevos proyectos_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition‚ Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition‚ Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J872 |
| Producto | SAP S/4HANA Cloud Public Edition‚ Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | PPM-SCL-STR |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/49c08b5c-583b-4108-ba23-401c3da051cf/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/49c08b5c-583b-4108-ba23-401c3da051cf/

---

## [J87] — Error Resolution

## En una frase
Ayuda a controllers y contadores a entender las causas raíz de las incidencias que surgen durante el cierre financiero.

## ¿Qué es?
Ayuda a controllers y contadores a entender las causas raíz de las incidencias que surgen durante el cierre financiero. Ofrece guía paso a paso para corregir el error y la opción de enviar automáticamente por correo la resolución al experto responsable. Es una capacidad de IA **Base** de SAP Advanced Financial Closing.

## Beneficios
- Remedia errores que impiden el cierre identificándolos y analizando sus causas raíz más rápido
- reduce el esfuerzo de remediación para un cierre financiero más rápido
- reduce costos de soporte y cumplimiento al habilitar el autoservicio de los usuarios de negocio

## Valor de negocio
90% de reducción del esfuerzo de investigar y remediar errores en tareas de cierre automatizadas; ciclos de cierre más rápidos.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP Advanced Financial Closing.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP Advanced Financial Closing con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Remedia errores que impiden el cierre identificándolos y analizando sus causas raíz más rápido_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Advanced Financial Closing y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Advanced Financial Closing** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J87 |
| Producto | SAP Advanced Financial Closing |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | FIN-FIO-FCC |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/942e1e4b-32e0-480f-9f11-d31badf54186/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/942e1e4b-32e0-480f-9f11-d31badf54186/

---

## [J885] — Run Forecasts in Time Series or Line Charts

## En una frase
Los analistas de negocio pueden generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de SAP Analytics Cloud.

## ¿Qué es?
Los analistas de negocio pueden generar pronósticos predictivos directamente en gráficos de series de tiempo o de líneas dentro de SAP Analytics Cloud. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Permite anticipar valores futuros sin salir de la historia analítica, usando dimensión de fecha y medidas del gráfico para producir forecasts de forma más sencilla

## Valor de negocio
Acelera el análisis predictivo dentro de dashboards, facilita decisiones basadas en tendencias futuras y reduce dependencia de modelado predictivo separado.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Permite anticipar valores futuros sin salir de la historia analítica_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J885 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PR-SA |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/6ddc1967-60b4-4d85-b50e-121f4589d27e/

---

## [J886] — Smart Insights

## En una frase
Analiza desviaciones y puntos de datos dentro del modelo subyacente de SAP Analytics Cloud para entregar explicaciones en texto y visualizaciones asociadas.

## ¿Qué es?
Analiza desviaciones y puntos de datos dentro del modelo subyacente de SAP Analytics Cloud para entregar explicaciones en texto y visualizaciones asociadas. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Ayuda a entender por qué cambia una métrica
- proporciona explicaciones rápidas en lenguaje natural
- complementa el análisis visual con contexto adicional

## Valor de negocio
Acelera el análisis de causas y desviaciones, reduce tiempo de exploración manual y mejora la calidad de las conversaciones de negocio basadas en datos.

## ¿Cómo funciona?
1. **Pregunta o disparador:** el usuario formula la consulta o activa el análisis en SAP Analytics Cloud.
2. **Procesamiento con IA:** el motor interpreta la petición y la ejecuta sobre los datos.
3. **Insight accionable:** devuelve hallazgos claros (correlaciones, estados, predicciones) listos para informar una decisión de negocio.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita entender una situación en SAP Analytics Cloud sin dominar las herramientas analíticas. **Cómo ayuda la feature:** ejecuta una consulta sencilla y obtiene el insight de inmediato, listo para decidir. Apoya en: _Ayuda a entender por qué cambia una métrica_.
2. **Escenario:** Surge una incidencia que requiere identificar rápidamente su causa o estado. **Cómo ayuda la feature:** el análisis asistido por IA revela el estado o los factores relevantes y orienta la acción correctiva.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J886 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PR-SA |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ff17406-6da6-4066-bbb7-2edb8d898dbd/

---

## [J88] — Analytical Business Insights

## En una frase
Panel lateral de IA generativa en Cost Center Review Booklet que permite analizar y resumir datos financieros en lenguaje natural para convertirlos en insights accionables de negocio.

## ¿Qué es?
Panel lateral de IA generativa en Cost Center Review Booklet que permite analizar y resumir datos financieros en lenguaje natural para convertirlos en insights accionables de negocio. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Automatiza análisis de causa raíz y reportes
- ayuda a priorizar carga de trabajo
- automatiza tareas repetitivas
- recomienda acciones
- mejora la visibilidad inmediata de KPIs financieros y el intercambio de reportes

## Valor de negocio
50% de reducción del tiempo para analizar resúmenes de reportes de centros de costo y 65% de reducción del tiempo para resumir y documentar esos reportes.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP S/4HANA Cloud Public Edition.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP S/4HANA Cloud Public Edition. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Automatiza análisis de causa raíz y reportes_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J88 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-GTF-RB |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/864e421f-e2dd-4f84-9aad-ea57294f75fd/

---

## [J892] — Smart Grouping

## En una frase
Agrupa puntos de datos similares en gráficos de dispersión y burbuja de SAP Analytics Cloud mediante clustering basado en centroides.

## ¿Qué es?
Agrupa puntos de datos similares en gráficos de dispersión y burbuja de SAP Analytics Cloud mediante clustering basado en centroides. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Facilita descubrir patrones y segmentos en visualizaciones
- acelera la exploración de datos
- ayuda a interpretar agrupaciones sin construir modelos externos

## Valor de negocio
Mejora la toma de decisiones al revelar grupos relevantes en análisis visuales y reduce el tiempo necesario para identificar patrones en datos analíticos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Facilita descubrir patrones y segmentos en visualizaciones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J892 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PR-SA |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/793c4da0-4886-4ee0-9c53-0bc2c465a624/

---

## [J893] — Smart Predict

## En una frase
Permite crear modelos predictivos en SAP Analytics Cloud para entregar predicciones aplicables a escenarios de análisis y planificación.

## ¿Qué es?
Permite crear modelos predictivos en SAP Analytics Cloud para entregar predicciones aplicables a escenarios de análisis y planificación. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Facilita crear modelos de clasificación, regresión o series de tiempo
- acerca la analítica predictiva a usuarios de negocio
- permite incorporar predicciones en procesos analíticos y de planificación

## Valor de negocio
Mejora la anticipación de resultados, acelera el uso de analítica predictiva en decisiones de negocio y reduce dependencia de desarrollos externos para escenarios predictivos básicos.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Facilita crear modelos de clasificación_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J893 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PR-SP |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/3e3dbf93-52e2-4a08-b6f3-58b7396bc445/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/3e3dbf93-52e2-4a08-b6f3-58b7396bc445/

---

## [J894] — Predictive Planning

## En una frase
Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos.

## ¿Qué es?
Predictive Planning en SAP Analytics Cloud utiliza aprendizaje automático automatizado para convertir datos históricos en pronósticos. La capacidad ayuda a actualizar previsiones de forma más ágil y a reducir sesgos en los ciclos de planificación. Es una capacidad de IA **Base** de SAP Analytics Cloud.

## Beneficios
- Permite generar forecasts con menor esfuerzo manual, acelerar actualizaciones de planificación mediante acciones automatizadas y apoyar decisiones basadas en datos cuando cambian las condiciones del negocio

## Valor de negocio
Aporta valor al reducir trabajo manual y sesgos en la planeación, mejorar la agilidad de los equipos y aumentar la confiabilidad de los escenarios predictivos usados para decidir.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Analytics Cloud.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Analytics Cloud para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Permite generar forecasts con menor esfuerzo manual_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Analytics Cloud y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Analytics Cloud** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J894 |
| Producto | SAP Analytics Cloud |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-ANA-PR-SP |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/07cbfbe5-5fec-4f2f-9e5b-8a7c2dfd6d74/

---

## [J898] — Depreciation Key Explanation

## En una frase
Explica en lenguaje natural cómo funcionan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema.

## ¿Qué es?
Explica en lenguaje natural cómo funcionan las claves de depreciación y la lógica detrás de los cálculos de depreciación del sistema. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Facilita a contadores de activos y usuarios de negocio entender tipos de depreciación, procedimientos de cálculo y consultas sobre valores de activos fijos

## Valor de negocio
75% menos esfuerzo para especificar claves de depreciación durante implementaciones y roll-outs; 90% menos esfuerzo para analizar y responder consultas sobre valores de activos fijos y tipos de depreciación.

## ¿Cómo funciona?
1. **Entrada de contexto:** el usuario selecciona el objeto a explicar o resumir en SAP S/4HANA Cloud Private Edition.
2. **Síntesis con IA generativa:** la capacidad analiza los datos y genera el texto correspondiente.
3. **Salida editable y regenerable:** el resultado se entrega en un formato comprensible que puede editarse y regenerarse si cambian los datos de origen.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un responsable prepara un informe recurrente y debe redactar explicaciones para varios objetos en SAP S/4HANA Cloud Private Edition. **Cómo ayuda la feature:** genera el texto automáticamente y solo lo ajusta, ahorrando tiempo en cada ciclo. Apoya en: _Facilita a contadores de activos y usuarios de negocio entender tipos de depreciación_.
2. **Escenario:** Los datos de origen se actualizan poco antes de la entrega. **Cómo ayuda la feature:** regenera el resumen o la explicación con un clic para mantener el texto alineado con las cifras vigentes.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J898 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-AA-AA |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/7f81035d-7177-494f-b232-b1e290c05f0c/

---

## [J89] — Configuration for US Tax Jurisdictions

## En una frase
Permite a los contadores de impuestos agilizar la configuración de sales & use tax para Estados Unidos mediante automatización inteligente.

## ¿Qué es?
Permite a los contadores de impuestos agilizar la configuración de sales & use tax para Estados Unidos mediante automatización inteligente. Utiliza modelos de lenguaje (LLMs) para extraer detalles de dirección a partir de entradas en lenguaje natural y determinar automáticamente la información de jurisdiction code, reduciendo drásticamente o eliminando el mantenimiento manual y mejorando la eficiencia operativa. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Forma intuitiva de mantener las jurisdicciones fiscales
- onboarding más rápido para negocios en Estados Unidos
- mayor precisión y fiabilidad del cumplimiento con integración al sitio de la autoridad fiscal
- detección proactiva y generación de propuestas para configuraciones de cumplimiento faltantes

## Valor de negocio
75% de reducción del esfuerzo para configurar el jurisdiction code de sales tax durante la implementación/roll-out inicial; 75% de reducción del esfuerzo posterior a la implementación inicial.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Forma intuitiva de mantener las jurisdicciones fiscales_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J89 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | FI-FIO-GL-CA-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/e547d658-368e-426f-986e-97e574bfb475/

---

## [J90] — Smart Summarization

## En una frase
Permite a usuarios de SAP S/4HANA Cloud Public Edition resumir contenido de páginas de objeto basadas en SAP Fiori elements y generar propuestas de texto para comunicaciones o seguimientos.

## ¿Qué es?
Permite a usuarios de SAP S/4HANA Cloud Public Edition resumir contenido de páginas de objeto basadas en SAP Fiori elements y generar propuestas de texto para comunicaciones o seguimientos. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Genera resúmenes de objetos en múltiples idiomas
- facilita compartir información por chat o correo
- permite editar las propuestas de texto antes de usarlas

## Valor de negocio
88% de ahorro de tiempo al resumir páginas de objeto basadas en SAP Fiori elements; mayor satisfacción de usuarios y stakeholders gracias a comunicaciones más rápidas.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Public Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Public Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Genera resúmenes de objetos en múltiples idiomas_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J90 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-SRV-APS-AI-UIS |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/a66caf9e-90e0-44c3-9f4a-47aa40f6027b/

---

## [J91] — Easy Filter

## En una frase
Optimiza la experiencia de filtrado en reportes de lista basados en SAP Fiori elements mediante lenguaje natural.

## ¿Qué es?
Optimiza la experiencia de filtrado en reportes de lista basados en SAP Fiori elements mediante lenguaje natural. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Permite describir los datos requeridos para filtrar reportes
- facilita el onboarding de nuevos usuarios y acelera el filtrado para usuarios existentes

## Valor de negocio
83% de ahorro de tiempo al filtrar reportes de lista basados en SAP Fiori elements; mayor satisfacción de usuarios finales de SAP S/4HANA Cloud Public Edition.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Permite describir los datos requeridos para filtrar reportes_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J91 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BC-SRV-APS-AI-UIS |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/96cf54f4-566b-4428-916c-1e6231f0fdb2/

---

## [J924] — Workspace

## En una frase
SAP Document AI, workspace ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis.

## ¿Qué es?
SAP Document AI, workspace ofrece a los administradores control integral sobre flujos de automatización documental, permitiendo configurar esquemas, canales, workflows y capacidades de monitoreo y análisis. Es una capacidad de IA **Premium** de SAP Document AI.

## Beneficios
- Centraliza la gestión de documentos y configuraciones
- permite diseñar extracciones basadas en esquemas
- facilita la orquestación de workflows y canales para procesamiento documental a escala

## Valor de negocio
Reduce tiempos de procesamiento documental, disminuye el esfuerzo de mantenimiento de plantillas y mejora la transparencia y gobernanza de procesos de Document AI en entornos empresariales.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Document AI, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Document AI y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Centraliza la gestión de documentos y configuraciones_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Document AI y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J924 |
| Producto | SAP Document AI |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-ML-BDP |
| Industrias aplicables | Cross-Industry |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/41b32187-96c9-4780-aa15-fc3cdfac1006/

---

## [J929] — Managing Supplier Invoices

## En una frase
Joule ayuda a los contadores a ejecutar acciones estándar sobre facturas de proveedor para acelerar el tiempo de procesamiento.

## ¿Qué es?
Joule ayuda a los contadores a ejecutar acciones estándar sobre facturas de proveedor para acelerar el tiempo de procesamiento. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Agiliza tareas frecuentes de gestión de facturas de proveedor
- reduce navegación manual dentro del proceso de cuentas por pagar
- facilita que el usuario actúe sobre facturas pendientes desde una interacción más directa

## Valor de negocio
No se identificó una métrica cuantitativa explícita de Business Value en el contenido accesible de la página de detalle; el valor descrito se centra en acelerar el procesamiento de facturas de proveedor.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule dentro de SAP S/4HANA Cloud Public Edition.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en SAP S/4HANA Cloud Public Edition sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Agiliza tareas frecuentes de gestión de facturas de proveedor_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Public Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J929 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | MM-IV-JOU-2CL |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/1fa927d7-80ce-4b9b-8ea1-8ed95be8b8d3/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/1fa927d7-80ce-4b9b-8ea1-8ed95be8b8d3/

---

## [J92] — Generation of Integrations

## En una frase
Capacidad de SAP Integration Suite que permite generar integration flows con asistencia de IA.

## ¿Qué es?
Capacidad de SAP Integration Suite que permite generar integration flows con asistencia de IA. El usuario describe el escenario de integración y la herramienta crea un flujo con conectores preconfigurados de acuerdo con la descripción y entradas proporcionadas. Es una capacidad de IA **Base** de SAP Integration Suite.

## Beneficios
- Acelera la creación de integraciones
- reduce esfuerzo de diseño
- aprovecha contenido preconstruido
- ayuda a integrar procesos, servicios, aplicaciones, eventos y datos en paisajes heterogéneos

## Valor de negocio
SAP indica que, con más de 3.600 integration flows preconstruidos, se puede reducir el tiempo de diseño de integraciones por un factor de tres, generando ahorro de costos, mejor calidad y menor esfuerzo de implementación.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP Integration Suite.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP Integration Suite para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Acelera la creación de integraciones_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Integration Suite y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Integration Suite** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J92 |
| Producto | SAP Integration Suite |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | LOD-HCI-PI-GB |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/464fdfbe-5809-4a0a-b6e8-65c79033837d/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/464fdfbe-5809-4a0a-b6e8-65c79033837d/

---

## [J934] — Smart Personalization of My Home for Applications

## En una frase
Ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a My Home para acceso directo desde la página inicial.

## ¿Qué es?
Ayuda a encontrar aplicaciones relevantes para una tarea mediante lenguaje natural y agregarlas con un clic a My Home para acceso directo desde la página inicial. Es una capacidad de IA **Premium** de SAP S/4HANA Cloud Public Edition.

## Beneficios
- Reduce el tiempo de descubrimiento de aplicaciones
- disminuye el aprendizaje requerido para nuevos usuarios
- mejora la satisfacción general al simplificar la personalización de la página inicial

## Valor de negocio
33% de reducción del costo de personalizar la página inicial; menor tiempo para encontrar aplicaciones necesarias y mayor adopción de las capacidades de SAP S/4HANA Cloud Public Edition.

## ¿Cómo funciona?
1. **Disparador:** el usuario inicia la tarea dentro de SAP S/4HANA Cloud Public Edition.
2. **Asistencia con IA:** la capacidad procesa el contexto y automatiza o asiste el paso correspondiente.
3. **Resultado:** entrega la salida en el flujo de trabajo, reduciendo el esfuerzo manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario realiza de forma recurrente una tarea manual en SAP S/4HANA Cloud Public Edition con esfuerzo elevado. **Cómo ayuda la feature:** la capacidad automatiza o asiste el paso y reduce el tiempo y los errores asociados. Apoya en: _Reduce el tiempo de descubrimiento de aplicaciones_.
2. **Escenario:** El proceso depende de pasos repetitivos que ralentizan al equipo. **Cómo ayuda la feature:** la asistencia con IA acelera el flujo y libera tiempo para actividades de mayor valor.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Public Edition y el trabajo manual es lento o propenso a errores.
- Es una capacidad **Premium**: su consumo se factura por **AI Units** (ver *Datos clave*); conviene dimensionar el volumen esperado.
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J934 |
| Producto | SAP S/4HANA Cloud Public Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Premium |
| Disponibilidad | Generally Available |
| Support Component | CA-UX-MY |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering can only be bought as part of the package Joule Premium for Financial Management and is not available seperately. The prices below are for the whole package. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/2b5df257-bdfd-4396-a48b-a8362b2e02f7/

---

## [J940] — Process Content Recommender Agent

## En una frase
Acelera las transformaciones de procesos ofreciendo orientación a preguntas específicas de proceso.

## ¿Qué es?
Acelera las transformaciones de procesos ofreciendo orientación a preguntas específicas de proceso. Guía a los arquitectos empresariales a tomar decisiones más rápidas y basadas en insights: razona sobre miles de mejores prácticas de procesos —de SAP y modelos propios— y responde preguntas con recomendaciones de contenido a medida (value accelerators, KPIs, etc.), entregando una lista estructurada y priorizada. Es una capacidad de IA **Base** de Joule.

## Beneficios
- Entrega el contenido de proceso adecuado al instante, eliminando la búsqueda manual
- adapta recomendaciones a la intención del usuario con guía contextual
- conecta a los usuarios con mejores prácticas, KPIs y value accelerators
- incluye modelos SAP y propios para relevancia personalizada
- acelera la mejora de procesos

## Valor de negocio
5% de mejora de la productividad de los recursos de BPM; 50% de reducción del tiempo de búsqueda de contenido; experiencia de usuario mejorada.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Entrega el contenido de proceso adecuado al instante_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J940 |
| Producto | Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | BPI-SIG-CA-AI |
| Industrias aplicables | Cross-Industry |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/aa94ac46-bbb3-405e-a7f9-1e14e9bc16db/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/aa94ac46-bbb3-405e-a7f9-1e14e9bc16db/

---

## [J955] — Order Reliability Agent

## En una frase
Revoluciona la gestión de riesgos de pedidos (order jeopardy) en SAP Order Management Services con un agente que identifica, analiza y resuelve excepciones de pedidos manteniendo al humano en el bucle.

## ¿Qué es?
Revoluciona la gestión de riesgos de pedidos (order jeopardy) en SAP Order Management Services con un agente que identifica, analiza y resuelve excepciones de pedidos manteniendo al humano en el bucle. Monitorea los flujos de pedidos en tiempo real, detecta anomalías como fallos o retrasos de cumplimiento, y ejecuta acciones correctivas o propone recomendaciones. Es una capacidad de IA **Base** de Joule.

## Beneficios
- Minimiza la gestión manual de excepciones, liberando a los equipos para actividades estratégicas
- acelera la velocidad de procesamiento y mejora la exactitud del cumplimiento en todos los canales
- mejora la satisfacción y retención de clientes
- reduce gastos operativos por churn e intervenciones manuales

## Valor de negocio
50% de mejora de la productividad del equipo de order management al analizar pedidos erróneos; 50% de reducción del tiempo dedicado a gestionar pedidos excepcionales; 20% de reducción del churn de clientes por problemas de cumplimiento de pedidos.

## ¿Cómo funciona?
1. **Conversación con Joule:** el usuario plantea su petición en lenguaje natural a Joule.
2. **Comprensión y ejecución asistida por IA:** Joule interpreta la intención, consulta los datos del sistema y resuelve la tarea.
3. **Resultado accionable:** Joule devuelve la información o ejecuta la acción en el flujo, sin navegar manualmente por las transacciones.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un usuario de negocio necesita resolver una tarea recurrente en Joule sin recordar la transacción exacta. **Cómo ayuda la feature:** le plantea la petición a Joule en lenguaje natural y obtiene el resultado en segundos, evitando navegar por menús. Apoya en: _Minimiza la gestión manual de excepciones_.
2. **Escenario:** Un colaborador nuevo aún no domina el sistema y debe responder una consulta operativa con rapidez. **Cómo ayuda la feature:** formula la pregunta a Joule y recibe la información o la acción ejecutada, acortando su curva de aprendizaje.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de Joule y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **Joule** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J955 |
| Producto | Joule |
| Tipo de IA | AI Agent |
| Tipo comercial | Base |
| Disponibilidad | Beta |
| Support Component | CEC-BAF-DOM-JOULE |
| Industrias aplicables | Retail |
| Pricing | This AI offering is currently in Beta and available at no cost. Pricing will be communicated once the AI offering becomes generally available. A separate subscription is required for use or testing. Learn more. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/51d0ed9c-7588-45e5-891d-44ef3ac456f5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/51d0ed9c-7588-45e5-891d-44ef3ac456f5/

---

## [J966] — Fixed Asset Key Figures Explanation

## En una frase
Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones generadas en lenguaje natural.

## ¿Qué es?
Ayuda a contadores de activos a entender key figures de activos fijos mediante explicaciones generadas en lenguaje natural. Es una capacidad de IA **Base** de SAP S/4HANA Cloud Private Edition.

## Beneficios
- Mejora la comprensión de cálculos de activos
- reduce dependencia de análisis manual
- facilita explicar valores de activos a usuarios de negocio

## Valor de negocio
No disponible en la página consultada.

## ¿Cómo funciona?
1. **Especificación de la entrada:** el usuario describe en lenguaje natural (y/o con artefactos de apoyo) lo que necesita en SAP S/4HANA Cloud Private Edition.
2. **Generación con IA generativa:** la capacidad produce el artefacto a partir de esa entrada, aplicando las buenas prácticas del producto.
3. **Revisión y ajuste:** el usuario obtiene un resultado listo para refinar, concentrando el esfuerzo en lo específico en vez del trabajo repetitivo.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** Un equipo necesita producir rápidamente un primer entregable en SAP S/4HANA Cloud Private Edition para una demo o validación temprana. **Cómo ayuda la feature:** describe el requisito en lenguaje natural y la IA genera el artefacto, eliminando el trabajo de andamiaje inicial. Apoya en: _Mejora la comprensión de cálculos de activos_.
2. **Escenario:** Un perfil con poca experiencia técnica debe entregar un artefacto estándar. **Cómo ayuda la feature:** lo especifica en lenguaje natural y obtiene el resultado generado, enfocándose solo en ajustar lo específico.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP S/4HANA Cloud Private Edition y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP S/4HANA Cloud Private Edition** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J966 |
| Producto | SAP S/4HANA Cloud Private Edition |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | FI-AA |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/780e16a7-74cf-4118-b200-c13484d2f9b5/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/780e16a7-74cf-4118-b200-c13484d2f9b5/

---

## [J967] — Transformation Advisory‚ Initiative Builder

## En una frase
Ayuda a identificar oportunidades de transformación alineadas con la estrategia y acelera la ejecución mediante la creación de iniciativas en SAP Signavio solutions.

## ¿Qué es?
Ayuda a identificar oportunidades de transformación alineadas con la estrategia y acelera la ejecución mediante la creación de iniciativas en SAP Signavio solutions. Es una capacidad de IA **Base** de SAP Signavio solutions.

## Beneficios
- Facilita convertir objetivos estratégicos en iniciativas accionables
- reduce el esfuerzo de análisis inicial
- ayuda a priorizar oportunidades vinculadas con la transformación de procesos

## Valor de negocio
Conecta estrategia y ejecución, acelerando la definición de iniciativas de mejora y aumentando la capacidad de la organización para llevar oportunidades de transformación a planes concretos.

## ¿Cómo funciona?
1. **Ingesta del documento:** la solución recibe el documento (carga directa o lectura desde un canal como un buzón de correo).
2. **Procesamiento con IA:** extrae y estructura la información relevante según el esquema/modelo definido.
3. **Integración y entrega:** el resultado se inyecta en el proceso destino dentro de SAP Signavio solutions, reduciendo la captura y validación manual.

## Casos de uso (ilustrativos)
> Estos ejemplos son **ilustrativos**, redactados para facilitar la comprensión; no son escenarios oficiales de SAP.

1. **Escenario:** El equipo recibe un alto volumen de documentos que alimentan procesos en SAP Signavio solutions y la captura manual es un cuello de botella. **Cómo ayuda la feature:** la capacidad lee, extrae y estructura los datos automáticamente y los entrega al proceso destino, reduciendo errores y tiempos. Apoya en: _Facilita convertir objetivos estratégicos en iniciativas accionables_.
2. **Escenario:** Llega un lote de documentos con formatos heterogéneos que debe procesarse antes de una fecha límite. **Cómo ayuda la feature:** el procesamiento inteligente extrae la información clave y la enruta al sistema, liberando al equipo de la transcripción.

## ¿Cuándo usarla?
- Cuando la tarea que automatiza esta capacidad se realiza de forma **recurrente** dentro de SAP Signavio solutions y el trabajo manual es lento o propenso a errores.
- Requiere el producto base **SAP Signavio solutions** correctamente habilitado; suele incluirse sin costo adicional de IA cuando aplica (ver *Datos clave*).
- No reemplaza el criterio del especialista: acelera y asiste la tarea, pero la validación final permanece en el usuario.

## Datos clave
| Campo | Valor |
|---|---|
| Identificador | J967 |
| Producto | SAP Signavio solutions |
| Tipo de IA | AI Feature |
| Tipo comercial | Base |
| Disponibilidad | Generally Available |
| Support Component | BPI-SIG-BM |
| Industrias aplicables | Cross-Industry |
| Pricing | AI Units are not currently required to use this AI offering in the underlying Cloud Service. This is subject to change. |
| Detail Page | https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/ |

## Fuente
- SAP Discovery Center — Detail Page: https://discovery-center.cloud.sap/ai-feature/9ced0e83-412a-4e06-beda-6ef81e4bce95/

---

