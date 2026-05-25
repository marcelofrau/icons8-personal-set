#!/usr/bin/env python3
"""
Download FluentUI (Microsoft) emojis to replace OpenMoji.
Falls back to Twemoji for emojis not present in FluentUI.

FluentUI:  https://cdn.jsdelivr.net/gh/shuding/fluentui-emoji-unicode/assets/<unicode>_3d.png
Twemoji:   https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/svg/<unicode>.svg
"""

import urllib.request
import pathlib
import subprocess
import sys
import time
import shutil

BASE = pathlib.Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

PREFIX = "fluentui"

FLUENTUI_CDN = "https://cdn.jsdelivr.net/gh/shuding/fluentui-emoji-unicode/assets/{code}_3d.png"
TWEMOJI_CDN = "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/svg/{code}.svg"

EMOJI_MAP = [
    # (our_name, unicode_hex, has_fluentui)
    ("beaming-emoji",        "1f601", True),
    ("blue-heart",           "1f499", True),
    ("broken-heart-emoji",   "1f494", False),
    ("clapping",             "1f44f", True),
    ("cloud-emoji",          "2601",  False),
    ("fire-emoji",           "1f525", True),
    ("flexed-biceps",        "1f4aa", True),
    ("folded-hands",         "1f64f", True),
    ("green-heart",          "1f49a", True),
    ("grinning-emoji",       "1f600", True),
    ("heart-eyes",           "1f60d", True),
    ("joy-emoji",            "1f602", True),
    ("kissing-heart",        "1f618", True),
    ("lightning-emoji",      "26a1",  False),
    ("purple-heart",         "1f49c", True),
    ("rainbow-emoji",        "1f308", True),
    ("red-heart-emoji",      "2764",  True),
    ("rose-emoji",           "1f339", True),
    ("snowflake-emoji",      "2744",  False),
    ("sparkling-heart",      "1f496", False),
    ("star-emoji",           "2b50",  False),
    ("sun-emoji",            "2600",  True),
    ("thumbs-down-emoji",    "1f44e", True),
    ("thumbs-up-emoji",      "1f44d", True),
    ("waving",               "1f44b", True),
    ("yellow-heart",         "1f49b", True),
    # Gaming
    ("chess-pawn",           "265f",  False),
    ("club",                 "2663",  True),
    ("diamond-suit",         "2666",  True),
    ("flower-cards",         "1f3b4", False),
    ("game-die",             "1f3b2", True),
    ("heart-suit",           "2665",  True),
    ("joker",                "1f0cf", True),
    ("joystick-emoji",       "1f579", False),
    ("mahjong",              "1f004", True),
    ("puzzle-piece",         "1f9e9", True),
    ("slot-machine",         "1f3b0", False),
    ("spade",                "2660",  True),
    ("video-game",           "1f3ae", False),
]

def download_file(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
        return True
    except Exception:
        return False

def svg_to_png(svg_path, png_path, size=100):
    try:
        subprocess.run(
            ["magick", str(svg_path), "-background", "none",
             "-filter", "Lanczos", "-resize", f"{size}x{size}",
             str(png_path)],
            capture_output=True, timeout=30, check=True
        )
        return True
    except Exception:
        return False

ok = 0
fail = 0

for name, code, has_fluentui in EMOJI_MAP:
    small_file = SMALL / f"{PREFIX}-{name}-50.png"
    large_file = LARGE / f"{PREFIX}-{name}-100.png"

    if small_file.exists() and large_file.exists():
        print(f"  EXIST {PREFIX}-{name}")
        ok += 1
        continue

    if has_fluentui:
        url = FLUENTUI_CDN.format(code=code)
        tmp = BASE / f"__tmp_{name}.png"
        if download_file(url, tmp):
            subprocess.run(
                ["magick", str(tmp), "-filter", "Lanczos", "-resize", "100x100", str(large_file)],
                capture_output=True, timeout=30
            )
            subprocess.run(
                ["magick", str(tmp), "-filter", "Lanczos", "-resize", "50x50", str(small_file)],
                capture_output=True, timeout=30
            )
            tmp.unlink(missing_ok=True)
            if large_file.exists() and small_file.exists():
                print(f"  FLUENTUI {PREFIX}-{name}")
                ok += 1
                continue
    else:
        svg_url = TWEMOJI_CDN.format(code=code)
        svg_tmp = BASE / f"__tmp_{name}.svg"
        if download_file(svg_url, svg_tmp):
            png_tmp = BASE / f"__tmp_{name}.png"
            if svg_to_png(svg_tmp, png_tmp, 100):
                shutil.move(png_tmp, large_file)
                svg_to_png(svg_tmp, small_file, 50)
                svg_tmp.unlink(missing_ok=True)
                if large_file.exists() and small_file.exists():
                    print(f"  TWEMOJI {PREFIX}-{name}")
                    ok += 1
                    continue

    print(f"  FAIL {PREFIX}-{name}")
    fail += 1
    time.sleep(0.3)

print(f"\nDownloaded: {ok} OK, {fail} fail(s)")
