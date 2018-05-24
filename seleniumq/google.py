import os
import time

from .seleniumq import *

# Задаем путь к драйверу Google Chrome
path = os.getcwd().replace("seleniumq", "drivers") + os.sep + "windows_x32" + os.sep + "chromedriver.exe"

# инициализируем драйвер Google Chrome
driver = webdriver.Chrome(executable_path=path)
# задаем url страницы книги
url = "https://books.google.ru/books?id=dD38AgAAQBAJ&printsec=frontcover&dq=%D0%BC%D0%B0%D1%82+%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7+%D0%B4%D0%B5%D0%BC%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87&hl=ru&sa=X&ved=0ahUKEwjx__XOtIDbAhUCKywKHWiOADIQ6AEIMzAC#v=onepage&q&f=false"
# переводим браузер в полноэкранный режим
# driver.fullscreen_window()
first_window = driver.get(url)
imgs = driver.find_elements_by_tag_name("img")

link = find_image(imgs)

download_image(driver=driver, link=link, file_name="image1.png")

time.sleep(1)
driver.close()
