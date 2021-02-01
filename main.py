from UI import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print('!!!')
        self.pixmap = QPixmap('map.png')
        self.image = QLabel(self)
        self.image.move(30, 100)
        self.image.resize(400, 300)
        self.image.setPixmap(self.pixmap)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
