#!/usr/bin/env bash
# Per-blog management helper. Work on ONE blog without touching the others.
#
#   ./manage.sh list                 # show all blogs + where each one's files live
#   ./manage.sh dev   <slug>         # live local preview of one blog (reloads on save)
#   ./manage.sh build <slug>         # build just one blog -> public/<slug>/
#   ./manage.sh where <slug>         # print the exact paths to edit for that blog
#
# Common edits:
#   design / layout / colors  ->  themes/<slug>/static/style.css  and  themes/<slug>/layouts/
#   title / tagline / domain  ->  sites/<slug>/hugo.toml
#   posts                     ->  sites/<slug>/content/posts/   (normally Netgrid-owned)
set -euo pipefail
cd "$(dirname "$0")"
CMD="${1:-list}"; SLUG="${2:-}"

slugs() { for d in sites/*/; do basename "$d"; done; }
check() { [ -n "$SLUG" ] && [ -d "sites/$SLUG" ] || { echo "Unknown blog '$SLUG'. Options:"; slugs | sed 's/^/  /'; exit 1; }; }

case "$CMD" in
  list)
    printf "%-14s %-26s %s\n" "SLUG" "TITLE" "EDIT DESIGN AT"
    for s in $(slugs); do
      title=$(grep -m1 '^title' "sites/$s/hugo.toml" | cut -d'"' -f2)
      printf "%-14s %-26s themes/%s/\n" "$s" "$title" "$s"
    done ;;
  dev)
    check
    echo "Live preview: http://localhost:1313/  (Ctrl-C to stop)"
    hugo server -s "sites/$SLUG" --disableFastRender --bind 0.0.0.0 ;;
  build)
    check
    rm -rf "public/$SLUG"
    hugo -s "sites/$SLUG" -d "../../public/$SLUG" --gc --minify --logLevel error
    echo "Built -> public/$SLUG/ ($(find "public/$SLUG" -name '*.html' | wc -l | tr -d ' ') pages)" ;;
  where)
    check
    echo "Blog:      $SLUG"
    echo "Design:    themes/$SLUG/static/style.css"
    echo "Layouts:   themes/$SLUG/layouts/   (index.html = homepage, _default/single.html = article)"
    echo "Settings:  sites/$SLUG/hugo.toml   (title, tagline, baseURL/domain)"
    echo "Posts:     sites/$SLUG/content/posts/" ;;
  *)
    echo "Usage: ./manage.sh {list|dev <slug>|build <slug>|where <slug>}"; exit 1 ;;
esac
