# импорт пакета os
import os
# импорт webdriver-а, через данный объект происходит основное функционирование selenium
from selenium import webdriver


def download_image(driver: webdriver, link: str, file_name, output_dir=None):
    """
    Функция осуществляет скачивание изображения по его ссылке
    обязательные аргументы - объект-драйвер, ссылка на изображение,
    и имя файла
    необязательный аргумент - директория, по умолчанию задана текущая
    """
    if output_dir is None:
        output_dir = os.getcwd()
    # переход драйвера по ссылке
    driver.get(link)
    # скачивание картинки как файла
    driver.get_screenshot_as_file(output_dir + os.sep + file_name)

# работа selenium имитирует работу пользователя в веб-браузере,
# но логика его работы отличается
# потому необходимо реализовать следующие функции
def close_tab(tab_name: str):
    """закрытие вкладки по ее названию"""
    pass


def add_new_tab():
    """Создание новой вкладки,
    функция возвращает имя данной вкладки"""
    pass


def change_tab_to(tab_name: str):
    """Переключение вкладки по имени"""
    pass

def find_image(images: list):
    """
    Функция принимает список объектов,
    полученной методом find_elements_by_tag_name("img"),
    объекта класса webdriver.
    Функция возвращает ссылку на изображение.
    """
    # Страница книги должна быть самой большой картинкой на странице
    # потому происходит обход всех картинок и осуществляется поиск
    # картинки с максимальной пощадью
    link = ""
    area = 0
    for image in images:
        width, height = image.size["width"], image.size["height"]

        if width * height >= area:
            area = width * height
            link = image.get_attribute("src")

    return link


def find_buttons(driver:webdriver):
    buttons = driver.find_elements_by_xpath("//div[@role='button']//img")
    return buttons


def next_page(buttons):
    for button in buttons:
        if "right" in button.get_attribute("src"):
            button.click()
            break
