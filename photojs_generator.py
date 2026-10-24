import os
import json

PHOTO_FOLDER = "photos"
OUTPUT_FILE = "photos.js"

IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp"
)

photos = [
    f for f in os.listdir(PHOTO_FOLDER)
    if f.lower().endswith(IMAGE_EXTENSIONS)
]

photos.sort()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(
        "const photos = "
        + json.dumps(photos, indent=4)
        + ";\n"
    )

print(f"Generated {OUTPUT_FILE} with {len(photos)} images")