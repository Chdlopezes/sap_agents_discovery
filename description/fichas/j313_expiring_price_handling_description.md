# J313 — Expiring Price Handling

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
