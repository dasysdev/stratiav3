# Entrenamiento propio de PAA

Fecha: 2026-10-27. Tarea T-042 (criterio 1). Update descrito por el usuario en la sesión y recogido en las notas de T-042. La segunda nota sustituye a la primera en lo que respecta al catálogo.

## Decisiones del usuario (primera nota)

- Entrenamiento propio de PAA, independiente del de taxo, con pasadas solo de PAA, «para que se autorefine en reglas, criterios, definición de semillas».
- Alcance de lo que se refina solo: estrategia de semillas, vocabulario de criterios de elección (como el índice de rasgos, D-056) y calibración de reglas.
- Empieza por un piloto de medición de 3-4 clases, sin inducción.
- Clasificación única: sin doble pasada de estabilidad en el piloto.

Límites que propuso Claude, a confirmar en este intake:

- «Calibración de reglas» = ajustar parámetros dentro de las reglas vigentes (por ejemplo, cuántas preguntas o materiales exige la prueba (a)), validado contra los casos de control y con informe.
- Crear o retirar reglas (D-100 a D-113) sigue siendo decisión del usuario.
- Nada se acepta si empeora una métrica frente al control.
- El número de candidatos no es objetivo.
- (Sustituido abajo: «PAA no escribe el catálogo».)

Riesgos: volumen de búsquedas en Google (primer bloqueo probable), sobreajuste a sábanas, dependencia de la versión del catálogo. Coste orientativo por clase: ~10 búsquedas (~5 min) y 0,7-1,3 M tokens (casi todo caché).

## Decisión del usuario (segunda nota): PAA sí modifica el catálogo

Sustituye «sin escribir el catálogo». Palabras del usuario: «aportar nuevos requisitos, aportar reglas para AC de un requisito constituido y confirmar requisitos inferidos». «Si es así no habría conflicto».

Cuatro papeles, todos aditivos o sobre lo que es de PAA:

1. Requisitos nuevos, con id propio y origen «paa».
2. Reglas de AC por requisito: artefacto nuevo (cierra el fondo de OQ-59).
3. Confirmar o revisar las inferidas (D-094; por ejemplo, `inf/01` con los dos polos).
4. Aportaciones aditivas de precisión y de sustento a requisitos existentes.

Las revisiones estructurales de requisitos que nacen de las referencias (separar, sacar, partir) entran a la compilación de taxo: PAA deja un **registro** que lee el próximo entrenamiento de taxo, que las reevalúa al compilar. Un solo escritor por requisito. Cierra el fondo de OQ-58.

## Piloto

- 3-4 clases muy distintas, de las ya ejecutadas, con su conjunto de semillas por la regla vigente.
- Medir qué varía entre clases: semillas, clics, criterios, dudas.
- Cada conjunto, clasificado una vez, con la versión del catálogo anotada.
- Casos de control de PAA: lo esperado de cada clase lo decide el usuario, junto con sábanas.
