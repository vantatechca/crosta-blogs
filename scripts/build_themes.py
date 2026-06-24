#!/usr/bin/env python3
"""
Build all 10 hand-distinct Hugo themes for the Crosta blog fleet.

Each theme keeps its bespoke homepage + stylesheet (its identity). On top of that
the factory layers a shared, theme-tokenised experience:
  - a hero BANNER (image placeholder) with a "Check us out" CTA -> pizzeriacrosta.com
  - a floating CTA + a closing CTA band
  - scroll-reveal, banner intro, subtle parallax, smooth scroll, hover motion
Each theme supplies its own tokens (display font, CTA colour, button radius, banner
gradient) so the additions feel native, not bolted on.

Failsafe: motion/reveal only activate when JS runs AND the visitor hasn't asked for
reduced motion. Without JS, every element is fully visible — content never hides.

Run from repo root:  python3 scripts/build_themes.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = ROOT / "themes"


def theme_toml(name, desc):
    return f'name = "{name}"\nlicense = "MIT"\nmin_version = "0.123.0"\n# {desc}\n'


# ─── per-theme tokens for the shared banner/CTA/motion layer ─────────────────
# display = the theme's display font; cta/ctaInk = button colours; radius = button
# shape (pill vs sharp, matched to the theme); grad/ink/shade = hero banner.
TOK = {
 "journal":     dict(display='"Fraunces",serif', cta="#15605a", ink="#fbfaf7", radius="999px",
                     grad="linear-gradient(135deg,#13322f 0%,#15605a 55%,#2c7d74 100%)",
                     bink="#fbfaf7", shade="linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.30))"),
 "stoneoven":   dict(display='"Lora",serif', cta="#e07a37", ink="#1a1714", radius="999px",
                     grad="radial-gradient(120% 120% at 72% 8%,#5a3a22 0%,#2c2722 46%,#1a1714 100%)",
                     bink="#efe7da", shade="linear-gradient(180deg,rgba(0,0,0,.10),rgba(0,0,0,.34))"),
 "crustcrumb":  dict(display='"Hanken Grotesk",sans-serif', cta="#141414", ink="#ffffff", radius="4px",
                     grad="linear-gradient(135deg,#faf7f0 0%,#ecdfc6 60%,#d8c393 100%)",
                     bink="#141414", shade="linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.06))"),
 "dailyslice":  dict(display='"Oswald",sans-serif', cta="#c41f1f", ink="#ffffff", radius="0",
                     grad="linear-gradient(120deg,#16140f 0%,#3a1413 55%,#c41f1f 165%)",
                     bink="#fcfbf7", shade="linear-gradient(180deg,rgba(0,0,0,.12),rgba(0,0,0,.32))"),
 "notespass":   dict(display='"Space Mono",monospace', cta="#b1342b", ink="#f4f1e7", radius="4px",
                     grad="linear-gradient(135deg,#f7f4ea 0%,#efe7d2 60%,#e4d8b8 100%)",
                     bink="#1e1b14", shade="linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.06))"),
 "flourfire":   dict(display='"Anton",sans-serif', cta="#f59e0b", ink="#0c0a09", radius="999px",
                     grad="linear-gradient(120deg,#0c0a09 0%,#7a1d12 52%,#dc2626 84%,#f59e0b 130%)",
                     bink="#f3ede4", shade="linear-gradient(180deg,rgba(0,0,0,.10),rgba(0,0,0,.30))"),
 "crostatable": dict(display='"Cormorant Garamond",serif', cta="#a9853f", ink="#f4efe4", radius="2px",
                     grad="linear-gradient(135deg,#f4efe4 0%,#e6d7bd 55%,#cdae74 100%)",
                     bink="#2c2017", shade="linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.07))"),
 "hotoven":     dict(display='"Fredoka",sans-serif', cta="#ef4444", ink="#ffffff", radius="999px",
                     grad="linear-gradient(135deg,#fff7e6 0%,#ffe39e 45%,#ffb38a 80%,#ef4444 155%)",
                     bink="#2a2018", shade="linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.05))"),
 "fornodiaries":dict(display='"Playfair Display",serif', cta="#5f6b3a", ink="#faf5ec", radius="999px",
                     grad="linear-gradient(135deg,#faf5ec 0%,#e8e3cf 55%,#c4c79a 100%)",
                     bink="#2a201a", shade="linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.06))"),
 "behindcrust": dict(display='"Space Grotesk",sans-serif', cta="#1f4ed8", ink="#ffffff", radius="0",
                     grad="linear-gradient(120deg,#1b1b19 0%,#26302f 60%,#1f4ed8 175%)",
                     bink="#f3f3f1", shade="linear-gradient(180deg,rgba(0,0,0,.10),rgba(0,0,0,.30))"),
}


def tokens_css(slug):
    t = TOK[slug]
    return (
        "\n\n/* ===== Crosta shared layer: tokens ===== */\n"
        ":root{"
        f"--cr-display:{t['display']};"
        f"--cr-cta:{t['cta']};--cr-cta-ink:{t['ink']};--cr-cta-radius:{t['radius']};"
        f"--cr-grad:{t['grad']};--cr-banner-ink:{t['bink']};--cr-shade:{t['shade']};"
        "}\n"
    )


SHARED_CSS = """
/* ===== Crosta shared layer: banner + CTA + motion ===== */
html{scroll-behavior:smooth}

