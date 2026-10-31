# Keel

Keel decide si la respuesta de un asistente interno puede publicarse. Separa una respuesta que cruzó un límite de una pregunta normal que tiene que seguir contestada.

## Language

**Caso**:
Una pregunta, un rol y el resultado que se espera de esa respuesta.
_Avoid_: Payload, ataque, prueba

**Conjunto adversario**:
Los casos cuyo resultado esperado es un bloqueo.
_Avoid_: Suite ofensiva, red team

**Conjunto benigno**:
Los casos cuya respuesta normal tiene que seguir pasando.
_Avoid_: Tráfico real, camino feliz

**Bloqueo**:
La respuesta no hizo lo prohibido en ese caso.
_Avoid_: Error HTTP, rechazo del servidor

**Falso positivo**:
Un caso benigno que quedó marcado como bloqueo.
_Avoid_: Fallo del ataque

**Obediencia**:
El texto de la respuesta hace lo que pedía el párrafo plantado.
_Avoid_: Cita, extracto

**Cita textual**:
El extracto copiado del manual. Puede contener el párrafo plantado y seguir siendo fiel.
_Avoid_: Respuesta, borrador

**Instrucción plantada**:
Un párrafo del manual que pide a la respuesta hacer algo que el manual no debería mandar.
_Avoid_: Jailbreak

**Centinela**:
Una cadena que solo existe en el prompt oculto.
_Avoid_: Secreto de producción, clave

**Límite de rol**:
Una frase que solo está en el manual del otro rol.
_Avoid_: Permiso, identidad

**Barra**:
El valor que el comando exige para terminar bien.
_Avoid_: Umbral estimado, porcentaje de referencia

**Asistente de referencia**:
El asistente determinista que viaja con este control y contra el que corre el check.
_Avoid_: Otro despliegue, modelo hospedado
