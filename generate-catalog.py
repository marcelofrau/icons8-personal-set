#!/usr/bin/env python3
"""
Generate an icon catalog markdown file with 32x32 previews and direct download links.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
OUTPUT = BASE_DIR / "icon-catalog.md"
OUTPUT_AI = BASE_DIR / "icon-catalog-ai.md"
CATALOG_DIR = BASE_DIR / "catalog"

LAST_CATS = {"Emojis / Expressions", "Food & Drinks"}

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
        "bridge", "firewall", "hibernate", "internet", "lock-screen",
        "memory-slot", "network", "processor", "router", "shutdown",
        "sleep", "sleep-mode", "torrent", "video-card", "vpn", "wifi",
    ],
    "Text Editing": [
        "bold", "italic", "underline", "strikethrough",
        "align-left", "align-center", "align-right", "align-justify",
        "numbered-list", "find-and-replace", "replace", "select-all",
    ],
    "Applications / Brands": [
        "3d-claude-ai-logo", "3d-perplexity-ai-logo", "amazon",
        "anime",
        "android", "android-studio", "apple-logo", "behance",
        "blue-windows-logo", "bot", "chatbot", "chatgpt", "chrome",
        "deepseek", "discord", "docker", "dribbble", "eclipse",
        "facebook-logo", "figma", "git", "github", "github-copilot",
        "gmail-logo", "inkscape", "instagram-logo", "intellij-idea",
        "java", "javascript", "linkedin", "ms-excel", "ms-powerpoint",
        "ms-word", "mysql", "node-js", "notion", "obs-studio", "opera",
        "pinterest", "playstation", "php", "python", "raspberry",
        "redis", "reddit", "skype", "snapchat", "spotify-logo",
        "steam-circled",         "sublime-text", "swift", "teamviewer",
        "soulseek", "telegram", "tiktok", "twitch", "twitter", "typescript",
        "virtualbox", "visual-studio", "vlc", "whatsapp-logo",
        "windows-10", "winrar", "xbox", "youtube", "zoom",
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
        "7zip", "affinity-designer", "anydesk", "crystaldiskinfo",
        "drill", "foxit-reader", "gimp", "google-drive", "hammer",
        "msi-afterburner", "nextcloud", "notepad-plus-plus",
        "paint-net", "pliers", "remote-desktop", "ruler", "saw",
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
        "copy", "cursor", "cut", "data-transfer", "delete", "delete-shield",
        "down", "download", "download-from-cloud", "duplicate",
        "edit-pencil", "erase", "eye", "eye-1", "forward", "home",
        "info", "info-1", "info-popup", "left", "link", "menu", "minus",
        "options", "paste", "pencil", "pin", "play", "plus", "plus-math",
        "push-pin", "redo", "refresh", "remove", "response", "right",
        "save", "search", "sort", "switch-off", "synchronize", "trash",
        "undo", "unchecked-checkbox", "up", "upload",
        "discover",
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
        "bash", "checkout", "class", "clone", "code", "command-line",
        "fork", "indent", "library", "outdent", "patch", "pipeline",
        "programming", "run-command", "source-code", "spell-check",
        "tag", "variable",
    ],
    "Communication / Social": [
        "chat", "chat-message", "comments", "disconnected",
    ],
    "Design / Creative": [
        "color-palette", "design", "paint-brush", "paint-palette",
        "picture", "pencil-drawing", "video-editing", "timeline",
    ],
    "Security": [
        "access-denied", "administrator", "bank-safe", "bios",
        "conflict", "error-sign", "key", "no-entry", "stop-sign",
    ],
    "Transportation": [
        "car", "gas-station", "taxi",
    ],
    "Food & Drinks": [
        # Fruits
        "blueberry", "coconut", "date", "kiwi", "lemon", "lychee",
        "mango", "melon", "olive", "papaya", "pomegranate", "fig",
        # Food
        "bacon", "baguette", "bread", "cheese", "chili-pepper",
        "chocolate-bar", "croissant", "cupcake", "doughnut",
        "french-fries", "garlic", "honey", "meat", "noodles", "onion",
        "pancake", "peanut", "popcorn", "pretzel", "salad", "sandwich",
        "sausage", "spaghetti", "steak", "sushi", "taco", "toast",
        "egg", "rice", "dumpling", "lollipop", "muffin", "shrimp", "soup",
        # Drinks
        "beer", "bottle-of-water", "champagne", "cocktail", "coffee",
        "lime", "milk", "orange-juice", "soda", "tea", "water",
        "white-wine", "wine-bottle", "wine-glass",
        # FluentUI food emojis
        "fluentui-lemon", "fluentui-fig", "fluentui-egg", "fluentui-rice",
        "fluentui-dumpling", "fluentui-lollipop", "fluentui-muffin",
        "fluentui-shrimp", "fluentui-soup",
        # Coffee extras
        "coffee-espresso", "coffee-latte-1", "coffee-latte-2", "coffee-cup",
    ],
    "Miscellaneous": [
        "automatic", "bang", "box-important", "broom", "company",
        "compass", "clipboard", "broken-link", "chain", "tags",
        "price-tag", "export", "import", "restore-page", "mirror",
        "documentary", "done", "done-1", "doctors-bag",
        "energy-meter", "engine", "flash-on",
        "full-tool-storage-box", "gear", "globe-africa", "gps-signal",
        "home-address", "home-office",
        "housekeeping", "idea", "ingredients", "inspection",
        "real-estate", "recycle", "robotic", "rocket", "sound",
        "test-passed", "test-tube", "two-gears", "video-gallery",
        "tv-show", "film-reel", "children", "speed", "wizard",
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
    return re.sub(r"^(icons8|fluentui)-", "", name)


def sort_key(cat: str) -> tuple[int, str]:
    return (1 if cat in LAST_CATS else 0, cat)


COMPACT_THRESHOLD = 200
ULTRA_COMPACT_THRESHOLD = 500


def write_full_row(base: str, name: str, style: str) -> str:
    short = icon_key(name)
    sizes = ["16", "32", "48", "128", "256"]
    links = " / ".join(f"[{s}](../{s}x{s}/{base}-{s}.png)" for s in sizes)
    links += f" / [src50](../50x50/{base}-50.png) / [src100](../100x100/{base}-100.png)"
    links += f" / [.ico](../ico/{base}.ico)"
    return f"| ![{short}](../32x32/{base}-32.png) | `{short}` | {style} | {links} |"


def write_compact_row(base: str, name: str) -> str:
    short = icon_key(name)
    return f"- `{short}` — [.ico](../ico/{base}.ico)"


def write_tight_row(base: str, name: str) -> str:
    short = icon_key(name)
    return f"- `{short}`"


def write_category_file(cat: str, items: list) -> str:
    """Write one category markdown file to catalog/. Returns the filename."""
    safe = cat.replace("/", "-").replace(" ", "-")
    filename = f"{safe}.md"
    path = CATALOG_DIR / filename

    lines = [f"# {cat}\n", f"{len(items)} icons\n", ""]

    if len(items) < COMPACT_THRESHOLD:
        lines.append("| Preview | Name | Style | Download |")
        lines.append("|---|---|---|---|")
        for base, name, style in items:
            lines.append(write_full_row(base, name, style))
    elif len(items) < ULTRA_COMPACT_THRESHOLD:
        lines.append(f"Category too large for preview table ({len(items)} icons). Listing with download links:\n")
        for base, name, _ in items:
            lines.append(write_compact_row(base, name))
    else:
        lines.append(f"Large category ({len(items)} icons). Listing names only — browse via file browser:\n")
        for base, name, _ in items:
            lines.append(write_tight_row(base, name))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {filename} ({len(items)} icons)")
    return filename


def main():
    src = BASE_DIR / "50x50"
    icons = []
    for f in sorted(src.glob("*.png")):
        base = extract_base(f.stem)
        name = strip_style(base)
        style = get_style(base)
        icons.append((base, name, style))

    def categorize(name: str) -> str:
        key = icon_key(name)
        if key in ICON_TO_CAT:
            return ICON_TO_CAT[key]
        if name in ICON_TO_CAT:
            return ICON_TO_CAT[name]
        if base.startswith("retro-"):
            return "Gaming / Console"
        if base.startswith("fluentui-"):
            return "Emojis / Expressions"
        return "Other"

    by_cat: dict[str, list] = {}
    for base, name, style in icons:
        cat = categorize(name)
        by_cat.setdefault(cat, []).append((base, name, style))

    CATALOG_DIR.mkdir(exist_ok=True)

    # Write per-category files
    print("Writing category files...")
    cat_files: dict[str, str] = {}
    for cat in sorted(by_cat.keys(), key=sort_key):
        cat_files[cat] = write_category_file(cat, by_cat[cat])

    # Write summary index
    md = []
    md.append("# Icon Catalog\n")
    md.append("> Auto-generated by `generate-catalog.py`.\n")
    md.append(f"**Total icons: {len(icons)}**  \n")
    md.append("Each category has a separate file with 32x32 previews and download links.\n")
    md.append("")
    md.append("| Category | Count | File |")
    md.append("|---|---|---|")
    for cat in sorted(by_cat.keys(), key=sort_key):
        count = len(by_cat[cat])
        fname = cat_files[cat]
        md.append(f"| {cat} | {count} | [{fname}](catalog/{fname}) |")
    md.append("")

    Path(OUTPUT).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\nSummary written to {OUTPUT}")
    print(f"Total icons: {len(icons)}")

    # --- AI-friendly catalog ---
    sizes = ["16", "32", "48", "128", "256"]
    md_ai = []
    md_ai.append("# Icon Catalog (AI-friendly)\n")
    md_ai.append(f"Total icons: {len(icons)}")
    md_ai.append(f"Sizes: {', '.join(sizes)}px + source sizes 50, 100px")
    md_ai.append(f"Archive: .ico ({'+'.join(sizes)})\n")
    md_ai.append("Each entry below is the icon filename stem (without size suffix).")
    md_ai.append("To locate the files, append the desired size and extension:")
    md_ai.append("")
    md_ai.append("  <entry>         -> <dir>/<entry>-<size>.png")
    md_ai.append("  icons8-pdf-3d  -> 32x32/icons8-pdf-3d-32.png")
    md_ai.append("                 -> ico/icons8-pdf-3d.ico")
    md_ai.append("")
    md_ai.append("Available directories: 16x16/, 32x32/, 48x48/, 128x128/,")
    md_ai.append("256x256/, 50x50/ (source), 100x100/ (source), ico/")
    md_ai.append("")
    md_ai.append("Prefixes: icons8-*-3d (Icons8 3d-fluency), icons8-*-2d (fluency),")
    md_ai.append("fluentui-* (FluentUI/Twemoji), retro-* (KyleBing retro console)")
    md_ai.append("")

    for cat in sorted(by_cat.keys(), key=sort_key):
        items = by_cat[cat]
        md_ai.append(f"## {cat}")
        for base, name, style in items:
            md_ai.append(f"- {base}")
        md_ai.append("")

    Path(OUTPUT_AI).write_text("\n".join(md_ai) + "\n", encoding="utf-8")
    print(f"AI catalog written to {OUTPUT_AI}")


if __name__ == "__main__":
    main()
