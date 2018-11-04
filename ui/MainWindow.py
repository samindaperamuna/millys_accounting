from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox

from generated.Ui_MainWindow import Ui_MainWindow
from ui import OpenDialog
from ui.COFDialog import COFDialog
from ui.CreateCompanyDialog import CreateCompanyDialog
from ui.OpenDialog import OpenDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from the designer.
        self.setupUi(self)
        self.setFixedSize(self.size())

        # Center window on screen.
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def action_new_triggered(self):
        result = QMessageBox.question(self, "Confirm Entity Creation.", "Are you sure you want to create a new entity?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            ui = CreateCompanyDialog(parent=self)
            ui.show()

    def action_open_triggered(self):
        ui = OpenDialog(parent=self)
        ui.show()

    @staticmethod
    def action_exit_triggered():
        exit(0)

    def action_cof_triggered(self):
        ui = COFDialog(parent=self)
        ui.show()
