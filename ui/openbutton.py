# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openbutton.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 413)
        self.seachbutton = QtWidgets.QPushButton(Form)
        self.seachbutton.setGeometry(QtCore.QRect(260, 40, 75, 23))
        self.seachbutton.setObjectName("seachbutton")
        self.Displaydatabase = QtWidgets.QWidget(Form)
        self.Displaydatabase.setGeometry(QtCore.QRect(20, 70, 521, 211))
        self.Displaydatabase.setObjectName("Displaydatabase")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.Displaydatabase)
        self.verticalScrollBar.setGeometry(QtCore.QRect(500, 9, 20, 191))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.Displaydatabase)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 190, 501, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 40, 141, 16))
        self.label.setObjectName("label")
        self.openButton_2 = QtWidgets.QPushButton(Form)
        self.openButton_2.setGeometry(QtCore.QRect(200, 360, 75, 23))
        self.openButton_2.setObjectName("openButton_2")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(290, 360, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.seachbutton.setText(_translate("Form", "Search "))
        self.label.setText(_translate("Form", "OPEN DATABASE"))
        self.openButton_2.setText(_translate("Form", "Open"))
        self.cancelButton.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

