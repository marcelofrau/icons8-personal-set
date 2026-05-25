```
           CCCCCCCCCCCCC
         CCCCCCCCCCCCCCCCCCCC
       CCCCCCCCCCCCCCCCCCCCCCCCC
      CCCCCCCCCCC       CCCCCCCCCCC
     CCCCCCCCC           CCCCCCCCCCC
    CCCCCCC               CCCCCCCCCCC
   CCCCCCC                 CCCCCCCCCCC
  CCCCCCC                   CCCCCCCCCCC
  CCCCCC                     CCCCCCCCCCC
  CCCCCC                     CCCCCCCCCCC             88888888
  CCCCCC        IIIIIIIIIIIICCCCCCCCCCC             888    888
  CCCCCC        IIIIIIIIIIII CCCCCCCCCCC           888      888
  CCCCCC        IIIIIIIIIIII  CCCCCCCCCCC         888        888
  CCCCCC        IIIIIIIIIIII   CCCCCCCCCCC        888888888888888
  CCCCCC        IIIIIIIIIIII    CCCCCCCCCCC       888        888
  CCCCCC        IIIIIIIIIIII     CCCCCCCCCCC      888        888
  CCCCCC        IIIIIIIIIIII      CCCCCCCCCCC     888        888
  CCCCCC        IIIIIIIIIIII       CCCCCCCCCCC
   CCCCCC                         CCCCCCCCCCC
    CCCCCCC                     CCCCCCCCCCC
     CCCCCCCCC                 CCCCCCCCCCC
      CCCCCCCCCCC           CCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCC
             CCCCCCCCCCCCC
```

# Icons8 Personal Icon Set

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Icons](https://img.shields.io/badge/icons-401-3d82e6?logo=icons8&logoColor=white)](missing-icons.md)
[![Styles](https://img.shields.io/badge/styles-3d--fluency%20%7C%20fluency-ff6b6b)]()
[![Sizes](https://img.shields.io/badge/sizes-16%E2%80%93256px%20%7C%20.ico-00c853)]()

Personal icon library from **Icons8** — **401 icons** in **3d-fluency** and **fluency** styles, with multi-size PNGs (16–256px) and Windows `.ico` files.

## Stats

| | Count |
|---|---|
| 3d-fluency icons | 204 |
| fluency icons | 197 |
| Total `.ico` files | 401 |
| Size variants | 7 (50, 100, 16, 32, 48, 128, 256) |

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
