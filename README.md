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
[![Icons](https://img.shields.io/badge/icons-629-3d82e6?logo=icons8&logoColor=white)](icon-catalog.md)
[![Styles](https://img.shields.io/badge/styles-3d--fluency%20%7C%20fluency%20%7C%20fluentui--emoji%20%7C%20retro-ff6b6b)]()
[![Sizes](https://img.shields.io/badge/sizes-16%E2%80%93256px%20%7C%20.ico-00c853)]()

A ready-to-use **desktop icon library** — **629 icons** in **3d-fluency**, **fluency**, **fluentui-emoji**, and **retro** styles, available as multi-size PNGs (16–256px) and Windows `.ico` files.

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
|---|---|---|---|---|
| [Icons8](https://icons8.com) — 3d-fluency | 3D rendered | 486 icons | [Free with attribution](https://icons8.com/license) |
| [Icons8](https://icons8.com) — fluency | Flat 2D | 127 icons | [Free with attribution](https://icons8.com/license) |
| [FluentUI Emoji](https://github.com/microsoft/fluentui-emoji) — Microsoft | 3D emoji | 28 icons | [MIT](https://github.com/microsoft/fluentui-emoji/blob/main/LICENSE) |
| [Twemoji](https://github.com/jdecked/twemoji) — Twitter/X | Emoji (fallback) | 11 icons | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [KyleBing/retro-game-console-icons](https://github.com/KyleBing/retro-game-console-icons) — Retro console | Flat retro | 16 icons | [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html) |

### Download Sources

All icons were obtained from the following public CDNs and repositories:

| Source | Base URL | Used for |
|---|---|---|
| Icons8 CDN | `https://img.icons8.com/<style>/<size>/<name>.png` | All `icons8-*-3d-*` and `icons8-*-2d-*` icons |
| FluentUI Emoji CDN (shuding fork) | `https://cdn.jsdelivr.net/gh/shuding/fluentui-emoji-unicode/assets/<unicode>_3d.png` | All `fluentui-*` emoji icons (primary) |
| Twemoji CDN (jdecked fork) | `https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/svg/<unicode>.svg` | `fluentui-*` emoji icons not in FluentUI set (fallback) |
| KyleBing retro console icons | `https://raw.githubusercontent.com/KyleBing/retro-game-console-icons/main/series_trimui/300w@1x/<FILE>.png` | All `retro-*` console icons |
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

**FluentUI Emoji CDN pattern** (3D PNG):

```
https://cdn.jsdelivr.net/gh/shuding/fluentui-emoji-unicode/assets/<unicode>_3d.png
```

**Twemoji CDN pattern** (SVG, converted to PNG for fallback):

```
https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/svg/<unicode>.svg
```

**KyleBing retro console CDN pattern** (300px PNG, resized to 50&times;50 and 100&times;100):

```
https://raw.githubusercontent.com/KyleBing/retro-game-console-icons/main/series_trimui/300w@1x/<FILE>.png
```

> See [`download-missing.py`](download-missing.py), [`download-more.py`](download-more.py), [`download-fluentui.py`](download-fluentui.py), and [`download-consoles.py`](download-consoles.py) for the complete list of icon names and their source URLs.

### Attribution

**Icons8** requires attribution when used for free. If you use this library in your project, please include a credit line such as: *"Icons by Icons8 (https://icons8.com)"* or reference this repository.

**FluentUI Emoji** by Microsoft (MIT License). Attribution: *"Emojis by Microsoft FluentUI Emoji (https://github.com/microsoft/fluentui-emoji)"*.

**Twemoji** graphics are licensed under CC-BY 4.0 by Twitter/X and contributors. Attribution: *"Emoji graphics by Twemoji (https://github.com/jdecked/twemoji)"*.

**Retro console icons** by KyleBing (GPL-3.0). Attribution: *"Console icons by KyleBing (https://github.com/KyleBing/retro-game-console-icons)"*.

## Stats

| | Count |
|---|---|---|
| 3d-fluency icons (Icons8) | 486 |
| fluency icons (Icons8) | 127 |
| FluentUI emojis (with Twemoji fallback) | 39 |
| Retro console icons (KyleBing) | 16 |
| Total icons | 629 |
| Size variants | 7 (50, 100, 16, 32, 48, 128, 256) |
| Total `.ico` files | 629 |
| Total PNG files | 4,403 |
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
| `fluentui-<name>-<size>.png` | `fluentui-heart-eyes-50.png` | fluentui-emoji | FluentUI / Twemoji |
| `retro-<name>-<size>.png` | `retro-nes-50.png` | retro | KyleBing |
| `<name>.ico` | `fluentui-heart-eyes.ico` | multi-res | Generated |

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

MIT — the code and pipeline are MIT. The icon assets themselves are subject to their respective licenses (Icons8: free with attribution; FluentUI Emoji: MIT; Twemoji graphics: CC-BY 4.0; KyleBing retro console icons: GPL-3.0).
