import logging

from sqlalchemy.exc import ProgrammingError

from data.DBManager import DBManager
from data.model.Company import Company


class CompanyDao:
    """This class contains the company data manipulation methods."""

    @staticmethod
    def create_company(self, name, address, tax_number):
        """Create a company record."""
        db = DBManager()
        if db.Session is not None:
            try:
                session = db.Session()
                company = Company(name=name, address=address, taxNumber=tax_number)
                session.add(company)
                session.commit()
                return True
            except ProgrammingError as e:
                logging.error("Unable to create the company information: {0}".format(str(e)))
                return False
        else:
            logging.error("Invalid connection information. Make sure the database is created.")
            return False
