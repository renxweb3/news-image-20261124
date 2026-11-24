#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page (1024x1024 PNG).

Deterministic: fixed text, fixed layout, no network, no randomness.
Regenerates entry.png in this directory. Run: python3 draw.py
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
INK = (15, 15, 15)
PAPER = (250, 248, 242)
RULE = (15, 15, 15)
ACCENT = (158, 27, 27)
NAVY = (16, 34, 64)
STEEL = (90, 130, 180)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = (cur + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill=INK, max_w=None):
    if max_w:
        for line in wrap(draw, text, fnt, max_w):
            draw.text((W / 2, y), line, font=fnt, fill=fill, anchor="ma")
            y += int(fnt.size * 1.25)
        return y
    draw.text((W / 2, y), text, font=fnt, fill=fill, anchor="ma")
    return y + int(fnt.size * 1.25)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    y = 22
    y = centered(d, y, "THE WORLD", font(SERIF_B, 76))
    d.line([(MARGIN, y + 2), (W - MARGIN, y + 2)], fill=RULE, width=3)
    y += 12
    y = centered(d, y, "TUESDAY, 24 NOVEMBER 2026  ·  ONE-DAY EDITION",
                 font(SANS_B, 23))
    d.line([(MARGIN, y + 2), (W - MARGIN, y + 2)], fill=RULE, width=1)

    # --- lead headline ---
    y += 12
    y = centered(d, y, "NVIDIA BRINGS BACK HUANG", font(SERIF_B, 48))
    y = centered(d, y, "AFTER TRUMP STEPS IN", font(SERIF_B, 48))
    y += 6
    deck = ("The board reinstates its chief executive less than two weeks "
            "after his resignation, after pressure from Washington; "
            "shares jump as the White House takes credit.")
    y = centered(d, y, deck, font(SANS, 22), max_w=920)
    y += 8

    # --- lead art: night circuit band ---
    art_top, art_h = y, 100
    d.rectangle([MARGIN, art_top, W - MARGIN, art_top + art_h], fill=NAVY)
    for cx in range(MARGIN + 30, W - MARGIN - 20, 64):
        d.line([(cx, art_top + 18), (cx, art_top + art_h - 18)],
               fill=(38, 68, 110), width=2)
        d.ellipse([cx - 5, art_top + 26, cx + 5, art_top + 36], fill=STEEL)
        d.ellipse([cx - 5, art_top + art_h - 36, cx + 5,
                   art_top + art_h - 26], fill=STEEL)
    chip = (W // 2 - 52, art_top + 30, W // 2 + 52, art_top + art_h - 30)
    d.rectangle(chip, outline=(200, 210, 225), width=3)
    d.rectangle([chip[0] + 10, chip[1] + 10, chip[2] - 10, chip[3] - 10],
                outline=(120, 150, 190), width=1)
    d.text((W / 2, art_top + art_h / 2), "NV", font=font(SANS_B, 44),
           fill=(235, 240, 248), anchor="mm")
    d.text((W - MARGIN - 8, art_top + art_h - 10),
           "CHIP GIANT'S WHIPLASH WEEK", font=font(SANS, 15),
           fill=(160, 180, 205), anchor="rb")
    y = art_top + art_h + 14

    # --- story cells: 2 columns x 3 rows ---
    stories = [
        ("SPACE", "NATO vows to defend orbit as Russian nuclear-satellite reports mount",
         "Allies warn of a weapon in space after reports Moscow could launch one within weeks."),
        ("UKRAINE", "Zaporizhzhia strike kills 2, wounds 40; Russian toll passes 700,000",
         "An overnight attack hits an apartment block as a new analysis counts the war dead."),
        ("JUSTICE", "Fourteen nations back ICJ's Myanmar genocide verdict",
         "Britain, Spain, Canada and Australia among states affirming the court's ruling."),
        ("GAZA", "Strikes kill Hamas security chief; UN says war erased 77 years of progress",
         "Airstrikes kill seven in Gaza as a UN report warns development has been undone."),
        ("CLIMATE", "COP31 ends without a deal as fossil-fuel split sinks talks",
         "The summit closes in failure amid deep divisions over finance and fuels."),
        ("TECH", "States sue Musk firms over Grok's sexualised images",
         "Oregon and Virginia lead action over AI-generated abuse imagery from the chatbot."),
    ]
    col_w = (W - 2 * MARGIN - 28) // 2
    row_h = 136
    for idx, (kicker, head, deck) in enumerate(stories):
        col = idx % 2
        row = idx // 2
        x = MARGIN + col * (col_w + 28)
        top = y + row * row_h
        d.text((x, top), kicker, font=font(SANS_B, 19), fill=ACCENT)
        ty = top + 26
        for line in wrap(d, head, font(SERIF_B, 25), col_w)[:2]:
            d.text((x, ty), line, font=font(SERIF_B, 25), fill=INK)
            ty += 30
        for line in wrap(d, deck, font(SANS, 19), col_w)[:2]:
            d.text((x, ty), line, font=font(SANS, 19), fill=(60, 60, 60))
            ty += 23
        if col == 0:
            d.line([(x + col_w + 14, top), (x + col_w + 14, top + row_h - 16)],
                   fill=(200, 196, 188), width=1)
    y = y + 3 * row_h + 6

    # --- numbers strip ---
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
    y += 10
    strip = ("700,000+  Russian soldiers killed, per new analysis    ·    "
             "$41bn  Sanofi buys Insmed    ·    5.6  Nepal quake    ·    "
             "6,500  Rohingya to be returned by Malaysia")
    for line in wrap(d, strip, font(SANS_B, 18), W - 2 * MARGIN):
        d.text((W / 2, y), line, font=font(SANS_B, 18), fill=INK, anchor="ma")
        y += 23
    y += 4
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=1)
    y += 8
    d.text((W / 2, y), "Headlines checked against reporting from 24 November 2026.",
           font=font(SANS, 16), fill=(90, 90, 90), anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
