#!/usr/bin/env python3
"""
Download retro game console icons from KyleBing/retro-game-console-icons.
Licensed under GPL-3.0. Attribute: "Console icons by KyleBing (https://github.com/KyleBing/retro-game-console-icons)"

Source: https://raw.githubusercontent.com/KyleBing/retro-game-console-icons/main/series_trimui/300w@1x/<FILE>.png
"""

import urllib.request
import pathlib
import subprocess
import time

BASE = pathlib.Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"
PREFIX = "retro"
CDN = "https://raw.githubusercontent.com/KyleBing/retro-game-console-icons/main/series_trimui/300w@1x/{file}"

CONSOLES = [
    # (our_name, kylebing_file, display_name)
    ("nes",            "FC.png",      "NES / Famicom"),
    ("snes",           "SFC.png",     "SNES / Super Famicom"),
    ("nintendo-64",    "N64.png",     "Nintendo 64"),
    ("gamecube",       "NGC.png",     "GameCube"),
    ("game-boy",       "GB.png",      "Game Boy"),
    ("game-boy-color", "GBC.png",     "Game Boy Color"),
    ("game-boy-advance", "GBA.png",   "Game Boy Advance"),
    ("nintendo-ds",    "NDS.png",     "Nintendo DS"),
    ("sega-genesis",   "MD.png",      "Sega Genesis / Mega Drive"),
    ("sega-saturn",    "SATURN.png",  "Sega Saturn"),
    ("dreamcast",      "DC.png",      "Dreamcast"),
    ("neogeo",         "NEOGEO.png",  "Neo Geo"),
    ("game-gear",      "GG.png",      "Sega Game Gear"),
    ("master-system",  "MS.png",      "Sega Master System"),
    ("pc-engine",      "PCE.png",     "PC Engine / TurboGrafx-16"),
    ("virtual-boy",    "VB.png",      "Virtual Boy"),
]

def download_file(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
        return True
    except Exception as e:
        print(f"    DL error: {e}")
        return False

ok = 0
fail = 0

for name, kbfile, display in CONSOLES:
    small_file = SMALL / f"{PREFIX}-{name}-50.png"
    large_file = LARGE / f"{PREFIX}-{name}-100.png"

    if small_file.exists() and large_file.exists():
        print(f"  EXIST {PREFIX}-{name} ({display})")
        ok += 1
        continue

    url = CDN.format(file=kbfile)
    tmp = BASE / f"__tmp_console_{name}.png"

    if download_file(url, tmp):
        subprocess.run(
            ["magick", str(tmp), "-filter", "Lanczos",
             "-resize", "100x100", str(large_file)],
            capture_output=True, timeout=30
        )
        subprocess.run(
            ["magick", str(tmp), "-filter", "Lanczos",
             "-resize", "50x50", str(small_file)],
            capture_output=True, timeout=30
        )
        tmp.unlink(missing_ok=True)

        if large_file.exists() and small_file.exists():
            print(f"  DOWNLOADED {PREFIX}-{name} ({display})")
            ok += 1
        else:
            print(f"  FAIL resize {PREFIX}-{name} ({display})")
            fail += 1
    else:
        print(f"  FAIL download {PREFIX}-{name} ({display})")
        fail += 1

    time.sleep(0.2)

print(f"\nDownloaded: {ok} OK, {fail} fail(s)")
