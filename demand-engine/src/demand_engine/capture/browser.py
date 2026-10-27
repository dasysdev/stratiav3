"""The Chrome of the capture engine and the page operations a visit needs.

Chrome stable, headed (Xvfb or the host desktop), persistent profile, no automation flags
and no --headless: the sites see an ordinary Chrome with its own user agent. Each site works
in its own window, so every page is visible and rendered (a background tab is throttled and
its lazy content does not load). Launch flags adapted from stratia.rpa (launcher.py).
"""
from __future__ import annotations

import base64
import json
import os
import random
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

from .cdp import Cdp, CdpError

SINGLETON_FILES = ("SingletonLock", "SingletonSocket", "SingletonCookie")


def _flag(name: str) -> bool:
    return os.environ.get(name, "0") == "1"


def chrome_args(profile: Path, port: int) -> list[str]:
    args = [
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-session-crashed-bubble",
        "--hide-crash-restore-bubble",
        # No desktop keyring in the container: without this Chrome asks for a password
        "--password-store=basic",
        "--lang=es-ES",
        "--accept-lang=es-ES,es",
        "--window-size=1920,1080",
        # Windows of the other sites keep rendering while covered
        "--disable-backgrounding-occluded-windows",
        "--disable-renderer-backgrounding",
        "--disable-background-timer-throttling",
    ]
    if _flag("CAPTURE_NO_SANDBOX"):
        args.append("--no-sandbox")
    if _flag("CAPTURE_DISABLE_GPU"):
        args.append("--disable-gpu")
    args.append("about:blank")
    return args


