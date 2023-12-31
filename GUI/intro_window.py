from introWindow import Ui_IntroWindow
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import Qt

from game2_window import GameWindow


class IntroWindow(QMainWindow, Ui_IntroWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.show()

        self.showMaximized()

        self.start_btn.clicked.connect(self.strat_game)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # start_game function when Enter key is pressed
            self.start_game()

    def strat_game(self):
        self.call_game_window()


    def call_game_window(self):
        self.game_window = GameWindow()
        self.game_window.show()
        self.hide()


        
if __name__ == "__main__":
    app = QApplication([])
    intro_window = IntroWindow()
    intro_window.showMaximized()
    app.exec_()


# pyside6-uic introWindow.ui -o introWindow.py
