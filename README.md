# Crosta Blogs — multi-site blog fleet for Pizzeria Crosta

Ten independent blog sites, one repo, one theme each. Static Hugo output, built for
Netgrid-driven publishing and Render Static Site hosting. This is the **per-client repo
pattern** — clone it per client, swap the blog list + domains, and you have another fleet.

| # | Blog | Theme slug | Design direction | Placeholder domain |
|---|------|-----------|------------------|--------------------|
| 1 | The Crosta Journal | `journal` | Literary culinary review — drop-cap lead essay | thecrostajournal.com |
| 2 | Stories from the Stone Oven | `stoneoven` | Dark hearth, glowing ember | stonovenstories.com |
| 3 | Crust & Crumb | `crustcrumb` | Minimal bakery, precise grid | crustandcrumb.co |
| 4 | The Daily Slice | `dailyslice` | Newsstand masthead + headlines | thedailyslice.co |
| 5 | Notes from the Pass | `notespass` | Kitchen dockets, ticket stamps | notesfromthepass.com |
| 6 | Flour & Fire | `flourfire` | Bold dark, fire-gradient type | flourandfire.co |
| 7 | The Crosta Table | `crostatable` | Elegant dining, menu leaders | thecrostatable.com |
| 8 | Hot Out the Oven | `hotoven` | Playful, chunky rounded cards | hotouttheoven.com |
| 9 | Forno Diaries | `fornodiaries` | Italian diary, dated timeline | fornodiaries.com |
| 10 | Behind the Crust | `behindcrust` | Documentary, framed "plates" | behindthecrust.com |

> **Domains are placeholders.** See *Swapping domains* below.

## Repo layout

```
crosta-blogs/
├── build.sh                 # build all 10 sites -> public/<slug>/
├── render-build.sh          # build ONE site by slug (used by Render)
├── render.yaml              # Render blueprint: 10 static-site services
├── scripts/
│   ├── generate_sites.py    # writes each site's hugo.toml + sample posts
│   ├── build_themes.py      # template factory (shared shell + per-theme assembly)
│   ├── build_themes_defs.py # the 10 bespoke theme designs (palette/type/homepage/css)
│   └── make_previews.py     # self-contained homepage previews -> previews/
├── themes/<slug>/           # one Hugo theme per blog
└── sites/<slug>/            # one Hugo site per blog (config + content)
```

Themes and the per-site sample content are **generated** by the scripts so the whole
fleet stays consistent. In production, Netgrid writes the real posts into
`sites/<slug>/content/posts/` (the generator's sample posts are just seeds).

## Build locally

```bash
./build.sh                         # pure Hugo build of all 10 -> public/  (safe anytime)
python3 scripts/make_previews.py   # optional: standalone homepage previews

./scaffold.sh                      # DEV ONLY: regenerate themes/configs + sample seed posts
```

`build.sh` is a pure build and never touches `content/`. Run `./scaffold.sh` only when you
change the blog list or a theme design — it re-seeds sample posts, so don't run it against a
live site whose posts are owned by Netgrid.

Requires Hugo **extended** ≥ 0.123. `build.sh` expects `hugo` on PATH; `render-build.sh`
fetches it automatically.

## Managing one blog

Each blog is fully isolated: its own theme in `themes/<slug>/`, its own config + content in
`sites/<slug>/`, and its own Render service. Editing one never affects the others.

```bash
./manage.sh list             # all blogs + where each one's design lives
./manage.sh where journal    # exact paths to edit for one blog
./manage.sh dev journal      # live local preview (reloads on save) at localhost:1313
./manage.sh build journal    # build just that one blog
```

Where to edit, by task:

| Want to change… | Edit |
|---|---|
| Colors / layout / fonts | `themes/<slug>/static/style.css` and `themes/<slug>/layouts/` |
| Homepage structure | `themes/<slug>/layouts/index.html` |
| Article page | `themes/<slug>/layouts/_default/single.html` |
| Title / tagline / domain | `sites/<slug>/hugo.toml` |
| Posts | `sites/<slug>/content/posts/` (normally Netgrid-owned) |

Commit and push only that blog's folders. **Render build filters** (in `render.yaml`) mean a
push touching only `themes/journal/**` or `sites/journal/**` rebuilds *only* the journal
service — the other nine don't redeploy.

### The one rule: hand-edits vs. the generators

Once you start hand-editing a blog's `themes/<slug>/` directly, that theme is yours — **don't
run `./scaffold.sh` against it**, because the generators in `scripts/` would overwrite it from
the Python definitions. Use the generators only for bootstrapping a new client/blog or making a
deliberate fleet-wide change; use `manage.sh` + direct edits for tuning a single live blog.

## Swapping domains

Edit the `BLOGS` list in `scripts/generate_sites.py` — the 4th field of each tuple is the
domain. It becomes the site's `baseURL`. Re-run `./build.sh`. Then attach the matching
custom domain to each service in Render and point DNS (CNAME/ANAME) at it; Render issues
free SSL automatically.

## Deploy on Render

1. Push this repo to Git (one repo per client).
2. In Render: **New → Blueprint**, point at the repo. `render.yaml` creates 10 free
   Static Sites, each building only its own blog (`./render-build.sh <slug>`).
3. For each service, **Settings → Custom Domains**, add the real domain.

Static Sites are free and don't spin down. A publish is a git commit → Render rebuild
(~30–60s) → live. That's the "lag is fine" path.

## Adding / removing a blog

Add a tuple to `BLOGS` in `generate_sites.py`, add a matching theme in
`build_themes_defs.py` (or reuse an existing `theme` slug), add a service block to
`render.yaml`. Re-run `./build.sh`.

See **NETGRID.md** for the publishing contract.
