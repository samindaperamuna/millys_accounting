import logging

from PyQt5.QtWidgets import QDialog, QMessageBox

from data.DBManager import DBManager
from generated.Ui_CreateCompanyDialog import Ui_CreateCompanyDialog


class CreateCompanyDialog(QDialog, Ui_CreateCompanyDialog):

    def __init__(self, parent):
        super(CreateCompanyDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())

    def create_button_clicked(self):
        logging.debug("DB creation initialized.")
        self.init_database()
        logging.debug("DB creation completed.")

    def init_database(self):
        if self.validate() is True:
            # Create the database.
            db_man = DBManager()
            db_man.create_database(self.nameText.text(), self.userText.text(), self.passText.text())
        else:
            print("Invalid")

    def validate(self):
        if self.nameText.text() is "":
            self.show_missing_field_dialog("Please enter the company name.")
            self.nameText.setFocus()
            return False
        elif self.addressText.toPlainText() is "":
            self.show_missing_field_dialog("Please enter the company address.")
            self.addressText.setFocus()
            return False
        elif self.taxNumText.text() is "":
            self.show_missing_field_dialog("Please enter the tax number.")
            self.taxNumText.setFocus()
            return False
        elif self.userText.text() is "":
            self.show_missing_field_dialog("Please enter the database username.")
            self.userText.setFocus()
            return False
        elif self.passText.text() is "":
            self.show_missing_field_dialog("Please enter a database password.")
            self.passText.setFocus()
            return False
        elif self.retypePassText.text() is "":
            self.show_missing_field_dialog("Please retype the database password.")
            self.retypePassText.setFocus()
            return False
        elif self.passText.text() != self.retypePassText.text():
            self.show_missing_field_dialog("Passwords do not match.")
            self.retypePassText.selectAll()
            self.retypePassText.setFocus()
            return False

        return True

    @staticmethod
    def show_missing_field_dialog(msg):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setMaximumWidth(500)
        msg_box.setWindowTitle("Missing Required Field")
        msg_box.setText(msg)

        msg_box.exec()

    def cancel_button_clicked(self):
        self.close()
