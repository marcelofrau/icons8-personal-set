#!/usr/bin/env python3
"""
Download M:\ drive folder icons from Icons8 CDN.
Usage:
    python download-m-icons.py
"""

import urllib.request
import pathlib
import sys

BASE = pathlib.Path(__file__).parent.resolve()
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

# (name, style) — verified on Icons8 CDN
ITEMS = [
    ("anime",           "2d"),   # M:\Animes
    ("children",        "2d"),   # M:\Child Movies
    ("pencil-drawing",  "3d"),   # M:\Desenhos (drawings)
    ("tv-show",         "3d"),   # M:\Series
    ("soulseek",        "2d"),   # M:\Soulseek
    ("film-reel",       "3d"),   # M:\Short
    ("clock",           "3d"),   # M:\temp
]

STYLE_MAP = {"3d": "3d-fluency", "2d": "fluency"}
SUFFIX_MAP = {"3d": "-3d", "2d": "-2d"}


def already_exists(name):
    for suffix in ["-3d", "-2d", ""]:
        for prefix in ["icons8"]:
            if (SMALL / f"{prefix}-{name}{suffix}-50.png").exists():
                return True
    return False


def main():
    ok = 0
    fail = 0
    skipped = 0

    print("=" * 60)
    print("  M:\\ Drive Folder Icons Download")
    print("=" * 60)
    print()

    for name, style in ITEMS:
        if already_exists(name):
            print(f"  SKIP  {name} (already exists)")
            skipped += 1
            continue

        api_style = STYLE_MAP[style]
        suffix = SUFFIX_MAP[style]
        small_file = SMALL / f"icons8-{name}{suffix}-50.png"
        large_file = LARGE / f"icons8-{name}{suffix}-100.png"

        url_small = f"https://img.icons8.com/{api_style}/50/{name}.png"
        url_large = f"https://img.icons8.com/{api_style}/100/{name}.png"

        try:
            urllib.request.urlretrieve(url_small, small_file)
            urllib.request.urlretrieve(url_large, large_file)
            print(f"  ICONS8 {name} ({style})")
            ok += 1
        except Exception as e:
            small_file.unlink(missing_ok=True)
            large_file.unlink(missing_ok=True)
            print(f"  FAIL  {name} ({style}): {e}")
            fail += 1

    print(f"\nResults: {ok} OK, {fail} fail(s), {skipped} skipped")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
