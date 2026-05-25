#!/usr/bin/env python3
"""
Download dev tools, apps, and utility icons from Icons8.

Usage:
    python download-dev.py
"""

import urllib.request
import pathlib
import sys

BASE = pathlib.Path(__file__).parent.resolve()
SMALL = BASE / "50x50"
LARGE = BASE / "100x100"

# (name, style) — verified on Icons8 CDN
ITEMS = [
    # --- IDEs / Dev Tools ---
    ("android-studio",   "2d"),
    ("eclipse",          "2d"),
    ("intellij-idea",    "2d"),
    ("visual-studio",    "2d"),
    ("git",              "2d"),
    ("bash",             "2d"),
    ("node-js",          "2d"),
    ("javascript",       "2d"),
    ("typescript",       "2d"),
    ("php",              "2d"),
    ("swift",            "2d"),
    ("css3",             "2d"),
    # --- Apps / Software ---
    ("7zip",             "2d"),
    ("affinity-designer","2d"),
    ("anydesk",          "2d"),
    ("crystaldiskinfo",  "2d"),
    ("foxit-reader",     "2d"),
    ("gimp",             "2d"),
    ("google-drive",     "2d"),
    ("inkscape",         "2d"),
    ("ms-excel",         "3d"),
    ("ms-powerpoint",    "2d"),
    ("ms-word",          "3d"),
    ("msi-afterburner",  "2d"),
    ("mysql",            "2d"),
    ("nextcloud",        "2d"),
    ("notepad-plus-plus","2d"),
    ("obs-studio",       "2d"),
    ("opera",            "2d"),
    ("paint-net",        "2d"),
    ("redis",            "2d"),
    ("remote-desktop",   "2d"),
    ("skype",            "2d"),
    ("sublime-text",     "2d"),
    ("teamviewer",       "2d"),
    ("virtualbox",       "2d"),
    ("vlc",              "3d"),
    ("zoom",             "3d"),
    # --- Dev actions / Code ---
    ("checkout",         "2d"),
    ("class",            "3d"),
    ("clone",            "2d"),
    ("dashboard",        "3d"),
    ("fork",             "3d"),
    ("indent",           "2d"),
    ("job",              "3d"),
    ("library",          "3d"),
    ("outdent",          "2d"),
    ("patch",            "2d"),
    ("pipeline",         "3d"),
    ("run-command",      "2d"),
    ("spell-check",      "2d"),
    ("variable",         "2d"),
    # --- Network / Infra ---
    ("bridge",           "3d"),
    ("internet",         "2d"),
    ("network",          "2d"),
    ("router",           "2d"),
    ("torrent",          "2d"),
    ("wifi",             "3d"),
    # --- UI / General ---
    ("delete",           "2d"),
    ("duplicate",        "2d"),
    ("options",          "2d"),
    ("sort",             "2d"),
    ("upload",           "3d"),
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
    print("  Dev / Apps / Utilities Icon Download")
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
