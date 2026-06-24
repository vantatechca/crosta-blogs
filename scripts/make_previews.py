#!/usr/bin/env python3
"""Make self-contained homepage previews: inline each site's style.css into its
index.html so the design renders standalone (fonts still load from Google)."""
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
    # replace the stylesheet link with an inline <style>
    idx = re.sub(r'<link[^>]+style\.css[^>]*>', f'<style>{css}</style>', idx)
    (OUT / f"{slug}.html").write_text(idx)
    print(f"  preview: {slug}.html")
print(f"\n{len(SLUGS)} previews in previews/")
