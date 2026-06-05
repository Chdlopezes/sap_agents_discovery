# J778 — Requirement Generation

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
