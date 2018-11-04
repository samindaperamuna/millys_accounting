from PyQt5.QtWidgets import QDialog, QMessageBox

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
        if self.validate():
            db_name = self.dbList.currentItem().text()
            user = self.usernameText.text()
            pwd = self.passwordText.text()

            if not DBManager.check_user_permissions(db_name, user, pwd):
                QMessageBox.critical(self, "Invalid Credentials", "Invalid username password combination.",
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                is_success, result = DBManager().connect_database(db_name, user, pwd)
                if is_success:
                    QMessageBox.information(self, "Connection Success", result, QMessageBox.Ok, QMessageBox.Ok)
                    self.close()
                else:
                    QMessageBox.critical(self, "Connection Failed", result, QMessageBox.Ok, QMessageBox.Ok)

    def cancel_button_click(self):
        self.close()

    def validate(self):
        if len(self.dbList.selectedItems()) < 1:
            QMessageBox.critical(self, "Invalid Database", "Please select a database to proceed", QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.dbList.setFocus()
            return False
        elif self.usernameText.text() is "":
            QMessageBox.critical(self, "Invalid Username", "Please enter a username", QMessageBox.Ok, QMessageBox.Ok)
            self.usernameText.setFocus()
            return False
        elif self.passwordText.text() is "":
            QMessageBox.critical(self, "Invalid Password", "Please enter a password", QMessageBox.Ok, QMessageBox.Ok)
            self.passwordText.setFocus()
            return False

        return True
