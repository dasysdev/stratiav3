# Sistema capture: motor de captura y almacén común de fichas congeladas

Decisión del usuario del 2026-10-28 (estudio T-063, alternativa B), recogida en la tarea T-066 y depositada el mismo día.

## Decisión

El motor de captura (D-046) y el almacén de fichas congeladas pasan de demand-engine a un sistema propio de primer nivel, `capture/`, compartido por demand-engine, web-audit y la futura auditoría, para que todos evalúen la misma instantánea de una ficha.

La captura se comparte; su interpretación sigue en cada sistema.

Regla del almacén: `fetch` y `freeze` rechazan un ID que ya tiene ficha; la captura nueva lleva otro ID. Nunca se sustituye una ficha congelada.

Enmienda D-046 en dónde vive el motor.

## Alternativas descartadas

- A: el motor y las fichas siguen en demand-engine y web-audit depende de demand-engine.
- C: solo el motor pasa a un sistema común; cada sistema guarda sus capturas (capturas duplicadas por sistema).
- D: dentro de references (otra ejecución, otra naturaleza, sin versión fijada).

## Fases

- T-066: construir y probar `capture/`, sin mover datos ni consumidores.
- T-067: corte (mover las fichas congeladas y el perfil de Chrome sin volver a capturar ni alterar ninguna ficha, y repuntar los consumidores).
