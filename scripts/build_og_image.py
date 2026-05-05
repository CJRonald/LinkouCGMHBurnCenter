"""Generate OG preview images (1200x630) for Chinese and English.

Output:
    assets/images/og-image.png      (Chinese)
    assets/images/og-image-en.png   (English)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "assets" / "images"

W, H = 1200, 630
BG_COLOR = (44, 90, 160)       # --primary-color #2c5aa0
ACCENT_COLOR = (0, 166, 81)    # --accent-color #00a651
TEXT_COLOR = (255, 255, 255)


def find_font(candidates: list, size: int) -> ImageFont.FreeTypeFont:
    for path in candidates:
        if Path(path).exists():
            print(f"  Using font: {path}", file=sys.stderr)
            return ImageFont.truetype(path, size)
    print(f"WARN: no font found in {candidates}, using default", file=sys.stderr)
    return ImageFont.load_default()


# macOS system font candidates — ordered by preference
# PingFang (macOS 10.11+) first, then STHeiti fallback, then Arial Unicode
ZH_FONTS = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
]
EN_FONTS = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/Library/Fonts/Arial.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
]


def render(title: str, subtitle: str, fonts: list, out_name: str) -> None:
    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Decorative left bar
    draw.rectangle([0, 0, 20, H], fill=ACCENT_COLOR)

    title_font = find_font(fonts, 84)
    subtitle_font = find_font(fonts, 38)

    # Title centered vertically in upper half
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(
        ((W - title_w) / 2, H * 0.32),
        title,
        font=title_font,
        fill=TEXT_COLOR,
    )

    # Subtitle below
    sub_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(
        ((W - sub_w) / 2, H * 0.56),
        subtitle,
        font=subtitle_font,
        fill=(220, 230, 245),
    )

    out_path = OUT_DIR / out_name
    img.save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    render(
        "林口長庚燒傷中心",
        "Linkou CGMH Burn Center",
        ZH_FONTS,
        "og-image.png",
    )
    render(
        "Linkou CGMH Burn Center",
        "Taiwan's Largest Burn Treatment Center",
        EN_FONTS,
        "og-image-en.png",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
