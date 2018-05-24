# импорт классов QApplication и QMainWindow
# из пакета QtWidgets библиотеки PyQt5
# QApplication используется для создания приложения,
# а QMainWindow для создания главного окна приложения
from PyQt5.QtWidgets import QApplication, QMainWindow
# импорт заготовки GUI из модуля pattern_gui пакета GUI
from GUI.pattern_gui import Ui_MainWindow


# описываем класс GUI, наследующий Ui_MainWindow
class GUI(Ui_MainWindow):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window
        self.setupUi(main_window)
        main_window.show()

    # данный метод добавляет логику GUI
    # на данном этапе не реализован
    def add_logic(self):
        pass

# runner приложени - если модуль исполняется, а не
# импортируется другим модулем, то;
# импортируется модуль sys
# инициализируется приложение
# инициализируется главное окно приложения
# с помощью полученного объекта main_window
# инициализируется объект ui, то есть создается
# графический интерфейс пользователя,
# далее к GUI добавляется логика(метод add_logic)
# объявляется системный выход из приложения(при нажатии на крестик)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = GUI(main_window)
    ui.add_logic()
    sys.exit(app.exec_())
