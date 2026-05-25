# Project Context for AI Agents

## Overview
Desktop icon library: 628 icons in 4 styles, each with 7 PNG sizes + `.ico`.

## Environment
- **Path:** `C:\Users\fraumar\Apps\_downloads\icons8`
- **Git remote:** `git@github-personal:marcelofrau/icons8-personal-set` (branch `main`)
- **Platform:** Windows (PowerShell 7+)
- **Dependencies:** ImageMagick 7 (`magick`), optipng, Python 3

## Directory Structure
```
50x50/           Source PNGs small (primary source)
100x100/         Source PNGs large (primary source)
16x16/            Generated 16px
32x32/            Generated 32px
48x48/            Generated 48px
128x128/          Generated 128px
256x256/          Generated 256px
ico/              Multi-resolution .ico (16+32+48+128+256)
process-icons.py      Pipeline: resize + optipng + ico (parallel)
generate-catalog.py   Generates icon-catalog.md and icon-catalog-ai.md
download-missing.py   Download batch 1 (46 Icons8 icons)
download-more.py      Download batch 2 (112 Icons8 icons)
download-fluentui.py  Download 39 emojis (FluentUI + Twemoji fallback)
download-consoles.py  Download 16 retro consoles (KyleBing)
icon-catalog.md       Full catalog with 32x32 previews and links
icon-catalog-ai.md    Minimal AI-friendly catalog (names only, by category)
README.md             Full documentation, attribution, stats
PIPELINE.md           Technical pipeline docs
AGENTS.md             This file
```

## Naming Convention

| Stem pattern | Example dir/file | Style |
|---|---|---|
| `icons8-<name>` | `50x50/icons8-amazon-50.png` | Icons8 3d-fluency (legacy, no suffix) |
| `icons8-<name>-3d` | `50x50/icons8-pdf-3d-50.png` | Icons8 3d-fluency (explicit) |
| `icons8-<name>-2d` | `50x50/icons8-zip-2d-50.png` | Icons8 fluency (flat) |
| `fluentui-<name>` | `50x50/fluentui-heart-eyes-50.png` | FluentUI/Twemoji emoji |
| `retro-<name>` | `50x50/retro-nes-50.png` | KyleBing retro console |

Each stem produces: `<dir>/<stem>-<size>.png` for sizes 16,32,48,128,256 + source 50,100, plus `ico/<stem>.ico`.

## Scripts

### `process-icons.py`
Pipeline principal. Scans 50x50/100x100, generates missing sizes with Lanczos, runs optipng -o7, creates .ico.
```bash
python process-icons.py --workers 16
```

### `generate-catalog.py`
Generates two files:
- `icon-catalog.md` — full table with 32x32 previews and download links
- `icon-catalog-ai.md` — minimal list per category (name stems only)

Custom category sort places "Emojis / Expressions" last.

### Download scripts
Each is standalone, meant to be run once. They download to 50x50/ and 100x100/.
- `download-missing.py` — 46 icons (apps, emojis, file ops, storage)
- `download-more.py` — 112 icons (devices, tools, audio, gaming, animals, food)
- `download-fluentui.py` — 39 emojis (FluentUI 3D PNG primary, Twemoji SVG fallback for 11 missing)
- `download-consoles.py` — 16 retro consoles from KyleBing GitHub raw (300px → 50/100 source)

## Icon Sources

| Source | Count | License |
|---|---|---|
| Icons8 3d-fluency | 414 | Free with attribution |
| Icons8 fluency | 159 | Free with attribution |
| FluentUI Emoji (Microsoft) | 28 | MIT |
| Twemoji (jdecked fork) | 11 | CC-BY 4.0 |
| KyleBing retro consoles | 16 | GPL-3.0 |

## Current Stats
- **Total icons:** 628 (unique, after dedup)
- **Size variants:** 7 (50, 100, 16, 32, 48, 128, 256)
- **Total PNGs:** 4,396 (628 × 7)
- **Total .ico:** 628
- **Categories:** 27

## Key Decisions
1. No suffix = 3d-fluency style (legacy compatibility)
2. Try Icons8 3d-fluency first; fall back to fluency on 404
3. OpenMoji removed; replaced with FluentUI 3D emoji (28) + Twemoji fallback (11)
4. KyleBing retro consoles added for missing hardware (16 icons)
5. Emojis/Expressions category sorted last in both catalogs
6. `generate-catalog.py` `ICON_TO_CAT` dict: last category wins for duplicates
7. Only `icons8-` prefix is stripped for display; `fluentui-` and `retro-` are kept as-is

## Tags
- `v1.0` — current stable milestone (all 628 icons processed, both catalogs generated, README finalized)

## Common Tasks
- **Regenerate catalogs:** `python generate-catalog.py`
- **Process new icons:** drop PNGs in 50x50/ + 100x100/, then `python process-icons.py --workers 16`
- **Download new Icons8:** add to download script or manually fetch, name with `-3d`/`-2d` suffix
- **Add to category:** edit `CATEGORIES` dict in `generate-catalog.py`, then regenerate
- **Check duplicates:** `python -c "from pathlib import Path; [print(x) for x in Path('50x50').glob('*.png')]"`
- **Full re-download:** wipe 50x50/, 100x100/, rerun download scripts, then process-icons

## Important Constraints
- Never use `gh` CLI; only plain `git`
- Git remote uses host `github-personal` (SSH config alias)
- All download scripts kept in repo for reproducibility
- Pipeline skips existing files (idempotent)
