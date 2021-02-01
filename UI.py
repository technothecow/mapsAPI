from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mapsAPI", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c",
                                       None))
