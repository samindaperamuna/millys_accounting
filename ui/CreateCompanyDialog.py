from PyQt5.QtWidgets import QDialog

from generated.Ui_CreateCompanyDialog import Ui_CreateCompanyDialog


class CreateCompanyDialog(QDialog, Ui_CreateCompanyDialog):

    def __init__(self, parent):
        super(CreateCompanyDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())
