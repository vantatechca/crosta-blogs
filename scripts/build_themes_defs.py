#!/usr/bin/env python3
"""Per-theme design definitions. Each theme: distinct palette, type pairing, and
bespoke homepage. Plain strings (not f-strings) so Hugo {{ }} passes through literally."""

THEMES = []
def T(**kw): THEMES.append(kw)

def build(write_theme, header, footer):
    for th in THEMES:
        write_theme(
            th["slug"], th["desc"], th["fonts"], th.get("brandline", ""),
            th["css"], th["index"], th.get("header"), th.get("footer"),
        )

# Shared homepage data preamble (posts only; featured/top from frontmatter).
PRE = (
'{{ $posts := where .Site.RegularPages "Section" "posts" }}\n'
'{{ $featured := where $posts "Params.featured" true }}\n'
'{{ $top := where $posts "Params.top" true }}\n'
'{{ $lead := index $featured 0 }}\n'
)

# ============================================================ 1. THE CROSTA JOURNAL
# Literary culinary review. Paper-white, ink, deep teal-ink accent. Fraunces + Spectral.
# Signature: drop-cap lead essay on a narrow measure; italic deks; thin ink rules.
T(
slug="journal",
desc="The Crosta Journal — literary culinary review",
fonts='<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Spectral:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">',
brandline=(
'<a class="jm-word" href="{{ "/" | relURL }}">The Crosta Journal</a>\n'
'<p class="jm-tag">{{ .Site.Params.tagline }}</p>\n'
'<hr class="jm-rule">'
),
css='''
:root{--ink:#16211f;--paper:#fbfaf7;--accent:#15605a;--soft:#6c736f;--line:#d9d6cd}
*{box-sizing:border-box}
body.t-journal{margin:0;background:var(--paper);color:var(--ink);
 font-family:"Spectral",Georgia,serif;font-size:19px;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:1140px;margin:0 auto;padding:0 28px 80px}
.site-head__inner{max-width:1140px;margin:0 auto;padding:48px 28px 0;text-align:center}
.jm-word{display:block;font-family:"Fraunces",serif;font-weight:600;font-size:clamp(34px,6vw,60px);
 letter-spacing:-.02em;text-decoration:none;line-height:1}
.jm-tag{font-style:italic;color:var(--soft);margin:.6em 0 1.4em;font-size:18px}
.jm-rule{border:0;border-top:1px solid var(--ink);margin:0}
.site-foot__inner{max-width:1140px;margin:0 auto;padding:40px 28px;border-top:1px solid var(--line);
 display:flex;justify-content:space-between;color:var(--soft);font-size:15px;font-style:italic}
/* lead essay */
.lead{display:grid;grid-template-columns:1fr;max-width:680px;margin:56px auto 0;text-align:center}
.lead__kicker{font-family:"Fraunces",serif;font-size:13px;letter-spacing:.22em;text-transform:uppercase;
 color:var(--accent);margin:0 0 18px}
.lead__title{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(32px,5.2vw,52px);
 line-height:1.08;letter-spacing:-.02em;margin:0}
.lead__title a{text-decoration:none}
.lead__dek{font-style:italic;color:var(--soft);font-size:21px;margin:18px 0 0}
.lead__body{text-align:left;margin:34px auto 0;max-width:600px}
.lead__body p:first-of-type::first-letter{font-family:"Fraunces",serif;font-weight:600;float:left;
 font-size:74px;line-height:.74;padding:6px 12px 0 0;color:var(--accent)}
.lead__more{display:inline-block;margin-top:10px;font-style:italic;color:var(--accent)}
/* featured pair */
.collection{margin:72px 0 0;border-top:1px solid var(--ink);padding-top:14px}
.collection__label{font-family:"Fraunces",serif;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--soft);margin:0 0 24px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:48px}
.pair__item h3{font-family:"Fraunces",serif;font-weight:600;font-size:25px;line-height:1.15;margin:0 0 8px}
.pair__item h3 a{text-decoration:none}
.pair__item p{color:var(--soft);margin:0}
/* index */
.index{margin:64px 0 0;border-top:1px solid var(--ink);padding-top:14px}
.index__row{display:grid;grid-template-columns:120px 1fr;gap:24px;padding:18px 0;border-bottom:1px solid var(--line);align-items:baseline}
.index__row a{text-decoration:none;font-family:"Fraunces",serif;font-size:21px}
.index__date{color:var(--soft);font-style:italic;font-size:15px}
/* article */
.post{max-width:680px;margin:56px auto 0}
.post__eyebrow span{color:var(--accent);font-family:"Fraunces",serif;font-size:13px;letter-spacing:.12em}
.post__title{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(30px,5vw,46px);line-height:1.1;margin:.2em 0}
.post__dek{font-style:italic;color:var(--soft);font-size:21px}
.post__meta{color:var(--soft);font-size:14px;letter-spacing:.04em;text-transform:uppercase;font-family:"Fraunces",serif}
.post__body{margin-top:28px}
.post__body p:first-of-type::first-letter{font-family:"Fraunces",serif;font-weight:600;float:left;font-size:68px;line-height:.74;padding:6px 12px 0 0;color:var(--accent)}
.post__back{display:inline-block;margin-top:40px;font-style:italic;color:var(--accent)}
.archive{max-width:760px;margin:48px auto 0}
.archive__title{font-family:"Fraunces",serif;font-size:40px}
.archive__item{list-style:none;padding:16px 0;border-bottom:1px solid var(--line)}
.archive__list{padding:0}
.archive__name{font-family:"Fraunces",serif;font-size:22px;display:block}
.archive__date{color:var(--soft);font-style:italic;font-size:14px}
.archive__sum{color:var(--soft);margin:.3em 0 0}
@media(max-width:720px){.pair{grid-template-columns:1fr;gap:32px}.index__row{grid-template-columns:1fr}}
''',
index=PRE + '''{{ define "main" }}
{{ with $lead }}
<article class="lead">
  <p class="lead__kicker">The Lead Essay</p>
  <h2 class="lead__title"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
  {{ with .Params.summary }}<p class="lead__dek">{{ . }}</p>{{ end }}
  <div class="lead__body">{{ .Summary }}<a class="lead__more" href="{{ .RelPermalink }}">Continue reading →</a></div>
</article>
{{ end }}

{{ $rest := after 1 $featured }}
{{ with $rest }}
<section class="collection">
  <p class="collection__label">From the Journal</p>
  <div class="pair">
    {{ range first 2 . }}
    <div class="pair__item">
      <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
      <p>{{ .Params.summary }}</p>
    </div>
    {{ end }}
  </div>
</section>
{{ end }}

<section class="index">
  <p class="collection__label">The Index</p>
  {{ range first 10 $posts }}
  <div class="index__row">
    <span class="index__date">{{ .Date.Format "Jan 2, 2006" }}</span>
    <a href="{{ .RelPermalink }}">{{ .Title }}</a>
  </div>
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 2. STORIES FROM THE STONE OVEN
# Dark hearth. Charcoal stone ground, warm cream text, ember-orange glow. Lora + Source Serif.
# Signature: full-bleed dark hero with a glowing ember rule; story cards stacked like logs.
T(
slug="stoneoven",
desc="Stories from the Stone Oven — dark hearth storytelling",
fonts='<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;1,500&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">',
header_html='''<header class="site-head so-hero">
  <div class="so-hero__glow"></div>
  <div class="site-head__inner">
    <a class="so-word" href="{{ "/" | relURL }}">Stories from the<br><em>Stone Oven</em></a>
    <p class="so-tag">{{ .Site.Params.tagline }}</p>
    <span class="so-ember"></span>
  </div>
</header>
''',
css='''
:root{--stone:#211d19;--stone2:#2c2722;--cream:#efe7da;--ember:#e07a37;--ember2:#f2a65a;--soft:#a99b89;--line:#3a342d}
*{box-sizing:border-box}
body.t-stoneoven{margin:0;background:var(--stone);color:var(--cream);
 font-family:"Source Serif 4",Georgia,serif;font-size:18px;line-height:1.75}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 28px 90px}
.so-hero{position:relative;overflow:hidden;background:radial-gradient(120% 90% at 50% -10%,#3a302568,transparent 60%),var(--stone)}
.so-hero__glow{position:absolute;left:50%;bottom:-160px;transform:translateX(-50%);width:680px;height:300px;
 background:radial-gradient(closest-side,#e07a3733,transparent);filter:blur(10px);pointer-events:none}
.site-head__inner{position:relative;max-width:1080px;margin:0 auto;padding:90px 28px 56px;text-align:center}
.so-word{display:block;font-family:"Lora",serif;font-weight:600;font-size:clamp(34px,6.5vw,68px);line-height:1.02;
 text-decoration:none;letter-spacing:-.01em}
.so-word em{color:var(--ember2);font-style:italic}
.so-tag{color:var(--soft);font-style:italic;font-size:19px;margin:22px 0 26px}
.so-ember{display:block;width:160px;height:3px;margin:0 auto;border-radius:3px;
 background:linear-gradient(90deg,transparent,var(--ember),var(--ember2),var(--ember),transparent);
 box-shadow:0 0 18px #e07a3788}
.site-foot__inner{max-width:1080px;margin:0 auto;padding:44px 28px;border-top:1px solid var(--line);
 display:flex;justify-content:space-between;color:var(--soft);font-size:15px}
/* featured stories — stacked logs */
.tales{margin:64px 0 0;display:grid;gap:2px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.tale{background:var(--stone2);padding:34px 32px;display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:start;transition:background .2s}
.tale:hover{background:#332d27}
.tale__no{font-family:"Lora",serif;font-size:40px;color:var(--ember);font-style:italic;line-height:1}
.tale__t{font-family:"Lora",serif;font-weight:600;font-size:27px;margin:0 0 8px;line-height:1.15}
.tale__t a{text-decoration:none}
.tale__s{color:var(--soft);margin:0}
.tale__meta{color:var(--ember2);font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:10px 0 0}
/* more list */
.embers{margin:60px 0 0}
.embers__h{font-family:"Lora",serif;font-style:italic;color:var(--ember2);font-size:15px;letter-spacing:.18em;text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:12px}
.ember-row{display:flex;justify-content:space-between;gap:20px;padding:18px 0;border-bottom:1px solid var(--line)}
.ember-row a{font-family:"Lora",serif;font-size:21px;text-decoration:none}
.ember-row span{color:var(--soft);font-style:italic;white-space:nowrap}
/* article */
.post{max-width:700px;margin:60px auto 0}
.post__eyebrow span{color:var(--ember2);font-size:13px;letter-spacing:.1em}
.post__title{font-family:"Lora",serif;font-weight:600;font-size:clamp(30px,5vw,48px);line-height:1.1;margin:.2em 0}
.post__dek{color:var(--soft);font-style:italic;font-size:21px}
.post__meta{color:var(--ember);font-size:13px;letter-spacing:.12em;text-transform:uppercase}
.post__body{margin-top:26px}
.post__back{display:inline-block;margin-top:40px;color:var(--ember2);font-style:italic}
.archive{max-width:760px;margin:48px auto 0}
.archive__title{font-family:"Lora",serif;font-size:40px;color:var(--ember2)}
.archive__list{padding:0}
.archive__item{list-style:none;padding:18px 0;border-bottom:1px solid var(--line)}
.archive__name{font-family:"Lora",serif;font-size:22px;display:block}
.archive__date{color:var(--soft);font-style:italic;font-size:14px}
.archive__sum{color:var(--soft);margin:.3em 0 0}
@media(max-width:680px){.tale{grid-template-columns:1fr;gap:8px}.tale__no{font-size:28px}}
''',
index=PRE + '''{{ define "main" }}
{{ with $featured }}
<section class="tales">
  {{ range $i, $p := first 4 . }}
  <article class="tale">
    <div class="tale__no">{{ printf "%02d" (add $i 1) }}</div>
    <div>
      <h2 class="tale__t"><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h2>
      <p class="tale__s">{{ $p.Params.summary }}</p>
      <p class="tale__meta">{{ $p.Date.Format "January 2006" }}</p>
    </div>
  </article>
  {{ end }}
</section>
{{ end }}

<section class="embers">
  <p class="embers__h">More from the hearth</p>
  {{ range first 8 $posts }}
  <div class="ember-row">
    <a href="{{ .RelPermalink }}">{{ .Title }}</a>
    <span>{{ .Date.Format "Jan 2" }}</span>
  </div>
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 3. CRUST & CRUMB
# Clean minimal Scandinavian bakery. White, near-black, soft wheat accent. Hanken Grotesk + space.
# Signature: precise centered wordmark, generous air, fine hairlines, restrained 2-col grid.
T(
slug="crustcrumb",
desc="Crust & Crumb — minimal bakery-science notes",
fonts='<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;800&family=Newsreader:ital,opsz@1,6..72&display=swap" rel="stylesheet">',
brandline=(
'<a class="cc-word" href="{{ "/" | relURL }}">Crust&nbsp;<span>&amp;</span>&nbsp;Crumb</a>\n'
'<p class="cc-tag">{{ .Site.Params.tagline }}</p>'
),
css='''
:root{--ink:#141414;--paper:#ffffff;--wheat:#bc9a4a;--soft:#8a8a85;--line:#e9e7e1}
*{box-sizing:border-box}
body.t-crustcrumb{margin:0;background:var(--paper);color:var(--ink);
 font-family:"Hanken Grotesk",system-ui,sans-serif;font-size:17px;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:980px;margin:0 auto;padding:0 32px 120px}
.site-head__inner{max-width:980px;margin:0 auto;padding:96px 32px 0;text-align:center}
.cc-word{display:inline-block;font-weight:800;font-size:clamp(30px,5vw,46px);letter-spacing:-.03em;text-decoration:none}
.cc-word span{color:var(--wheat);font-weight:500}
.cc-tag{color:var(--soft);font-size:16px;max-width:440px;margin:14px auto 0;line-height:1.5}
.site-foot__inner{max-width:980px;margin:0 auto;padding:48px 32px;border-top:1px solid var(--line);
 display:flex;justify-content:space-between;color:var(--soft);font-size:13px;letter-spacing:.02em}
/* hero: single featured, ultra-minimal */
.cc-hero{margin:88px auto 0;text-align:center;max-width:640px}
.cc-hero__no{font-family:"Newsreader",serif;font-style:italic;color:var(--wheat);font-size:16px;margin:0 0 18px}
.cc-hero__t{font-weight:800;font-size:clamp(28px,4.6vw,42px);line-height:1.12;letter-spacing:-.025em;margin:0}
.cc-hero__t a{text-decoration:none}
.cc-hero__s{color:var(--soft);font-size:18px;margin:18px 0 0}
.cc-hero__link{display:inline-block;margin-top:22px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;border-bottom:1px solid var(--ink);padding-bottom:3px;text-decoration:none}
/* grid */
.cc-sec{margin:110px 0 0}
.cc-sec__h{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--ink);padding-bottom:12px;margin-bottom:0}
.cc-sec__h h2{font-size:13px;letter-spacing:.2em;text-transform:uppercase;font-weight:600;margin:0}
.cc-sec__h .ct{margin-left:auto;color:var(--soft);font-size:12px}
.cc-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 56px}
.cc-card{padding:38px 0;border-bottom:1px solid var(--line)}
.cc-card__idx{font-family:"Newsreader",serif;font-style:italic;color:var(--wheat);font-size:15px}
.cc-card h3{font-weight:600;font-size:22px;letter-spacing:-.01em;line-height:1.2;margin:8px 0 8px}
.cc-card h3 a{text-decoration:none}
.cc-card p{color:var(--soft);margin:0;font-size:15.5px}
.cc-card__date{display:block;margin-top:14px;color:var(--soft);font-size:12px;letter-spacing:.1em;text-transform:uppercase}
/* article */
.post{max-width:660px;margin:80px auto 0}
.post__eyebrow span{color:var(--wheat);font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.post__title{font-weight:800;font-size:clamp(28px,4.6vw,40px);letter-spacing:-.025em;line-height:1.12;margin:.3em 0}
.post__dek{color:var(--soft);font-size:19px}
.post__meta{color:var(--soft);font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.post__body{margin-top:26px;font-size:17px}
.post__back{display:inline-block;margin-top:44px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;text-decoration:none;border-bottom:1px solid var(--ink);padding-bottom:3px}
.archive{max-width:680px;margin:64px auto 0}
.archive__title{font-weight:800;font-size:34px;letter-spacing:-.02em}
.archive__list{padding:0}
.archive__item{list-style:none;padding:22px 0;border-bottom:1px solid var(--line)}
.archive__name{font-weight:600;font-size:20px;display:block}
.archive__date{color:var(--soft);font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.archive__sum{color:var(--soft);margin:.3em 0 0;font-size:15px}
@media(max-width:680px){.cc-grid{grid-template-columns:1fr;gap:0}}
''',
index=PRE + '''{{ define "main" }}
{{ with $lead }}
<section class="cc-hero">
  <p class="cc-hero__no">Featured</p>
  <h1 class="cc-hero__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h1>
  <p class="cc-hero__s">{{ .Params.summary }}</p>
  <a class="cc-hero__link" href="{{ .RelPermalink }}">Read the note</a>
</section>
{{ end }}

{{ $top4 := after 1 $featured }}
{{ with $top4 }}
<section class="cc-sec">
  <div class="cc-sec__h"><h2>Selected notes</h2><span class="ct">{{ len $posts }} in total</span></div>
  <div class="cc-grid">
    {{ range $i, $p := . }}
    <article class="cc-card">
      <span class="cc-card__idx">{{ printf "%02d" (add $i 2) }}</span>
      <h3><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h3>
      <p>{{ $p.Params.summary }}</p>
      <span class="cc-card__date">{{ $p.Date.Format "02 Jan 2006" }}</span>
    </article>
    {{ end }}
  </div>
</section>
{{ end }}
{{ end }}
''',
)

# ============================================================ 4. THE DAILY SLICE
# Newsstand. Oswald condensed heds + PT Serif body. News-red. Masthead w/ date+edition.
# Signature: edition masthead, top-story+sidebar split, dense 3-col recent grid, red kickers.
T(
slug="dailyslice",
desc="The Daily Slice — pizza newsstand",
fonts='<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=PT+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">',
header_html='''<header class="site-head ds-mast">
  <div class="site-head__inner">
    <div class="ds-mast__top">
      <span>{{ now.Format "Monday, January 2, 2006" }}</span>
      <span>Pizzeria Crosta · Edition No. {{ now.Format "06" }}</span>
    </div>
    <a class="ds-word" href="{{ "/" | relURL }}">The Daily Slice</a>
    <p class="ds-tag">{{ .Site.Params.tagline }}</p>
  </div>
</header>
''',
css='''
:root{--ink:#16140f;--paper:#fcfbf7;--red:#c41f1f;--soft:#6f6a60;--line:#d7d2c6;--rule:#16140f}
*{box-sizing:border-box}
body.t-dailyslice{margin:0;background:var(--paper);color:var(--ink);font-family:"PT Serif",Georgia,serif;font-size:17px;line-height:1.6}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px 90px}
.ds-mast{border-bottom:4px double var(--rule)}
.site-head__inner{max-width:1180px;margin:0 auto;padding:14px 24px 18px}
.ds-mast__top{display:flex;justify-content:space-between;font-family:"Oswald",sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--soft);border-bottom:1px solid var(--line);padding-bottom:10px}
.ds-word{display:block;text-align:center;font-family:"Oswald",sans-serif;font-weight:700;font-size:clamp(40px,8vw,86px);letter-spacing:-.01em;text-decoration:none;margin:14px 0 4px;text-transform:uppercase}
.ds-tag{text-align:center;font-style:italic;color:var(--soft);margin:0}
.site-foot__inner{max-width:1180px;margin:0 auto;padding:30px 24px;border-top:4px double var(--rule);display:flex;justify-content:space-between;font-family:"Oswald",sans-serif;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft)}
/* front page split */
.ds-front{display:grid;grid-template-columns:2fr 1fr;gap:0 40px;margin-top:36px;border-bottom:1px solid var(--rule);padding-bottom:36px}
.ds-lead__kicker{font-family:"Oswald",sans-serif;color:var(--red);font-weight:600;font-size:13px;letter-spacing:.14em;text-transform:uppercase}
.ds-lead__t{font-family:"Oswald",sans-serif;font-weight:700;font-size:clamp(30px,4.6vw,52px);line-height:1.02;margin:.15em 0 .2em;text-transform:uppercase;letter-spacing:-.01em}
.ds-lead__t a{text-decoration:none}
.ds-lead__d{font-size:20px;color:#332f28}
.ds-lead p:last-child{color:var(--soft)}
.ds-side{border-left:1px solid var(--line);padding-left:34px}
.ds-side__h{font-family:"Oswald",sans-serif;font-weight:600;font-size:13px;letter-spacing:.14em;text-transform:uppercase;border-bottom:2px solid var(--rule);padding-bottom:8px;margin:0 0 10px}
.ds-side__row{padding:14px 0;border-bottom:1px solid var(--line)}
.ds-side__row a{font-family:"Oswald",sans-serif;font-weight:500;font-size:19px;line-height:1.12;text-decoration:none;display:block}
.ds-side__row span{font-size:13px;color:var(--soft);font-style:italic}
/* recent grid */
.ds-more{margin-top:34px}
.ds-more__h{font-family:"Oswald",sans-serif;font-weight:600;color:var(--red);font-size:13px;letter-spacing:.14em;text-transform:uppercase;border-bottom:2px solid var(--rule);padding-bottom:8px}
.ds-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0 32px}
.ds-cell{padding:22px 0;border-bottom:1px solid var(--line)}
.ds-cell h3{font-family:"Oswald",sans-serif;font-weight:500;font-size:21px;line-height:1.12;margin:0 0 6px}
.ds-cell h3 a{text-decoration:none}
.ds-cell p{margin:0;color:var(--soft);font-size:15px}
.ds-cell__date{font-family:"Oswald",sans-serif;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
/* article */
.post{max-width:720px;margin:40px auto 0}
.post__eyebrow span{font-family:"Oswald",sans-serif;color:var(--red);font-size:12px;letter-spacing:.12em;text-transform:uppercase}
.post__title{font-family:"Oswald",sans-serif;font-weight:700;font-size:clamp(30px,5vw,52px);line-height:1.04;text-transform:uppercase;margin:.15em 0}
.post__dek{font-size:21px;color:#332f28;font-style:italic}
.post__meta{font-family:"Oswald",sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--soft)}
.post__body{margin-top:24px;column-gap:40px}
.post__body p:first-of-type::first-letter{font-family:"Oswald",sans-serif;font-weight:700;float:left;font-size:62px;line-height:.8;padding:4px 10px 0 0;color:var(--red)}
.post__back{font-family:"Oswald",sans-serif;display:inline-block;margin-top:36px;color:var(--red);text-transform:uppercase;letter-spacing:.08em;font-size:14px;text-decoration:none}
.archive{max-width:820px;margin:36px auto 0}
.archive__title{font-family:"Oswald",sans-serif;font-weight:700;text-transform:uppercase;font-size:42px}
.archive__list{padding:0}
.archive__item{list-style:none;padding:18px 0;border-bottom:1px solid var(--line)}
.archive__name{font-family:"Oswald",sans-serif;font-weight:500;font-size:22px;display:block}
.archive__date{font-family:"Oswald",sans-serif;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
.archive__sum{color:var(--soft);margin:.3em 0 0}
@media(max-width:860px){.ds-front{grid-template-columns:1fr}.ds-side{border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:20px}.ds-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.ds-grid{grid-template-columns:1fr}}
''',
index=PRE + '''{{ define "main" }}
<section class="ds-front">
  <div class="ds-lead">
    {{ with $lead }}
    <p class="ds-lead__kicker">Top Story</p>
    <h2 class="ds-lead__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
    <p class="ds-lead__d">{{ .Params.summary }}</p>
    <p>{{ .Summary }}</p>
    {{ end }}
  </div>
  <aside class="ds-side">
    <p class="ds-side__h">Today's Headlines</p>
    {{ range first 4 $top }}
    <div class="ds-side__row"><a href="{{ .RelPermalink }}">{{ .Title }}</a><span>{{ .Date.Format "Jan 2" }}</span></div>
    {{ end }}
  </aside>
</section>

<section class="ds-more">
  <p class="ds-more__h">More from the kitchen</p>
  <div class="ds-grid">
    {{ range first 6 $posts }}
    <article class="ds-cell">
      <span class="ds-cell__date">{{ .Date.Format "Jan 2" }}</span>
      <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
      <p>{{ .Params.summary }}</p>
    </article>
    {{ end }}
  </div>
</section>
{{ end }}
''',
)

# ============================================================ 5. NOTES FROM THE PASS
# Kitchen docket / chef's notebook. Mono headers + humanist body. Stamp-red. Docket cards.
# Signature: perforated ticket top edge, dashed dockets, FIRE/ON THE PASS stamps, order nums.
T(
slug="notespass",
desc="Notes from the Pass — kitchen docket notebook",
fonts='<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Spline+Sans:wght@400;500;600&display=swap" rel="stylesheet">',
brandline=(
'<div class="np-ticket-edge"></div>\n'
'<a class="np-word" href="{{ "/" | relURL }}">NOTES FROM THE PASS</a>\n'
'<p class="np-tag">{{ .Site.Params.tagline }}</p>'
),
css='''
:root{--paper:#f4f1e7;--ink:#1e1b14;--stamp:#b1342b;--blue:#3a5a78;--soft:#736d5f;--line:#cbc5b4}
*{box-sizing:border-box}
body.t-notespass{margin:0;background:var(--paper);color:var(--ink);font-family:"Spline Sans",system-ui,sans-serif;font-size:16.5px;line-height:1.65;
 background-image:repeating-linear-gradient(0deg,transparent,transparent 31px,#cbc5b440 31px,#cbc5b440 32px)}
a{color:inherit}
.wrap{max-width:920px;margin:0 auto;padding:0 24px 90px}
.site-head__inner{max-width:920px;margin:0 auto;padding:0 24px;text-align:center;position:relative}
.np-ticket-edge{height:14px;background:radial-gradient(circle at 7px 14px,transparent 7px,var(--paper) 7px) repeat-x;background-size:14px 14px;background-position:0 0;margin:0 -100vw;border-top:2px solid var(--ink)}
.np-word{display:inline-block;font-family:"Space Mono",monospace;font-weight:700;font-size:clamp(22px,4vw,40px);letter-spacing:.04em;text-decoration:none;margin:40px 0 6px}
.np-tag{font-family:"Space Mono",monospace;color:var(--soft);font-size:13px;margin:0 0 8px}
.site-foot__inner{max-width:920px;margin:0 auto;padding:30px 24px;border-top:2px dashed var(--line);display:flex;justify-content:space-between;font-family:"Space Mono",monospace;font-size:12px;color:var(--soft)}
/* dockets */
.np-stack{margin-top:40px;display:grid;gap:26px}
.np-docket{background:#fbf9f1;border:1.5px dashed var(--ink);border-radius:3px;padding:22px 24px;position:relative;box-shadow:3px 4px 0 #1e1b1410}
.np-docket__bar{display:flex;justify-content:space-between;align-items:center;font-family:"Space Mono",monospace;font-size:12px;letter-spacing:.06em;color:var(--soft);border-bottom:1.5px dashed var(--line);padding-bottom:10px;margin-bottom:12px}
.np-stamp{font-family:"Space Mono",monospace;font-weight:700;color:var(--stamp);border:2px solid var(--stamp);border-radius:3px;padding:2px 8px;transform:rotate(-3deg);font-size:11px;letter-spacing:.1em}
.np-docket__no{color:var(--blue);font-weight:700}
.np-docket h2{font-family:"Spline Sans",sans-serif;font-weight:600;font-size:24px;line-height:1.2;margin:0 0 8px}
.np-docket h2 a{text-decoration:none}
.np-docket p{margin:0;color:#403a2f}
.np-docket__chk{font-family:"Space Mono",monospace;font-size:12px;color:var(--soft);margin-top:12px}
.np-docket__chk b{color:var(--stamp)}
/* line list */
.np-line{margin-top:48px;border-top:2px dashed var(--ink);padding-top:8px}
.np-line__h{font-family:"Space Mono",monospace;font-size:12px;letter-spacing:.14em;color:var(--soft);text-transform:uppercase}
.np-line__row{display:flex;gap:14px;align-items:baseline;padding:12px 0;border-bottom:1px dashed var(--line);font-family:"Space Mono",monospace;font-size:14px}
.np-line__row .n{color:var(--blue);font-weight:700}
.np-line__row a{font-family:"Spline Sans",sans-serif;font-size:17px;text-decoration:none;flex:1}
.np-line__row .d{color:var(--soft)}
/* article */
.post{max-width:680px;margin:40px auto 0;background:#fbf9f1;border:1.5px dashed var(--ink);border-radius:3px;padding:34px}
.post__eyebrow span{font-family:"Space Mono",monospace;color:var(--stamp);font-size:12px;letter-spacing:.06em}
.post__title{font-family:"Spline Sans",sans-serif;font-weight:600;font-size:clamp(26px,4.4vw,38px);line-height:1.15;margin:.2em 0}
.post__dek{color:var(--soft);font-style:italic}
.post__meta{font-family:"Space Mono",monospace;font-size:12px;color:var(--soft)}
.post__body{margin-top:22px}
.post__back{font-family:"Space Mono",monospace;display:inline-block;margin-top:30px;color:var(--stamp);text-decoration:none}
.archive{max-width:760px;margin:40px auto 0}
.archive__title{font-family:"Spline Sans",sans-serif;font-weight:600;font-size:34px}
.archive__list{padding:0}
.archive__item{list-style:none;padding:16px 0;border-bottom:1px dashed var(--line)}
.archive__name{font-family:"Spline Sans",sans-serif;font-weight:600;font-size:20px;display:block}
.archive__date{font-family:"Space Mono",monospace;font-size:12px;color:var(--soft)}
.archive__sum{color:var(--soft);margin:.3em 0 0}
''',
index=PRE + '''{{ define "main" }}
<section class="np-stack">
  {{ range $i, $p := first 4 $featured }}
  <article class="np-docket">
    <div class="np-docket__bar">
      <span class="np-docket__no">ORDER #{{ printf "%03d" (add $i 1) }}</span>
      <span class="np-stamp">{{ if $p.Params.top }}FIRE{{ else }}ON THE PASS{{ end }}</span>
    </div>
    <h2><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h2>
    <p>{{ $p.Params.summary }}</p>
    <p class="np-docket__chk">{{ range $p.Params.tags }}<b>✓</b> {{ . }}&nbsp;&nbsp;{{ end }}· {{ $p.Date.Format "Mon Jan 2" }}</p>
  </article>
  {{ end }}
</section>

<section class="np-line">
  <p class="np-line__h">// service log</p>
  {{ range $i, $p := first 8 $posts }}
  <div class="np-line__row">
    <span class="n">{{ printf "%02d" (add $i 1) }}</span>
    <a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a>
    <span class="d">{{ $p.Date.Format "01/02" }}</span>
  </div>
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 6. FLOUR & FIRE
# Bold dark. Anton huge display + Archivo body. Fire GRADIENT (amber->crimson), not single acid.
# Signature: giant gradient hero headline, oversized numerals on featured rows, spark divider.
T(
slug="flourfire",
desc="Flour & Fire — bold dark fire-gradient",
fonts='<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">',
brandline=(
'<a class="ff-word" href="{{ "/" | relURL }}">FLOUR <span>&amp;</span> FIRE</a>\n'
'<p class="ff-tag">{{ .Site.Params.tagline }}</p>'
),
css='''
:root{--bg:#0c0a09;--bg2:#16110e;--cream:#f3ede4;--soft:#9a9088;--a1:#f59e0b;--a2:#dc2626;--line:#2a2320}
*{box-sizing:border-box}
body.t-flourfire{margin:0;background:var(--bg);color:var(--cream);font-family:"Archivo",system-ui,sans-serif;font-size:17px;line-height:1.7}
a{color:inherit}
.wrap{max-width:1100px;margin:0 auto;padding:0 26px 100px}
.site-head__inner{max-width:1100px;margin:0 auto;padding:70px 26px 30px;text-align:center}
.ff-word{display:inline-block;font-family:"Anton",sans-serif;font-size:clamp(44px,10vw,108px);letter-spacing:.01em;text-decoration:none;line-height:.92;text-transform:uppercase}
.ff-word span{background:linear-gradient(90deg,var(--a1),var(--a2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.ff-tag{color:var(--soft);font-style:italic;font-size:18px;margin:16px 0 0}
.site-foot__inner{max-width:1100px;margin:0 auto;padding:40px 26px;border-top:1px solid var(--line);display:flex;justify-content:space-between;color:var(--soft);font-size:14px}
/* hero lead */
.ff-lead{margin:44px 0 0;padding:44px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.ff-lead__k{font-family:"Anton",sans-serif;font-size:14px;letter-spacing:.2em;text-transform:uppercase;color:var(--a1)}
.ff-lead__t{font-family:"Anton",sans-serif;font-size:clamp(38px,8vw,92px);line-height:.96;text-transform:uppercase;margin:.1em 0 .15em;
 background:linear-gradient(110deg,var(--cream) 30%,var(--a1) 75%,var(--a2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.ff-lead__t a{text-decoration:none}
.ff-lead__d{color:var(--soft);font-size:21px;max-width:680px}
.ff-lead__more{display:inline-block;margin-top:16px;font-weight:600;color:var(--a1);text-decoration:none;letter-spacing:.04em}
/* featured big rows */
.ff-rows{margin-top:8px}
.ff-row{display:grid;grid-template-columns:auto 1fr auto;gap:30px;align-items:center;padding:30px 0;border-bottom:1px solid var(--line);transition:padding-left .2s}
.ff-row:hover{padding-left:10px}
.ff-row__no{font-family:"Anton",sans-serif;font-size:clamp(40px,7vw,80px);line-height:1;
 background:linear-gradient(180deg,var(--a1),var(--a2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.ff-row__t{font-family:"Anton",sans-serif;font-size:clamp(22px,3.4vw,34px);text-transform:uppercase;line-height:1.04;margin:0}
.ff-row__t a{text-decoration:none}
.ff-row__s{color:var(--soft);margin:6px 0 0;font-size:15.5px}
.ff-row__d{color:var(--a1);font-family:"Anton",sans-serif;font-size:13px;letter-spacing:.12em;text-transform:uppercase;white-space:nowrap}
.ff-spark{height:2px;margin:50px 0 0;background:linear-gradient(90deg,transparent,var(--a2),var(--a1),var(--a2),transparent);box-shadow:0 0 14px #f59e0b66}
.ff-recent__h{font-family:"Anton",sans-serif;font-size:14px;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);margin:30px 0 4px}
.ff-recent__row{display:flex;justify-content:space-between;gap:18px;padding:15px 0;border-bottom:1px solid var(--line)}
.ff-recent__row a{font-family:"Anton",sans-serif;font-size:21px;text-transform:uppercase;text-decoration:none}
.ff-recent__row span{color:var(--soft);white-space:nowrap}
/* article */
.post{max-width:720px;margin:50px auto 0}
.post__eyebrow span{color:var(--a1);font-family:"Anton",sans-serif;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
.post__title{font-family:"Anton",sans-serif;font-size:clamp(34px,6vw,64px);text-transform:uppercase;line-height:.98;margin:.12em 0;
 background:linear-gradient(110deg,var(--cream) 40%,var(--a1));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.post__dek{color:var(--soft);font-size:21px;font-style:italic}
.post__meta{color:var(--a1);font-family:"Anton",sans-serif;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
.post__body{margin-top:24px}
.post__back{display:inline-block;margin-top:38px;color:var(--a1);font-weight:600;text-decoration:none}
.archive{max-width:780px;margin:50px auto 0}
.archive__title{font-family:"Anton",sans-serif;font-size:46px;text-transform:uppercase;background:linear-gradient(110deg,var(--cream),var(--a1));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.archive__list{padding:0}
.archive__item{list-style:none;padding:18px 0;border-bottom:1px solid var(--line)}
.archive__name{font-family:"Anton",sans-serif;font-size:24px;text-transform:uppercase;display:block}
.archive__date{color:var(--a1);font-size:13px}
.archive__sum{color:var(--soft);margin:.3em 0 0}
@media(max-width:640px){.ff-row{grid-template-columns:auto 1fr;gap:18px}.ff-row__d{display:none}}
''',
index=PRE + '''{{ define "main" }}
{{ with $lead }}
<section class="ff-lead">
  <p class="ff-lead__k">Feature</p>
  <h2 class="ff-lead__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
  <p class="ff-lead__d">{{ .Params.summary }}</p>
  <a class="ff-lead__more" href="{{ .RelPermalink }}">Read it →</a>
</section>
{{ end }}

<section class="ff-rows">
  {{ range $i, $p := after 1 $featured }}
  <article class="ff-row">
    <div class="ff-row__no">{{ printf "%02d" (add $i 2) }}</div>
    <div>
      <h3 class="ff-row__t"><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h3>
      <p class="ff-row__s">{{ $p.Params.summary }}</p>
    </div>
    <div class="ff-row__d">{{ $p.Date.Format "Jan 2006" }}</div>
  </article>
  {{ end }}
</section>

<div class="ff-spark"></div>
<p class="ff-recent__h">Latest</p>
{{ range first 6 $posts }}
<div class="ff-recent__row"><a href="{{ .RelPermalink }}">{{ .Title }}</a><span>{{ .Date.Format "Jan 2" }}</span></div>
{{ end }}
{{ end }}
''',
)

# ============================================================ 7. THE CROSTA TABLE
# Elegant dining. Cormorant Garamond + Jost labels. Bone/walnut/gold. Menu aesthetic.
# Signature: menu-style featured rows with dotted leaders + course labels; refined centered hero.
T(
slug="crostatable",
desc="The Crosta Table — elegant hospitality / menu",
fonts='<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">',
brandline=(
'<p class="ct-over">Pizzeria Crosta presents</p>\n'
'<a class="ct-word" href="{{ "/" | relURL }}">The Crosta Table</a>\n'
'<p class="ct-tag">{{ .Site.Params.tagline }}</p>\n'
'<div class="ct-orn">✦</div>'
),
css='''
:root{--bone:#f4efe4;--walnut:#2c2017;--gold:#a9853f;--soft:#8a7c6b;--line:#ddd3c2}
*{box-sizing:border-box}
body.t-crostatable{margin:0;background:var(--bone);color:var(--walnut);font-family:"Cormorant Garamond",Georgia,serif;font-size:20px;line-height:1.65}
a{color:inherit}
.wrap{max-width:880px;margin:0 auto;padding:0 30px 110px}
.site-head__inner{max-width:880px;margin:0 auto;padding:74px 30px 0;text-align:center}
.ct-over{font-family:"Jost",sans-serif;font-weight:400;font-size:12px;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);margin:0 0 14px}
.ct-word{display:block;font-weight:500;font-size:clamp(40px,7vw,76px);letter-spacing:.01em;text-decoration:none;line-height:1}
.ct-tag{font-style:italic;color:var(--soft);font-size:21px;margin:14px 0 22px}
.ct-orn{color:var(--gold);font-size:18px;letter-spacing:.4em}
.site-foot__inner{max-width:880px;margin:0 auto;padding:40px 30px;border-top:1px solid var(--line);display:flex;justify-content:space-between;font-family:"Jost",sans-serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
/* featured lead — plated */
.ct-lead{text-align:center;max-width:600px;margin:60px auto 0}
.ct-lead__c{font-family:"Jost",sans-serif;font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold)}
.ct-lead__t{font-weight:600;font-size:clamp(32px,5vw,50px);line-height:1.08;margin:.25em 0}
.ct-lead__t a{text-decoration:none}
.ct-lead__d{font-style:italic;color:var(--soft);font-size:21px}
.ct-lead__more{font-family:"Jost",sans-serif;display:inline-block;margin-top:16px;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);text-decoration:none;border-bottom:1px solid var(--gold);padding-bottom:4px}
/* menu list */
.ct-menu{margin:72px 0 0}
.ct-menu__h{text-align:center;font-family:"Jost",sans-serif;font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:var(--soft);margin-bottom:8px}
.ct-menu__h::after{content:"";display:block;width:46px;height:1px;background:var(--gold);margin:14px auto 0}
.ct-item{display:grid;grid-template-columns:1fr auto;align-items:baseline;gap:0 14px;padding:22px 0;border-bottom:1px solid var(--line)}
.ct-item__lead{display:flex;align-items:baseline;gap:10px;min-width:0}
.ct-item__t{font-weight:600;font-size:26px;line-height:1.1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ct-item__t a{text-decoration:none}
.ct-item__dots{flex:1;border-bottom:1.5px dotted var(--line);transform:translateY(-5px);min-width:24px}
.ct-item__date{font-family:"Jost",sans-serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);white-space:nowrap}
.ct-item__s{grid-column:1/-1;color:var(--soft);font-style:italic;font-size:18px;margin:4px 0 0}
/* article */
.post{max-width:640px;margin:60px auto 0;text-align:center}
.post__eyebrow span{font-family:"Jost",sans-serif;color:var(--gold);font-size:11px;letter-spacing:.2em;text-transform:uppercase}
.post__title{font-weight:600;font-size:clamp(32px,5vw,52px);line-height:1.08;margin:.2em 0}
.post__dek{font-style:italic;color:var(--soft);font-size:22px}
.post__meta{font-family:"Jost",sans-serif;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
.post__body{margin-top:26px;text-align:left}
.post__back{font-family:"Jost",sans-serif;display:inline-block;margin-top:40px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);text-decoration:none}
.archive{max-width:700px;margin:56px auto 0;text-align:center}
.archive__title{font-weight:600;font-size:44px}
.archive__list{padding:0;text-align:left}
.archive__item{list-style:none;padding:20px 0;border-bottom:1px solid var(--line)}
.archive__name{font-weight:600;font-size:24px;display:block}
.archive__date{font-family:"Jost",sans-serif;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.archive__sum{color:var(--soft);font-style:italic;margin:.3em 0 0}
@media(max-width:560px){.ct-item__t{white-space:normal}.ct-item__dots{display:none}}
''',
index=PRE + '''{{ define "main" }}
{{ with $lead }}
<section class="ct-lead">
  <p class="ct-lead__c">Chef's Selection</p>
  <h2 class="ct-lead__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
  <p class="ct-lead__d">{{ .Params.summary }}</p>
  <a class="ct-lead__more" href="{{ .RelPermalink }}">Read</a>
</section>
{{ end }}

<section class="ct-menu">
  <p class="ct-menu__h">The Table</p>
  {{ range first 8 $posts }}
  <article class="ct-item">
    <div class="ct-item__lead">
      <span class="ct-item__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></span>
      <span class="ct-item__dots"></span>
    </div>
    <span class="ct-item__date">{{ .Date.Format "Jan 2" }}</span>
    <p class="ct-item__s">{{ .Params.summary }}</p>
  </article>
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 8. HOT OUT THE OVEN
# Playful & fun. Fredoka rounded + Nunito body. Tomato/basil/cheese multicolor. Chunky rounded cards.
# Signature: oven-timer badge "FRESH · 90s", sticker tags, staggered colorful card grid.
T(
slug="hotoven",
desc="Hot Out the Oven — playful & fresh",
fonts='<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">',
brandline=(
'<a class="ho-word" href="{{ "/" | relURL }}">Hot Out the Oven</a>\n'
'<p class="ho-tag">{{ .Site.Params.tagline }}</p>\n'
'<span class="ho-timer">● FRESH · OUT IN 90s</span>'
),
css='''
:root{--paper:#fffdf5;--ink:#2a2018;--tomato:#ef4444;--basil:#16a34a;--cheese:#f4b740;--soft:#8d8275;--card:#ffffff}
*{box-sizing:border-box}
body.t-hotoven{margin:0;background:var(--paper);color:var(--ink);font-family:"Nunito",system-ui,sans-serif;font-size:17px;line-height:1.65}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px 90px}
.site-head__inner{max-width:1080px;margin:0 auto;padding:64px 26px 0;text-align:center}
.ho-word{display:inline-block;font-family:"Fredoka",system-ui;font-weight:700;font-size:clamp(38px,7vw,72px);letter-spacing:-.01em;text-decoration:none;color:var(--tomato);transform:rotate(-1.5deg)}
.ho-tag{font-weight:600;color:var(--ink);font-size:19px;margin:12px 0 16px}
.ho-timer{display:inline-block;background:var(--ink);color:#fff;font-family:"Fredoka",system-ui;font-weight:600;font-size:13px;letter-spacing:.08em;padding:7px 16px;border-radius:999px}
.ho-timer::first-letter{color:var(--cheese)}
.site-foot__inner{max-width:1080px;margin:0 auto;padding:38px 26px;border-top:3px dotted var(--cheese);display:flex;justify-content:space-between;color:var(--soft);font-weight:600;font-size:14px}
/* hero card */
.ho-hero{margin:46px 0 0;background:var(--ink);color:#fff;border-radius:26px;padding:46px;position:relative;overflow:hidden}
.ho-hero::after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,var(--cheese),transparent 70%);opacity:.35}
.ho-hero__b{display:inline-block;background:var(--tomato);color:#fff;font-family:"Fredoka",system-ui;font-weight:600;font-size:12px;letter-spacing:.1em;padding:5px 14px;border-radius:999px;text-transform:uppercase}
.ho-hero__t{font-family:"Fredoka",system-ui;font-weight:700;font-size:clamp(30px,5vw,52px);line-height:1.05;margin:.25em 0 .2em}
.ho-hero__t a{text-decoration:none;color:#fff}
.ho-hero__d{color:#e6dccb;font-size:19px;max-width:560px}
.ho-hero__go{display:inline-block;margin-top:18px;background:var(--cheese);color:var(--ink);font-family:"Fredoka",system-ui;font-weight:600;padding:11px 22px;border-radius:999px;text-decoration:none}
/* card grid */
.ho-grid{margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}
.ho-card{background:var(--card);border:2px solid var(--ink);border-radius:22px;padding:26px;box-shadow:5px 6px 0 var(--ink);transition:transform .15s}
.ho-card:hover{transform:translate(-2px,-2px)}
.ho-card:nth-child(3n+1){box-shadow:5px 6px 0 var(--tomato)}
.ho-card:nth-child(3n+2){box-shadow:5px 6px 0 var(--basil)}
.ho-card:nth-child(3n){box-shadow:5px 6px 0 var(--cheese)}
.ho-card__tags{margin-bottom:10px}
.ho-card__tags span{display:inline-block;font-family:"Fredoka",system-ui;font-weight:500;font-size:11px;letter-spacing:.04em;text-transform:uppercase;padding:3px 10px;border-radius:999px;border:1.5px solid var(--ink);margin:0 5px 5px 0}
.ho-card h3{font-family:"Fredoka",system-ui;font-weight:600;font-size:23px;line-height:1.15;margin:0 0 8px}
.ho-card h3 a{text-decoration:none}
.ho-card p{margin:0;color:#4a4036;font-size:15.5px}
.ho-card__date{display:block;margin-top:14px;font-weight:700;color:var(--soft);font-size:13px}
/* article */
.post{max-width:680px;margin:46px auto 0;background:var(--card);border:2px solid var(--ink);border-radius:24px;padding:38px;box-shadow:6px 7px 0 var(--cheese)}
.post__eyebrow span{display:inline-block;background:var(--basil);color:#fff;font-family:"Fredoka",system-ui;font-size:11px;letter-spacing:.06em;padding:3px 10px;border-radius:999px;text-transform:uppercase;margin-right:5px}
.post__title{font-family:"Fredoka",system-ui;font-weight:700;font-size:clamp(28px,4.6vw,42px);line-height:1.1;margin:.3em 0}
.post__dek{color:var(--soft);font-weight:600;font-size:19px}
.post__meta{color:var(--soft);font-weight:700;font-size:13px}
.post__body{margin-top:22px}
.post__back{display:inline-block;margin-top:30px;background:var(--ink);color:#fff;font-family:"Fredoka",system-ui;padding:10px 20px;border-radius:999px;text-decoration:none}
.archive{max-width:760px;margin:46px auto 0}
.archive__title{font-family:"Fredoka",system-ui;font-weight:700;font-size:38px;color:var(--tomato)}
.archive__list{padding:0}
.archive__item{list-style:none;background:var(--card);border:2px solid var(--ink);border-radius:18px;padding:18px 22px;margin:0 0 14px;box-shadow:4px 5px 0 var(--cheese)}
.archive__name{font-family:"Fredoka",system-ui;font-weight:600;font-size:21px;display:block}
.archive__date{font-weight:700;color:var(--soft);font-size:13px}
.archive__sum{color:#4a4036;margin:.3em 0 0}
''',
index=PRE + '''{{ define "main" }}
{{ with $lead }}
<section class="ho-hero">
  <span class="ho-hero__b">🔥 Fresh batch</span>
  <h2 class="ho-hero__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
  <p class="ho-hero__d">{{ .Params.summary }}</p>
  <a class="ho-hero__go" href="{{ .RelPermalink }}">Dig in →</a>
</section>
{{ end }}

<section class="ho-grid">
  {{ range after 1 $featured }}
  <article class="ho-card">
    <div class="ho-card__tags">{{ range .Params.tags }}<span>{{ . }}</span>{{ end }}</div>
    <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
    <p>{{ .Params.summary }}</p>
    <span class="ho-card__date">{{ .Date.Format "Jan 2" }}</span>
  </article>
  {{ end }}
  {{ range first 3 (after 0 $posts) }}
  {{ if not .Params.featured }}
  <article class="ho-card">
    <div class="ho-card__tags">{{ range .Params.tags }}<span>{{ . }}</span>{{ end }}</div>
    <h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
    <p>{{ .Params.summary }}</p>
    <span class="ho-card__date">{{ .Date.Format "Jan 2" }}</span>
  </article>
  {{ end }}
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 9. FORNO DIARIES
# Personal Italian diary. Playfair Display italic datelines + EB Garamond body. Olive accent.
# Signature: vertical timeline of dated entries, big italic datelines, "Dear forno," openers.
T(
slug="fornodiaries",
desc="Forno Diaries — personal Italian diary",
fonts='<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">',
brandline=(
'<a class="fd-word" href="{{ "/" | relURL }}">Forno Diaries</a>\n'
'<p class="fd-tag">{{ .Site.Params.tagline }}</p>'
),
css='''
:root{--paper:#faf5ec;--ink:#2a201a;--olive:#5f6b3a;--soft:#857a6a;--line:#e0d8c8}
*{box-sizing:border-box}
body.t-fornodiaries{margin:0;background:var(--paper);color:var(--ink);font-family:"EB Garamond",Georgia,serif;font-size:19px;line-height:1.72}
a{color:inherit}
.wrap{max-width:760px;margin:0 auto;padding:0 28px 100px}
.site-head__inner{max-width:760px;margin:0 auto;padding:72px 28px 0;text-align:center}
.fd-word{display:inline-block;font-family:"Playfair Display",serif;font-style:italic;font-weight:500;font-size:clamp(38px,7vw,68px);text-decoration:none;line-height:1}
.fd-tag{color:var(--soft);font-style:italic;font-size:19px;margin:14px 0 10px}
.site-head__inner::after{content:"~";display:block;color:var(--olive);font-family:"Playfair Display",serif;font-size:28px}
.site-foot__inner{max-width:760px;margin:0 auto;padding:40px 28px;border-top:1px solid var(--line);display:flex;justify-content:space-between;color:var(--soft);font-style:italic;font-size:15px}
/* diary timeline */
.fd-diary{margin:54px 0 0;position:relative;padding-left:30px}
.fd-diary::before{content:"";position:absolute;left:6px;top:8px;bottom:8px;width:2px;background:var(--line)}
.fd-entry{position:relative;padding:0 0 44px}
.fd-entry::before{content:"";position:absolute;left:-30px;top:14px;width:11px;height:11px;border-radius:50%;background:var(--olive);box-shadow:0 0 0 4px var(--paper)}
.fd-entry__date{font-family:"Playfair Display",serif;font-style:italic;font-size:15px;letter-spacing:.04em;color:var(--olive);text-transform:uppercase}
.fd-entry__t{font-family:"Playfair Display",serif;font-weight:500;font-size:clamp(24px,4vw,34px);line-height:1.14;margin:.15em 0 .2em}
.fd-entry__t a{text-decoration:none}
.fd-entry__d{color:var(--soft);font-style:italic;margin:0 0 8px}
.fd-entry__b{margin:0}
.fd-entry__more{color:var(--olive);font-style:italic}
.fd-entry--feat .fd-entry__t{font-size:clamp(28px,4.6vw,40px)}
.fd-entry--feat::before{width:14px;height:14px;background:var(--ink)}
/* article */
.post{max-width:640px;margin:54px auto 0}
.post__eyebrow span{color:var(--olive);font-style:italic;font-size:15px}
.post__title{font-family:"Playfair Display",serif;font-weight:500;font-size:clamp(28px,5vw,44px);line-height:1.12;margin:.2em 0}
.post__dek{color:var(--soft);font-style:italic;font-size:21px}
.post__meta{font-family:"Playfair Display",serif;font-style:italic;color:var(--olive);font-size:15px}
.post__body{margin-top:24px}
.post__body p:first-of-type::first-letter{font-family:"Playfair Display",serif;font-style:italic;float:left;font-size:58px;line-height:.8;padding:8px 10px 0 0;color:var(--olive)}
.post__back{display:inline-block;margin-top:40px;color:var(--olive);font-style:italic}
.archive{max-width:680px;margin:54px auto 0}
.archive__title{font-family:"Playfair Display",serif;font-style:italic;font-weight:500;font-size:42px}
.archive__list{padding:0}
.archive__item{list-style:none;padding:20px 0;border-bottom:1px solid var(--line)}
.archive__name{font-family:"Playfair Display",serif;font-weight:500;font-size:24px;display:block}
.archive__date{color:var(--olive);font-style:italic;font-size:15px}
.archive__sum{color:var(--soft);font-style:italic;margin:.3em 0 0}
''',
index=PRE + '''{{ define "main" }}
<section class="fd-diary">
  {{ range $i, $p := first 8 $posts }}
  <article class="fd-entry{{ if $p.Params.featured }} fd-entry--feat{{ end }}">
    <p class="fd-entry__date">{{ $p.Date.Format "Monday, 2 January 2006" }}</p>
    <h2 class="fd-entry__t"><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h2>
    <p class="fd-entry__d">{{ $p.Params.summary }}</p>
    {{ if $p.Params.featured }}<p class="fd-entry__b">{{ $p.Summary }} <a class="fd-entry__more" href="{{ $p.RelPermalink }}">continue →</a></p>{{ end }}
  </article>
  {{ end }}
</section>
{{ end }}
''',
)

# ============================================================ 10. BEHIND THE CRUST
# Documentary BTS. Space Grotesk + Space Mono captions + Inter body. Charcoal/paper/cobalt.
# Signature: framed "plates" with mono credit captions (PLATE 01 / 06:14 / THE MIX), contact strip.
T(
slug="behindcrust",
desc="Behind the Crust — documentary / behind-the-scenes",
fonts='<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Inter:wght@400;500&display=swap" rel="stylesheet">',
brandline=(
'<div class="bc-mast">\n'
'  <a class="bc-word" href="{{ "/" | relURL }}">Behind the Crust</a>\n'
'  <span class="bc-rec">● REC</span>\n'
'</div>\n'
'<p class="bc-tag">{{ .Site.Params.tagline }}</p>'
),
css='''
:root{--paper:#f3f3f1;--ink:#1a1a18;--cobalt:#1f4ed8;--soft:#76746e;--line:#d8d7d2}
*{box-sizing:border-box}
body.t-behindcrust{margin:0;background:var(--paper);color:var(--ink);font-family:"Inter",system-ui,sans-serif;font-size:16.5px;line-height:1.66}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 26px 90px}
.site-head__inner{max-width:1120px;margin:0 auto;padding:40px 26px 0}
.bc-mast{display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid var(--ink);padding-bottom:14px}
.bc-word{font-family:"Space Grotesk",sans-serif;font-weight:700;font-size:clamp(28px,5vw,52px);letter-spacing:-.02em;text-decoration:none}
.bc-rec{font-family:"Space Mono",monospace;font-size:12px;letter-spacing:.1em;color:var(--cobalt)}
.bc-tag{font-family:"Space Mono",monospace;font-size:13px;color:var(--soft);margin:14px 0 0}
.site-foot__inner{max-width:1120px;margin:0 auto;padding:30px 26px;border-top:2px solid var(--ink);display:flex;justify-content:space-between;font-family:"Space Mono",monospace;font-size:12px;color:var(--soft)}
/* plates grid */
.bc-plates{margin:40px 0 0;display:grid;grid-template-columns:1.4fr 1fr;gap:24px}
.bc-plate{border:1px solid var(--ink);background:#fff;display:flex;flex-direction:column}
.bc-plate__cap{display:flex;justify-content:space-between;font-family:"Space Mono",monospace;font-size:11px;letter-spacing:.06em;color:var(--soft);border-bottom:1px solid var(--line);padding:9px 14px}
.bc-plate__cap b{color:var(--cobalt)}
.bc-plate__body{padding:26px 24px 24px}
.bc-plate__t{font-family:"Space Grotesk",sans-serif;font-weight:600;font-size:clamp(22px,3vw,34px);line-height:1.08;margin:0 0 10px;letter-spacing:-.01em}
.bc-plate__t a{text-decoration:none}
.bc-plate__s{color:#3d3c38;margin:0}
.bc-plate__more{font-family:"Space Mono",monospace;font-size:12px;color:var(--cobalt);text-decoration:none;display:inline-block;margin-top:14px}
.bc-plate--lead .bc-plate__body{padding:40px 34px}
/* contact sheet */
.bc-sheet{margin:48px 0 0;border-top:2px solid var(--ink);padding-top:8px}
.bc-sheet__h{font-family:"Space Mono",monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin:0 0 6px}
.bc-frames{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1px;background:var(--ink);border:1px solid var(--ink)}
.bc-frame{background:#fff;padding:20px 18px}
.bc-frame__n{font-family:"Space Mono",monospace;font-size:11px;color:var(--cobalt)}
.bc-frame h3{font-family:"Space Grotesk",sans-serif;font-weight:600;font-size:18px;line-height:1.16;margin:8px 0 6px}
.bc-frame h3 a{text-decoration:none}
.bc-frame__d{font-family:"Space Mono",monospace;font-size:11px;color:var(--soft)}
/* article */
.post{max-width:700px;margin:40px auto 0}
.post__eyebrow span{font-family:"Space Mono",monospace;color:var(--cobalt);font-size:12px;letter-spacing:.04em}
.post__title{font-family:"Space Grotesk",sans-serif;font-weight:700;font-size:clamp(28px,5vw,48px);letter-spacing:-.02em;line-height:1.06;margin:.2em 0}
.post__dek{color:var(--soft);font-size:20px}
.post__meta{font-family:"Space Mono",monospace;font-size:12px;color:var(--soft)}
.post__body{margin-top:24px}
.post__back{font-family:"Space Mono",monospace;display:inline-block;margin-top:36px;color:var(--cobalt);text-decoration:none}
.archive{max-width:780px;margin:40px auto 0}
.archive__title{font-family:"Space Grotesk",sans-serif;font-weight:700;font-size:38px;letter-spacing:-.02em}
.archive__list{padding:0}
.archive__item{list-style:none;padding:18px 0;border-bottom:1px solid var(--line)}
.archive__name{font-family:"Space Grotesk",sans-serif;font-weight:600;font-size:21px;display:block}
.archive__date{font-family:"Space Mono",monospace;font-size:12px;color:var(--cobalt)}
.archive__sum{color:var(--soft);margin:.3em 0 0}
@media(max-width:740px){.bc-plates{grid-template-columns:1fr}}
''',
index=PRE + '''{{ define "main" }}
<section class="bc-plates">
  {{ with $lead }}
  <article class="bc-plate bc-plate--lead">
    <div class="bc-plate__cap"><span>PLATE 01</span><span><b>{{ .Date.Format "15:04" }}</b> · LEAD</span></div>
    <div class="bc-plate__body">
      <h2 class="bc-plate__t"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
      <p class="bc-plate__s">{{ .Summary }}</p>
      <a class="bc-plate__more" href="{{ .RelPermalink }}">→ open the file</a>
    </div>
  </article>
  {{ end }}
  <div style="display:grid;gap:24px">
  {{ range $i, $p := first 2 (after 1 $featured) }}
    <article class="bc-plate">
      <div class="bc-plate__cap"><span>PLATE {{ printf "%02d" (add $i 2) }}</span><span><b>{{ $p.Date.Format "Jan 2" }}</b></span></div>
      <div class="bc-plate__body">
        <h2 class="bc-plate__t"><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h2>
        <p class="bc-plate__s">{{ $p.Params.summary }}</p>
      </div>
    </article>
  {{ end }}
  </div>
</section>

<section class="bc-sheet">
  <p class="bc-sheet__h">// contact sheet — all frames</p>
  <div class="bc-frames">
    {{ range $i, $p := first 6 $posts }}
    <article class="bc-frame">
      <span class="bc-frame__n">FRAME {{ printf "%02d" (add $i 1) }}</span>
      <h3><a href="{{ $p.RelPermalink }}">{{ $p.Title }}</a></h3>
      <span class="bc-frame__d">{{ $p.Date.Format "2006.01.02" }}</span>
    </article>
    {{ end }}
  </div>
</section>
{{ end }}
''',
)
