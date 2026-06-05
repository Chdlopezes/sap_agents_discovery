# J28 — Goods Receipt Processing

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
