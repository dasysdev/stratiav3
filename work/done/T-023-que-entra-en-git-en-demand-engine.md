---
id: T-023
title: Qué entra en git en demand-engine
status: hecha
depends:
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Versionar lo que gobierna el sistema (código, reglamento, casos, definición de los estudios del MPIR) y los resultados del entrenamiento (catálogo compilado, reglas e informes de cada ciclo); dejar en var/, desechable y sin copia, la salida de la ejecución (runs), el estado de la máquina, los datos de terceros, lo regenerable; los secretos, fuera. Git no es una copia de seguridad

## Criterios de aceptación

- [x] runs/ movido a var/runs/ (código, reglamento, skill y cola al día); catalog/rules/importance.candidate.json ignorado; regla refs/ retirada; .env.example con los nombres de las variables
- [x] Resultados del entrenamiento en git: catálogo compilado (cat/, runtime/, traits.json, empty.json, skeleton.json), rules/importance.json (con runs y accepted) e informes agregados en demand-engine/training/reports/ (train report escribe ahí por defecto)
- [x] Sin registro de cambios de las referencias (pins.json en var/refs/): las versiones usadas quedan en las reglas del entrenamiento (refs) y en cada modelo (engine.refs)
- [x] MPIR: ficha del referente e inventario (qué y por qué) versionados; comprobaciones, bloqueos, estado de cada recurso, instantáneas y log en var/mpir/
- [x] Los enlaces de docs/ a informes apuntan a training/reports/; check_docs sin errores
- [x] skeleton-0.json borrado; decidido qué hacer con catalog-review y REVIEW.md
- [x] var/ documentado como desechable y sin copia: se regenera (refs fetch, taxo page fetch, mpir capture)
- [x] CLAUDE.md y README de demand-engine con la regla de qué entra en git

## Resultado

Qué entra en git en demand-engine: lo que gobierna y los resultados del entrenamiento (catálogo, reglas con ejecuciones y versiones de las referencias, training/reports/, studies/ del MPIR); var/ desechable (runs, refs con pins.json, pages, corpus, cola); cada modelo guarda engine.refs; 60 pruebas en verde

## Notas

- 2026-10-25 Criterio (usuario, 2026-10-25): runs/ es salida del sistema y no va a git. En git, lo que gobierna la ejecución, incluido el catálogo compilado por el entrenamiento y catalog/runtime/ (recomendado: la ejecución siguiente lo reutiliza). La cola (var/queue.jsonl) se queda en var/ porque apunta a runs/. Pendiente del usuario: retirar o no catalog-review y REVIEW.md, y el destino de la copia de seguridad.
- 2026-10-25 Decisión del usuario (2026-10-25): de var/ no se guarda nada; es desechable. Se retira la copia de seguridad y la pregunta por su destino. Pendiente: qué hacer con runs/ (fuera de git; ¿pasa a var/ con el mismo trato?).
- 2026-10-25 Decisiones del usuario (2026-10-25): runs/ pasa a var/runs/ («ok»); «git no es un backup»; «los resultados del entrenamiento sí deben ir a git» → catálogo compilado, reglas publicadas con su procedencia y métricas, e informes agregados de cada ciclo en training/reports/. Los informes de baseline, v1 y v2 se tratan como informes de ciclo (calibración del clasificador).
- 2026-10-25 Implementada a petición del usuario («implementalo») sin esperar a T-003: nada de esto exige adoptar git y no se hace ningún commit. catalog-review y REVIEW.md: se conserva la herramienta (no se borra código sin aprobación) y REVIEW.md se trata como salida (ignorado).
- 2026-10-25 Decisión del usuario (2026-10-25): «ya no hace falta llevar ningún tipo de registro sobre cambios en las refs. Solo necesitamos saber qué versión de ref se ha usado para el entrenamiento y para generar el modelo de demanda». refs.lock.json retirado (pins.json vuelve a var/refs/); train induce/compile guardan refs en las reglas (rellenado en las reglas 3 publicadas con las versiones fijadas, las únicas descargadas) y model assemble guarda engine.refs en cada modelo.
