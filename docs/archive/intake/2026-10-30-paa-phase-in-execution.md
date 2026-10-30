# PAA como fase de la ejecución del modelo de demanda

**Origen:** conversación del 2026-10-30, piloto GSC de Burrito Blanco (hito `piloto-gsc-bb`, tarea T-105). Los modelos del piloto (T-095) no tienen nada de PAA: `/demand-model` no lanza PAA y la pasada de PAA nunca se compiló en el catálogo real (T-092).

**Palabras del usuario:** «PAA debe ejecutarse como una fase posterior a la creación del modelo usando taxo». Ante la propuesta de Claude (opción A, entrada provisional), el usuario respondió «sí».

## Decisión

1. **PAA es una fase de la ejecución.** La ejecución de un modelo de demanda (`/demand-model`) tiene dos fases:
   - **fase 1:** clasificación con el reglamento de taxo y ensamblado del modelo (lo de hoy);
   - **fase 2, PAA:** sobre el modelo ensamblado de la fase 1.
2. **Clase y semillas con taxo.** La clase del conjunto es la clave del modelo ensamblado. Las semillas siguen la regla vigente del README del motor PAA (núcleo + valores del rasgo que más condiciona las prestaciones). Las semillas salen de la clave del modelo y de las referencias que consulta taxo (`bin/taxo`). Un conjunto por clave distinta, como ya fija D-116.
3. **Reutilización de búsquedas.** Una búsqueda ya capturada con la misma semilla, en otro conjunto, se reutiliza: no se repite. Fundamento: las semillas repetidas devuelven las mismas preguntas en el mismo orden (README del motor PAA, estrategia de semillas).
4. **Búsqueda y clasificación** como hoy: `bin/paa run` y el agente de `/paa-classify` con su reglamento (`classifier/paa.md`), con el catálogo de la clase del modelo.
5. **Entrada provisional en el modelo (opción A).** Lo que propone la clasificación del conjunto (requisitos candidatos, confirmaciones de requisitos y de cuestiones inferidas, aportaciones, pistas de valoración y marcas de comparación) entra en el modelo de esa ejecución:
   - marcado «no compilado» y encolado para el entrenamiento, igual que un bloque generado en ejecución (D-044, D-045);
   - el catálogo compilado no cambia en la ejecución;
   - la importancia de un requisito candidato sin regla es el voto del agente, provisional (D-045).
6. **Nuevo ensamblado.** Después de la fase 2, el modelo se ensambla de nuevo y se vuelve a componer por ámbito (D-155), para que las unidades RI × ámbito incluyan lo de PAA.
7. **El entrenamiento de PAA sigue igual.** La entrada en el catálogo compilado sigue siendo la pasada de PAA con el control (D-178, D-180). La ejecución no decide nada sobre el catálogo: solo usa lo de PAA como provisional.
8. **Si la fase 2 no termina** (un bloqueo de Google, un fallo de la búsqueda o de la clasificación), el modelo de la fase 1 queda como resultado y la ejecución lo informa. La fase 2 se puede reanudar después (`bin/paa run` es reanudable).

## Alternativa descartada (opción B)

Que la ejecución lance `bin/paa compile` y lo de PAA entre en el catálogo compilado si el control acepta la pasada. Se descarta porque cada ficha movería el catálogo compartido y porque el control solo decide sobre el total de los conjuntos de control: un conjunto nuevo sin caso de control no se mide.

## Lo que enmienda

- **D-045** (ejecución, `/demand-model`): la ejecución incluye la fase PAA.
- **D-114** (entrenamiento propio de PAA, independiente del de taxo): PAA sigue con su entrenamiento propio, pero además se ejecuta en cada modelo; su resultado en la ejecución es provisional.
- **D-094 / construction-routes:** PAA es también una fase de la ejecución, no solo una vía de construcción del catálogo.

## Riesgos

- Más búsquedas en Google: una por semilla nueva en cada clave nueva (~8 semillas, ~10 min). Más probabilidad de bloqueo (D-096); los límites de ejecución del README no cambian.
- Coste de tokens del agente de PAA en cada ejecución (orientativo, D-114: 0,7–1,3 M por clase, casi todo caché).
- Lo provisional de PAA queda sin validar en el modelo hasta el entrenamiento.
