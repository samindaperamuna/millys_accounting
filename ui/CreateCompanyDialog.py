import logging

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox

from data.DBManager import DBManager
from data.dao.CompanyDao import CompanyDao
from data.model.Company import Company
from generated.Ui_CreateCompanyDialog import Ui_CreateCompanyDialog


class CreateCompanyDialog(QDialog, Ui_CreateCompanyDialog):

    def __init__(self, parent):
        super(CreateCompanyDialog, self).__init__(parent=parent)

        # Setup the user interface.
        self.setupUi(self)
        self.setFixedSize(self.size())

    def create_button_clicked(self):
        logging.info("DB creation initialized.")

        if self.validate():
            company = Company(name=self.nameText.text(),
                              address=self.addressText.toPlainText(),
                              taxNumber=self.taxNumText.text())
            db_thread = self.InitDbThread(self.userText.text(), self.passText.text(), company)
            db_thread.sig_success.connect(self.on_success)
            db_thread.sig_failure.connect(self.on_failure)
            db_thread.start()

    def show_info_dialog(self, title, msg):
        QMessageBox.information(self, title, msg, QMessageBox.Ok, QMessageBox.Ok)

    def show_error_dialog(self, title, msg):
        QMessageBox.critical(self, title, msg, QMessageBox.Ok, QMessageBox.Ok)

    def cancel_button_clicked(self):
        self.close()

    def validate(self):
        if self.nameText.text() is "":
            self.show_error_dialog("Missing Company Name", "Please enter the company name.")
            self.nameText.setFocus()
            return False
        elif self.addressText.toPlainText() is "":
            self.show_error_dialog("Missing Address", "Please enter the company address.")
            self.addressText.setFocus()
            return False
        elif self.taxNumText.text() is "":
            self.show_error_dialog("Missing Tax Number", "Please enter the tax number.")
            self.taxNumText.setFocus()
            return False
        elif self.userText.text() is "":
            self.show_error_dialog("Missing Username", "Please enter the database username.")
            self.userText.setFocus()
            return False
        elif self.passText.text() is "":
            self.show_error_dialog("Missing Password", "Please enter a database password.")
            self.passText.setFocus()
            return False
        elif self.retypePassText.text() is "":
            self.show_error_dialog("Missing Password Confirmation", "Please retype the database password.")
            self.retypePassText.setFocus()
            return False
        elif self.passText.text() != self.retypePassText.text():
            self.show_error_dialog("Password Mismatch", "Please confirm the correct password")
            self.retypePassText.selectAll()
            self.retypePassText.setFocus()
            return False

        return True

    @pyqtSlot(str, str, name="sig_success")
    def on_success(self, title, msg):
        self.show_info_dialog(title, msg)
        self.close()

    @pyqtSlot(str, str, name="sig_failure")
    def on_failure(self, title, msg):
        self.show_error_dialog(title, msg)

    class InitDbThread(QThread):
        """Handles the creation of the database, user and initial entries"""

        sig_success = pyqtSignal(str, str, name="sig_success")
        sig_failure = pyqtSignal(str, str, name="sig_failure")

        def __init__(self, username, password, company):
            QThread.__init__(self)
            self._username = username
            self._password = password
            self._company = company

        def __del__(self):
            self.wait()

        def run(self):
            """Create and initialize the database and add company information."""
            db_man = DBManager()
            db_created, result = db_man.create_database(self._company.name, self._username, self._password)

            if not db_created:
                self.sig_failure.emit("Database Creation Failure!", result)
            else:
                # Save the company info.
                company_created = CompanyDao.create_company(self._company)
                if company_created:
                    self.sig_success.emit("Database Created!", result)
                else:
                    self.sig_failure.emit("Save Company Error!", "Failed to save company details.")
