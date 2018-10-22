from sqlalchemy.orm import sessionmaker

from data import DBManager
from data.model.Company import Company


class CompanyDao:
    """This class contains the company data manipulation methods."""

    @staticmethod
    def create_company(self, name, address, tax_number):
        """Create a company record."""
        session = sessionmaker(DBManager.engine)
        company = Company(name, address, tax_number)
        session.add(company)
        session.commit()
