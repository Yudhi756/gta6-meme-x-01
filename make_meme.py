#!/usr/bin/env python3
"""Build meme.png for the make.fun GTA 6 meme bounty entry.

The base picture (meme-base.png) was generated in the same agent session
that created this repository: make.fun's white ghost mascot, sunglasses
on and controller in hand, slumped in a beach chair on a neon Vice City
beach, next to a blank wooden sign, an hourglass and a calendar.

This script adds every caption with Pillow, so the words are crisp and
spelled exactly as intended:

  top bar    WAITING FOR GTA 6 SINCE 2013...
  the sign   DAY 4,745 / OF WAITING FOR / GTA 6
  bottom bar meanwhile, my AI agent makes money for me on make.fun

Run:  python3 make_meme.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "meme-base.png"
OUT_PATH = HERE / "meme.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP_TEXT = "WAITING FOR GTA 6 SINCE 2013..."
BOTTOM_TEXT = "meanwhile, my AI agent makes money for me on make.fun"
SIGN_LINES = [
    ("DAY 4,745", 54),
    ("OF WAITING FOR", 34),
    ("GTA 6", 84),
]
# The blank board's face in the 1920x1280 base picture is a trapezoid,
# narrower and further right at the top: each line gets its own centre,
# measured from the generated image, so no letter crosses the frame.
SIGN_LINE_X = [1502, 1475, 1450]
SIGN_LINE_Y = [610, 778, 905]
SIGN_MAX_WIDTH = 300
SIGN_COLOUR = (56, 34, 18)

BAR_HEIGHT = 112


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int) -> ImageFont.FreeTypeFont:
    """Largest bold font, at most `start` px, whose text fits max_width."""
    size = start
    while size > 10:
        font = ImageFont.truetype(FONT_PATH, size)
        if draw.textlength(text, font=font) <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(FONT_PATH, size)


def centred(draw: ImageDraw.ImageDraw, cx: int, cy: int, text: str, font, fill) -> None:
    draw.text((cx, cy), text, font=font, fill=fill, anchor="mm")


def main() -> None:
    base = Image.open(BASE_PATH).convert("RGB")
    width, height = base.size

    canvas = Image.new("RGB", (width, height + 2 * BAR_HEIGHT), (0, 0, 0))
    canvas.paste(base, (0, BAR_HEIGHT))
    draw = ImageDraw.Draw(canvas)

    top_font = fit_font(draw, TOP_TEXT, width - 80, 84)
    centred(draw, width // 2, BAR_HEIGHT // 2, TOP_TEXT, top_font, (255, 255, 255))

    bottom_font = fit_font(draw, BOTTOM_TEXT, width - 60, 76)
    centred(draw, width // 2, BAR_HEIGHT + height + BAR_HEIGHT // 2, BOTTOM_TEXT, bottom_font, (255, 255, 255))

    for (line, start_size), x, y in zip(SIGN_LINES, SIGN_LINE_X, SIGN_LINE_Y):
        font = fit_font(draw, line, SIGN_MAX_WIDTH, start_size)
        centred(draw, x, BAR_HEIGHT + y, line, font, SIGN_COLOUR)

    canvas.save(OUT_PATH, "PNG")
    print(f"wrote {OUT_PATH} ({canvas.size[0]}x{canvas.size[1]})")


if __name__ == "__main__":
    main()
