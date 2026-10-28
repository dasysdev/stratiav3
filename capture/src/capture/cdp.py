"""Minimal Chrome DevTools Protocol client over a synchronous WebSocket.

Adapted from stratia.rpa (app/browser/infra/cdp_session.py): one connection per target and
one request id per command. Unlike rpa, events are kept in `events`, because the capture
reads the Network events of the main document. Runtime.enable is never sent: a page can
detect it. An event with a handler in `handlers` is also handed to it as it arrives, even
while a command waits for its reply (the audit profile answers Fetch pauses that way).
"""
from __future__ import annotations

import json
import time
from typing import Callable

from websockets.exceptions import WebSocketException
from websockets.sync.client import connect


class CdpError(RuntimeError):
    pass


class Cdp:
    def __init__(self, ws_url: str) -> None:
        try:
            self._ws = connect(ws_url, max_size=None, open_timeout=10, close_timeout=1)
        except (WebSocketException, OSError, TimeoutError) as exc:
            raise CdpError(f"no se pudo conectar con {ws_url}: {exc}") from exc
        self._id = 0
        self.events: list[dict] = []
        self.handlers: dict[str, Callable[[dict], None]] = {}
        self._replies: dict[int, dict] = {}  # replies read while a handler's command waited

    def close(self) -> None:
        try:
            self._ws.close()
        except Exception:  # noqa: BLE001 - closing must never fail a command
            pass

    def _recv(self, timeout: float) -> dict | None:
        try:
            raw = self._ws.recv(timeout=max(0.0, timeout))
        except TimeoutError:
            return None
        except (WebSocketException, OSError) as exc:
            raise CdpError(f"conexión CDP perdida: {exc}") from exc
        try:
            return json.loads(raw)
        except ValueError:
            return {}

    def send(self, method: str, params: dict | None = None, timeout: float = 30) -> dict:
        self._id += 1
        msg_id = self._id
        try:
            self._ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
        except (WebSocketException, OSError) as exc:
            raise CdpError(f"conexión CDP perdida al enviar {method}: {exc}") from exc
        deadline = time.monotonic() + timeout
        while (left := deadline - time.monotonic()) > 0:
            msg = self._replies.pop(msg_id, None) or self._recv(left)
            if msg is None:
                break
            if msg.get("id") == msg_id:
                if "error" in msg:
                    raise CdpError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result") or {}
            if "id" in msg:
                self._replies[msg["id"]] = msg
            elif "method" in msg:
                self._event(msg)
        raise CdpError(f"sin respuesta a {method} en {timeout:.0f} s")

    def _event(self, msg: dict) -> None:
        self.events.append(msg)
        handler = self.handlers.get(msg["method"])
        if handler is not None:
            handler(msg.get("params") or {})

    def pump(self, seconds: float) -> None:
        """Read events for `seconds` (also keeps Chrome's send buffer empty while idle)."""
        deadline = time.monotonic() + seconds
        while (left := deadline - time.monotonic()) > 0:
            msg = self._recv(left)
            if msg is None:
                return
            if "method" in msg:
                self._event(msg)

    def evaluate(self, expression: str, context_id: int | None = None, timeout: float = 30,
                 await_promise: bool = False):
        params = {"expression": expression, "returnByValue": True, "awaitPromise": await_promise}
        if context_id is not None:
            params["contextId"] = context_id
        result = self.send("Runtime.evaluate", params, timeout=timeout)
        if "exceptionDetails" in result:
            detail = result["exceptionDetails"]
            text = (detail.get("exception") or {}).get("description") or detail.get("text")
            raise CdpError(f"error en la página: {text}")
        return (result.get("result") or {}).get("value")
