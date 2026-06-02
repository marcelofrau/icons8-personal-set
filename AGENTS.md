# Project Context for AI Agents

Desktop icon library: **2034 icons** across 4 source styles, each with 7 PNG sizes + `.ico`.

## Quick Stats
- **FluentUI 3D emoji:** 1315 — `fluentui-<name>` — MIT
- **Icons8 3d-fluency:** 698 — `icons8-<name>` (no suffix) or `icons8-<name>-3d` — Free with attribution
- **Retro consoles:** 16 — `retro-<name>` — GPL-3.0
- **Non-prefix legacy:** `coffee-cup`, `coffee-espresso`, `coffee-latte-1`, `coffee-latte-2`, `mario-question-mark`
- **Total PNGs:** 14,238 (2034 × 7 sizes), **.ico:** 2034
- **Categories:** 27 (index: `icon-catalog.md`, per-category: `catalog/*.md`)

## Environment
- **Platform:** Windows, PowerShell 7+
- **Deps:** ImageMagick 7 (`magick`), optipng, Python 3
- **Git:** `github.com/user/icons8-personal-set` (`main`)

## Directory Layout
```
50x50/ 100x100/          Source PNGs (primary — drop new icons here)
16x16/ 32x32/ 48x48/      Generated sizes (Lanczos)
128x128/ 256x256/          Generated sizes (Lanczos)
ico/                      Multi-res .ico (16+32+48+128+256)
process-icons.py          Pipeline: resize + optipng + ico
generate-catalog.py       Generates icon-catalog.md + catalog/*.md
catalog/                  Per-category markdown files (27)
download-missing.py           Icons8 batch 1 (46 icons)
download-more.py              Icons8 batch 2 (112 icons)
download-fluentui.py          FluentUI emoji + Twemoji fallback (39)
download-consoles.py          KyleBing retro consoles (16)
download-dev.py               Icons8 dev/app utilities (63)
download-food.py              Icons8 + FluentUI food/drink (60)
download-m-icons.py           M:\ drive folder icons (6: anime, children, pencil-drawing, film-reel, soulseek, tv-show)
download-openburning.py       OpenBurningSuite disc/optical icons (5: discover, speed, timeline, video-editing, wizard)
download-fluentui-massive.py  Bulk FluentUI 3D CDN (~1267)
fluentui_3d_list.txt          Input list for download-fluentui-massive.py
icon-catalog-ai.md            Minimal AI-friendly catalog (stems only)
openburning-icons.md          OBS feature-to-icon mapping with 32x32 previews
```

## Naming Convention
| Stem | Example | Style |
|---|---|---|
| `icons8-<name>` | `icons8-amazon-50.png` | 3d-fluency (legacy, no suffix) |
| `icons8-<name>-3d` | `icons8-pdf-3d-50.png` | 3d-fluency (explicit) |
| `icons8-<name>-2d` | `icons8-zip-2d-50.png` | fluency (flat) |
| `fluentui-<name>` | `fluentui-heart-eyes-50.png` | FluentUI/Twemoji emoji |
| `retro-<name>` | `retro-nes-50.png` | KyleBing retro console |

Each stem → 7 sizes + `.ico`: `<dir>/<stem>-<size>.png` for 16,32,48,128,256 + 50,100, plus `ico/<stem>.ico`.

## Scripts

### Process new icons
```bash
python process-icons.py --workers 16    # parallel, skips existing
```
Scans 50x50/ + 100x100/, generates missing sizes with Lanczos, runs optipng -o7, creates .ico.

### Regenerate catalogs
```bash
python generate-catalog.py               # updates icon-catalog.md + catalog/*.md
```

### Download scripts
Each is standalone, downloads to 50x50/ + 100x100/. Then run `process-icons.py`.
- `download-missing.py`, `download-more.py` — Icons8: try 3d-fluency first, fall back to fluency on 404
- `download-fluentui.py` — FluentUI 3D CDN, Twemoji SVG fallback for missing
- `download-consoles.py` — KyleBing GitHub raw (300px → 50/100)
- `download-dev.py` — Dev tools/apps from Icons8 fluency (63)
- `download-food.py` — Icons8 food/drink + FluentUI fallback (60)
- `download-m-icons.py` — M: drive folder icons (icons8 Icons8 3d-fluency/fluency, tries both)
- `download-openburning.py` — OBS-related icons (Icons8, tries 3d-fluency then fluency)
- `download-fluentui-massive.py` — Bulk FluentUI from `fluentui_3d_list.txt`, resizes with magick

## Key Details
- **No suffix = 3d-fluency** (legacy convention)
- **Icons8:** try 3d-fluency first; 404 → fluency (flat)
- **Only `icons8-` prefix is stripped** for display; `fluentui-` and `retro-` kept as-is
- **Catalog sort:** "Emojis / Expressions" and "Food & Drinks" sorted last
- **generate-catalog.py:** `ICON_TO_CAT` dict — last category wins for duplicates
- **Large categories** (>200 items) get compact listing; >500 → names only
- **Non-prefix icons** (coffee-*, mario-question-mark) classified as "Other"
