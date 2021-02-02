from UI import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from request import generate_map


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        if generate_map(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()):
            self.pixmap = QPixmap('map.png')
            self.label.setPixmap(self.pixmap)
        else:
            self.statusbar.showMessage('Request error', 5000)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
