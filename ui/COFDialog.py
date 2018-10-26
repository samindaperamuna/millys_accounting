from PyQt5.QtWidgets import QDialog

from generated.UI_COFDialog import Ui_COFDialog


class COFDialog(QDialog, Ui_COFDialog):

    def __init__(self, parent):
        super(COFDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())

    @staticmethod
    def add_button_click(self):
        print("Add button clicked.")

    @staticmethod
    def delete_button_click(self):
        print("Cancel button clicked.")
