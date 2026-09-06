from pix2text import Pix2Text
from PIL import Image
from pathlib import Path

img_path = "./imgs/26李林880题-试题册（数一）/pages/page_44.png"
p2t = Pix2Text.from_config()

# MFD：检测图片中的公式
results = p2t.recognize_page(img=img_path)

print(results)