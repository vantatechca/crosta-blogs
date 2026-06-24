#!/usr/bin/env bash
# DEV-TIME ONLY. Regenerates themes + site configs + SAMPLE seed content.
# Run this when you change the blog list (scripts/generate_sites.py) or a theme
# design (scripts/build_themes_defs.py). Do NOT run on a live site — generate_sites.py
# re-creates the sample seed posts. In production, content/ is owned by Netgrid.
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/generate_sites.py
python3 scripts/build_themes.py
echo "Scaffold refreshed. Now run ./build.sh"
