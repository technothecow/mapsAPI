from UI import Ui_MainWindow
from PyQt5.QtGui import *
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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 16777238 and float(self.lineEdit_3.text()) < 90:
            self.lineEdit_3.setText(str(float(self.lineEdit_3.text()) * 2))
            self.button_clicked()
        elif event.key() == 16777239 and float(self.lineEdit_3.text()) > 0.01:
            self.lineEdit_3.setText(str(float(self.lineEdit_3.text()) / 2))
            self.button_clicked()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
