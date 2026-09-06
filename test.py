from pathlib import Path
from src.download_utils import download_zip
from paddleocr import PaddleOCRVL


download_zip()
output_dir = Path("./output")
output_dir.mkdir(parents=True, exist_ok=True)

pipeline = PaddleOCRVL()

output = pipeline.predict("./imgs/a/formulas/00000.png")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_json(save_path=output_dir) ## 保存当前图像的结构化json结果
    res.save_to_markdown(save_path=output_dir) ## 保存当前图像的markdown格式的结果
    res.save_to_word(save_path=output_dir) ## 保存当前图像的Word格式的结果