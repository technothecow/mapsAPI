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
        key = event.key()
        if key in {16777238, 16777239, 65, 68, 87, 83}:
            if key == 16777238 and float(self.lineEdit_3.text()) < 90:
                self.lineEdit_3.setText(str(float(self.lineEdit_3.text()) * 2))
            elif key == 16777239 and float(self.lineEdit_3.text()) > 0.01:
                self.lineEdit_3.setText(str(float(self.lineEdit_3.text()) / 2))
            elif key == 83 and abs(float(self.lineEdit_2.text()) - float(self.lineEdit_3.text())) < 85:
                self.lineEdit_2.setText(str(float(self.lineEdit_2.text()) - float(self.lineEdit_3.text())))
            elif key == 87 and abs(float(self.lineEdit_2.text()) + float(self.lineEdit_3.text())) < 85:
                self.lineEdit_2.setText(str(float(self.lineEdit_2.text()) + float(self.lineEdit_3.text())))
            elif key == 65 and abs(float(self.lineEdit.text()) - float(self.lineEdit_3.text())) < 180:
                self.lineEdit.setText(str(float(self.lineEdit.text()) - float(self.lineEdit_3.text())))
            elif key == 68 and abs(float(self.lineEdit.text()) + float(self.lineEdit_3.text())) < 180:
                self.lineEdit.setText(str(float(self.lineEdit.text()) + float(self.lineEdit_3.text())))
            self.button_clicked()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
