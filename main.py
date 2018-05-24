import os
import time

from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from seleniumq import seleniumq
from pdf_maker import create_pdf_from_images
from GUI.gui import GUI

# url = "http://python.org"
url = "https://books.google.ru/books?id=dD38AgAAQBAJ&printsec=frontcover&dq=%D0%B4%D0%B5%D0%BC%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87&hl=ru&sa=X&ved=0ahUKEwiln5vlspHbAhXlKJoKHbSLA8EQ6AEILjAB#v=onepage&q=%D0%B4%D0%B5%D0%BC%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87&f=false"
# driver = webdriver.Chrome(executable_path=os.getcwd()+os.path+"drivers"+os.path+"windows_x32"+os.sep+"chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\\Users\\stu\\.dfy\\diplom\\drivers\\windows_x32\\chromedriver.exe")
driver.maximize_window()
driver.get(url)

imgs = driver.find_elements_by_tag_name("img")

buttons = driver.find_elements_by_xpath("//div[@role='button']//img")

current_link = url


def next_page():
    for button in buttons:
        if "right" in button.get_attribute("src"):
            button.click()
            break


def area(d):
    return d.size['width'] * d.size['height']


def find_img():
    imgs = driver.find_elements_by_tag_name("img")
    return max(imgs, key=area)


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    # cropped_image.show()


def download_image(driver, link, file_name, output_dir=os.getcwd() + os.sep):
    driver.get(link)
    driver.get_screenshot_as_file(output_dir + file_name)


links = []


def criteria():
    pass


while criteria() is False:
    print(i)

    img=find_img()
    time.sleep(1)
    link = img.get_attribute("src")
    links.append(link)
    next_page()

for i, link in enumerate(links):
    filename = "file" + str(i) + ".png"
    download_image(driver=driver, link=link, file_name=filename)
    crop(filename,(600,0,1200,800),os.getcwd())

# link = seleniumq.find_image(imgs)
#
# script = "window.open({})".format(link)
#
# driver.execute_script(script)
# seleniumq.download_image(driver=driver, link=url, file_name="file{}.png".format(i))
#
# driver.save_screenshot("file{}.png".format(i))

create_pdf_from_images(["file{}.png".format(i) for i in range(amount_pages)])

driver.close()

if __name__ == '__main__':
    gui=GUI()
    gui.show()