#!/usr/bin/env python3
"""
Generate per-site Hugo configs + sample content for the Pizzeria Crosta blog fleet.
Themes themselves are hand-built under ../themes. This only wires up sites + seeds
sample posts so each site renders (featured / top / recent all populate).

Run from repo root:  python3 scripts/generate_sites.py
"""
import os, textwrap, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITES = ROOT / "sites"

# slug, title, theme, domain, tagline, brand/accent intent
BLOGS = [
    ("journal",      "The Crosta Journal",        "journal",     "thecrostajournal.com",
        "Long-form writing on dough, fire, and the craft of Neapolitan pizza."),
    ("stoneoven",    "Stories from the Stone Oven","stoneoven",   "stonovenstories.com",
        "Tales from the hearth — the people, the heat, the slow rise."),
    ("crustcrumb",   "Crust & Crumb",             "crustcrumb",  "crustandcrumb.co",
        "A precise look at fermentation, hydration, and the science of a perfect base."),
    ("dailyslice",   "The Daily Slice",           "dailyslice",  "thedailyslice.co",
        "Fresh pizza news, served daily."),
    ("notespass",    "Notes from the Pass",       "notespass",   "notesfromthepass.com",
        "Working notes from the line — straight off the pass."),
    ("flourfire",    "Flour & Fire",              "flourfire",   "flourandfire.co",
        "Where 00 flour meets 480°C. The bold side of pizza."),
    ("crostatable",  "The Crosta Table",          "crostatable", "thecrostatable.com",
        "Hospitality, pairings, and the art of the shared table."),
    ("hotoven",      "Hot Out the Oven",          "hotoven",     "hotouttheoven.com",
        "Fresh, fast, and a little bit cheesy. Pizza, the fun way."),
    ("fornodiaries", "Forno Diaries",             "fornodiaries","fornodiaries.com",
        "A running diary from the oven — entry by entry."),
    ("behindcrust",  "Behind the Crust",          "behindcrust", "behindthecrust.com",
        "Behind the scenes at Pizzeria Crosta — the makers, the method."),
]

# Sample posts per blog: (title, summary, body, featured, top, tags)
def posts_for(slug, title):
    base = [
        ("The 72-hour cold ferment, explained",
         "Why we let our dough rest for three days before it ever sees the oven.",
         "Cold fermentation is the quiet engine behind a great crust. Over 72 hours in the "
         "fridge, the yeast works slowly while enzymes break starches into simpler sugars. "
         "The payoff is a base that's lighter, more digestible, and tastes of more than just "
         "flour.\n\nAt Pizzeria Crosta we mix on Monday for a Thursday bake. The dough comes "
         "out blistered and open-crumbed, with that faint sourness you only get from time.",
         True, True, ["dough", "fermentation"]),
        ("Choosing your San Marzano",
         "Not every tin marked San Marzano earns the name. Here's what we look for.",
         "A true San Marzano tomato grows in volcanic soil south of Naples and carries a DOP "
         "seal. They're sweeter, less acidic, and have fewer seeds than a standard plum "
         "tomato.\n\nWe crush ours by hand and season only with salt — a good tomato doesn't "
         "need rescuing.",
         True, False, ["ingredients", "sauce"]),
        ("Reading the leopard spots",
         "Those charred bubbles on the cornicione aren't a flaw. They're the signature.",
         "Leoparding — the leopard-print char on a Neapolitan crust — happens fast and hot. "
         "At around 450°C the puffed edge catches in seconds.\n\nToo pale and the oven's "
         "cold; too black and you've lost the floor. The window is about ninety seconds.",
         False, True, ["technique", "oven"]),
        ("Why we mill our own 00",
         "A note on the flour that starts everything.",
         "Tipo 00 is ground fine as talc. Milling closer to bake day keeps the flour lively "
         "and the gluten strong, which is what lets a thin base hold its shape under a wet "
         "topping.",
         False, False, ["flour", "ingredients"]),
        ("A week on the pass",
         "Six hundred pizzas, one oven, and the rhythm that holds it together.",
         "Service is choreography. The pass is where it all lands — last look, last wipe of "
         "the rim, then out the door in under a minute. This is what a Friday actually feels "
         "like from behind the counter.",
         False, False, ["service", "kitchen"]),
    ]
    return base

def write_config(slug, title, theme, domain, tagline):
    d = SITES / slug
    (d / "content" / "posts").mkdir(parents=True, exist_ok=True)
    cfg = f'''baseURL = "https://{domain}/"
languageCode = "en-us"
title = "{title}"
theme = "{theme}"
themesDir = "../../themes"
paginate = 8
enableRobotsTXT = true
# Relative asset + internal links so CSS/links resolve whether the site is served
# at a domain root, a subpath, an onrender.com URL, or opened as a file. Prevents
# the "/style.css 404 -> unstyled page" failure.
relativeURLs = true
canonifyURLs = false

[params]
  tagline = "{tagline}"
  brand = "Pizzeria Crosta"
  brandURL = "https://pizzeriacrosta.com/"
  description = "{tagline}"

[markup.goldmark.renderer]
  unsafe = true

[taxonomies]
  tag = "tags"
'''
    (d / "hugo.toml").write_text(cfg)

def write_posts(slug, title):
    pdir = SITES / slug / "content" / "posts"
    start = datetime.date(2026, 6, 20)
    for i, (ptitle, summary, body, featured, top, tags) in enumerate(posts_for(slug, title)):
        date = (start - datetime.timedelta(days=i*2)).isoformat()
        tagstr = ", ".join(f'"{t}"' for t in tags)
        fm = (
            "---\n"
            f'title: "{ptitle}"\n'
            f"date: {date}T09:00:00Z\n"
            f'summary: "{summary}"\n'
            f"featured: {str(featured).lower()}\n"
            f"top: {str(top).lower()}\n"
            f'author: "Crosta Kitchen"\n'
            f"tags: [{tagstr}]\n"
            "---\n\n"
            f"{body}\n"
        )
        fname = ptitle.lower().replace(" ", "-").replace("'", "").replace(",", "")[:50]
        (pdir / f"{fname}.md").write_text(fm)

def write_about(slug, title, tagline):
    pdir = SITES / slug / "content"
    about = (
        "---\n"
        'title: "About"\n'
        "---\n\n"
        f"**{title}** is a blog by Pizzeria Crosta. {tagline}\n\n"
        "Visit the pizzeria at [pizzeriacrosta.com](https://pizzeriacrosta.com/).\n"
    )
    (pdir / "about.md").write_text(about)

if __name__ == "__main__":
    for slug, title, theme, domain, tagline in BLOGS:
        write_config(slug, title, theme, domain, tagline)
        write_posts(slug, title)
        write_about(slug, title, tagline)
        print(f"  wired {slug:14s} -> theme:{theme:12s} {domain}")
    print(f"\nGenerated {len(BLOGS)} sites under sites/")
