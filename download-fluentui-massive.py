#!/usr/bin/env python3
"""
Download ALL 3D emojis from Microsoft FluentUI Emoji repo (1267 new).
Naming: fluentui-<name> (underscores -> hyphens).
Skips already-downloaded icons. Parallel download + resize.

Usage:
    python download-fluentui-massive.py --workers 8
"""

import urllib.request
import pathlib
import subprocess
import sys
import time
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote

BASE = pathlib.Path(__file__).parent.resolve()
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

CDN = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/{name_dir}/3D/{stem}_3d.png"


def run(cmd: list[str]) -> bool:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def download_file(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "python"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        return True
    except Exception:
        return False


def process_one(stem: str, name_dir: str) -> str:
    our_name = f"fluentui-{stem.replace('_', '-')}"

    small_file = SMALL / f"{our_name}-50.png"
    large_file = LARGE / f"{our_name}-100.png"

    # Download from CDN
    url = CDN.format(name_dir=quote(name_dir), stem=stem)
    tmp = BASE / f"__tmp_ms_{stem}.png"

    if not download_file(url, tmp):
        return f"FAIL DL  {our_name}"

    # Resize to both sizes
    ok = True
    if not run(["magick", str(tmp), "-filter", "Lanczos",
                "-resize", "100x100", str(large_file)]):
        ok = False
    if not run(["magick", str(tmp), "-filter", "Lanczos",
                "-resize", "50x50", str(small_file)]):
        ok = False

    tmp.unlink(missing_ok=True)

    if not ok:
        small_file.unlink(missing_ok=True)
        large_file.unlink(missing_ok=True)
        return f"FAIL RESIZE {our_name}"

    return f"OK {our_name}"


def main():
    parser = argparse.ArgumentParser(description="Download FluentUI 3D emojis")
    parser.add_argument("--workers", type=int, default=4,
                        help="Parallel workers (default: 4)")
    args = parser.parse_args()

    list_file = BASE / "fluentui_3d_list.txt"
    if not list_file.exists():
        print("ERROR: fluentui_3d_list.txt not found")
        return 1

    with open(list_file) as f:
        lines = f.read().strip().splitlines()

    entries = []
    for line in lines:
        parts = line.split("|", 1)
        stem = parts[0]
        name_dir = parts[1] if len(parts) > 1 else stem
        entries.append((stem, name_dir))

    # Get existing fluentui stems
    existing = set()
    for f in SMALL.glob("fluentui-*-50.png"):
        existing.add(f.stem.replace("-50", ""))

    # Filter to new ones only
    to_download = []
    for stem, name_dir in entries:
        our_name = f"fluentui-{stem.replace('_', '-')}"
        if our_name not in existing:
            to_download.append((stem, name_dir))

    total = len(to_download)
    print(f"Total: {total} new FluentUI emojis to download ({len(existing)} already have)")
    print(f"Workers: {args.workers}")
    print()

    if total == 0:
        print("Nothing to do.")
        return 0

    ok_count = 0
    fail_count = 0
    done = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_one, stem, name_dir): stem
                   for stem, name_dir in to_download}

        for future in as_completed(futures):
            result = future.result()
            done += 1
            if result.startswith("OK"):
                ok_count += 1
            else:
                fail_count += 1

            # Progress every 25 or on errors
            if result.startswith("OK") and done % 25 == 0:
                print(f"  [{done}/{total}] {result}")
            elif not result.startswith("OK"):
                print(f"  [{done}/{total}] {result}")

    print()
    print(f"Results: {ok_count} OK, {fail_count} failed (of {total} new)")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
