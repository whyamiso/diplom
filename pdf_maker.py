import os

from fpdf import FPDF


def create_pdf_from_images(images: list, output_file: str = None):
    if output_file is None:
        output_file = os.getcwd() + os.sep + "yourfile.pdf"
    pdf = FPDF()
    for image in images:
        pdf.add_page()
        pdf.image(image)
    pdf.output(output_file, "F")
