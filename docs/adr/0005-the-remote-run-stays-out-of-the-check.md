# ADR-0005: La corrida contra otro proceso no entra al check

Estado: Accepted
Fecha: 2026-11-09

## Context

El puerto ya acepta otro asistente, y hasta ahora no había cliente. Una corrida contra un proceso vivo tiene que poder fecharse. Meterla en el check lo ataría a la red y a un nombre que no es el de este producto.

## Decision

`python -m keel` sigue con el asistente de referencia. `python -m keel.remote` lee `KEEL_ASSISTANT_URL`, hace `POST /v1/answers` con `question` y `role`, y toma `answer` y `citations[].excerpt`. El informe nombra esa URL e imprime `ran_on`. No envía una clave. Si el proceso no contesta, o no devuelve un texto, el comando termina sin una tasa. Esa corrida no sustituye las tasas del README.

## Alternatives

**Hacer que el check use la URL cuando exista.** Descartado: un entorno con la variable puesta cambiaría la barra del merge.

**Clonar aquí el proceso que se quiere vigilar.** Descartado: acopla los releases y mete en este repositorio un nombre ajeno.

## Consequences

Una tasa de esta corrida se pega en el README solo después de que el comando la imprima, con la fecha. El check sigue sin red y sin clave.
