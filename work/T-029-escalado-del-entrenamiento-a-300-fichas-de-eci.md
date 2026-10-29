---
id: T-029
title: Escalado del entrenamiento a 300 fichas de ECI
status: bloqueada
depends: T-028, T-030, T-031
milestone: codigo
reason: Aparcada por decisión del usuario (2026-10-29): el entrenamiento masivo espera
created: 2026-10-25
---

## Objetivo

Con el sistema validado en el piloto (T-024 a T-028), capturar las otras 270 fichas de la selección, clasificarlas en dos ejecuciones con agentes de Claude Code y repetir el ciclo de entrenamiento sobre las 300; cierra T-020

## Criterios de aceptación

- [ ] Cambios que pidió el veredicto del piloto aplicados
- [ ] 270 fichas restantes capturadas en una jornada (ritmo B, tope 300, sin desplazamiento) con su resumen por resultado
- [ ] Dos ejecuciones con las 300 fichas, comprobadas y ensambladas, con el consumo de tokens registrado
- [ ] Ciclo bin/train sobre las 300 y el control, pasada de control sin empeorar e informe agregado en training/reports/
- [ ] T-020 con sus criterios marcados y cerrada

## Notas

- 2026-10-26 Veredicto del piloto (T-028): el ciclo funciona de punta a punta sin bloqueos (captura 30/30, clasificación 60/60, induce y compile aceptados por familias, control sin empeorar, informe training/reports/2026-10-26-v4-report.md). Se puede escalar. Antes de hacerlo: (1) coste: 0,75–0,93 M tokens por caso, el 92 % lectura de caché; 300 fichas × 2 ejecuciones ≈ 500 M tokens más 25 M del control; confirmar con el usuario que se mantienen las dos ejecuciones completas (D-045, paso 2) o una completa y otra de muestra, que no está en el canon. (2) Registro de tokens: a mano, un agente por caso, no escala a 600; que train batch usage lea el mapa agente → caso o los transcripts del lote de una vez. (3) Clave inestable por el nombre de la especialización (lijadoras: esp.a-bateria / esp.bateria): que bin/model blocks muestre las especializaciones ya usadas en la clase para reutilizar el id; la inducción sigue en OQ-49. (4) Informe: con 600 modelos, agrupar «Usado sin compilar» y las divergencias por clase. (5) Decisiones pendientes del usuario que conviene tener antes del ciclo de las 300: OQ-51 (medida descriptiva; datos y propuesta en la OQ) e I-20 (rasgos mal etiquetados en bloques generados: precisar DRAFTING.md y avisar en el informe). I-21 e I-22 (precisiones del reglamento) no bloquean. (6) Se mantiene: fase 1 por tipo (la guardia de register evita los duplicados aunque el tipo no sea la clase) y la primera carga sin desplazamiento (las pestañas vacías de ECI solo afectan a hechos de la capa general).
- 2026-10-26 Revisión del ciclo de reglas 4 (2026-10-26): D-055 (crítico por requisito y clase; la medida descriptiva puede ser crítica), D-056 (rasgos abiertos, propuestos y votados por los agentes) y D-057 (hoja más específica, hermana como alias, unidad de exposición). Se aplican en T-030 antes de escalar; OQ-51 (dimensiones de detalle) se revisa con los datos de las 300. Descartado: contar A y B como un solo voto.
- 2026-10-26 Espera también a T-031 (D-060): el catálogo se redacta de nuevo con las reglas de formulación antes de escalar, para no acumular votos sobre cuestiones compuestas.
- 2026-10-26 T-032 (control v6): (1) consumo 2,15 M tokens por caso con el reglamento v3 (× 2,4): 300 fichas × 2 ejecuciones ≈ 1,3 G tokens, no 500 M; medir antes dónde va el contexto (listas de información resolutiva en bin/model blocks, salida 3 veces mayor) y decidir con el usuario. (2) La aplicación de la oferta es inestable (8/14) por I-30 (descuento del boletín, D-074), I-31 (unidad de exposición) e I-34 (variantes): conviene resolverlas antes de escalar. (3) La aceptación de la información resolutiva por dos tiendas no se pudo medir en el control (9/14 de una tienda): medirla aquí. (4) Votos al alza (ver T-032): revisar la deriva en el ciclo de las 300.
- 2026-10-29 Repaso de OQ (2026-10-29): OQ-51 decidida por D-191 (dimensiones de detalle al árbol, sin suelo); la nota 5 queda resuelta. La inducción de especializaciones va en su propia tarea (D-190).
