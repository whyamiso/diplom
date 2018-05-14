import os

from selenium import webdriver


def download_image(driver: webdriver, link: str, file_name, output_dir=None):
    if output_dir is None:
        output_dir = os.getcwd()
    driver.get(link)
    driver.get_screenshot_as_file(output_dir + os.sep + file_name)


def close_tab(tab_name: str):
    pass


def add_new_tab(tab_name: str):
    pass


def change_tab_to(tab_name: str):
    pass


def find_image(images: list):
    """
    Функция принимает список объектов,
    полученной методом find_elements_by_tag_name("img"),
    объекта класса webdriver.
    Функция возвращает ссылку на изображение.
    """
    link = ""
    area = 0
    for image in images:
        width, height = image.size["width"], image.size["height"]

        if width * height > area:
            area = width * height
            link = image.get_attribute("src")

    return link
