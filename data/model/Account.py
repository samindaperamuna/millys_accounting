from sqlalchemy import Integer, Column, String, Float, ForeignKey, Date, func, Boolean
from sqlalchemy.orm import relationship

from data.DBManager import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    balance = Column(Float, default=0, nullable=False)
    typeId = Column(Integer, ForeignKey("account_type.id"))
    accountType = relationship("AccountType")
    createdBy = Column(String(45), default=None)
    createdDate = Column(Date, default=func.now(), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
