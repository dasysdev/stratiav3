# Ámbitos pertinentes: un modelo de demanda y una ficha por ámbito

Decisión del usuario del 2026-10-28, tomada en la sesión de T-056 antes de implantar nada, y recogida por Claude el mismo día. Solo documentación.

## Pregunta del usuario

«Hemos diseñado que cada ámbito tiene sus requisitos aplicables y posiblemente sus pistas de valoración. 1. Analiza esto críticamente. Si realmente es así. 2. ¿Cómo debería abordarse esto? ¿El modelo es uno y lo que cambia es una ficha de aplicabilidad?»

## Análisis de Claude

- **La demanda no depende del ámbito.** La pregunta, su importancia, su información resolutiva y sus pistas son del RI, no de la interfaz. El modelo es uno.
- **Lo que cambia por ámbito es la función de la interfaz.** De los motivos posibles para que un RI no corresponda a un ámbito, la falta de una propiedad o un campo en su vocabulario no sirve (casi nunca es absoluta, y viola la independencia de un campo o formato y la invariante 14); la entidad sirve en parte; la función del ámbito sí, fundamentada.
- **En la V1** (Web y Web Schema.org), Web no tiene excepciones (es el recurso completo) y Web Schema.org, previsiblemente ninguna o casi: todas las entidades de la capa general tienen tipo en Schema.org. Donde la función limita de verdad es en Catálogos distribuidos, aplazado.
- **Las pistas no cambian por ámbito.** Lo que cambia es dónde y cómo aparece el dato: localización, no valoración.
- **D-145 mezcla dos papeles** de una propiedad recomendada por Google: prueba de demanda (sin ámbito, como los PTD de Amazon) y localizador en el marcado (propio de Web Schema.org).

Alternativas comparadas: A, un campo de ámbitos en cada RI del catálogo; B, un modelo y una ficha por ámbito; C, sin aplicabilidad (todo pertinente en todo ámbito). Claude recomendó B.

## Propuestas de Claude

1. **Alternativa B.** El modelo de demanda es uno: preguntas, importancia, información resolutiva y pistas no dependen del ámbito. Cada ámbito tiene una **ficha** propia, versionada, con dos partes:
   - **Pertinencia:** por defecto, todo RI del modelo es pertinente en el ámbito. Las excepciones son NA fundamentados en la función del ámbito, formulados como reglas (por entidad o componente), no RI a RI. La falta de una propiedad o un campo en el vocabulario del ámbito no es motivo. Web no tiene excepciones.
   - **Localización:** el vocabulario del ámbito (por ejemplo, las propiedades de Schema.org, citadas `fuente:Tipo.propiedad@versión`) relacionado con las aportaciones de la información resolutiva. Llega al auditor como expresiones ilustrativas del perfil del RI: orienta, no cierra la búsqueda ni decide la pertinencia.
   - La auditoría compone modelo × ficha para obtener las unidades RI × ámbito y registra la versión de la ficha.
   - Las pistas de valoración siguen sin ámbito.
2. **Precisar D-145.** Una propiedad que un consumidor del perfil de Web Schema.org recomienda sin exigir tiene dos papeles separados: **apoyo de demanda** (origen «referencias», sin ámbito, como los PTD de Amazon, D-052) y **localizador** en la ficha de Web Schema.org. Desaparece «apoyo del modelo para ese ámbito».
3. **La no pertinencia, solo a nivel de RI** (la unidad es RI × ámbito); no hay aportaciones no exigibles por ámbito.

Con esto se cierra OQ-76: vía (referencias como apoyo y ficha de ámbito), mapeo (propiedad → requisito o aportación, o candidato si ninguno la cubre), ámbito pertinente (ficha, por excepción) y versión (citas con `@versión` a la versión fijada compartida en references, comprobadas con `bin/model refs`). La implantación en demand-engine es T-056.

## Respuesta del usuario

«si como dices»
