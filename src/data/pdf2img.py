import os
import pymupdf
from pathlib import Path
from .const import imgs_dir, pdf_dir

os.makedirs(imgs_dir, exist_ok=True)

def pdf_to_images(pdfname, dpi=200):

    output_folder = Path(imgs_dir) / Path(pdfname).stem / 'pages'
    os.makedirs(output_folder, exist_ok=True)
    pdf_path = Path(pdf_dir) / pdfname
    doc = pymupdf.open(pdf_path)
    zoom = dpi / 72
    matrix = pymupdf.Matrix(zoom, zoom)

    total_pages = len(doc)

    for page_num in range(total_pages):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=matrix)
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(output_path)
        print(f"已保存: {output_path}")
    
    doc.close()
    print(f"处理完成，共 {total_pages} 页")

if __name__ == '__main__':

    pdf_to_images('a.pdf')