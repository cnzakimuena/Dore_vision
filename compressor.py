
import os
from pypdf import PdfWriter


if __name__ == '__main__':
    input_path = r".\document\Dore_vision.pdf"
    writer = PdfWriter(clone_from=input_path)

    for page in writer.pages:
        for img in page.images:
            # quality as % whereas 100 is best quality
            img.replace(img.image, quality=1)

    ouput_path = r".\Dore_vision.pdf"
    with open(ouput_path, "wb") as f:
        writer.write(f)

os.remove(input_path)
