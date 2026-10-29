"""Sirve site/ en 127.0.0.1 y registra cada petición (hora, método, ruta, cabeceras) en un JSONL.

Uso: python3 serve.py PUERTO LOG.jsonl
Solo sirve los ficheros de site/; no lista directorios.
"""
import json
import sys
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"


class Handler(SimpleHTTPRequestHandler):
    log_path: Path

    def list_directory(self, path):
        self.send_error(404)
        return None

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_request(self, code="-", size="-"):
        entry = {
            "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "method": self.command, "path": self.path, "status": code,
            "headers": dict(self.headers.items()),
        }
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> None:
    port, log = int(sys.argv[1]), Path(sys.argv[2])
    Handler.log_path = log
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(SITE)))
    server.serve_forever()


if __name__ == "__main__":
    main()
