# импорт стандартного python-модуля для взаимодействия с ОС
import os
# импорт стандартного python-модуль для работы с pdf
from fpdf import FPDF


def create_pdf_from_images(images: list, output_file: str = None):
    """
    Функция принимает на вход 2 аргумента:
    images - список абсолютных путей к png-изображениям
    output_file - название выходного pdf-файла,
    необязатедьный аргумент
    """
    # если output_file неуказан, то по умолчанию его значение равно None
    # в этом случае задаем директорию файла текущую дирекорию,
    # а имя "output.pdf"
    if output_file is None:
        output_file = os.getcwd() + os.sep + "output.pdf"
    # инициализируем объект класса FPDF
    pdf = FPDF()
    # для каждого изображения из списка
    # сначала создаем в pdf-документе пустую страницу,
    # затем на страницу добавляем изображение
    for image in images:
        pdf.add_page()
        pdf.image(image)
    # записываем pdf-документ в необходимую директорию
    pdf.output(output_file, "F")
