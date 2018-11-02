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
                self.show_error_dialog("Invalid username password combination.")
            else:
                if DBManager().connect_database(db_name, user, pwd):
                    self.show_info_dialog("Connected to the database.")
                    self.close()
                else:
                    self.show_error_dialog("Couldn't connect to the database.")

    def cancel_button_click(self):
        self.close()

    def validate(self):
        if len(self.dbList.selectedItems()) < 1:
            self.show_info_dialog("Please select a database to proceed")
            self.dbList.setFocus()
            return False
        elif self.usernameText.text() is "":
            self.show_info_dialog("Please enter a username")
            self.usernameText.setFocus()
            return False
        elif self.passwordText.text() is "":
            self.show_info_dialog("Please enter a password")
            self.passwordText.setFocus()
            return False

        return True

    @staticmethod
    def show_info_dialog(msg):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setMaximumWidth(500)
        msg_box.setWindowTitle("Information")
        msg_box.setText(msg)

        msg_box.exec()

    @staticmethod
    def show_error_dialog(msg):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setMaximumWidth(500)
        msg_box.setWindowTitle("Error")
        msg_box.setText(msg)

        msg_box.exec()
