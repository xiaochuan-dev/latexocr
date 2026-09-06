import zipfile
import os
from huggingface_hub import hf_hub_download

def download_zip():
    if not os.path.exists('./imgs.zip'):
        zip_path = hf_hub_download(
            repo_id="xiaochuan-dev/latex",
            filename="imgs.zip",
            repo_type="dataset"
        )

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
            
        print("解压完成！图片在 . 目录下")