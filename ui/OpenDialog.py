from PyQt5.QtWidgets import QDialog

from data.DBManager import DBManager
from generated.UI_OpenDialog import Ui_OpenDialog


class OpenDialog(QDialog, Ui_OpenDialog):

    def __init__(self, parent):
        super(OpenDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.list_databases()

    def list_databases(self):
        db = DBManager()
        self.dbList.addItems(db.list_databases())

    def open_button_click(self):
        print("Open button clicked.")

    def cancel_button_click(self):
        self.close()
