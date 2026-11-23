#!/usr/bin/env bash
# macOS / Linux launcher. Needs Node.js 18+. Builds if needed and serves on http://127.0.0.1:4173/
set -e
cd "$(dirname "$0")"
command -v node >/dev/null 2>&1 || { echo "Node.js 18 or newer is required (https://nodejs.org)"; exit 1; }
[ -d node_modules ] || npm install --no-audit --no-fund
[ -f dist/index.html ] || npm run build
echo "MEDICINE 2040 web app: http://127.0.0.1:4173/  (Ctrl-C stops the server)"
( sleep 3; open "http://127.0.0.1:4173/" 2>/dev/null || xdg-open "http://127.0.0.1:4173/" 2>/dev/null || true ) &
npm run preview
