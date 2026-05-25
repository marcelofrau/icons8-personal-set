#!/usr/bin/env python3
"""
Batch download new Icons8 icons: devices, tools, emojis, apps, gaming.
"""

import urllib.request, pathlib, time, sys

BASE = pathlib.Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

# (name, style) — style is '3d' or '2d'
TO_DOWNLOAD = [
    # --- Devices / Hardware ---
    ("smartphone", "3d"),
    ("smartphone-tablet", "3d"),
    ("iphone", "2d"),
    ("ipad", "2d"),
    ("cell-phone", "2d"),
    ("android-tablet", "2d"),
    ("smart-home", "3d"),
    ("google-home", "2d"),
    ("nest", "3d"),
    ("tv", "3d"),
    ("monitor", "3d"),
    ("display", "2d"),
    ("lcd", "2d"),
    # Power
    ("plug", "3d"),
    ("battery", "3d"),
    ("ups", "2d"),
    # Tools
    ("wrench", "3d"),
    ("hammer", "3d"),
    ("screwdriver", "2d"),
    ("pliers", "3d"),
    ("drill", "3d"),
    ("saw", "3d"),
    ("ruler", "3d"),
    ("toolbox", "3d"),
    ("soldering-iron", "3d"),
    # Audio
    ("headphones", "2d"),
    ("microphone", "3d"),
    ("subwoofer", "3d"),
    # Networking
    ("switch", "3d"),
    ("hub", "3d"),
    ("satellite", "3d"),
    ("radar", "3d"),
    # Peripherals
    ("webcam", "3d"),
    ("mouse", "3d"),
    ("hdmi-cable", "2d"),
    # --- New Emojis ---
    ("sleeping", "3d"),
    ("disappointed", "3d"),
    ("skull", "3d"),
    ("ghost", "3d"),
    ("alien", "3d"),
    ("robot", "3d"),
    ("clown", "2d"),
    ("pray", "2d"),
    ("nerd", "2d"),
    ("partying-face", "3d"),
    ("hot-face", "3d"),
    ("cold-face", "3d"),
    ("apple", "3d"),
    ("banana", "3d"),
    ("grapes", "3d"),
    ("watermelon", "3d"),
    ("strawberry", "3d"),
    ("cherry", "3d"),
    ("peach", "3d"),
    ("pear", "3d"),
    ("pineapple", "2d"),
    ("avocado", "3d"),
    ("tomato", "3d"),
    ("eggplant", "3d"),
    ("broccoli", "3d"),
    ("carrot", "3d"),
    ("corn", "3d"),
    ("hot-dog", "3d"),
    ("pizza", "2d"),
    ("hamburger", "3d"),
    ("cookie", "3d"),
    ("cake", "2d"),
    ("candy", "3d"),
    ("dog", "3d"),
    ("wolf", "3d"),
    ("fox", "3d"),
    ("lion", "2d"),
    ("tiger", "3d"),
    ("horse", "3d"),
    ("unicorn", "3d"),
    ("zebra", "3d"),
    ("deer", "3d"),
    ("cow", "3d"),
    ("pig", "3d"),
    ("frog", "3d"),
    ("chicken", "3d"),
    ("snake", "3d"),
    ("dragon", "2d"),
    ("whale", "3d"),
    ("dolphin", "3d"),
    ("fish", "3d"),
    ("octopus", "3d"),
    ("bee", "2d"),
    ("butterfly", "3d"),
    ("snail", "3d"),
    ("koala", "3d"),
    ("panda", "3d"),
    ("monkey-face", "3d"),
    ("gorilla", "2d"),
    ("elephant", "3d"),
    ("camel", "3d"),
    ("giraffe", "2d"),
    ("llama", "2d"),
    ("sheep", "2d"),
    ("mouse", "3d"),
    ("hamster", "3d"),
    ("rabbit", "3d"),
    ("bat", "3d"),
    ("bear", "3d"),
    ("owl", "3d"),
    ("duck", "3d"),
    ("swan", "3d"),
    ("peacock", "3d"),
    ("flamingo", "3d"),
    ("crab", "3d"),
    ("lobster", "3d"),
    ("jellyfish", "3d"),
    ("cactus", "2d"),
    ("rose", "3d"),
    ("sunflower", "3d"),
    ("palm-tree", "3d"),
    ("maple-leaf", "2d"),
    ("mushroom", "3d"),
]

STYLE_MAP = {"3d": "3d-fluency", "2d": "fluency"}
SUFFIX_MAP = {"3d": "-3d", "2d": "-2d"}

# Check which base names already exist (without style suffix)
existing_bases = set()
for f in SMALL.glob("*.png"):
    import re
    base = re.sub(r"-(?:3d|2d)?-?(?:50|100|16|32|48|128|256)$", "", f.stem)
    base = re.sub(r"^icons8-", "", base)
    existing_bases.add(base)

ok = 0
fail = 0
skipped_names = []

for name, style in TO_DOWNLOAD:
    if name in existing_bases:
        skipped_names.append(name)
        continue

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

    time.sleep(0.25)

print(f"\nDownloaded: {ok} OK, {fail} fail(s)")
if skipped_names:
    print(f"Skipped (name conflict): {', '.join(skipped_names)}")