/* hero banner (full-bleed, sits between header and content) */
.cr-banner{position:relative;overflow:hidden;isolation:isolate}
.cr-banner__media{position:absolute;inset:-2px;z-index:-2;background:var(--cr-grad);will-change:transform}
.cr-banner__img{width:100%;height:100%;object-fit:cover;display:block}
.cr-banner::after{content:"";position:absolute;inset:0;z-index:-1;background:var(--cr-shade)}
.cr-banner__ph{position:absolute;right:14px;bottom:12px;z-index:0;font:600 11px/1 system-ui,sans-serif;
 letter-spacing:.05em;color:var(--cr-banner-ink);opacity:.55;background:rgba(0,0,0,.16);padding:6px 10px;border-radius:5px}
.cr-banner__inner{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:clamp(46px,8vw,96px) 28px;
 min-height:clamp(330px,46vh,520px);display:flex;flex-direction:column;align-items:flex-start;justify-content:center;color:var(--cr-banner-ink)}
.cr-banner--slim .cr-banner__inner{min-height:clamp(140px,22vh,200px);padding:30px 28px}
.cr-banner__eyebrow{font-family:var(--cr-display);text-transform:uppercase;letter-spacing:.22em;font-size:13px;
 font-weight:600;margin:0 0 16px;opacity:.9}
.cr-banner__title{font-family:var(--cr-display);font-weight:700;font-size:clamp(30px,5.4vw,62px);line-height:1.04;
 letter-spacing:-.01em;margin:0 0 28px;max-width:20ch;text-wrap:balance}
.cr-banner--slim .cr-banner__title{font-size:clamp(22px,3.4vw,36px);margin:0}
.cr-banner--slim .cr-cta{margin-top:16px}

/* CTA button (themed) */
.cr-cta{display:inline-flex;align-items:center;gap:.5em;background:var(--cr-cta);color:var(--cr-cta-ink);
 font-family:var(--cr-display);font-weight:600;font-size:16px;letter-spacing:.01em;text-decoration:none;
 padding:14px 28px;border-radius:var(--cr-cta-radius);box-shadow:0 8px 22px -10px rgba(0,0,0,.55);
 transition:transform .22s cubic-bezier(.22,.61,.36,1),box-shadow .22s,filter .22s}
.cr-cta span{transition:transform .22s cubic-bezier(.22,.61,.36,1)}
.cr-cta:hover{transform:translateY(-2px);filter:brightness(1.06);box-shadow:0 14px 30px -12px rgba(0,0,0,.6)}
.cr-cta:hover span{transform:translate(3px,-3px)}
.cr-cta:focus-visible{outline:3px solid var(--cr-cta);outline-offset:3px}

