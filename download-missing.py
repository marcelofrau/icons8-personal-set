#!/usr/bin/env python3
"""
Download new icons from Icons8 for Applications, Emojis, File/Folder, Storage groups.
"""

import urllib.request
import pathlib
import sys
import time

BASE = pathlib.Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

# (name, style) where style is '3d' or '2d'
TO_DOWNLOAD = [
    # -- Applications / Brands --
    ("discord", "3d"),
    ("twitter", "2d"),
    ("twitch", "3d"),
    ("reddit", "3d"),
    ("docker", "2d"),
    ("figma", "2d"),
    ("notion", "2d"),
    ("android", "2d"),
    ("apple-logo", "3d"),
    ("xbox", "2d"),
    ("playstation", "3d"),
    ("nintendo-switch", "2d"),
    ("windows-10", "3d"),
    ("pinterest", "3d"),
    ("snapchat", "3d"),
    ("tiktok", "3d"),
    ("behance", "3d"),
    ("dribbble", "2d"),
    # -- Emojis / Expressions --
    ("smiling", "2d"),
    ("happy", "2d"),
    ("sad", "2d"),
    ("angry", "2d"),
    ("surprised", "2d"),
    ("wink", "2d"),
    ("laughing", "2d"),
    ("crying", "2d"),
    ("thumbs-up", "3d"),
    ("thumbs-down", "2d"),
    ("ok-hand", "3d"),
    ("broken-heart", "3d"),
    ("moon", "2d"),
    ("rainbow", "3d"),
    ("snowflake", "3d"),
    ("lightning-bolt", "3d"),
    ("cloud", "3d"),
    ("tornado", "2d"),
    ("umbrella", "3d"),
    ("confused", "3d"),
    ("cool", "2d"),
    # -- File / Folder Operations --
    ("new-document", "2d"),
    ("folder-tree", "2d"),
    ("copy-link", "2d"),
    ("move-to-folder", "3d"),
    ("invert-selection", "2d"),
    # -- Storage / Media --
    ("tape-drive", "2d"),
    ("micro-sd", "3d"),
    # -- Gaming / Console --
    ("controller", "3d"),
    ("xbox-controller", "2d"),
    ("steam", "3d"),
    ("gaming", "2d"),
    ("virtual-reality", "3d"),
    ("psp", "2d"),
    ("ps5", "2d"),
]

STYLE_MAP = {"3d": "3d-fluency", "2d": "fluency"}
SUFFIX_MAP = {"3d": "-3d", "2d": "-2d"}

ok = 0
fail = 0

for name, style in TO_DOWNLOAD:
    api_style = STYLE_MAP[style]
    suffix = SUFFIX_MAP[style]
    small_file = SMALL / f"icons8-{name}{suffix}-50.png"
    large_file = LARGE / f"icons8-{name}{suffix}-100.png"

    if small_file.exists() and large_file.exists():
        print(f"  EXIST {name} ({style})")
        ok += 1
        continue

    url_small = f"https://img.icons8.com/{api_style}/50/{name}.png"
    url_large = f"https://img.icons8.com/{api_style}/100/{name}.png"

    try:
        urllib.request.urlretrieve(url_small, small_file)
        urllib.request.urlretrieve(url_large, large_file)
        print(f"  DOWNLOADED {name} ({style})")
        ok += 1
    except Exception as e:
        print(f"  FAIL {name} ({style}): {e}")
        fail += 1

    time.sleep(0.3)

print(f"\nDownloaded: {ok} OK, {fail} fail(s)")
