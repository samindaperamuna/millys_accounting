import logging

from sqlalchemy.exc import ProgrammingError

from data.DBManager import DBManager
from data.model.AccountType import AccountType


class AccountTypeDao:
    """This class contains the Account data manipulation methods."""

    @staticmethod
    def create_account_type(description):
        """Create an Account record"""
        db = DBManager()
        if db.Session is not None:
            try:
                session = db.Session()
                accountType = AccountType(description=description)
                session.add(accountType)
                session.commit()
                return True
            except ProgrammingError as e:
                logging.error("Unable to create the account information: {0}".format(str(e)))
                return False
        else:
            logging.error("Invalid connection information. Make sure the database is created.")
            return False
