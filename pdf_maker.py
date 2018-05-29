# импорт стандартного python-модуля для взаимодействия с ОС
import os
# импорт стандартного python-модуль для работы с pdf
from math import trunc

from PIL import Image
from pathlib import Path
from fpdf import FPDF


def create_pdf_from_images(images: list, size_in_pt: tuple, output_dir: str = None, output_file: str = None):
    """
    Функция принимает на вход 2 аргумента:
    images - список абсолютных путей к png-изображениям
    output_file - название выходного pdf-файла,
    необязатедьный аргумент
    """
    # если output_file неуказан, то по умолчанию его значение равно None
    # в этом случае задаем директорию файла текущую дирекорию,
    # а имя "output.pdf"
    if output_dir is None:
        output_dir = os.getcwd()

    if output_file is None:
        output_file = "output.pdf"

    # инициализируем объект класса FPDF
    pdf = FPDF('P', 'pt', size_in_pt)
    # для каждого изображения из списка
    # сначала создаем в pdf-документе пустую страницу,
    # затем на страницу добавляем изображение
    for image in images:
        pdf.add_page()
        pdf.image(image)
    # записываем pdf-документ в необходимую директорию
    pdf.output(output_dir + os.sep + output_file, "F")


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    img_path = Path(image_path)
    image_obj = Image.open(img_path)
    cropped_image = image_obj.crop(coords)

    # saved_location = Path(saved_location)
    cropped_image.save(saved_location)
    # cropped_image.show()


def define_page_area(image_path):
    img_path = Path(image_path)
    image_obj = Image.open(img_path)

    width, height = image_obj.size

    pix = image_obj.load()

    cnt = 0

    while True:
        t = pix[cnt, 0][0]
        cnt += 1
        if t > 50:
            break
    x1 = cnt

    cnt = width - 1

    while True:
        t = pix[cnt, 0][0]
        cnt -= 1
        if t > 100:
            break
    x2 = cnt

    return x1, 0, x2, height


def px_to_pt(page_size_in_px):
    width_in_px, height_in_px = page_size_in_px
    width_in_pt = trunc(width_in_px * 4 / 3)
    height_in_pt = trunc(height_in_px * 4 / 3)
    return width_in_pt, height_in_pt


def define_page_size(path_to_image):
    img_path = Path(path_to_image)
    img = Image.open(img_path)

    return img.size