class Browser:
    """A Chrome on `port`: launched here (and closed by `stop`) or already running, in which
    case it is shared (one Chrome and one profile per container)."""

    def __init__(self, profile: Path, port: int | None = None, chrome: str | None = None) -> None:
        self.profile = profile
        self.port = port or int(os.environ.get("CAPTURE_CDP_PORT", "9223"))
        self.chrome = chrome or os.environ.get("CAPTURE_CHROME", "google-chrome")
        self._proc: subprocess.Popen | None = None
        self._cdp: Cdp | None = None
        self._lock = threading.Lock()
        self.info: dict = {}

    def _json(self, path: str, timeout: float = 3):
        with urllib.request.urlopen(f"http://127.0.0.1:{self.port}{path}", timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def alive(self) -> bool:
        try:
            self._json("/json/version", timeout=2)
            return True
        except (urllib.error.URLError, OSError, ValueError):
            return False

    def start(self) -> None:
        if not self.alive():
            self.profile.mkdir(parents=True, exist_ok=True)
            # A lock left by a Chrome that no longer serves the port is garbage
            for name in SINGLETON_FILES:
                (self.profile / name).unlink(missing_ok=True)
            log = open(self.profile.parent / "chrome.log", "ab")
            self._proc = subprocess.Popen([self.chrome, *chrome_args(self.profile, self.port)],
                                          stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                                          start_new_session=True)
            deadline = time.monotonic() + 30
            while not self.alive():
                if self._proc.poll() is not None or time.monotonic() > deadline:
                    raise CdpError(f"Chrome no arrancó; ver {self.profile.parent / 'chrome.log'}")
                time.sleep(0.3)
        version = self.version()
        self.info = {"product": version.get("Browser"), "user_agent": version.get("User-Agent")}
        self._cdp = Cdp(version["webSocketDebuggerUrl"])

    def version(self) -> dict:
        return self._json("/json/version")

    def new_window(self) -> "Page":
        with self._lock:
            target = self._cdp.send("Target.createTarget", {"url": "about:blank", "newWindow": True})
        target_id = target["targetId"]
        return Page(self, target_id, Cdp(f"ws://127.0.0.1:{self.port}/devtools/page/{target_id}"))

    def close_window(self, page: "Page") -> None:
        page.cdp.close()
        with self._lock:
            try:
                self._cdp.send("Target.closeTarget", {"targetId": page.target_id})
            except CdpError:
                pass

    def close_other_tabs(self, keep: "Page") -> int:
        """Close every tab but `keep` and return how many: a run cut short leaves its tab
        behind, and a hung tab shares its renderer with a new one of the same site."""
        closed = 0
        with self._lock:
            for target in self._cdp.send("Target.getTargets")["targetInfos"]:
                if target["type"] == "page" and target["targetId"] != keep.target_id:
                    try:
                        self._cdp.send("Target.closeTarget", {"targetId": target["targetId"]})
                        closed += 1
                    except CdpError:
                        pass
        return closed

    def stop(self) -> None:
        """Close Chrome only if this object launched it."""
        if self._proc is not None:
            try:
                with self._lock:
                    self._cdp.send("Browser.close", timeout=5)
            except CdpError:
                pass
            try:
                self._proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                self._proc.kill()
        if self._cdp is not None:
            self._cdp.close()


class Page:
    """One window. Scripts of the engine run in an isolated world: the page cannot see
    or alter them, and they see a pristine DOM API."""

    def __init__(self, browser: Browser, target_id: str, cdp: Cdp) -> None:
        self.browser = browser
        self.target_id = target_id
        self.cdp = cdp
        self.frame_id = ""
        self._context: int | None = None
        cdp.send("Network.enable", {"maxTotalBufferSize": 200_000_000,
                                    "maxResourceBufferSize": 50_000_000})

    # ------------------------------------------------------------ navigation
    def navigate(self, url: str) -> dict:
        """Start a navigation and return Page.navigate's result (frameId, loaderId, errorText)."""
        self.cdp.events.clear()
        self._context = None
        result = self.cdp.send("Page.navigate", {"url": url}, timeout=60)
        self.frame_id = result.get("frameId", self.frame_id)
        return result

    def wait_ready(self, timeout: float = 45) -> bool:
        """Wait for readyState 'complete' of the new document; False on timeout."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                if self.main_response() is not None or self.main_failure():
                    if self.cdp.evaluate("document.readyState", timeout=10) == "complete":
                        return True
            except CdpError:
                pass  # the document was being replaced
            self.cdp.pump(0.3)
        return False

    def wait_stable(self, quiet: float = 1.5, timeout: float = 10) -> None:
        """Wait until the element count and the text length stop changing for `quiet` s."""
        probe = "document.getElementsByTagName('*').length + ':' + (document.body ? document.body.innerText.length : 0)"
        deadline = time.monotonic() + timeout
        last, since = None, time.monotonic()
        while time.monotonic() < deadline:
            try:
                now = self.eval(probe)
            except CdpError:
                now = None
            if now != last:
                last, since = now, time.monotonic()
            elif time.monotonic() - since >= quiet:
                return
            self.cdp.pump(0.5)

    def idle(self, seconds: float, stop: threading.Event | None = None) -> None:
        """Stay on the page reading its events (and discarding them) for `seconds`."""
        deadline = time.monotonic() + seconds
        while (left := deadline - time.monotonic()) > 0:
            if stop is not None and stop.is_set():
                return
            self.cdp.pump(min(1.0, left))
            if len(self.cdp.events) > 5000:
                del self.cdp.events[:-1000]

    # ------------------------------------------------------------ scripts
    def eval(self, expression: str, timeout: float = 30, await_promise: bool = False):
        """Evaluate in the engine's isolated world, recreating it after a navigation."""
        for attempt in (1, 2):
            if self._context is None:
                world = self.cdp.send("Page.createIsolatedWorld",
                                      {"frameId": self.frame_id, "worldName": "capture"})
                self._context = world["executionContextId"]
            try:
                return self.cdp.evaluate(expression, self._context, timeout, await_promise)
            except CdpError as exc:
                if attempt == 2 or "context" not in str(exc).lower():
                    raise
                self._context = None

    # ------------------------------------------------------------ reading
    def scroll_through(self, budget: float, rng: random.Random, stop: threading.Event | None = None) -> int:
        """Scroll down with the mouse wheel, as a reader would, until the end of the page or
        `budget` seconds. Returns the number of wheel steps (lazy content loads on the way)."""
        size = self.eval("[innerWidth, innerHeight]") or [1920, 1080]
        x = size[0] * rng.uniform(0.35, 0.65)
        y = size[1] * rng.uniform(0.4, 0.6)
        self.cdp.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
        deadline = time.monotonic() + budget
        steps, stuck, last = 0, 0, None
        while time.monotonic() < deadline and steps < 120 and stuck < 3:
            if stop is not None and stop.is_set():
                break
            self.cdp.send("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": x, "y": y,
                                                       "deltaX": 0, "deltaY": rng.randint(250, 700)})
            steps += 1
            self.cdp.pump(rng.uniform(0.3, 1.2))
            pos = self.eval("[Math.round(scrollY), document.scrollingElement ? document.scrollingElement.scrollHeight - innerHeight : 0]")
            if not pos:
                break
            if pos[0] >= pos[1] - 2:
                stuck += 1  # at the end: a few more steps let lazy content extend the page
            elif pos == last:
                stuck += 1
            else:
                stuck = 0
            last = pos
        return steps

    def main_response(self) -> dict | None:
        """The last Document response of the main frame (after redirects and challenges)."""
        found = None
        for ev in self.cdp.events:
            p = ev.get("params", {})
            if ev.get("method") == "Network.responseReceived" and p.get("type") == "Document" \
                    and p.get("frameId") == self.frame_id:
                found = p
        return found

    def main_failure(self) -> str:
        response = self.main_response()
        for ev in self.cdp.events:
            p = ev.get("params", {})
            if ev.get("method") == "Network.loadingFailed" and p.get("type") == "Document" \
                    and (response is None or p.get("requestId") == response.get("requestId")):
                return p.get("errorText", "error")
        return ""

    def redirects(self) -> list[dict]:
        chain = []
        for ev in self.cdp.events:
            p = ev.get("params", {})
            if ev.get("method") == "Network.requestWillBeSent" and p.get("type") == "Document" \
                    and p.get("frameId") == self.frame_id and p.get("redirectResponse"):
                r = p["redirectResponse"]
                chain.append({"url": r.get("url"), "status": r.get("status"), "to": p["request"]["url"]})
        return chain

    def response_body(self, request_id: str) -> bytes:
        """Body of a response; retried while Chrome has not finished receiving it."""
        deadline = time.monotonic() + 30
        while True:
            try:
                body = self.cdp.send("Network.getResponseBody", {"requestId": request_id}, timeout=60)
                break
            except CdpError:
                if time.monotonic() > deadline:
                    raise
                self.cdp.pump(0.5)
        if body.get("base64Encoded"):
            return base64.b64decode(body["body"])
        return body.get("body", "").encode("utf-8")

    def cookie_names(self, url: str) -> list[str]:
        cookies = self.cdp.send("Network.getCookies", {"urls": [url]}).get("cookies", [])
        return sorted({c["name"] for c in cookies})

    def mhtml(self) -> bytes:
        return self.cdp.send("Page.captureSnapshot", {"format": "mhtml"}, timeout=180)["data"].encode("utf-8")


SIGNALS = """(() => {
  const gl = document.createElement('canvas').getContext('webgl');
  let webgl = null;
  if (gl) { const ext = gl.getExtension('WEBGL_debug_renderer_info'); webgl = gl.getParameter(ext ? ext.UNMASKED_RENDERER_WEBGL : gl.RENDERER); }
  return {webdriver: navigator.webdriver, languages: navigator.languages, platform: navigator.platform,
          timezone: Intl.DateTimeFormat().resolvedOptions().timeZone, cores: navigator.hardwareConcurrency,
          memory_gb: navigator.deviceMemory, screen: [screen.width, screen.height],
          window: [outerWidth, outerHeight], webgl,
          brands: navigator.userAgentData ? navigator.userAgentData.brands.map(b => `${b.brand} ${b.version}`) : null};
})()"""


def signals(browser: Browser) -> dict:
    """What a site sees of the engine's Chrome: user agent, webdriver, languages, WebGL…"""
    page = browser.new_window()
    try:
        page.navigate("about:blank")
        return {**browser.info, **(page.eval(SIGNALS) or {})}
    finally:
        browser.close_window(page)
