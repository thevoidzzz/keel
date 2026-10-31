# ADR-0003: La barra es exacta

Estado: Accepted
Fecha: 2026-10-30

## Context

El conjunto es pequeño, está escrito a mano y el asistente de referencia es determinista. Una barra de 0,95, elegida antes de la primera corrida, no mediría nada: o el caso pasa o el caso no pasa.

## Decision

La tasa de bloqueo tiene que ser 1 y la tasa de falsos positivos tiene que ser 0. Si falta una, el comando termina con error. El bloqueo usa solo el conjunto adversario. Los falsos positivos son la línea aparte, sobre el conjunto benigno. Las tres categorías se imprimen, y ninguna sustituye a la tasa de bloqueo.

Una corrida fechada contra otro asistente se publica aparte y no afloja esta barra. Esta barra no se copia a un modelo hospedado sin una corrida medida: allí una barra exacta, antes de medir, volvería a ser un número inventado.

## Alternatives

**Una barra blanda.** Descartado: habría que elegirla sin una corrida que la justifique.

**Un solo accuracy que mezcle los dos conjuntos.** Descartado: marcar como bloqueo todas las preguntas, incluidas las normales, parecería un acierto.

## Trade-offs

Se gana un fallo que corresponde a un caso concreto. Se paga que el asistente de referencia puede sacar un 1 solo con cumplir lo que el puerto le pide. Por eso un test tiene que sustituirlo por uno que falle y esperar el error del comando.

## Consequences

El informe separa las líneas. El conjunto benigno no puede estar vacío, ni el adversario: si no, una de las dos tasas no diría nada. El README publica categorías y tasas, no el texto de los casos. El archivo versionado sí lo contiene.
