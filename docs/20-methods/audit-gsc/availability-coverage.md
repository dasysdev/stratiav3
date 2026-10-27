---
id: audit-gsc-availability-coverage
title: Disponibilidad efectiva y cobertura (procedimiento)
layer: method
status: propuesta
version: 0.2
updated: 2026-10-27
sources: [GSC0 §8, FUND §5.3, FUND §9.4, INTAKE 2026-10-27-ac-applicability-and-reliability]
---

# Disponibilidad efectiva y cobertura

Procedimiento operativo para aplicar la puerta previa definida en el modelo. La definición, la escala binaria y la regla **disponibilidad efectiva = 0 → IR = 0** son canon: ver [disponibilidad efectiva](../../10-model/effective-availability.md).

## Comprobación previa

**Pregunta:** ¿existe al menos un dato, afirmación o relación pertinente que pueda obtenerse y leerse efectivamente bajo el perfil de consumo previsto para el ámbito?

| Resultado | Regla y consecuencia |
|---|---|
| **Disponibilidad efectiva = 1** | Existe algún elemento pertinente utilizable, aunque sea incompleto o general. Continuar con los seis AC. |
| **Disponibilidad efectiva = 0** | Se ha acreditado que no existe información pertinente utilizable, por ausencia o imposibilidad efectiva de obtenerla y leerla bajo el perfil. **IR = 0; no valorar los AC.** |
| **Comprobación inconclusa** | No se ha podido fundamentar el binario. Registrar estado del procedimiento y motivo **sin asignar un tercer valor a la escala 0/1**, sin fijar IR ni fabricar valoraciones de AC. |

> **Estado: propuesta V1.** FUND §5.3 establece que el tratamiento formal de una comprobación inconclusa «requiere especificación sin introducir un tercer valor en su escala binaria». La **comprobación inconclusa** como estado procedimental fuera de la escala es la propuesta de GSC0 para ese pendiente.

**Advertencia:** un recurso recuperado correctamente puede carecer de información pertinente. A la inversa, una irregularidad técnica puede coexistir con información pertinente efectivamente utilizable en otra representación admisible del ámbito.

## Suficiencia de exploración proporcional al juicio

La cobertura necesaria es **proporcional a la afirmación que debe sostenerse**:

- Para **afirmar presencia** basta probar al menos un elemento pertinente efectivamente utilizable. Esto **no implica** que la exploración esté completa para valorar después cada AC.
- Para **afirmar ausencia de información pertinente**, se necesita demostrar una revisión adecuada de las fuentes, representaciones y zonas plausibles del ámbito, incluyendo relaciones y expresiones alternativas razonables.
- Para **afirmar carencia de un componente o variante** en Concreción/Aplicabilidad, se necesita cobertura dirigida a ese componente y conjunto, no únicamente una búsqueda general.
- Para **afirmar coherencia o contradicción**, se necesita inspección adecuada de afirmaciones comparables relevantes; no se puede inferir exactitud a partir de la falta de conflictos encontrados.
- Para **afirmar fiabilidad**, la cobertura y el soporte dependen de la naturaleza y volatilidad del hecho, sin imponer a todos los casos una verificación externa idéntica.

> **Estado: vigente** (FUND §9.4). **La ausencia requiere una prueba de cobertura.** Una búsqueda infructuosa no demuestra que no haya información pertinente. Para fundamentar un resultado negativo hay que documentar qué recursos y representaciones se obtuvieron, qué se inspeccionó, qué candidatos aparecieron, por qué no aportan información pertinente utilizable y qué limitaciones permanecen. La ausencia acreditada no se confunde con la insuficiencia de evidencia.

## Comprobación de cobertura (CO-01 a CO-09)

**CO-01.** Registrar el **universo examinable** definido por ámbito, recurso, perfil y condiciones, sin prometer cobertura de fuentes fuera de ese universo.

**CO-02.** Registrar los recursos obtenidos, representaciones y secciones comerciales inspeccionadas, entidades reconocidas y limitaciones de lectura.

**CO-03.** Verificar que se buscaron las **funciones informativas del RI** y formas de representación pertinentes, no solo una cadena literal o un único atributo.

**CO-04.** Revisar los **componentes de respuesta** y conjuntos afectados: saber qué se buscó para cada componente y dónde podría aparecer.

**CO-05.** Comprobar referencias, vínculos e identificadores que razonablemente pudieran conducir a una pieza decisiva dentro del ámbito autorizado.

**CO-06.** Antes de un juicio negativo, resolver o justificar los candidatos plausiblemente decisivos que permanecen pendientes.

**CO-07.** Distinguir: *no publicado*, *no obtenible/legible bajo el perfil*, *no localizado pese a revisión suficiente* y *no comprobado por cobertura insuficiente*. Son diagnósticos diferentes y no autorizan idénticas conclusiones.

**CO-08.** Conservar prueba de cómo se examinó el contenido y de los límites de esa inspección, especialmente para una ausencia.

**CO-09.** Si una comprobación no alcanza cobertura adecuada para su conclusión, ampliar inspección o declarar la decisión inconclusa/NE según la fase y el juicio afectados.

## Casos límite de obtención

- **Fallo puntual de una herramienta:** no se presume automáticamente ausencia de información; comprobar si se trata de una imposibilidad efectiva del perfil o de un fallo de auditoría no concluyente.
- **Contenido presente solo mediante interacción no admitida:** no es utilizable en ese ámbito/perfil; si no queda ningún otro elemento pertinente y se acredita la condición, disponibilidad efectiva = 0. La conformidad del mecanismo se juzga en el expediente técnico.
- **HTML utilizable y Schema.org defectuoso:** en Web puede existir disponibilidad efectiva 1 por HTML; en Web Schema.org hay que examinar aisladamente si su información pertinente es utilizable. No trasladar automáticamente uno de los resultados al otro.
- **Resultado positivo parcial:** basta para disponibilidad efectiva 1; no basta por sí mismo para otorgar GSC 2 a ningún AC.

## Registro de cobertura

### Cobertura

Alcance de inspección y comprobación que sustenta una conclusión; su exigencia depende de la naturaleza del juicio.

Cada comprobación susceptible de fundamentar una ausencia incluye: objetivo de la búsqueda, representaciones accesibles, regiones/entidades inspeccionadas, métodos semánticos y literales utilizados, alternativas verificadas, resultados, candidatos pendientes, limitaciones y conclusión razonada. **No se exige conservar una transcripción indiscriminada de cada operación irrelevante**, pero sí soporte adecuado para reexaminar la afirmación negativa.

> **Estado: vigente** (FUND §5.3).

Se registran separadamente **el efecto sobre la disponibilidad del RI** y **la incidencia técnica que lo provoca**, cuando esta se ha acreditado (FUND §5.3).

## Relacionado

- [Disponibilidad efectiva (canon)](../../10-model/effective-availability.md).
- [evidence.md](evidence.md) — evidencias de ausencia y de limitación de acceso.
- [calibration.md](calibration.md) — casos C (disponibilidad 0) y D (inconclusa).
