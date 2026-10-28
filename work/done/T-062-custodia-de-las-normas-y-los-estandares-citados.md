---
id: T-062
title: Custodia de las normas y los estándares citados (leyes, ISO 4217 e ISO 3166)
status: hecha
depends: T-060
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Registrar y congelar en references/ las fuentes normativas que hoy se citan sin custodia: las 8 normas del catálogo de demand-engine (unas 200 citas ley:…@fecha: TRLGDCU, UE-2023/988, UE-1007/2011, UE-1169/2011, CE-767/2009, RD-3423/2000, ES-RD-863/2003, LOCM), que también fundamentan decisiones técnicas (GPSR 19.c en D-144), y los códigos ISO que web-audit tiene pendientes (moneda, país y región; hoy causa de NE).

## Criterios de aceptación

- [x] Tipo law en references (BOE consolidado y EUR-Lex): congela el texto de la versión citada y lo lee por artículo y apartado; robots.txt y condiciones de reutilización comprobados
- [x] Cada cita ley: del catálogo resuelve a su norma y versión congeladas, o la discrepancia queda registrada; la comprobación de citas de demand-engine (T-061) ya no informa de fuentes sin registro
- [x] ISO 4217 e ISO 3166 registradas en references desde una fuente oficial reutilizable, o el motivo por el que no se puede, en web-audit/reference/inventory.md
- [x] Pruebas en verde (bin/run dev test)

## Resultado

Normas (8, BOE y EUR-Lex por Cellar) e ISO 4217/3166-1 en references con lectores (refs law); 108 citas ley: del catálogo pasadas a la versión fijada con pasaje idéntico; discrepancia del RD 863/2003 (8.4 suprimido) en T-064; 176 pruebas en verde

## Notas

- 2026-10-28 Decisiones del usuario (AskUserQuestion): versión de una norma = la fecha con que la fuente oficial nombra el texto (BOE: publicación de la última modificación incluida; EUR-Lex: fecha de la versión consolidada o, en el original, de su publicación en el DO); citas ley: anteriores a la fijada: reescribir el catálogo donde el pasaje no cambió y registrar las demás; ISO 3166-1 desde EU Vocabularies.
- 2026-10-28 references: tipo law (kinds/law.py). BOE por la API de legislación consolidada (texto.xml con la historia de cada bloque; --version da el texto a esa fecha); EUR-Lex por Cellar (publications.europa.eu; eur-lex.europa.eu responde con un desafío AWS WAF), versiones consolidadas por SPARQL, original por su fecha del DO. text.md: ## por artículo y por división, disposición, anexo o fórmula final (cierran el artículo anterior), una línea por párrafo con su marca. Lector: law_reference/law_passage/law_citation (ley:CÓDIGO-art.apartado.letra@versión; código = cite, gana el más largo), law_changes; CLI refs law. robots.txt: BOE permite /datosabiertos/, publications.europa.eu permite /resource/. Reutilización: licencia tipo del BOE (Resolución 27-06-2024, Ley 37/2007); Oficina de Publicaciones CC BY 4.0 / Decisión 2011/833/UE (el aviso legal de EUR-Lex no se pudo leer por el desafío).
- 2026-10-28 8 normas registradas y fijadas en la vigente: TRLGDCU 2026-02-28, LOCM 2022-03-30, RD 3423/2000 2000-12-28, RD 863/2003 2025-11-13, UE 1007/2011 2018-02-15, UE 1169/2011 2025-04-01, UE 2023/988 2026-05-29, CE 767/2009 2018-12-26. Congeladas también, para comparar, las versiones que citaba el catálogo: originales UE (2011-10-18, 2011-11-22, 2023-05-23, 2009-09-01) y RD 863/2003 2003-07-05. Las versiones de las normas se volvieron a congelar el mismo día tras corregir el corte de artículos (anexos y disposiciones quedaban dentro del último artículo): mismas fechas, nada dependía aún de ellas.
- 2026-10-28 Catálogo: 108 citas reescritas a la versión fijada (cat/alimentos, camas-para-mascotas, cojines-decorativos, comida-para-perros, confituras-y-gelatinas, ropa-de-casa, gen.json, hints.json, traits.json, REVIEW.md y la regla 6 de DRAFTING.md), todas con el pasaje idéntico entre la versión citada y la fijada (espacios aparte). Casos: UE-1169/2011@2011-10-25 era la fecha de adopción (DO 2011-11-22): se compara con el original y es igual. CE-767/2009-11.3 solo cambia en el número de la nota al pie ((27) → ( 6 )): mismo texto, reescrita. RD 863/2003@2003-07-04 era la fecha de la disposición (BOE 2003-07-05): bloque, fuente del requisito y apoyo del contenido de fruta (apartado 8.3 del anexo, igual) pasan a 2025-11-13. Las de TRLGDCU, LOCM y RD 3423/2000 ya estaban en la fijada. Modelos reensamblados (pienso-josera-sea-fish, funda-nordica-bordada-401): idénticos salvo la versión de las citas ley:.
- 2026-10-28 Discrepancia registrada (T-064): el RD 1026/2025 (BOE-A-2025-22947, en vigor el 14-06-2026) suprimió el apartado 8.4 del anexo del RD 863/2003 (indicación del contenido total de azúcares). El apoyo de esa aportación en cat.confituras-y-gelatinas/02 queda en ley:ES-RD-863/2003@2003-07-04: bin/model refs da 1 error y check --catalog 1 problema (respaldo fuera de las fuentes del requisito), a propósito, hasta T-064. Sin registro en references: ninguna. Sin versión (ley: 5): pistas y apoyos que se casan por prefijo, por diseño.
- 2026-10-28 ISO: iso-4217 (document; list-one.xml de SIX, agencia de mantenimiento, gratis; robots.txt permite /dam) e iso-3166-1 (nuevo tipo eu-authority: tabla Country de EU Vocabularies, release 20260923-0, CC BY 4.0; 253 códigos alfa-2 no retirados, entre ellos EU, IC, CP y CQ, que ISO reserva excepcionalmente). Lectores currency_codes y country_codes. ISO 3166-2: sin fuente oficial reutilizable y sin requisito que la use; motivo en web-audit/reference/inventory.md. Poner al día los requisitos de web-audit: T-065.
- 2026-10-28 Pruebas: 176 en verde (bin/run dev test); reqs check correcto. Documentación: requirement-blocks 1.32 (versión de las citas de normas = la fijada en references; composición textil @2018-02-15) con /docs-update, check_docs 0 errores; READMEs de references y demand-engine, DRAFTING.md, CLAUDE.md e inventory.md de web-audit al día.
