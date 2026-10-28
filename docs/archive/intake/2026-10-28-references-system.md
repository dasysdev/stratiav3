# Sistema references: custodia común de las fuentes externas

Decisión del usuario del 2026-10-28 (reorganización de las referencias, opción A), recogida en la tarea T-059 y depositada el mismo día.

## Decisión

Las fuentes externas congeladas por versión pasan a un sistema propio de primer nivel, `references/`: una custodia común (registro `references/sources.json`, con `uses` = los sistemas que usan cada fuente; versiones congeladas fuera de git y desechables en `references/var/`; una sola versión fijada por fuente en `pins.json`; diff) y lectores por formato.

Las fuentes se comparten; su interpretación sigue en cada sistema: el catálogo de bloques y el material de taxonomía, en demand-engine; las fichas de fuente y los requisitos técnicos (la referencia técnica), en `web-audit/reference/`.

Enmienda D-133 (que ponía las fuentes congeladas en `web-audit/reference/`) y la regla 4 de «Fuentes de los requisitos técnicos» de evaluation-scopes.

## Fases

- T-059: construir y probar `references/`, sin mover datos ni consumidores.
- T-060: corte (mover las fuentes congeladas y repuntar demand-engine y web-audit).
- T-061: propiedades de Google Search legibles por demand-engine.
