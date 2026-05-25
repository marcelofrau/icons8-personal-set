# Icon Generation Pipeline

## Project Structure

```
C:\Users\fraumar\Apps\_downloads\icons8\
├── 50x50\          Source (small sizes)
├── 100x100\        Source (large sizes)
├── 16x16\          Generated
├── 32x32\          Generated
├── 48x48\          Generated
├── 128x128\        Generated
├── 256x256\        Generated
├── ico\            Multi-resolution .ico
├── process-icons.py      Auto pipeline
├── missing-icons.md      Icon catalog by category
└── PIPELINE.md           This file
```

## Automated Pipeline (recommended)

```bash
python process-icons.py              # 8 workers (default)
python process-icons.py --workers 16  # faster on multi-core CPUs
```

The script:
1. Scans `50x50/` and `100x100/` for new PNGs
2. Generates derived sizes in parallel (16, 32, 48, 128, 256) using Lanczos
3. Optimizes with optipng -o7
4. Generates multi-resolution .ico

## Naming Convention

- **3D (3d-fluency):** `icons8-<name>-3d-<size>.png` (e.g. `icons8-pdf-3d-50.png`)
- **2D (fluency):** `icons8-<name>-2d-<size>.png` (e.g. `icons8-zip-2d-50.png`)
- **Legacy (273 originals):** `icons8-<name>-<size>.png` (e.g. `icons8-about-50.png`)
- **.ico:** follows same pattern without size: `icons8-<name>-3d.ico`, `icons8-<name>.ico`

## How to Add New Icons Manually

### Step 1: Download from Icons8

Try **3d-fluency** first; if 404, use **fluency**:

```
https://img.icons8.com/3d-fluency/50/<name>.png
https://img.icons8.com/3d-fluency/100/<name>.png
```

Save as:
```
50x50/icons8-<name>-3d-50.png        # if 3d-fluency
50x50/icons8-<name>-2d-50.png        # if fluency
```

### Step 2: Run the pipeline

```bash
python process-icons.py --workers 16
```

This generates all sizes, optimizes, and creates .ico automatically.

## Workflow Summary

```
Download Icons8 (3d-fluency → fluency) → 50x50/ + 100x100/
  ↓
python process-icons.py --workers N    →  all sizes + optipng + .ico
```