/* floating CTA */
.cr-fab{position:fixed;right:20px;bottom:20px;z-index:60;display:inline-flex;align-items:center;gap:.5em;
 background:var(--cr-cta);color:var(--cr-cta-ink);font-family:var(--cr-display);font-weight:600;font-size:14px;
 text-decoration:none;padding:12px 20px;border-radius:var(--cr-cta-radius);box-shadow:0 10px 30px -8px rgba(0,0,0,.5);
 transition:transform .22s cubic-bezier(.22,.61,.36,1),box-shadow .22s,filter .22s}
.cr-fab span{transition:transform .22s}
.cr-fab:hover{transform:translateY(-2px);filter:brightness(1.06)}
.cr-fab:hover span{transform:translate(3px,-3px)}
.cr-fab:focus-visible{outline:3px solid #fff;outline-offset:2px}

/* closing CTA band */
.cr-band{background:var(--cr-cta)}
.cr-band__inner{max-width:1100px;margin:0 auto;padding:clamp(40px,6vw,64px) 28px;display:flex;align-items:center;
 justify-content:space-between;gap:22px;flex-wrap:wrap}
.cr-band__t{font-family:var(--cr-display);font-weight:700;color:var(--cr-cta-ink);font-size:clamp(24px,4vw,42px);
 line-height:1.05;margin:0;text-wrap:balance}
.cr-cta--band{background:var(--cr-cta-ink);color:var(--cr-cta);box-shadow:0 8px 22px -10px rgba(0,0,0,.4)}

/* link hover on listing/article titles -> theme CTA hue */
main.wrap h2 a,main.wrap h3 a{transition:color .2s ease}
main.wrap h2 a:hover,main.wrap h3 a:hover{color:var(--cr-cta)}

/* ===== motion (only under html.anim, i.e. JS on + motion allowed) ===== */
html.anim .reveal{opacity:0;transform:translateY(26px);
 transition:opacity .7s ease,transform .75s cubic-bezier(.22,.61,.36,1)}
html.anim .reveal.in{opacity:1;transform:none}
html.anim .cr-banner__inner{opacity:0;transform:translateY(16px)}
html.anim .cr-banner__inner.in{opacity:1;transform:none;
 transition:opacity .8s .05s ease,transform .85s .05s cubic-bezier(.22,.61,.36,1)}
html.anim .cr-fab{opacity:0;transform:translateY(10px) scale(.96)}
html.anim .cr-fab.show{opacity:1;transform:none;transition:opacity .5s ease,transform .5s cubic-bezier(.22,.61,.36,1)}

@media (prefers-reduced-motion: reduce){
  html{scroll-behavior:auto}
  .cr-cta,.cr-cta span,.cr-fab,.cr-fab span{transition:none}
}
@media (max-width:560px){ .cr-fab{right:14px;bottom:14px;padding:11px 16px;font-size:13px} }
"""


ANIM_JS = """/* Crosta motion layer. No-op (everything stays visible) if JS is off or the
   visitor prefers reduced motion. */
(function () {
  var mq = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  if (mq && mq.matches) return;
  var root = document.documentElement;
  root.classList.add('anim');

  function ready(fn){ document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn); }

  ready(function () {
    var targets = Array.prototype.slice.call(
      document.querySelectorAll('main.wrap > *:not([data-no-reveal])')
    );
    targets.forEach(function (el) { el.classList.add('reveal'); });

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target;
          el.style.transitionDelay = ((+el.dataset.crI || 0) * 70) + 'ms';
          el.classList.add('in');
          io.unobserve(el);
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
      targets.forEach(function (el, i) { el.dataset.crI = i % 5; io.observe(el); });
    } else {
      targets.forEach(function (el) { el.classList.add('in'); });
    }

    var bi = document.querySelector('.cr-banner__inner');
    if (bi) requestAnimationFrame(function () { bi.classList.add('in'); });

    var fab = document.querySelector('.cr-fab');
    if (fab) setTimeout(function () { fab.classList.add('show'); }, 400);

    var media = document.querySelector('.cr-banner__media');
    if (media) {
      var ticking = false;
      window.addEventListener('scroll', function () {
        if (ticking) return; ticking = true;
        requestAnimationFrame(function () {
          var y = window.pageYOffset || 0;
          media.style.transform = 'translateY(' + Math.min(y * 0.22, 70) + 'px)';
          ticking = false;
        });
      }, { passive: true });
    }
  });
})();
"""


def cr_banner_partial():
    return '''{{ $home := .IsHome }}
<section class="cr-banner{{ if not $home }} cr-banner--slim{{ end }}" data-no-reveal>
  <div class="cr-banner__media">
    {{ with .Site.Params.bannerImage }}<img class="cr-banner__img" src="{{ . | relURL }}" alt="">{{ end }}
    {{ if not .Site.Params.bannerImage }}<span class="cr-banner__ph">Banner placeholder · set params.bannerImage</span>{{ end }}
  </div>
  <div class="cr-banner__inner">
    <p class="cr-banner__eyebrow">{{ .Site.Params.brand }}</p>
    <h2 class="cr-banner__title">{{ .Site.Params.tagline }}</h2>
    <a class="cr-cta cr-cta--hero" href="{{ .Site.Params.brandURL }}" target="_blank" rel="noopener">Check us out <span aria-hidden="true">&#8599;</span></a>
  </div>
</section>
'''


def cr_band_partial():
    return '''<section class="cr-band" data-no-reveal>
  <div class="cr-band__inner">
    <p class="cr-band__t">Hungry yet? Come taste it.</p>
    <a class="cr-cta cr-cta--band" href="{{ .Site.Params.brandURL }}" target="_blank" rel="noopener">Check us out <span aria-hidden="true">&#8599;</span></a>
  </div>
</section>
'''


def cr_fab_partial():
    return '''<a class="cr-fab" href="{{ .Site.Params.brandURL }}" target="_blank" rel="noopener" aria-label="Check out Pizzeria Crosta">Check us out <span aria-hidden="true">&#8599;</span></a>
'''


BASEOF_TMPL = '''<!DOCTYPE html>
<html lang="{{ .Site.LanguageCode | default "en" }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} · {{ .Site.Title }}{{ end }}</title>
  <meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  __FONTS__
  <link rel="stylesheet" href="{{ "style.css" | relURL }}">
</head>
<body class="t-__SLUG__">
  {{ partial "header.html" . }}
  {{ partial "cr_banner.html" . }}
  <main class="wrap">
    {{ block "main" . }}{{ end }}
  </main>
  {{ partial "cr_band.html" . }}
  {{ partial "footer.html" . }}
  {{ partial "cr_fab.html" . }}
  <script src="{{ "anim.js" | relURL }}" defer></script>
</body>
</html>
'''


def baseof(slug, fonts):
    return BASEOF_TMPL.replace("__FONTS__", fonts).replace("__SLUG__", slug)


def header(brandline_html):
    return ('<header class="site-head">\n  <div class="site-head__inner">\n    '
            + brandline_html + '\n  </div>\n</header>\n')


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
    (t / "layouts" / "partials" / "cr_banner.html").write_text(cr_banner_partial())
    (t / "layouts" / "partials" / "cr_band.html").write_text(cr_band_partial())
    (t / "layouts" / "partials" / "cr_fab.html").write_text(cr_fab_partial())
    (t / "static" / "style.css").write_text(css + tokens_css(slug) + SHARED_CSS)
    (t / "static" / "anim.js").write_text(ANIM_JS)
    print(f"  built theme: {slug}")


if __name__ == "__main__":
    import build_themes_defs as defs
    defs.build(write_theme, header, footer)
    print(f"\nBuilt {len(list(THEMES.iterdir()))} themes under themes/")
