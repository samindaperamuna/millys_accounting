import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow(flags=Qt.Window)
    ui = MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
