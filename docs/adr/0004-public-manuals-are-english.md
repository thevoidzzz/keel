# ADR-0004: Los manuales públicos están en inglés

Estado: Accepted
Fecha: 2026-10-30

## Context

Lo que un extraño lee tiene que poder evaluarlo sin depender de un idioma de trabajo. Mezclar idiomas en la primera corrida mediría a la vez la regla y la comprensión del texto.

## Decision

Lo que un extraño lee está en inglés: los manuales, el prompt, los casos, el README, los mensajes del comando, los tests y los commits. Lo que fija el diseño está en español: la arquitectura, el glosario y estos ADR.

El conjunto no mezcla idiomas. La comparación de las señales es la cadena exacta, así que una traducción no es la misma señal.

## Alternatives

**Manuales y casos en español.** Descartado para esta versión: la primera tasa mediría la regla y el idioma a la vez.

**Traducir también la arquitectura.** Descartado: el diseño se discute en español, y volver a redactarlo no cambia el comportamiento.

## Trade-offs

Se gana una línea de base explicable. Se paga que un lector de manuales en español no es el usuario de esta versión.

## Consequences

Las cadenas que la regla busca quedan en inglés, con las mayúsculas publicadas. Una pregunta en español, si entra, es otro conjunto y otra corrida. Hasta esa corrida, los casos publicados son inglés.
