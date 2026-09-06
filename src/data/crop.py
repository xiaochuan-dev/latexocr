from pathlib import Path
from PIL import Image
from pix2text import MathFormulaDetector
from .const import imgs_dir

mfd = MathFormulaDetector()

def crop_formulas(img_path: Path):
    image = Image.open(img_path).convert("RGB")

    results = mfd(image)

    print(f"{img_path.name}: 检测到 {len(results)} 个公式")

    for i, item in enumerate(results):
        box = item["box"]
        x1 = int(box[:, 0].min())
        y1 = int(box[:, 1].min())
        x2 = int(box[:, 0].max())
        y2 = int(box[:, 1].max())

        formula_img = image.crop((x1, y1, x2, y2))

        output_path = save_dir / f"{img_path.stem}_{i:03d}.png"
        formula_img.save(output_path)

        print(f"保存: {output_path}")


def crop(pdfname):
    pages_dir = Path(imgs_dir) / Path(pdfname).stem / 'pages'
    save_dir = Path(imgs_dir) / Path(pdfname).stem / 'formulas'
    save_dir.mkdir(parents=True, exist_ok=True)

    for img_path in sorted(pages_dir.glob("*.png")):
        crop_formulas(img_path)

if __name__ == '__main__':
    crop('26李林880题-试题册（数一）.pdf')