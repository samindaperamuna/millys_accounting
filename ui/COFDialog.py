from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog

from generated.UI_COFDialog import Ui_COFDialog


class COFDialog(QDialog, Ui_COFDialog):
    tableHeaders = ["Account Type", "Description", "Account Range", "Active"]

    tableData = {("Bank", "Cash", "1000-000", True),
                 ("Fixed Asset", "Balance Sheet", "2000-000", True),
                 ("Accounts Receivable", "Balance Sheet", "3000-000", True),
                 ("Accounts Receivable", "Balance Sheet", "3000-000", True),
                 ("Bank", "Cash", "1000-000", True)}

    def __init__(self, parent):
        super(COFDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())

        # Generate the data model.
        data_model = QStandardItemModel()
        data_model.setHorizontalHeaderItem()
        self.tableView.setModel(data_model)

    @staticmethod
    def add_button_click(self):
        print("Add button clicked.")

    @staticmethod
    def delete_button_click(self):
        print("Cancel button clicked.")
