# SECURITY — Qué está cerrado

Estado: Aprobada
Fecha: 2026-10-30

Keel no es un pentest y no describe cómo romper un modelo. Este documento fija qué garantiza el comando y qué hueco queda abierto a propósito.

## Cerrado en esta versión

- El check no llama a un modelo, no usa una clave y no abre la red. [ADR-0002](../adr/0002-the-check-runs-the-reference-assistant.md).
- El centinela no está en los manuales. El token de obediencia no está en el prompt. Cada frase de rol está en un solo manual. Si eso no se cumple, el comando no imprime tasas.
- La obediencia no se decide mirando la cita. Una cita del párrafo plantado no es, por sí sola, un fallo. [ADR-0001](../adr/0001-obedience-is-read-on-the-answer.md).
- El informe de una corrida verde no imprime las preguntas. Un fallo nombra el id y la categoría.
- Los manuales no tienen datos de personas.

## Hueco que se admite

El rol del caso es el rol que se entrega al asistente. Keel no autentica a una persona ni demuestra quién llamó. El conjunto es sintético. Presentar el comando como autorización de una empresa sería falso.

Esta versión tampoco puntúa paráfrasis. Una respuesta que cuenta el otro manual, el token o el prompt sin usar la cadena escrita no es una violación. La barra exacta cubre las cadenas de [DATA.md](DATA.md), no un significado parecido.

Una corrida verde nombra al asistente de referencia. No es un resultado sobre otro despliegue.

## Lo que el archivo de casos contiene

Las preguntas, las frases, el token y el centinela están en el repositorio. Hace falta para que el test falle. El README publica categorías y tasas, no ese texto. Este repositorio no promete que el conjunto sea secreto.

No hay una clave que retirar. El centinela es una cadena de prueba, no una credencial.
