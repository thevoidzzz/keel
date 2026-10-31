# CONTEXT — Keel

Estado: Aprobada
Fecha: 2026-10-30

Keel decide si la respuesta de un asistente interno puede publicarse. Una pregunta normal tiene que seguir contestada. La respuesta no puede obedecer una instrucción plantada en un manual, cruzar al manual de otro rol, ni revelar el prompt oculto. El vocabulario está en [GLOSSARY.md](../../GLOSSARY.md).

## Actores

| Actor | Qué hace |
| --- | --- |
| Quien publica | Corre el comando antes de aceptar un cambio y lee las tasas |
| Autor de los casos | Publica los manuales, el prompt y el conjunto en el repositorio. No hay un editor dentro del proceso |
| Evaluación | Corre el conjunto fijo y lee el informe. No es un usuario del asistente |

## Dentro de esta versión

Dos manuales sintéticos en inglés, dos roles, un prompt oculto con un centinela, tres categorías de caso, un conjunto benigno, un asistente de referencia determinista y el comando que imprime las tasas. El diseño se escribe en español. [ADR-0004](../adr/0004-public-manuals-are-english.md).

## Fuera

Servidor HTTP, pantalla, identidad, Docker y AWS. Un cliente que apunte a otro despliegue queda para después: esa corrida se fecha y no es el check. El detalle está en [ARCHITECTURE.md](ARCHITECTURE.md).

## Sistemas externos

Ninguno en el check. El asistente es un puerto. Esta versión lo implementa el asistente de referencia, sin red y sin clave. [ADR-0002](../adr/0002-the-check-runs-the-reference-assistant.md).
