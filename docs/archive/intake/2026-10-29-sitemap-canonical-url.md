# Descubribilidad: la URL que se busca en los sitemaps es la canónica

Cambio descrito por el usuario en la conversación (2026-10-29, T-084).

Usuario: «el requisito w-consumer/014 debe usar la url canónica».

Al proponerle que se recogiera en el canon, como interpretación adoptada de D-162, respondió: «si».

Lo aplicado en web-audit (requisito w-consumer/014, commit 33ee4cc), que el usuario confirma para el canon:

- La URL que se busca en los sitemaps es la URL canónica que declara la página: link rel=canonical de head o cabecera Link.
- Si la página no declara ninguna, se busca su URL final.
- Si declara varias distintas, la comprobación queda NE.

Contexto: en burritoblanco (rastreo burritoblanco-t083), las fichas auditadas son URL de variante (…-p-2024-964.html) cuya canónica (…-p-2024.html) es la que está en el sitemap.
