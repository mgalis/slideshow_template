from pillow_heif import register_heif_opener
from PIL import Image
import os

register_heif_opener()

for file in os.listdir("photos"):
    if file.lower().endswith(".heic"):

        src = os.path.join("photos", file)

        jpg_name = os.path.splitext(file)[0] + ".jpg"
        dst = os.path.join("photos", jpg_name)

        img = Image.open(src)
        img.save(dst, "JPEG", quality=95)

        print(f"Converted {file} -> {jpg_name}")