```
                                                    ,---.-,
                                                     '   ,'  '.
                                                    /   /      \
  ,--,                                             .   ;  ,/.  :
,--.'|               ,---.        ,---,            '   |  | :  ;
|  |,               '   ,'\   ,-+-. /  | .--.--.   '   |  ./   :
`--'_       ,---.  /   /   | ,--.'|'   |/  /    '  |   :       ,
,' ,'|     /     \.   ; ,. :|   |  ,"' |  :  /`./   \   \     /
'  | |    /    / ''   | |: :|   | /  | |  :  ;_      ;   ,   '\\
|  | :   .    ' / '   | .; :|   | |  | |\  \    `.  /   /      \
'  : |__ '   ; :__|   :    ||   | |  |/  `----.   \.   ;  ,/.  :
|  | '.'|'   | '.'|\   \  / |   | |--'  /  /`--'  /'   |  | :  ;
;  :    ;|   :    : `----'  |   |/     '--'.     / '   |  ./   :
|  ,   /  \   \  /          '---'        `--'---'  |   :      /
 ---`-'    `----'                                   \   \   .'
                                                     `---`-'
```

# Icons8 Personal Icon Set

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Icons](https://img.shields.io/badge/icons-613-3d82e6?logo=icons8&logoColor=white)](icon-catalog.md)
[![Styles](https://img.shields.io/badge/styles-3d--fluency%20%7C%20fluency-ff6b6b)]()
[![Sizes](https://img.shields.io/badge/sizes-16%E2%80%93256px%20%7C%20.ico-00c853)]()

A ready-to-use **desktop icon library** — **613 icons** in **3d-fluency** and **fluency** styles (plus OpenMoji emojis), available as multi-size PNGs (16–256px) and Windows `.ico` files.

## Purpose

Desktop applications — file managers, launchers, text editors, media players, system utilities — all need a rich set of icons at multiple resolutions. Instead of relying on a CDN or bundling bloated icon packs, this project provides a **local, offline-ready collection** of carefully selected icons in two visual styles.

Use them as:
- **File type icons** (PDF, ZIP, EXE, ISO, JSON, CSV, …)
- **Toolbar / UI actions** (filter, sort, rename, share, lock, …)
- **System status indicators** (online, volume, bell, mute, shutdown, …)
- **View modes** (list, details, thumbnails, icons, …)
- **Text editing controls** (bold, italic, align, numbered list, …)
- **Storage / drives** (USB, SSD, HDD, CD, Blu-ray, SD, …)
- **Applications / brands** (Discord, GitHub, Spotify, Facebook, …)
- **Emojis / expressions** (smiling, angry, thumbs-up, animals, food, …)
- **Gaming / consoles** (PlayStation, Xbox, Steam, controllers, …)
- **Hardware / devices** (smartphones, monitors, printers, keyboards, …)
- **Tools / DIY** (drill, saw, wrench, pliers, ruler, …)

Every icon has **7 size variants** (50, 100, 16, 32, 48, 128, 256) and a multi-resolution `.ico` file, so you can drop them directly into any desktop app without manual conversion.

## Sources & Attribution

This icon library is an aggregate of icons from multiple freely-available sources:

| Source | Style | Count | License |
|---|---|---|---|
| [Icons8](https://icons8.com) — 3d-fluency | 3D rendered | 486 icons | [Free with attribution](https://icons8.com/license) |
| [Icons8](https://icons8.com) — fluency | Flat 2D | 127 icons | [Free with attribution](https://icons8.com/license) |
| [OpenMoji](https://openmoji.org) — color | Emoji | 39 icons | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

### Download Sources

All icons were obtained from the following public CDNs and repositories:

| Source | Base URL | Used for |
|---|---|---|
| Icons8 CDN | `https://img.icons8.com/<style>/<size>/<name>.png` | All `icons8-*-3d-*` and `icons8-*-2d-*` icons |
| OpenMoji CDN | `https://cdn.openmoji.org/data/color-svg/` + Unicode hex | All `openmoji-*` emoji icons |
| Icons8 website (direct download) | `https://icons8.com/icons` | Original legacy icons (no style suffix, later recategorized as 3d-fluency) |

**Icons8 CDN patterns:**

```
# 3d-fluency (try first, fall back to fluency on 404)
https://img.icons8.com/3d-fluency/50/<name>.png
https://img.icons8.com/3d-fluency/100/<name>.png

# fluency (flat 2D fallback)
https://img.icons8.com/fluency/50/<name>.png
https://img.icons8.com/fluency/100/<name>.png
```

**OpenMoji CDN pattern** (downloaded as SVG, converted to 100×100 PNG):

```
https://cdn.openmoji.org/data/color-svg/<unicode-hex>.svg
```

> See [`download-missing.py`](download-missing.py) and [`download-more.py`](download-more.py) for the complete list of icon names and their source styles. These scripts document exactly which icons came from which CDN URL.

### Attribution

**Icons8** requires attribution when used for free. If you use this library in your project, please include a credit line such as: *"Icons by Icons8 (https://icons8.com)"* or reference this repository.

**OpenMoji** emojis are licensed under CC BY-SA 4.0. Attribution: *"Emojis by OpenMoji (https://openmoji.org)"* — if you modify or redistribute them, you must share under the same license.

## Stats

| | Count |
|---|---|
| 3d-fluency icons (Icons8) | 486 |
| fluency icons (Icons8) | 127 |
| OpenMoji emojis | 39 |
| Total icons | 613 |
| Size variants | 7 (50, 100, 16, 32, 48, 128, 256) |
| Total `.ico` files | 613 |
| Total PNG files | 4,291 |
| Icon categories | 27 |

## Structure

```
50x50/            Source PNGs (small)
100x100/          Source PNGs (large)
16x16/            16x16 PNGs
32x32/            32x32 PNGs
48x48/            48x48 PNGs
128x128/          128x128 PNGs
256x256/          256x256 PNGs
ico/              Multi-resolution .ico (16+32+48+128+256)
process-icons.py  Auto-processing pipeline
generate-catalog.py  Icon catalog generator
icon-catalog.md   Full catalog with previews
missing-icons.md  Icons grouped by category
PIPELINE.md       Technical pipeline docs
```

## Naming Convention

| Pattern | Example | Style | Source |
|---|---|---|---|
| `icons8-<name>-3d-<size>.png` | `icons8-pdf-3d-50.png` | 3d-fluency | Icons8 |
| `icons8-<name>-2d-<size>.png` | `icons8-zip-2d-50.png` | fluency | Icons8 |
| `icons8-<name>-<size>.png` | `icons8-about-50.png` | 3d-fluency | Icons8 (original) |
| `openmoji-<name>-<size>.png` | `openmoji-video-game-50.png` | emoji | OpenMoji |
| `icons8-<name>-<style>.ico` | `icons8-pdf-3d.ico` | multi-res | Generated |

## Requirements

- [ImageMagick 7](https://imagemagick.org/) (`magick` in PATH)
- [optipng](https://optipng.sourceforge.net/) (`optipng` in PATH)
- Python 3

## Pipeline

```bash
python process-icons.py --workers 16
```

Scans `50x50/` and `100x100/` for new PNGs, generates all sizes with Lanczos, optimizes with optipng -o7, and creates `.ico` files (parallel, skips existing).

## License

MIT — the code and pipeline are MIT. The icon assets themselves are subject to their respective licenses (Icons8: free with attribution; OpenMoji: CC BY-SA 4.0).
