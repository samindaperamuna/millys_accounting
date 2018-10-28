# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qml/UI_COFDialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_COFDialog(object):
    def setupUi(self, COFDialog):
        COFDialog.setObjectName("COFDialog")
        COFDialog.resize(640, 480)
        self.groupBox = QtWidgets.QGroupBox(COFDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 620, 460))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 35, 600, 375))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 410, 210, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(COFDialog)
        self.addButton.clicked.connect(COFDialog.add_button_click)
        self.deleteButton.clicked.connect(COFDialog.delete_button_click)
        QtCore.QMetaObject.connectSlotsByName(COFDialog)

    def retranslateUi(self, COFDialog):
        _translate = QtCore.QCoreApplication.translate
        COFDialog.setWindowTitle(_translate("COFDialog", "Chart of Accounts"))
        self.groupBox.setTitle(_translate("COFDialog", "Currently activated account types"))
        self.addButton.setText(_translate("COFDialog", "Add"))
        self.deleteButton.setText(_translate("COFDialog", "Delete"))
