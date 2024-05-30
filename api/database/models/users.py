from database.base_class import Base
from sqlalchemy import Column # Column
from sqlalchemy import Integer # Integer
from sqlalchemy import ARRAY # Array
from sqlalchemy import String # Varchar
from sqlalchemy import Numeric # Money
from sqlalchemy import Date # Date
from sqlalchemy import Uuid # UUID
from sqlalchemy import DateTime # Timestamp
from sqlalchemy.orm import column_property, composite, mapper, relationship

class User(Base):
    __tablename__ = 'user'
    IBAN = Column(String(18), primary_key=True, index=True)
    firstName = Column(String(45))
    lastName = Column(String(45))
    email = Column(String(45))
    phone = Column(String(45))
    birthDate = Column(Date)
    balance = Column(Integer)

    cards = relationship("Cards", back_populates="user")

