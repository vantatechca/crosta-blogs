#!/usr/bin/env bash
# Render build helper — builds ONE blog by slug. Used by each Render Static Site service.
#   Usage:  ./render-build.sh journal
# Render runs this at the repo root. Output lands in public/<slug>/, which each
# service sets as its Publish Directory.
set -euo pipefail
SLUG="${1:?usage: render-build.sh <slug>}"
HUGO_VERSION="${HUGO_VERSION:-0.139.0}"

# Render's build image doesn't ship Hugo — fetch the extended binary once.
if ! command -v hugo >/dev/null 2>&1 && [ ! -x ./hugo ]; then
  echo "Fetching Hugo ${HUGO_VERSION}…"
  curl -sSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
    | tar -xz hugo
fi
HUGO_BIN="$(command -v hugo || echo ./hugo)"

# NOTE: the python scaffolding scripts are NOT run here. Themes and site configs are
# committed to the repo, and content/ is owned by Netgrid. A deploy is a pure Hugo build
# so rebuilds never clobber published posts. Run ./scaffold.sh locally only when you
# change the blog list or a theme design.
"$HUGO_BIN" -s "sites/${SLUG}" -d "../../public/${SLUG}" --gc --minify
echo "Built ${SLUG} -> public/${SLUG}"
