#!/usr/bin/env python3
"""
Icons8 icon processing pipeline (parallel)

Usage:
    python process-icons.py
    python process-icons.py --workers 16

What it does:
    1. Scans 50x50/ and 100x100/ for new PNGs
    2. Generates derived sizes (16, 32, 48, 128, 256) with Lanczos
    3. Optimizes with optipng -o7
    4. Generates multi-resolution .ico with all 5 sizes

Naming:
    icons8-<name>-<3d|2d>-<size>.png   (new)
    icons8-<name>-<size>.png            (legacy)

Requirements:
    - ImageMagick 7 (magick in PATH)
    - optipng (in PATH)
"""

import os
import subprocess
import sys
import re
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
FOLDERS = {
    "source_small": "50x50",
    "source_large": "100x100",
    "16": "16x16",
    "32": "32x32",
    "48": "48x48",
    "128": "128x128",
    "256": "256x256",
    "ico": "ico",
}

SMALL_SIZES = [("16", "16x16"), ("32", "32x32"), ("48", "48x48")]
LARGE_SIZES = [("128", "128x128"), ("256", "256x256")]


def extract_base(stem: str) -> str:
    """Strip size suffix from filename.
    e.g. icons8-pdf-3d-50 -> icons8-pdf-3d
         icons8-about-50   -> icons8-about
    """
    return re.sub(r"-(?:50|100|16|32|48|128|256)$", "", stem)


def get_base_names(folder: str) -> set[str]:
    path = BASE_DIR / folder
    names = set()
    for f in path.glob("*.png"):
        names.add(extract_base(f.stem))
    return names


def get_new_icons() -> list[str]:
    sources = get_base_names(FOLDERS["source_small"]) & get_base_names(FOLDERS["source_large"])
    dests = set()
    for key in ["16", "32", "48", "128", "256"]:
        dests |= get_base_names(FOLDERS[key])
    return sorted(sources - dests)


def get_missing_ico() -> list[str]:
    sources = get_base_names(FOLDERS["source_small"])
    existing_ico = {f.stem for f in (BASE_DIR / FOLDERS["ico"]).glob("*.ico")}
    return sorted(sources - existing_ico)


def run(cmd: list[str]) -> bool:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def process_one_icon(name: str, steps: list[str]) -> tuple[str, bool]:
    src_small = BASE_DIR / FOLDERS["source_small"] / f"{name}-50.png"
    src_large = BASE_DIR / FOLDERS["source_large"] / f"{name}-100.png"

    if not src_small.exists():
        return (name, False)
    if not src_large.exists():
        return (name, False)

    for step in steps:
        if step == "resize":
            for size_str, folder_key in SMALL_SIZES:
                dst = BASE_DIR / folder_key / f"{name}-{size_str}.png"
                if not dst.exists():
                    run(["magick", str(src_small), "-filter", "Lanczos",
                         "-resize", f"{size_str}x{size_str}", str(dst)])
            for size_str, folder_key in LARGE_SIZES:
                dst = BASE_DIR / folder_key / f"{name}-{size_str}.png"
                if not dst.exists():
                    run(["magick", str(src_large), "-filter", "Lanczos",
                         "-resize", f"{size_str}x{size_str}", str(dst)])

        elif step == "optimize":
            for size_key in ["16", "32", "48", "128", "256"]:
                png = BASE_DIR / FOLDERS[size_key] / f"{name}-{size_key}.png"
                if png.exists():
                    run(["optipng", "-o7", "-quiet", str(png)])

        elif step == "ico":
            dst = BASE_DIR / FOLDERS["ico"] / f"{name}.ico"
            if not dst.exists():
                inputs = []
                all_ok = True
                for size_key in ["16", "32", "48", "128", "256"]:
                    png = BASE_DIR / FOLDERS[size_key] / f"{name}-{size_key}.png"
                    if not png.exists():
                        all_ok = False
                        break
                    inputs.append(str(png))
                if all_ok:
                    run(["magick"] + inputs + [str(dst)])

    return (name, True)


def main():
    parser = argparse.ArgumentParser(description="Icons8 icon processing pipeline")
    parser.add_argument("--workers", type=int, default=8,
                        help="Number of parallel workers (default: 8)")
    args = parser.parse_args()

    print("=" * 60)
    print(f"  Icons8 Icon Processing Pipeline  (workers={args.workers})")
    print("=" * 60)

    for cmd in ["magick", "optipng"]:
        try:
            subprocess.run([cmd, "--version"], capture_output=True, check=True)
        except (subprocess.FileNotFoundError, subprocess.CalledProcessError):
            print(f"ERROR: '{cmd}' not found in PATH")
            sys.exit(1)

    print("\nChecking directories...")
    for key, folder in FOLDERS.items():
        path = BASE_DIR / folder
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"  CREATED: {folder}/")
        else:
            count = len(list(path.glob("*.png"))) if folder != "ico" else len(list(path.glob("*.ico")))
            ext = "PNGs" if folder != "ico" else "ICOs"
            print(f"  {folder}/ ({count} {ext})")

    novos = get_new_icons()
    missing_ico = get_missing_ico()

    if not novos and not missing_ico:
        print("\nNothing to do. All icons already processed.")
        return

    todos = list(novos)
    for n in missing_ico:
        if n not in todos:
            todos.append(n)

    print(f"\n>>> {len(todos)} icon(s) to process (workers={args.workers})...")

    steps = ["resize", "optimize", "ico"]
    ok = 0
    falha = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_one_icon, name, steps): name for name in todos}
        for future in as_completed(futures):
            name, success = future.result()
            if success:
                ok += 1
            else:
                falha += 1
            print(f"  {'OK' if success else 'FAIL'} {name}")

    total_small = len(get_base_names(FOLDERS["source_small"]))
    total_large = len(get_base_names(FOLDERS["source_large"]))
    total_16 = len(get_base_names(FOLDERS["16"]))
    total_ico = len(list((BASE_DIR / FOLDERS["ico"]).glob("*.ico")))

    print(f"\n{'=' * 60}")
    print(f"  Processed: {ok} OK, {falha} fail(s)")
    print(f"  Sources:  {total_small} in 50x50/ | {total_large} in 100x100/")
    print(f"  Generated: {total_16} PNGs per size | {total_ico} .ico files")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
