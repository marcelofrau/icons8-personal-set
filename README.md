# Icons8 Personal Icon Set

Personal icon library from Icons8 in **3d-fluency** and **fluency** styles, with multi-size variants and Windows `.ico` format.

## Structure

```
├── 50x50/            Source PNGs (small size)
├── 100x100/          Source PNGs (large size)
├── 16x16/            Resized to 16×16
├── 32x32/            Resized to 32×32
├── 48x48/            Resized to 48×48
├── 128x128/          Resized to 128×128
├── 256x256/          Resized to 256×256
├── ico/              Multi-resolution .ico (16, 32, 48, 128, 256)
├── process-icons.py       Auto-processing pipeline
├── missing-icons.md       Icon catalog by category
└── PIPELINE.md            Technical pipeline docs
```

## Naming Convention

- `icons8-<name>-3d-<size>.png` — 3d-fluency icon
- `icons8-<name>-2d-<size>.png` — fluency icon
- `icons8-<name>-<size>.png` — legacy icon (273 originals)
- `icons8-<name>-3d.ico` / `icons8-<name>-2d.ico` — multi-resolution .ico

## Requirements

- ImageMagick 7 (`magick` in PATH)
- optipng (`optipng` in PATH)
- Python 3

## Pipeline

```bash
python process-icons.py --workers 16
```

Scans `50x50/` and `100x100/` for new PNGs, generates all sizes, optimizes with optipng, and creates `.ico` files.

## License

MIT
