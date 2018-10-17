from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget


class Ui_Form(object):

    def __init__(self):
        self.parent = None

    def setupUi(self, parent: QMainWindow, window: QWidget):
        self.parent = parent

        window.setObjectName("Form")
        window.resize(327, 155)

        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_new_clicked)

        self.pushButton_2 = QtWidgets.QPushButton(window)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 110, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(30, 30, 191, 51))
        self.label.setObjectName("label")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window: QWidget):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Yes "))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Create new entity?"))

    def on_new_clicked(self):
        main_window = QtWidgets.QMainWindow(parent=self.parent, flags=Qt.Window)
        new_window = Ui_Form()
        new_window.setupUi(self.parent, main_window)
        main_window.show()
