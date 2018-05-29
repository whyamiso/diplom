import os
import time

from PyQt5.QtWidgets import QMainWindow, QApplication
from selenium import webdriver

from GUI.gui import GUI
from seleniumq import next_page, find_image, download_image, find_buttons
from pdf_maker import create_pdf_from_images, crop, define_page_area, px_to_pt, define_page_size
from config import img_output_dir, pdf_output_dir, pdf_name


def criteria():
    if current_link is not None:
        prev_link = current_link


def download_book(url):
    driver = \
        webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(url)
    links = []

    buttons = find_buttons(driver=driver)

    current_link = None
    prev_link = None

    # while True:
    #     prev_link = current_link
    #     images = driver.find_elements_by_tag_name("img")
    #     link = find_image(images)
    #     # link = img.get_attribute("src")
    #     current_link = link
    #     links.append(link)
    #     time.sleep(5)
    #     next_page(buttons)
    #     buttons = find_buttons(driver=driver)
    #
    #     if prev_link == current_link:
    #         list(set(links))
    #         break

    for i in range(5):
        images = driver.find_elements_by_tag_name("img")
        link = find_image(images)
        links.append(link)
        next_page(buttons)
        time.sleep(2)
        buttons = find_buttons(driver=driver)

    for i, link in enumerate(links):
        time.sleep(1)
        download_image(driver, link, "image{}.png".format(i), output_dir=img_output_dir)

    driver.close()

    print("ska")
    images_names = os.listdir(img_output_dir)
    images = [img_output_dir + os.sep + image for image in images_names]
    print(images)

    page_area = define_page_area(images[0])

    print(page_area)

    try:
        for image in images:
            crop(image, page_area, image)

        page_size = define_page_size(images[0])

        page_area_in_pt = px_to_pt(page_size)

        page_area_in_pt = page_area_in_pt[0] - 100, page_area_in_pt[1] - 100

        print(page_area_in_pt)

        create_pdf_from_images(images, page_area_in_pt, output_dir=pdf_output_dir, output_file=pdf_name)
    except Exception as e:
        print(e)

    print("finish")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = GUI(main_window)
    ui.add_logic()
    ui.set_downloader(download_book)
    sys.exit(app.exec_())
