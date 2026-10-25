#!/bin/bash
# Main process of the container. With DISPLAY=:99 (default) it starts a virtual screen so
# Chrome runs headed without a desktop; with DISPLAY=:0 it links the host desktop (WSLg),
# mounted at /tmp/.X11-host so that Xvfb never writes into the host's socket directory.
set -e

case "${DISPLAY:-}" in
  :99)
    if ! xdpyinfo -display :99 >/dev/null 2>&1; then
      rm -f /tmp/.X99-lock /tmp/.X11-unix/X99
      Xvfb :99 -screen 0 "${CAPTURE_SCREEN:-1920x1080x24}" -nolisten tcp >/tmp/xvfb.log 2>&1 &
    fi ;;
  :0)
    [ -S /tmp/.X11-host/X0 ] && ln -sf /tmp/.X11-host/X0 /tmp/.X11-unix/X0 ;;
esac
exec "$@"
