# Repaso de las incidencias abiertas (2026-10-29)

Origen: conversación del 2026-10-29. El usuario pidió «resolvamos incidencias». Claude comprobó cada incidencia abierta contra el código y el catálogo y presentó una recomendación por incidencia. El usuario contestó «ok» a todas.

## Ya implantadas en el código: el canon lo recoge

- **I-40.** Los 490 requisitos del catálogo (`gen.json` y `cat/*.json`) tienen `resolving_info`. Se quita «aún no se registra en el catálogo» de demand-model. La descripción sigue sin implantar (3 de 490 requisitos la tienen).
- **I-42.** Se acepta la propuesta: el comienzo de la etiqueta encaja solo hasta un separador propio de cada clase de fuente. En una ley, el guion y el punto (artículo y apartado) y la arroba (fecha). En un atributo o una propiedad, el igual (valor) y la arroba. Es lo implantado en `demand-engine/src/demand_engine/demand/hints.py` (`cites`).
- **I-44.** Se acepta la propuesta: la búsqueda de duplicadas se hace también sobre lo que llega a cada requisito (misma propiedad y mismo AC por llaves distintas), como aviso que resuelve un revisor, además de la búsqueda por destino. Es lo implantado en `hints.py` (`check`).

## Decisiones

| Incidencia | Decisión |
|---|---|
| **I-41** · GTIN inválido | Se acepta la propuesta. La «sintaxis» de D-122 es la del marcado (serialización y vocabulario). Las reglas internas de un valor, como el dígito de control, son estructura del dato y cuentan en Fiabilidad. Si un perfil exige un GTIN válido, ese requisito técnico se evalúa también en el expediente técnico (hoy `ws-vocabulary/006`, del nivel de vocabulario). Los dos expedientes son independientes y en ninguno se cuenta dos veces. |
| **I-43** · `para` con un solo valor | Se acepta la propuesta: `para` admite una lista de valores de una misma llave (varias fuentes o varios tipos). La pista se escribe una vez y la búsqueda sigue siendo por etiquetas exactas. |
| **I-45** · Pistas de tipo en la capa general | Se acepta la propuesta: el origen «marco» se admite en las pistas dirigidas a un requisito de la capa general, que es parte del marco (D-045). Precisa la interpretación de D-136. |
| **I-46** · «Criterio, no lista» | Se acepta la propuesta: la comprobación automática cubre la forma (seis campos, destino, longitud). Lo de «criterio, no lista» lo juzga un agente revisor en el mismo paso que escribe las pistas, sin aprobación del usuario (D-136). |
| **I-47** · GS1 Web Vocabulary | Se adopta la alternativa: las dos fuentes quedan sin ficha hasta que un perfil las necesite. No se añade la clase «vocabulario complementario». Motivo: ninguna de las 45 fichas congeladas usa términos `gs1:`. |
| **I-50** · «Reformular» en PAA | Se acepta la propuesta: «reformular» se añade a las acciones de revisión de D-115, con el mismo tratamiento que las demás. PAA la deja y taxo la reevalúa al compilar (D-179). |
| **I-51** · Capa de clases internas | Se acepta la propuesta: la capa de clases internas queda marcada como superada por D-033 en product-taxonomy y data-model-governance, y se retira de ellos lo que ya no rige. |

## Código

Los cambios de código de I-43 (`para` con lista) y de I-46 (agente revisor) entran en la tarea T-089.
