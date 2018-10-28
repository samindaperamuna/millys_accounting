# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qml/UI_OpenDialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_OpenDialog(object):
    def setupUi(self, OpenDialog):
        OpenDialog.setObjectName("OpenDialog")
        OpenDialog.resize(350, 440)
        OpenDialog.setModal(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(OpenDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 390, 190, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.groupBox = QtWidgets.QGroupBox(OpenDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 330, 300))
        self.groupBox.setObjectName("groupBox")
        self.dbList = QtWidgets.QListWidget(self.groupBox)
        self.dbList.setGeometry(QtCore.QRect(10, 40, 310, 250))
        self.dbList.setObjectName("dbList")
        self.usernameText = QtWidgets.QLineEdit(OpenDialog)
        self.usernameText.setGeometry(QtCore.QRect(140, 320, 200, 30))
        self.usernameText.setPlaceholderText("")
        self.usernameText.setObjectName("usernameText")
        self.usernameLabel = QtWidgets.QLabel(OpenDialog)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 320, 100, 30))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(OpenDialog)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 360, 100, 30))
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordText = QtWidgets.QLineEdit(OpenDialog)
        self.passwordText.setGeometry(QtCore.QRect(140, 360, 200, 30))
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setPlaceholderText("")
        self.passwordText.setObjectName("passwordText")

        self.retranslateUi(OpenDialog)
        self.openButton.clicked.connect(OpenDialog.open_button_click)
        self.cancelButton.clicked.connect(OpenDialog.cancel_button_click)
        QtCore.QMetaObject.connectSlotsByName(OpenDialog)
        OpenDialog.setTabOrder(self.dbList, self.usernameText)
        OpenDialog.setTabOrder(self.usernameText, self.passwordText)
        OpenDialog.setTabOrder(self.passwordText, self.openButton)
        OpenDialog.setTabOrder(self.openButton, self.cancelButton)

    def retranslateUi(self, OpenDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenDialog.setWindowTitle(_translate("OpenDialog", "Open Database"))
        self.openButton.setText(_translate("OpenDialog", "Open"))
        self.cancelButton.setText(_translate("OpenDialog", "Cancel"))
        self.groupBox.setTitle(_translate("OpenDialog", "Select the database"))
        self.usernameLabel.setText(_translate("OpenDialog", "Username"))
        self.passwordLabel.setText(_translate("OpenDialog", "Password"))
