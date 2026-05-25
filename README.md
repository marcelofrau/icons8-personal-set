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
[![Icons](https://img.shields.io/badge/icons-401-3d82e6?logo=icons8&logoColor=white)](missing-icons.md)
[![Styles](https://img.shields.io/badge/styles-3d--fluency%20%7C%20fluency-ff6b6b)]()
[![Sizes](https://img.shields.io/badge/sizes-16%E2%80%93256px%20%7C%20.ico-00c853)]()

A ready-to-use **desktop icon library** built from [Icons8](https://icons8.com) — **401 icons** in **3d-fluency** and **fluency** styles, available as multi-size PNGs (16–256px) and Windows `.ico` files.

## Purpose

Desktop applications — file managers, launchers, text editors, media players, system utilities — all need a rich set of icons at multiple resolutions. Instead of relying on a CDN or bundling bloated icon packs, this project provides a **local, offline-ready collection** of carefully selected icons in two visual styles.

Use them as:
- **File type icons** (PDF, ZIP, EXE, ISO, JSON, CSV, …)
- **Toolbar / UI actions** (filter, sort, rename, share, lock, …)
- **System status indicators** (online, volume, bell, mute, shutdown, …)
- **View modes** (list, details, thumbnails, icons, …)
- **Text editing controls** (bold, italic, align, numbered list, …)
- **Storage / drives** (USB, SSD, HDD, CD, Blu-ray, SD, …)

Every icon has **7 size variants** (50, 100, 16, 32, 48, 128, 256) and a multi-resolution `.ico` file, so you can drop them directly into any desktop app without manual conversion.

## Stats

| | Count |
|---|---|
| 3d-fluency icons | 327 |
| fluency icons | 127 |
| Total `.ico` files | 454 |
| Size variants | 7 (50, 100, 16, 32, 48, 128, 256) |
| Total PNG files | 3,178 |
| Total PNG files | 2,807 |

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
missing-icons.md  Full icon catalog by category
PIPELINE.md       Technical pipeline docs
```

## Naming Convention

| Pattern | Example | Style |
|---|---|---|
| `icons8-<name>-3d-<size>.png` | `icons8-pdf-3d-50.png` | 3d-fluency |
| `icons8-<name>-2d-<size>.png` | `icons8-zip-2d-50.png` | fluency |
| `icons8-<name>-<size>.png` | `icons8-about-50.png` | legacy (273 originals) |
| `icons8-<name>-3d.ico` | `icons8-pdf-3d.ico` | 3d-fluency .ico |
| `icons8-<name>-2d.ico` | `icons8-zip-2d.ico` | fluency .ico |

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

MIT
