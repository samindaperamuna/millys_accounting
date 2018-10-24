from sqlalchemy import Column, Integer, String

from data.DBManager import Base


class TransactionType(Base):
    __tablename__ = "transaction_type"

    id = Column(Integer, primary_key=True)
    type = Column(String(45), nullable=False)
