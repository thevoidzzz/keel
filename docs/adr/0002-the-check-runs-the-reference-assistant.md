# ADR-0002: El check corre contra el asistente de referencia

Estado: Accepted
Fecha: 2026-10-30

## Context

El control tiene que poder fallar en CI sin red y sin clave. Si el check clonara otro proyecto, o llamara a un despliegue vivo, un fallo ajeno pararía este repositorio y metería aquí un nombre que no es el de este producto.

## Decision

El asistente es un puerto: entran la pregunta y el rol, y salen la respuesta y las citas. El check enchufa el asistente de referencia que vive en este repositorio. Es determinista, no llama a un modelo y no abre la red. El informe nombra a ese asistente junto a las tasas.

Una corrida contra otro despliegue se fecha, nombra a ese otro asistente y no sustituye al de referencia en el check. Esta versión no incluye el cliente de esa corrida.

Un test puede sustituir el puerto por un asistente que cruza el rol, escribe el token en la respuesta o copia el prompt. El comando termina con error. Esa sustitución no es un modo del producto.

## Alternatives

**Llamar a un modelo hospedado en cada pull request.** Descartado: el check fallaría por una clave ausente o por una factura, no por una respuesta que cruzó el rol.

**Hacer que el CI clone el asistente que se quiere vigilar.** Descartado: acopla los releases y nombra, dentro de este repositorio, un producto distinto.

## Trade-offs

Se gana un check repetible. Se paga que una tasa verde no es evidencia sobre otro despliegue. El README tiene que decir qué asistente produjo el número.

## Consequences

El job de tests no instala un SDK de modelo y no lee una clave. Ningún archivo versionado contiene una credencial. El asistente de referencia ignora el wording de la pregunta y devuelve el manual del rol. Hasta que exista el cliente HTTP, no hay una corrida fechada que ejecutar.
