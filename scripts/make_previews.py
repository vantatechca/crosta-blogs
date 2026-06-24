#!/usr/bin/env python3
"""Self-contained homepage previews: inline each site's style.css AND anim.js into
its index.html so the design + motion render standalone (fonts load from Google)."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
OUT = ROOT / "previews"
OUT.mkdir(exist_ok=True)

SLUGS = ["journal","stoneoven","crustcrumb","dailyslice","notespass",
         "flourfire","crostatable","hotoven","fornodiaries","behindcrust"]

for slug in SLUGS:
    idx = (PUB / slug / "index.html").read_text()
    css = (PUB / slug / "style.css").read_text()
    js = (PUB / slug / "anim.js").read_text()
    idx = re.sub(r'<link[^>]+style\.css[^>]*>', f'<style>{css}</style>', idx)
    idx = re.sub(r'<script[^>]+anim\.js[^>]*></script>', f'<script>{js}</script>', idx)
    (OUT / f"{slug}.html").write_text(idx)
    print(f"  preview: {slug}.html")
print(f"\n{len(SLUGS)} animated previews in previews/")
