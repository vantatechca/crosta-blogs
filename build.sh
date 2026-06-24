#!/usr/bin/env bash
# Build every blog into public/<slug>/. Pure Hugo build — safe to run anytime,
# never touches content/. (To regenerate themes/configs/seed content, run ./scaffold.sh.)
set -euo pipefail
cd "$(dirname "$0")"

rm -rf public && mkdir -p public

fail=0
for dir in sites/*/; do
  slug="$(basename "$dir")"
  if hugo -s "sites/$slug" -d "../../public/$slug" --gc --minify --logLevel error; then
    pages=$(find "public/$slug" -name '*.html' | wc -l | tr -d ' ')
    printf "  ✓ %-14s %s pages\n" "$slug" "$pages"
  else
    printf "  ✗ %-14s BUILD FAILED\n" "$slug"; fail=1
  fi
done

[ "$fail" -eq 0 ] && echo "All sites built into ./public/" || { echo "Some sites failed."; exit 1; }
