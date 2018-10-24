from sqlalchemy import Integer, String, Column

from data.DBManager import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    address = Column(String(100), nullable=False)
    taxNumber = Column(String(45), nullable=False)
