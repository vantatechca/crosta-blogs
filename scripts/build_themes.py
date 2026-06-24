#!/usr/bin/env python3
"""
Build all 10 hand-distinct Hugo themes for the Crosta blog fleet.

Design approach (per frontend-design skill):
- Each theme's HOMEPAGE (index.html) and STYLESHEET (style.css) are bespoke — they
  carry the brand identity. No two share a layout concept or palette.
- The article (single) and listing (list) pages share a sensible structural skeleton
  but inherit each theme's own CSS, so they read as the same publication.
- Featured / top stories are driven by frontmatter (featured: true, top: true) so
  Netgrid controls placement at publish time. No manual curation required.

Run from repo root:  python3 scripts/build_themes.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = ROOT / "themes"


def theme_toml(name, desc):
    return f'name = "{name}"\nlicense = "MIT"\nmin_version = "0.123.0"\n# {desc}\n'


# ---- shared shell (baseof). Body class = theme slug for CSS scoping safety. ----
def baseof(slug, fonts):
    return f'''<!DOCTYPE html>
<html lang="{{{{ .Site.LanguageCode | default "en" }}}}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{{{ if .IsHome }}}}{{{{ .Site.Title }}}}{{{{ else }}}}{{{{ .Title }}}} · {{{{ .Site.Title }}}}{{{{ end }}}}</title>
  <meta name="description" content="{{{{ with .Description }}}}{{{{ . }}}}{{{{ else }}}}{{{{ .Site.Params.description }}}}{{{{ end }}}}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {fonts}
  <link rel="stylesheet" href="{{{{ "style.css" | relURL }}}}">
</head>
<body class="t-{slug}">
  {{{{ partial "header.html" . }}}}
  <main class="wrap">
    {{{{ block "main" . }}}}{{{{ end }}}}
  </main>
  {{{{ partial "footer.html" . }}}}
</body>
</html>
'''


def header(brandline_html):
    return f'''<header class="site-head">
  <div class="site-head__inner">
    {brandline_html}
  </div>
</header>
'''


def footer():
    return '''<footer class="site-foot">
  <div class="site-foot__inner">
    <span>{{ .Site.Title }} — a blog by
      <a href="{{ .Site.Params.brandURL }}">{{ .Site.Params.brand }}</a></span>
    <span class="site-foot__year">© {{ now.Year }}</span>
  </div>
</footer>
'''


def list_tpl():
    return '''{{ define "main" }}
<section class="archive">
  <h1 class="archive__title">{{ .Title }}</h1>
  {{ with .Content }}<div class="archive__intro">{{ . }}</div>{{ end }}
  <ul class="archive__list">
    {{ range .Pages }}
    <li class="archive__item">
      <a href="{{ .RelPermalink }}">
        <span class="archive__date">{{ .Date.Format "Jan 2, 2006" }}</span>
        <span class="archive__name">{{ .Title }}</span>
      </a>
      {{ with .Params.summary }}<p class="archive__sum">{{ . }}</p>{{ end }}
    </li>
    {{ end }}
  </ul>
</section>
{{ end }}
'''


def single_tpl():
    return '''{{ define "main" }}
<article class="post">
  <header class="post__head">
    <p class="post__eyebrow">{{ range .Params.tags }}<span>#{{ . }}</span> {{ end }}</p>
    <h1 class="post__title">{{ .Title }}</h1>
    {{ with .Params.summary }}<p class="post__dek">{{ . }}</p>{{ end }}
    <p class="post__meta">{{ with .Params.author }}{{ . }} · {{ end }}{{ .Date.Format "January 2, 2006" }} · {{ .ReadingTime }} min read</p>
  </header>
  <div class="post__body">
    {{ .Content }}
  </div>
  <footer class="post__foot">
    <a class="post__back" href="{{ "/" | relURL }}">← Back to {{ .Site.Title }}</a>
  </footer>
</article>
{{ end }}
'''


def _fix_main(html):
    """Go templates: vars set before `{{ define "main" }}` aren't in scope inside it.
    Move any leading preamble to just after the define opener."""
    marker = '{{ define "main" }}'
    if marker in html:
        before, after = html.split(marker, 1)
        before = before.strip()
        if before:
            return marker + "\n" + before + "\n" + after
    return html


def write_theme(slug, desc, fonts, brandline, css, index_html,
                header_html=None, footer_html=None):
    index_html = _fix_main(index_html)
    t = THEMES / slug
    (t / "layouts" / "_default").mkdir(parents=True, exist_ok=True)
    (t / "layouts" / "partials").mkdir(parents=True, exist_ok=True)
    (t / "static").mkdir(parents=True, exist_ok=True)
    (t / "theme.toml").write_text(theme_toml(slug, desc))
    (t / "layouts" / "_default" / "baseof.html").write_text(baseof(slug, fonts))
    (t / "layouts" / "index.html").write_text(index_html)
    (t / "layouts" / "_default" / "list.html").write_text(list_tpl())
    (t / "layouts" / "_default" / "single.html").write_text(single_tpl())
    (t / "layouts" / "partials" / "header.html").write_text(header_html or header(brandline))
    (t / "layouts" / "partials" / "footer.html").write_text(footer_html or footer())
    (t / "static" / "style.css").write_text(css)
    print(f"  built theme: {slug}")


# Themes are registered by importing the per-theme modules below.
if __name__ == "__main__":
    import build_themes_defs as defs
    defs.build(write_theme, header, footer)
    print(f"\nBuilt {len(list(THEMES.iterdir()))} themes under themes/")
