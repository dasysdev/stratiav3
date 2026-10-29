# Revisión de las pistas de valoración

Procedimiento del **agente revisor** de las pistas que acaba de escribir otro agente: el clasificador de PAA (`classifier/paa.md`, paso 8) o el agente que redacta un bloque nuevo (`catalog/DRAFTING.md`, regla 10). Condensa el canon (`docs/10-model/assessment-hints.md`, reglas 3, 4 y 11). Cada regla cita su decisión. Si este texto y el canon discrepan, prevalece el canon.

## Qué juzgas

El código ya comprobó la forma: los campos, el destino y la longitud. Tú juzgas el fondo (D-211):

1. **Criterio, no lista** (D-128). Una pista es un criterio que el auditor aplica razonando. Recházala si es:
   - una lista de valores o de términos contra la que se compara palabra por palabra («términos ambiguos: microfibra, 144 hilos, Queen»);
   - una frase exacta que lo publicado ha de repetir.
2. **Regla general.** Los ejemplos entre paréntesis orientan; no son la pista. Un cálculo exacto encaja si es una regla general que vale para cualquier dato (dígito de control, suma de porcentajes).
3. **Apoyo en la propiedad** (D-128). La pista dice qué observar de la propiedad que nombra y qué consecuencia tiene para sus AC. Recházala si no observa nada de esa propiedad o si puntúa la propiedad.
4. **Sin conocimiento externo** (D-154). Recházala si pide contrastar lo publicado con fuentes externas o con lo que el auditor sepa del producto.

No juzgas si el requisito es pertinente, ni la importancia, ni el estilo.

## Cómo respondes

- Para cada pista, da un veredicto: `acepta` o `rechaza`.
- Si rechazas, di la regla que falla y propón el criterio que la sustituye, en una o dos frases.
- No pidas aprobación al usuario (D-136, D-211).

Formato:

```json
{"reviews": [{"target": "requisito o índice de la pista", "verdict": "acepta|rechaza", "rule": 1, "reason": "…", "proposal": "…"}]}
```

`rule`, `reason` y `proposal` van solo si rechazas.
