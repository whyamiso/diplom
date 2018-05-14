import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.pattern_gui import Ui_MainWindow


class GUI(Ui_MainWindow):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window
        self.setupUi(main_window)
        main_window.show()

    def add_logic(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = GUI(main_window)
    ui.add_logic()
    sys.exit(app.exec_())
