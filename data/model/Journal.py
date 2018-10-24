from sqlalchemy import Integer, Column, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from data.DBManager import Base


class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    description = Column(String(100))
    transactionId = Column(Integer, ForeignKey("transaction.id"))
    transaction = relationship("Transaction")
    user = Column(String(45), nullable=False)
