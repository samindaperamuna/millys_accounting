import logging

from data.DBManager import DBManager
from data.model.Company import Company


class CompanyDao:
    """This class contains the company data manipulation methods."""

    @staticmethod
    def create_company(self, name, address, tax_number):
        """Create a company record."""
        db = DBManager()
        if db.Session is not None:
            session = db.Session()
            company = Company(name=name, address=address, taxNumber=tax_number)
            session.add(company)
            session.commit()
        else:
            logging.error("Invalid connection information. Make sure the database is created.")
