"""Pregunta a los chats públicos con el Chrome real del motor (capture.browser, como PAA).

  probe            abre cada chat y dice si ofrece un campo de texto sin iniciar sesión (no envía nada)
  ask CHAT FICHERO pega el prompt de FICHERO en CHAT ({BASE} = $CANARY_BASE), espera a que la respuesta se estabilice y guarda
                   el texto visible de la página en results/chat/CHAT-AAAAMMDDTHHMMSS.txt

Perfil de Chrome propio (capture/var/chrome-chats), separado del de captura y del de PAA.
Ritmo de persona: una pregunta por chat y ejecución; nada en paralelo.
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from datetime import datetime
from pathlib import Path

from capture.browser import Browser

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "capture" / "var" / "chrome-chats" / "profile"

CHATS = {
    "chatgpt": "https://chatgpt.com/",
    "claude": "https://claude.ai/new",
    "gemini": "https://gemini.google.com/app",
    "perplexity": "https://www.perplexity.ai/",
    "copilot": "https://copilot.microsoft.com/",
    "meta": "https://www.meta.ai/",
}

# El primer campo editable visible: textarea o contenteditable.
FIND_INPUT = """(() => {
  const els = [...document.querySelectorAll('textarea, [contenteditable="true"]')];
  const vis = els.filter(e => { const r = e.getBoundingClientRect(); return r.width > 50 && r.height > 10; });
  const e = vis[0];
  if (!e) return null;
  const r = e.getBoundingClientRect();
  return {tag: e.tagName, x: r.x + r.width / 2, y: r.y + r.height / 2,
          placeholder: e.getAttribute('placeholder') || e.getAttribute('aria-label') || ''};
})()"""

TEXT = "document.body ? document.body.innerText : ''"


def browser() -> Browser:
    b = Browser(PROFILE, port=int(os.environ.get("CHATS_CDP_PORT", "9226")))
    b.start()
    return b


def click(page, x: float, y: float) -> None:
    page.cdp.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
    page.cdp.pump(random.uniform(0.2, 0.4))
    for kind in ("mousePressed", "mouseReleased"):
        page.cdp.send("Input.dispatchMouseEvent", {"type": kind, "x": x, "y": y, "button": "left", "clickCount": 1})
        page.cdp.pump(random.uniform(0.05, 0.15))


def enter(page) -> None:
    for kind in ("keyDown", "keyUp"):
        page.cdp.send("Input.dispatchKeyEvent", {"type": kind, "key": "Enter", "code": "Enter",
                                                 "windowsVirtualKeyCode": 13, "text": "\r" if kind == "keyDown" else ""})


REJECT = """(() => {
  const want = /^(rechazar todo|rechazar las que no son esenciales|solo las necesarias|rechazar)$/i;
  const b = [...document.querySelectorAll('button, [role=button]')].find(e => want.test(e.innerText.trim()));
  if (!b) return null;
  b.scrollIntoView({block: 'center'});
  const r = b.getBoundingClientRect();
  return {text: b.innerText.trim(), x: r.x + r.width / 2, y: r.y + r.height / 2};
})()"""


def open_chat(b: Browser, name: str):
    page = b.new_window()
    page.navigate(CHATS[name])
    page.wait_ready()
    page.idle(random.uniform(4, 6))
    # Un aviso de cookies tapa el campo de texto: se rechaza, como en PAA.
    button = page.eval(REJECT)
    if button:
        click(page, button["x"], button["y"])
        page.idle(random.uniform(3, 5))
        if page.eval(REJECT):  # el clic no llegó (botón fuera de la ventana): se pulsa desde la página
            page.eval(REJECT.replace("if (!b) return null;", "if (!b) return null; b.click();"))
            page.idle(random.uniform(3, 5))
        page.wait_ready()
    return page


def probe() -> None:
    b = browser()
    try:
        for name in CHATS:
            page = open_chat(b, name)
            try:
                found = page.eval(FIND_INPUT)
                url = page.eval("location.href")
                print(json.dumps({"chat": name, "url": url, "input": found}, ensure_ascii=False))
            finally:
                b.close_window(page)
    finally:
        b.stop()


def ask(name: str, prompt_file: Path, timeout: float = 240, quiet: float = 15) -> Path:
    prompt = prompt_file.read_text(encoding="utf-8").strip().replace("{BASE}", os.environ["CANARY_BASE"].rstrip("/"))
    b = browser()
    page = open_chat(b, name)
    try:
        box = page.eval(FIND_INPUT)
        if not box:
            raise SystemExit(f"{name}: no hay campo de texto (¿pide iniciar sesión?)")
        click(page, box["x"], box["y"])
        page.cdp.send("Input.insertText", {"text": prompt})
        page.idle(random.uniform(0.8, 1.5))
        enter(page)
        # La respuesta termina cuando el texto de la página deja de cambiar durante `quiet` segundos.
        start, last, since = time.monotonic(), page.eval(TEXT), time.monotonic()
        while time.monotonic() - start < timeout:
            page.idle(3)
            now = page.eval(TEXT)
            if now != last:
                last, since = now, time.monotonic()
            elif time.monotonic() - since >= quiet and time.monotonic() - start > 30:
                break
        out = HERE / "results" / "chat" / f"{name}-{datetime.now():%Y%m%dT%H%M%S}.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"CHAT: {name}\nPROMPT: {prompt_file.name}\nURL: {page.eval('location.href')}\n\n{last}",
                       encoding="utf-8")
        print(out)
        return out
    finally:
        b.close_window(page)
        b.stop()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "probe":
        probe()
    elif cmd == "ask":
        ask(sys.argv[2], Path(sys.argv[3]))
    else:
        raise SystemExit(__doc__)
