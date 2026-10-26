---
id: T-032
title: Tanda de control con los 14 casos de referencia tras T-030 y T-031
status: hecha
depends: T-031
milestone: codigo
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Comprobar que los cambios de canon del 2026-10-26 (D-055 a D-063: crítico y excepciones por requisito y clase, rasgos abiertos, reglas de formulación, información resolutiva) producen los efectos deseados, clasificando los 14 casos de demand-engine/cases con el reglamento v3 y el catálogo redactado de nuevo, y comparando con la v4

## Criterios de aceptación

- [x] Dos ejecuciones (A y B) de los 14 casos con el reglamento v3, comprobadas y ensambladas, con el consumo de tokens registrado
- [x] Informe en training/reports/ comparado con la v4: preguntas compuestas y condiciones internas antes y después, requisitos condicionados nuevos, componentes sin fuente pasados a inferidas, críticos y excepciones por requisito y clase, rasgos propuestos y aprobados, información resolutiva (aportaciones por origen; propuestas, aceptadas, rechazadas y nunca observadas), cobertura, estabilidad A/B y coherencia por requisito
- [x] Lista de efectos no deseados o reglas que no se cumplen, con propuesta, registrada como incidencias o en la tarea

## Resultado

Control v6 (reglamento v3, reglas 6): D-060 y críticos por excepción funcionan, composición 13-14/14; la oferta se vuelve inestable (8/14), hechos sin pregunta 14 → 66, votos al alza y × 2,4 tokens; I-30 a I-39 registradas e informe 2026-10-26-t032-control-report.md

## Notas

- 2026-10-26 Tanda v6 (var/runs/2026-10-26-v6-a y -b, reglamento v3, reglas 6): 28 agentes, 28/28 correctos y ensamblados, sin reintentos ni bloques generados; 60,31 M tokens (A 30,68 M, B 29,62 M; 2,15 M por caso, × 2,4 frente a la v4). Frente a la v4: composición 11+11 → 13+14/14; clave estable 13 → 14/14; aplicación estable 14 → 8/14 (I-30, I-31, I-34 y un fallo del agente en protector); hechos sin pregunta 14 → 66 (cambio 18, diseño y control 24: I-35); coherencia por requisito 11/313 → 46/358 (fuera de muestra; 34 suben); críticos por excepción 0 → 5 por ejecución; D-060 en lo redactado por el clasificador 7 incumplimientos → 0; votos de rasgo 730, 12 distintos del vigente, 0 propuestos; 1222 aportaciones nombradas y 49 nuevas, 0 aceptables (una tienda). Informes: training/reports/2026-10-26-t032-control-report.md y 2026-10-26-t032-train-report.md. Incidencias I-30 a I-39 registradas con propuesta.
- 2026-10-26 Efectos sin incidencia (de código o de seguimiento): (a) los votos de importancia suben en general (misma pregunta, caso y ejecución: 73 suben, 6 bajan de 542; principal 43 → 49 %, crítico 5 → 7 %); no se cambia la regla: lo decide la inducción, pero hay que revisar la deriva en el ciclo siguiente antes de dar por buenas las excepciones nuevas (eci + v6 en seco: 126 excepciones, 15 críticas, 47 cambian). (b) Expectativas de cases/ anteriores al catálogo y canon nuevos: inferida del sofá cama (el mecanismo de apertura ya es cat.sofas-cama/03), inferida de la bordada (busca «algodón»; la de la clase dice «fibras o hilo»), aplicación sin D-066/D-074/D-076; proponer su revisión. (c) train report toma los rasgos y la información resolutiva del catálogo compilado (traits.json, resolving.json), no de las ejecuciones: sin compilar salen a 0; calcularlos desde las ejecuciones, con la formulación, condicionados, inferidas y críticos de esta medición (script de solo lectura en el scratchpad de la sesión). (d) train report con runs vN-a/-b sin --out sobrescribe el informe del ciclo vN; aquí se usó --out.
