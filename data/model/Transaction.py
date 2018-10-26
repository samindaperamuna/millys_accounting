from sqlalchemy import Column, Integer, Date, func, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from data.DBManager import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.now(), nullable=False)
    description = Column(String(100))
    accountNumber = Column(String, ForeignKey("account.number"))
    account = relationship("Account")
    refId = Column(Integer, ForeignKey("transaction_ref.id"))
    transactionRef = relationship("TransactionRef")
    typeId = Column(Integer, ForeignKey("transaction_type.id"))
    transactionType = relationship("TransactionType")
    amount = Column(Float, default=0, nullable=False)
