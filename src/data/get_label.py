import json
from pathlib import Path
from PIL import Image
from pix2text import TextFormulaOCR
from .const import imgs_dir
from ..download_utils import download_zip


if __name__ == "__main__":
    download_zip()