# Resolución de las incidencias abiertas (I-11, I-13, I-15, I-17, I-18, I-23, I-25, I-29)

*Decisiones del usuario en la conversación del 2026-10-26 (sesión de T-034), transcritas para su trazabilidad.*

## Contexto

Palabras del usuario: «ayudame a solucionar todas las incidencias». Claude presentó cada incidencia con opciones y una recomendación. En I-11, I-13 e I-15 el usuario pidió más contexto («no se a que se refiere», «necesito mas contexto para entender», «no tengo suficnete contexto para decidir»), y Claude volvió a presentarlas explicadas.

En I-25, Claude dijo primero que «hallazgo» «no coincide con nada del canon». Antes de aplicarlo comprobó que el glosario ya define «hallazgo» en la auditoría, lo comunicó al usuario y le pidió que volviera a elegir.

## Decisiones

| Incidencia | Pregunta | Opción elegida | Descartadas |
|---|---|---|---|
| I-11 | «¿cambio el texto de la regla para que «vigente» incluya lo que decides en los updates, como ya se hace?» | «Cambiar el texto (Recomendado)»: «La regla pasa a decir lo que ya se hace. Ningún módulo cambia de estado.» | «Dejarlo» |
| I-13 | «¿corrijo los dos ejemplos (polar con solo sus preguntas propias; apoyo de la tapicería de piel escrito)?» | «Corregir los dos (Recomendado)»: «Cambia el texto de los ejemplos; las conclusiones (polar y piel son especializaciones) se mantienen.» | «Dejarlos» |
| I-15 | «¿corrijo el dato de warmth-level en el caso de las sábanas?» | «Corregir el dato (Recomendado)»: «Se añaden las otras dos categorías que lo tienen; el resultado del caso no cambia.» | «Dejarlo» |
| I-17 | «¿cierro la incidencia con la salvaguarda de cobertura que ya valida el entrenamiento?» | «Cerrar con la salvaguarda (Recomendado)»: «El efecto sobre D-030 se mide en la validación automática: no se acepta una relevancia que deje hechos declarados sin pregunta (D-050).» | «Comprobación de base explícita» |
| I-18 | «¿actualizo el método del MPIR para que renderizar con Chrome real sea el procedimiento por defecto?» | «Actualizarlo (Recomendado)»: «sampling-capture dice que se renderiza siempre, con el motivo de los bloqueos, como hace el motor que aprobaste.» | «Dejarlo» |
| I-23 | «¿cuentan los mensajes comunes de la tienda («envío gratis desde 49 €») como información de la oferta?» | «Sí, si fijan una condición comprobable (Recomendado)»: «Un importe, un plazo o un coste que vale para esta oferta cuenta en la pregunta que responde; las frases genéricas no cuentan.» | «No, nunca» |
| I-25 (1.ª) | «¿cómo distinguimos los dos sentidos de «aportación»?» | «Renombrar el del MPIR» | «Siempre con su adjetivo (Recomendado)» |
| I-25 (2.ª) | «¿qué nombre damos a lo que el MPIR llamaba «aportación» (confirmación, ampliación, profundización, diferenciación, discrepancia)?» | «Hallazgo (Recomendado)» | «Resultado del contraste», «Efecto sobre el modelo» |
| I-25 (3.ª) | «I-25: «hallazgo» ya es un término de la auditoría («interpretación fundada de una suficiencia, limitación, discrepancia o ausencia»). ¿Qué nombre damos a lo que el MPIR llamaba «aportación»?» | «Siempre con su adjetivo»: «No se renombra: «aportación resolutiva» y «aportación al modelo de demanda».» | «Resultado del contraste (Recomendado)», «Efecto sobre el modelo», «Hallazgo igualmente» |
| I-29 | «¿cuentan las opiniones sobre la tienda (reseñas de Google o Tripadvisor del comercio)?» | «Solo las del producto u oferta (Recomendado)»: «Las de la tienda no responden gen/15 ni activan gen.opiniones.» | «También las de la tienda» |

## Datos que Claude comprobó al presentarlas

- **I-13.** La tapicería de piel tiene apoyo en las referencias: el atributo `material` de Sofás en Shopify tiene los valores «Piel» y «Cuero», y `SOFA.upholstery.fabric_type` de Amazon tiene «Cuero».
- **I-13.** El polar trae bolitas, electricidad estática y pérdida de pelo. El gramaje y la transpirabilidad ya los pregunta la base de las sábanas, y el abrigo lo trae «uso invernal».
- **I-15.** En Shopify v2026-08, `warmth-level` también lo tienen Colchas y edredones y Cubrecolchones, que no son componentes del caso.
