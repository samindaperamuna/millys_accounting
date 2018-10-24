from sqlalchemy import Column, String, Integer

from data.DBManager import Base


class AccountType(Base):
    __tablename__ = "account_type"

    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
