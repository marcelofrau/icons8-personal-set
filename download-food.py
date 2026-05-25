#!/usr/bin/env python3
"""
Download food, drink, and fruit icons.
Priority: Icons8 3d-fluency -> Icons8 fluency -> FluentUI/Twemoji.
Uses ImageMagick + optipng for processing.

Usage:
    python download-food.py
"""

import urllib.request
import pathlib
import subprocess
import sys
import time
import shutil

BASE = pathlib.Path(__file__).parent.resolve()
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

PREFIX_FLUENTUI = "fluentui"

FLUENTUI_CDN = "https://cdn.jsdelivr.net/gh/shuding/fluentui-emoji-unicode/assets/{code}_3d.png"
TWEMOJI_CDN = "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/svg/{code}.svg"

# (name, style)  style is '3d' or '2d'  -- verified on Icons8 CDN
ICONS8_ITEMS = [
    # --- Fruits ---
    ("blueberry",      "3d"),
    ("coconut",        "3d"),
    ("date",           "2d"),
    ("kiwi",           "3d"),
    ("lychee",         "2d"),
    ("mango",          "3d"),
    ("melon",          "3d"),
    ("olive",          "3d"),
    ("papaya",         "3d"),
    ("pomegranate",    "3d"),
    ("lemon",          None),   # not on Icons8, will use FluentUI
    ("fig",            None),
    # --- Vegetables / Food ---
    ("bacon",          "3d"),
    ("baguette",       "3d"),
    ("bread",          "2d"),
    ("cheese",         "3d"),
    ("chili-pepper",   "3d"),
    ("chocolate-bar",  "3d"),
    ("croissant",      "3d"),
    ("cupcake",        "3d"),
    ("doughnut",       "3d"),
    ("french-fries",   "3d"),
    ("garlic",         "3d"),
    ("honey",          "2d"),
    ("meat",           "3d"),
    ("noodles",        "3d"),
    ("onion",          "3d"),
    ("pancake",        "3d"),
    ("peanut",         "3d"),
    ("popcorn",        "2d"),
    ("pretzel",        "3d"),
    ("salad",          "3d"),
    ("sandwich",       "2d"),
    ("sausage",        "3d"),
    ("spaghetti",      "3d"),
    ("steak",          "3d"),
    ("sushi",          "3d"),
    ("taco",           "3d"),
    ("toast",          "3d"),
    ("egg",            None),
    ("rice",           None),
    ("dumpling",       None),
    ("lollipop",       None),
    ("muffin",         None),
    ("shrimp",         None),
    ("soup",           None),
    # --- Drinks ---
    ("beer",           "2d"),
    ("bottle-of-water","2d"),
    ("champagne",      "2d"),
    ("cocktail",       "2d"),
    ("coffee",         "3d"),
    ("lime",           "2d"),
    ("milk",           "2d"),
    ("orange-juice",   "2d"),
    ("soda",           "3d"),
    ("tea",            "3d"),
    ("water",          "3d"),
    ("white-wine",     "2d"),
    ("wine-bottle",    "3d"),
    ("wine-glass",     "3d"),
]

# FluentUI/Twemoji fallback Unicode codes for items with style=None
FLUENTUI_FALLBACK = {
    "lemon":       "1f34b",
    "fig":         "1fad6",
    "egg":         "1f95a",
    "rice":        "1f35a",
    "dumpling":    "1f95f",
    "lollipop":    "1f36d",
    "muffin":      "1f9c1",
    "shrimp":      "1f990",
    "soup":        "1f372",
}

STYLE_MAP = {"3d": "3d-fluency", "2d": "fluency"}
SUFFIX_MAP = {"3d": "-3d", "2d": "-2d"}


def run(cmd: list[str]) -> bool:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def download_file(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
        return True
    except Exception:
        return False


def svg_to_png(svg_path, png_path, size=100):
    return run([
        "magick", str(svg_path), "-background", "none",
        "-filter", "Lanczos", "-resize", f"{size}x{size}",
        str(png_path)
    ])


def already_exists(name, prefix="icons8"):
    for suffix in ["-3d", "-2d", ""]:
        if (SMALL / f"{prefix}-{name}{suffix}-50.png").exists():
            return True
    return False


def main():
    ok = 0
    fail = 0
    skipped = 0

    print("=" * 60)
    print("  Food / Drink / Fruit Icon Download")
    print("=" * 60)
    print()

    for name, style in ICONS8_ITEMS:
        if already_exists(name, "icons8") or already_exists(name, PREFIX_FLUENTUI):
            print(f"  SKIP  {name} (already exists)")
            skipped += 1
            continue

        if style is not None:
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
                continue
            except Exception as e:
                small_file.unlink(missing_ok=True)
                large_file.unlink(missing_ok=True)
                print(f"  FAIL  {name} (icons8 {style}): {e}")
                fail += 1
        else:
            code = FLUENTUI_FALLBACK.get(name)
            if code is None:
                print(f"  FAIL  {name} (no fallback code)")
                fail += 1
                continue

            small_file = SMALL / f"{PREFIX_FLUENTUI}-{name}-50.png"
            large_file = LARGE / f"{PREFIX_FLUENTUI}-{name}-100.png"

            url = FLUENTUI_CDN.format(code=code)
            tmp = BASE / f"__tmp_food_{name}.png"

            if download_file(url, tmp):
                if run(["magick", str(tmp), "-filter", "Lanczos",
                        "-resize", "100x100", str(large_file)]) and \
                   run(["magick", str(tmp), "-filter", "Lanczos",
                        "-resize", "50x50", str(small_file)]):
                    tmp.unlink(missing_ok=True)
                    print(f"  FLUENTUI {PREFIX_FLUENTUI}-{name}")
                    ok += 1
                    continue

            # FluentUI failed, try Twemoji fallback
            svg_url = TWEMOJI_CDN.format(code=code)
            svg_tmp = BASE / f"__tmp_food_{name}.svg"
            if download_file(svg_url, svg_tmp):
                if svg_to_png(svg_tmp, large_file, 100) and \
                   svg_to_png(svg_tmp, small_file, 50):
                    svg_tmp.unlink(missing_ok=True)
                    print(f"  TWEMOJI {PREFIX_FLUENTUI}-{name}")
                    ok += 1
                    continue
                svg_tmp.unlink(missing_ok=True)

            tmp.unlink(missing_ok=True)
            print(f"  FAIL  {PREFIX_FLUENTUI}-{name}")
            fail += 1
            time.sleep(0.3)

    print()
    print(f"Results: {ok} OK, {fail} fail(s), {skipped} skipped (already exist)")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
