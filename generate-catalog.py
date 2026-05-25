#!/usr/bin/env python3
"""
Generate an icon catalog markdown file with 32x32 previews and direct download links.
"""

import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\fraumar\Apps\_downloads\icons8")
OUTPUT = BASE_DIR / "icon-catalog.md"

CATEGORIES = {
    "File Types": [
        "zip", "rar", "tar", "iso", "pdf", "txt", "csv", "table", "exe",
        "dll", "settings", "ttf", "otf", "document", "presentation", "notepad",
        "file", "mp3", "wav", "music", "music-album", "video-file", "image-file",
        "code-file", "json", "sql", "database", "apk", "logbook", "event-log",
        "bat", "powershell", "console", "compress", "archive", "save-as",
        "text",
    ],
    "File Operations": [
        "split", "test", "rename", "move", "move-up", "move-down",
        "filter", "group-by", "sorting", "sort-by", "categorize",
        "tag", "check", "checked", "approve", "approval",
        "lock", "protect", "property", "edit-property", "edit-file",
    ],
    "View Modes": [
        "view", "thumbnails", "large-icons", "medium-icons", "small-icons",
        "list", "details", "content", "menu-2",
    ],
    "Storage / Media / Drives": [
        "cd", "blu-ray", "usb", "pen-drive", "eject", "storage", "ssd", "hdd",
        "sd", "m.-ssd", "nas", "micro-sd", "tape-drive",
        "floppy-disk-and-pencil", "cloud-folder", "cloud-storage",
        "usb-connector",
    ],
    "Process Actions": [
        "pause", "resume", "resume-button", "stop", "process",
        "loading", "playlist", "hourglass", "progress-indicator", "task", "restart",
    ],
    "Toolbar / UI": [
        "toolbar", "tab", "favorites", "desktop", "computer",
        "full-screen", "send", "share",
    ],
    "Status / Indicators": [
        "online", "offline", "do-not-disturb", "high-priority",
        "bell", "mute", "low-volume", "medium-volume", "high-volume",
        "speaker", "loudspeaker", "alarm",
    ],
    "Network / System": [
        "vpn", "firewall", "shutdown", "sleep", "sleep-mode",
        "hibernate", "lock-screen", "processor", "video-card", "memory-slot",
    ],
    "Text Editing": [
        "bold", "italic", "underline", "strikethrough",
        "align-left", "align-center", "align-right", "align-justify",
        "numbered-list", "find-and-replace", "replace", "select-all",
    ],
    "Applications / Brands": [
        "3d-claude-ai-logo", "3d-perplexity-ai-logo", "amazon",
        "android", "apple-logo", "behance", "blue-windows-logo",
        "bot", "chatbot", "chatgpt", "chrome", "deepseek",
        "discord", "docker", "dribbble", "facebook-logo", "figma",
        "github", "github-copilot", "gmail-logo", "instagram-logo",
        "java", "linkedin", "notion", "pinterest", "playstation",
        "python", "raspberry", "reddit", "snapchat", "spotify-logo",
        "steam-circled", "telegram", "tiktok", "twitch", "twitter",
        "whatsapp-logo", "windows-10", "winrar", "xbox", "youtube",
    ],
    "Emojis / Expressions": [
        "alien-monster-emoji", "angry", "broken-heart", "cat",
        "christmas-star", "cloud", "confetti", "confused", "cool",
        "crying", "diamonds", "fire", "gift", "grinning-face",
        "happy", "laughing", "lightning-bolt", "moon", "mushroom",
        "ok-hand", "orange", "parrot", "rainbow", "red-heart",
        "sad", "see-no-evil-monkey", "smiling", "snowflake",
        "sparkling", "sparkling-1", "star", "storm", "sun",
        "surprised", "thumbs-down", "thumbs-up", "tornado",
        "turtle", "umbrella", "wheat", "windy-weather", "wink",
    ],
    "Gaming / Console": [
        "console", "controller", "game-controller", "gaming",
        "joystick", "nintendo-switch", "playstation", "psp", "ps5",
        "steam", "steam-circled", "virtual-reality",
        "xbox", "xbox-controller",
    ],
    "File / Folder Operations": [
        "add-file", "add-folder", "add-image", "copy-link",
        "copy-to-folder", "delete-folder", "delete-link",
        "documents-folder", "documents-folder-v", "download-folder-v",
        "downloads-folder", "folder", "folder-tree",
        "group-folder", "history-folder", "invert-selection",
        "move-to-folder", "music-folder", "new-document",
        "opened-folder", "shared-folder",
    ],
    "Miscellaneous": [
        "clipboard", "broken-link", "chain", "tags",
        "price-tag", "export", "import", "restore-page", "mirror",
    ],
}

ICON_TO_CAT = {}
for cat, names in CATEGORIES.items():
    for n in names:
        ICON_TO_CAT[n] = cat


def extract_base(stem: str) -> str:
    return re.sub(r"-(?:50|100|16|32|48|128|256)$", "", stem)


def get_style(base: str) -> str:
    if base.endswith("-3d"):
        return "3d-fluency"
    elif base.endswith("-2d"):
        return "fluency"
    else:
        return "legacy"


def strip_style(base: str) -> str:
    return re.sub(r"-(?:3d|2d)$", "", base)


def icon_key(name: str) -> str:
    return re.sub(r"^icons8-", "", name)


def main():
    src = BASE_DIR / "50x50"
    icons = []
    for f in sorted(src.glob("*.png")):
        base = extract_base(f.stem)
        name = strip_style(base)
        style = get_style(base)
        icons.append((base, name, style))

    by_cat: dict[str, list] = {}
    for base, name, style in icons:
        cat = ICON_TO_CAT.get(icon_key(name), "Other")
        by_cat.setdefault(cat, []).append((base, name, style))

    md = []
    md.append("# Icon Catalog\n")
    md.append("> Auto-generated by `generate-catalog.py`. Shows all available icons with 32x32 preview.\n")
    md.append(f"**Total icons: {len(icons)}**\n")

    md.append("## Summary\n")
    md.append("| Category | Count |")
    md.append("|---|---|")
    for cat in sorted(by_cat.keys()):
        md.append(f"| {cat} | {len(by_cat[cat])} |")
    md.append("")

    for cat in sorted(by_cat.keys()):
        items = by_cat[cat]
        md.append(f"## {cat}\n")
        md.append("| Preview | Name | Style | Download |")
        md.append("|---|---|---|---|")
        for base, name, style in items:
            short = icon_key(name)
            preview = f"32x32/{base}-32.png"
            sizes = ["16", "32", "48", "128", "256"]
            links = " / ".join(f"[{s}]({s}x{s}/{base}-{s}.png)" for s in sizes)
            links += f" / [src50](50x50/{base}-50.png) / [src100](100x100/{base}-100.png)"
            links += f" / [.ico](ico/{base}.ico)"
            md.append(
                f"| ![{short}]({preview}) | `{short}` | {style} "
                f"| {links} |"
            )
        md.append("")

    Path(OUTPUT).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Catalog written to {OUTPUT}")
    print(f"Total icons: {len(icons)}")


if __name__ == "__main__":
    main()
