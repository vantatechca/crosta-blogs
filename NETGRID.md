# Netgrid → Crosta Blogs publishing contract

Netgrid publishes a post by **writing one markdown file** into the right site's content
folder and triggering a rebuild. No manual curation — placement is driven entirely by
frontmatter, so Netgrid decides what's featured at publish time.

## Where files go

```
sites/<slug>/content/posts/<post-slug>.md
```

`<slug>` is the theme/site slug (`journal`, `stoneoven`, …). One blog = one slug = one repo
folder = one Render service.

## Frontmatter contract

```yaml
---
title: "The 72-hour cold ferment, explained"
date: 2026-06-20T09:00:00Z      # controls ordering (newest first)
summary: "Why we rest our dough three days before it sees the oven."
featured: true                  # appears in the homepage featured area
top: true                       # marks a "top story" (used by some themes' sidebars)
author: "Crosta Kitchen"
tags: ["dough", "fermentation"]
---

Body in markdown. First paragraph becomes the lead / drop-cap in several themes.
```

### How the flags drive layout (automatic)

- **`featured: true`** — the post enters the homepage featured set. The *newest* featured
  post becomes the lead (big hero / lead essay / top story / plate 01, depending on theme).
- **`top: true`** — surfaced in themes that have a "top stories" rail (e.g. The Daily Slice
  sidebar, the FIRE stamp on Notes from the Pass).
- Posts with neither flag still appear in each homepage's recent/index list and on the
  full archive — they're just not promoted.

Every theme reads the **same** fields, so one Netgrid post object maps cleanly to any blog.

## Adapter pseudocode (Netgrid side)

```ts
function toHugoMarkdown(post: NetgridPost): string {
  const fm = [
    "---",
    `title: ${JSON.stringify(post.title)}`,
    `date: ${post.publishedAt.toISOString()}`,
    `summary: ${JSON.stringify(post.excerpt)}`,
    `featured: ${post.isFeatured}`,
    `top: ${post.isTopStory}`,
    `author: ${JSON.stringify(post.author ?? "Crosta Kitchen")}`,
    `tags: [${post.tags.map(t => JSON.stringify(t)).join(", ")}]`,
    "---", "",
    post.bodyMarkdown,
  ].join("\n");
  return fm;
}

// publish = commit the file to the client repo, then let Render rebuild.
//   path: `sites/${post.blogSlug}/content/posts/${slugify(post.title)}.md`
//   commit + push  ->  Render auto-deploy  ->  live in ~30-60s
```

Two integration options, both fine given lag is acceptable:

1. **Git commit (simplest):** Netgrid commits the markdown via the GitHub API and pushes.
   Render's auto-deploy picks it up. No server to run.
2. **Build hook:** commit a batch of posts, then call the Render deploy hook once to
   rebuild the affected service(s).

## Notes

- Image fields: drop hero images into `sites/<slug>/static/` (or `assets/`) and reference
  them in the body; keep paths relative so they survive the per-site build.
- The sample posts written by `scripts/generate_sites.py` are seeds for local preview.
  In production, treat `content/posts/` as Netgrid-owned and stop running the generator
  against live sites (or have it skip existing files).
