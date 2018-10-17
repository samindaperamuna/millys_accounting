import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.Accounting import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow(flags=Qt.Window)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
