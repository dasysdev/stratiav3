// Extrae texto con extractores de referencia: turndown (por defecto y con gfm), readability(+turndown), html-to-text.
const fs = require('fs');
const { JSDOM } = require('jsdom');
const TurndownService = require('turndown');
const { gfm } = require('turndown-plugin-gfm');
const { Readability } = require('@mozilla/readability');
const { convert } = require('html-to-text');
const [file, outdir] = process.argv.slice(2);
const html = fs.readFileSync(file, 'utf8');
const out = {};
// Turndown por defecto sobre el documento entero (como describe searchVIU para Claude Code).
out['turndown'] = new TurndownService().turndown(html);
const tg = new TurndownService(); tg.use(gfm); out['turndown-gfm'] = tg.turndown(html);
// Turndown sobre el body tras quitar script/style (variante habitual).
{ const d = new JSDOM(html).window.document; d.querySelectorAll('script,style').forEach(n => n.remove());
  out['turndown-body'] = new TurndownService().turndown(d.body.innerHTML); }
// Readability (contenido principal) + Turndown.
{ const d = new JSDOM(html, { url: 'https://example.org/' }).window.document;
  const art = new Readability(d).parse();
  out['readability'] = (art ? `TITLE: ${art.title}\n` + new TurndownService().turndown(art.content) : ''); }
// html-to-text por defecto.
out['html-to-text'] = convert(html, { wordwrap: false });
// textContent del body (jsdom, sin scripts): texto bruto del DOM.
{ const d = new JSDOM(html).window.document; d.querySelectorAll('script,style').forEach(n => n.remove());
  out['textContent'] = d.title + '\n' + d.body.textContent; }
for (const [k, v] of Object.entries(out)) fs.writeFileSync(`${outdir}/${k}.txt`, v);
