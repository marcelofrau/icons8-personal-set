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
    "Gaming / Console": [
        "atari", "cards", "console", "controller", "dice",
        "game-controller", "gaming", "joystick", "nintendo-switch",
        "playstation", "playstation-5", "ps2", "ps5", "psp",
        "puzzle", "steam", "steam-circled", "steam-deck",
        "virtual-reality", "xbox", "xbox-controller",
        "xbox-series-s", "xbox-series-x",
        # FluentUI gaming emojis
        "fluentui-chess-pawn", "fluentui-club",
        "fluentui-diamond-suit", "fluentui-flower-cards",
        "fluentui-game-die", "fluentui-heart-suit",
        "fluentui-joker", "fluentui-joystick-emoji",
        "fluentui-mahjong", "fluentui-puzzle-piece",
        "fluentui-slot-machine", "fluentui-spade",
        "fluentui-video-game",
        # Retro console icons (KyleBing)
        "retro-nes", "retro-snes", "retro-nintendo-64",
        "retro-gamecube", "retro-game-boy", "retro-game-boy-color",
        "retro-game-boy-advance", "retro-nintendo-ds",
        "retro-sega-genesis", "retro-sega-saturn", "retro-dreamcast",
        "retro-neogeo", "retro-game-gear", "retro-master-system",
        "retro-pc-engine", "retro-virtual-boy",
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
    "Hardware / Devices": [
        "3d-printer", "android-tablet", "bluetooth", "camcorder",
        "camera", "cell-phone", "device-manager", "ipad", "iphone",
        "keyboard", "keyboard-1", "laptop", "laptop-coding",
        "lcd", "monitor", "motherboard", "mouse", "multiple-devices",
        "nest", "office-phone", "pos-terminal", "printer",
        "radio-waves", "server", "smart-home", "smartphone",
        "smartphone-tablet", "tv", "webcam", "workstation",
        "wi-fi-logo", "wi-fi-router", "wired-network",
    ],
    "Tools / DIY": [
        "drill", "hammer", "pliers", "ruler", "saw",
        "screwdriver", "soldering-iron", "toolbox", "tools",
        "tools-1", "wrench",
    ],
    "Power / Electronics": [
        "battery", "plug", "display", "google-home", "hdmi-cable",
        "hub", "radar", "satellite", "switch", "ups",
    ],
    "Audio": [
        "headphones", "loudspeaker", "microphone", "subwoofer",
    ],
    "UI / Navigation": [
        "add", "adjust", "arrow-down", "arrow-left", "arrow-right",
        "arrow-up", "arrow-upload", "back", "cancel", "check-mark",
        "close", "close-window", "close-window-x", "close-x",
        "copy", "cursor", "cut", "data-transfer",
        "delete-shield", "down", "download", "download-from-cloud",
        "edit-pencil", "erase", "eye", "eye-1", "forward", "home",
        "info", "info-1", "info-popup", "left", "link", "menu", "minus",
        "paste", "pencil", "pin", "play", "plus", "plus-math",
        "push-pin", "redo", "refresh", "remove", "response", "right",
        "save", "search", "switch-off", "synchronize", "trash", "undo",
        "unchecked-checkbox", "up",
    ],
    "Office / Productivity": [
        "about", "accounting", "alarm-clock", "application",
        "at-sign", "barcode", "book", "book-shelf", "bookmark",
        "calculator", "calendar", "certificate", "chart", "clock",
        "coin", "coins", "contacts", "control-panel", "copybook",
        "create", "credit-card-cv", "date-span", "documents",
        "empty-box", "graph-report", "inbox", "language", "layers",
        "mail", "mailbox", "maintenance", "manager", "map", "map-pin",
        "module", "moleskine", "navigation", "news", "package",
        "password", "pencil-cup", "popular", "print", "prize",
        "profile", "qr-code", "rating", "services", "services-1",
        "shop", "shopping-bag", "signing-a-document",         "today", "users", "verified-account",
        "writer-male",
    ],
    "Development / Code": [
        "code", "command-line", "programming", "source-code",
    ],
    "Communication / Social": [
        "chat", "chat-message", "comments", "disconnected",
    ],
    "Design / Creative": [
        "color-palette", "design", "paint-brush", "paint-palette",
        "picture",
    ],
    "Security": [
        "access-denied", "administrator", "bank-safe", "bios",
        "conflict", "error-sign", "key", "no-entry", "stop-sign",
    ],
    "Transportation": [
        "car", "gas-station", "taxi",
    ],
    "Miscellaneous": [
        "automatic", "bang", "box-important", "broom", "company",
        "compass", "clipboard", "broken-link", "chain", "tags",
        "price-tag", "export", "import", "restore-page", "mirror",
        "documentary", "done", "done-1", "doctors-bag",
        "energy-meter", "engine", "flash-on",
        "full-tool-storage-box", "gear", "globe-africa", "gps-signal",
        "hamburger", "home-address", "home-office",
        "housekeeping", "idea", "ingredients", "inspection",
        "real-estate", "recycle", "robotic", "rocket", "sound",
        "test-passed", "test-tube", "two-gears", "video-gallery",
    ],
    "Emojis / Expressions": [
        "alien", "alien-monster-emoji", "angry", "apple", "avocado",
        "banana", "bear", "bee", "broken-heart", "broccoli", "butterfly",
        "cactus", "cake", "camel", "candy", "carrot", "cat", "cherry", "chicken",
        "christmas-star", "cloud", "clown", "cold-face", "confetti", "confused",
        "cookie", "cool", "corn", "cow", "crab", "crying", "deer",
        "diamonds", "disappointed", "dog", "dolphin", "dragon",
        "duck", "eggplant", "elephant", "fire", "fish", "flamingo",
        "fox", "frog", "ghost", "gift", "giraffe", "gorilla", "grapes",
        "grinning-face", "hamburger", "hamster", "happy", "horse",
        "hot-dog", "hot-face", "jellyfish", "koala", "laughing",
        "lightning-bolt", "lion", "llama", "lobster", "maple-leaf",
        "monkey-face", "moon", "mouse", "mushroom", "nerd", "octopus",
        "ok-hand", "orange", "owl", "palm-tree", "panda", "parrot",
        "partying-face", "peach", "peacock", "pear", "pig", "pineapple",
        "pizza", "pray", "rabbit", "rainbow", "red-heart", "robot",
        "rose", "sad", "see-no-evil-monkey", "sheep", "skull",
        "sleeping", "smiling", "snail", "snake", "snowflake",
        "sparkling", "sparkling-1", "star", "strawberry", "storm",
        "sun", "sunflower", "surprised", "swan", "thumbs-down",
        "thumbs-up", "tiger", "tomato", "tornado", "turtle",
        "umbrella", "unicorn", "watermelon", "wheat", "whale",
        "windy-weather", "wink", "wolf", "zebra",
        # FluentUI + Twemoji emojis
        "fluentui-beaming-emoji", "fluentui-blue-heart",
        "fluentui-broken-heart-emoji", "fluentui-clapping",
        "fluentui-cloud-emoji", "fluentui-fire-emoji",
        "fluentui-flexed-biceps", "fluentui-folded-hands",
        "fluentui-green-heart", "fluentui-grinning-emoji",
        "fluentui-heart-eyes", "fluentui-joy-emoji",
        "fluentui-kissing-heart", "fluentui-lightning-emoji",
        "fluentui-purple-heart", "fluentui-rainbow-emoji",
        "fluentui-red-heart-emoji", "fluentui-rose-emoji",
        "fluentui-snowflake-emoji", "fluentui-sparkling-heart",
        "fluentui-star-emoji", "fluentui-sun-emoji",
        "fluentui-thumbs-down-emoji", "fluentui-thumbs-up-emoji",
        "fluentui-waving", "fluentui-yellow-heart",
    ],
}

ICON_TO_CAT = {}
for cat, names in CATEGORIES.items():
    for n in names:
        ICON_TO_CAT[n] = cat


def extract_base(stem: str) -> str:
    return re.sub(r"-(?:50|100|16|32|48|128|256)$", "", stem)


def get_style(base: str) -> str:
    if base.startswith("fluentui-"):
        return "fluentui-emoji"
    if base.startswith("retro-"):
        return "retro"
    if base.endswith("-3d") or not re.search(r"-(?:3d|2d)$", base):
        return "3d-fluency"
    return "fluency"


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

    def sort_key(cat: str) -> tuple[int, str]:
        return (1 if cat == "Emojis / Expressions" else 0, cat)

    md.append("## Summary\n")
    md.append("| Category | Count |")
    md.append("|---|---|")
    for cat in sorted(by_cat.keys(), key=sort_key):
        md.append(f"| {cat} | {len(by_cat[cat])} |")
    md.append("")

    for cat in sorted(by_cat.keys(), key=sort_key):
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
