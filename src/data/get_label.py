import json
from pathlib import Path
from PIL import Image
from pix2text import TextFormulaOCR
from .const import imgs_dir
from ..download_utils import download_zip


def recognize_formulas(pdfname, batch_size=64):
    formulas_dir = Path(imgs_dir) / Path(pdfname).stem / "formulas"

    img_paths = sorted(formulas_dir.glob("*.png"))

    if not img_paths:
        print("没有找到公式图片")
        return

    ocr = TextFormulaOCR.from_config(device="cuda")

    images = [
        Image.open(path).convert("RGB")
        for path in img_paths
    ]

    print(f"共 {len(images)} 个公式，开始识别...")

    results = ocr.recognize_formula(
        images,
        batch_size=batch_size,
        return_text=True,
    )

    data = {
        path.name: latex
        for path, latex in zip(img_paths, results)
    }

    output_path = formulas_dir / "formulas.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"识别完成: {output_path}")

    return data


if __name__ == "__main__":
    download_zip()
    recognize_formulas(
        "a.pdf",
        batch_size=128,
    )