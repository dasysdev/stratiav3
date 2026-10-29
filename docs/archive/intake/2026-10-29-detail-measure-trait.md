# Rasgo «medida de detalle» para aplicar D-191

Fecha: 2026-10-29. Origen: T-091 (entrenamiento: aplicar D-191 a D-194 y D-201), pregunta de Claude al usuario.

## Situación de partida

D-191 quita el suelo de principal a las dimensiones de detalle (altura de tacón, largo reclinado, longitud de cadena). El código no las distingue: todas tienen el rasgo «medida» (medida descriptiva), y «medida» lleva el suelo. Ejemplo real: `cat.botas/21` «¿Qué altura tiene la plataforma?» es «medida» y no baja de principal, aunque los votos la vean complementaria.

## Pregunta de Claude y respuesta del usuario

Pregunta: «¿Cómo las reconozco?». Opciones:

1. **Rasgo nuevo (recomendada):** «Añado al vocabulario el rasgo «medida-detalle», sin regla fija, como «magnitud» (D-051). Lo votan los agentes y lo fija el índice de rasgos. «medida» conserva su suelo. Reasigno los requisitos de detalle del catálogo por votos, no a mano.»
2. Marca en el requisito: campo «detail: true» que pone quien redacta.

Respuesta del usuario: **Rasgo nuevo**.
