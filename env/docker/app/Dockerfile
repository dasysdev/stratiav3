# Image of the project's Python code: Python 3.13 + uv + Google Chrome stable + Xvfb.
# Stages: base (system and uv), dev (dependencies with the dev group; code mounted),
# prod (runtime dependencies and code copied into the image).
#
# Chrome runs headed on Xvfb (or on the host display): the capture engine (capture/) never
# uses --headless. The Chrome package depends on wget, so it cannot be purged afterwards.
FROM python:3.13-slim-bookworm AS base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/work/capture/src:/work/demand-engine/src:/work/info-audit/src:/work/references/src:/work/web-audit/src \
    LANG=es_ES.UTF-8 \
    LC_ALL=es_ES.UTF-8 \
    TZ=Europe/Madrid \
    HOME=/home/app \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_LINK_MODE=copy \
    UV_CACHE_DIR=/tmp/uv-cache \
    PATH=/opt/venv/bin:$PATH \
    CAPTURE_CHROME=/usr/bin/google-chrome

COPY --from=ghcr.io/astral-sh/uv:0.12.24 /uv /uvx /usr/local/bin/

# Chrome stable + fonts (a Spanish store must render as on a Spanish desktop) + Xvfb.
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl wget gnupg tini procps locales xvfb x11-utils \
      fonts-liberation fonts-dejavu-core fonts-noto-core fonts-noto-color-emoji \
 && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
      | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update && apt-get install -y --no-install-recommends google-chrome-stable \
 && sed -i 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && locale-gen \
 && rm -rf /var/lib/apt/lists/*

# HOME writable by any UID: compose runs the container with the host UID.
RUN useradd -m -u 1000 -s /bin/bash app && chmod 777 /home/app \
 && mkdir -p /opt/venv && chmod 777 /opt/venv \
 && mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

COPY env/docker/app/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /work
ENTRYPOINT ["tini", "--", "/entrypoint.sh"]

# dev and prod install the dependencies of every member of the workspace (one per system);
# the members' code is on PYTHONPATH. base copies neither, so `bin/run dev lock` can build it
# without a uv.lock.

# ---------------------------------------------------------------- dev
FROM base AS dev
COPY pyproject.toml uv.lock /work/
COPY capture/pyproject.toml /work/capture/
COPY demand-engine/pyproject.toml /work/demand-engine/
COPY info-audit/pyproject.toml /work/info-audit/
COPY references/pyproject.toml /work/references/
COPY web-audit/pyproject.toml /work/web-audit/
RUN uv sync --locked --all-packages && rm -rf /tmp/uv-cache
USER app
CMD ["sleep", "infinity"]

# ---------------------------------------------------------------- prod
FROM base AS prod
COPY pyproject.toml uv.lock /work/
COPY capture/pyproject.toml /work/capture/
COPY demand-engine/pyproject.toml /work/demand-engine/
COPY info-audit/pyproject.toml /work/info-audit/
COPY references/pyproject.toml /work/references/
COPY web-audit/pyproject.toml /work/web-audit/
RUN uv sync --locked --all-packages --no-dev && rm -rf /tmp/uv-cache
COPY capture/src /work/capture/src
COPY demand-engine/src /work/demand-engine/src
COPY info-audit/src /work/info-audit/src
COPY info-audit/schemas /work/info-audit/schemas
COPY references/src /work/references/src
COPY web-audit/src /work/web-audit/src
USER app
CMD ["sleep", "infinity"]
