"""Regenerate the site's images from the app repos' store art.

Run from the repo root, with the app repos checked out next to this one:

    python tools/make-images.py

Screenshots are resized to 540 px wide WebP; icons to 192 px PNG and WebP.
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
REPOS = ROOT.parent
OUT = ROOT / "assets" / "img"

APPS = {
    "intervalworkout": {
        "icon": REPOS / "IntervalWorkout/src/IntervalWorkout.Android/Icon.png",
        "feature": REPOS / "IntervalWorkout/PlayStore/feature-graphic.png",
        "screens": REPOS / "IntervalWorkout/PlayStore/Screenshots",
    },
    "flickm": {
        "icon": REPOS / "Flickm/Design/store-art/play-icon-512.png",
        "feature": REPOS / "Flickm/Design/store-art/play-feature-1024x500.png",
        "screens": REPOS / "Flickm/Design/store-art/play-screenshots",
    },
}


def resize(im, width):
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def main():
    for app, src in APPS.items():
        out = OUT / app
        out.mkdir(parents=True, exist_ok=True)

        icon = Image.open(src["icon"]).convert("RGBA")
        resize(icon, 192).save(out / "icon.png", optimize=True)
        resize(icon, 192).save(out / "icon.webp", quality=90)

        # Open Graph preview for link unfurls (JPEG: widest support).
        Image.open(src["feature"]).convert("RGB").save(out / "og.jpg", quality=85)

        for shot in sorted(src["screens"].glob("*.png")):
            im = Image.open(shot).convert("RGB")
            resize(im, 540).save(out / f"{shot.stem}.webp", quality=82, method=6)

    # Touch icon from the placeholder brand mark in GreenHollowApps/brand/logos.
    mark = Image.new("RGB", (180, 180), "#2F6B3F")
    draw = ImageDraw.Draw(mark)
    draw.polygon([(90, 34), (144, 132), (36, 132)], fill="#8DB580")
    draw.rectangle([82, 132, 98, 152], fill="#4A3B2C")
    mark.save(ROOT / "apple-touch-icon.png", optimize=True)


if __name__ == "__main__":
    main()
