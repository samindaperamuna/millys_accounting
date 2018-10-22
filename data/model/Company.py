from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Company(base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    address = Column(String(100), nullable=False)
    taxNumber = Column(String(45), nullable=False)
