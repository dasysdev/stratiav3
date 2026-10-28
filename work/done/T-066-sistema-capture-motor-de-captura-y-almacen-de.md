---
id: T-066
title: Sistema capture: motor de captura y almacén de fichas congeladas comunes
status: hecha
depends:
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Crear el miembro de primer nivel capture/ (estudio T-063, alternativa B aprobada el 2026-10-28): el motor de captura (D-046) y el almacén de fichas congeladas, compartidos por demand-engine, web-audit y la futura auditoría, para que todos evalúen la misma instantánea de una ficha. La captura se comparte; su interpretación sigue en cada sistema. Esta tarea construye y prueba capture/ sin mover datos ni consumidores (eso es la tarea siguiente); demand-engine sigue funcionando como hoy.

## Criterios de aceptación

- [x] Decisión registrada con /docs-update (D-150; enmienda D-046 en dónde vive el motor): glosario, y los enlaces del canon al README del motor (sampling-capture x2, OQ-14, OQ-15, I-18) apuntan a capture/; python3 tools/check_docs.py correcto
- [x] capture/ es miembro del workspace de uv (websockets como dependencia suya) y entra en el contenedor (pyproject raíz, testpaths, PYTHONPATH y COPY del Dockerfile), con README que traslada el del motor y añade el almacén
- [x] src/capture/ contiene los 13 módulos del motor sin cambios de comportamiento, el almacén de fichas (fetch, freeze, read y page_path de pages.py) con capture/var/pages y capture/var/chrome-profile por defecto, y los lectores de página (json_ld, walk, text_lines)
- [x] Regla del almacén: fetch y freeze rechazan un ID que ya existe (la captura nueva lleva otro ID); nunca sustituyen una ficha congelada
- [x] capture/bin/ con la captura de una ficha suelta (desde el host delega en el contenedor, como hoy taxo page fetch)
- [x] Pruebas de capture en verde: las de demand-engine/tests/capture trasladadas, el almacén (incluido el rechazo de un ID existente) y la captura suelta de extremo a extremo con Chrome; las de demand-engine siguen en verde sin cambios

## Resultado

Sistema capture/ construido y probado (motor, almacén con rechazo de ID existente, bin/pages con delegación al contenedor; 34 pruebas, suite 210 en verde) y D-150 registrada con /docs-update

## Notas

- 2026-10-28 capture/ construido: 13 módulos copiados (solo cambian __init__: ROOT y perfil en capture/var/chrome-profile; y el docstring de once), pages.py con la regla del almacén (check_new: ID kebab-case y sin ID.html ni ID.json; fetch comprueba antes de visitar; escritura exclusiva), cli.py y bin/pages (fetch; desde el host comprueba el ID y delega). Pruebas: 34 en capture/tests (3 del motor copiadas + almacén + extremo a extremo con Chrome); suite completa 210 en verde, ninguna omitida. Probado a mano desde el host contra un servidor local en el contenedor: captura, rechazo del ID repetido sin lanzar nada y negativa por robots.txt con evidencia; capture/var limpiado después.
