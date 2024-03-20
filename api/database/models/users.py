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
    firstname = Column(String(20), nullable=False)
    preposition = Column(String(20), nullable=True)
    lastname = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String(13), unique=True)
    iban = Column(String(18), unique=True)
    password = Column(String, nullable=False)
    customer_id = Column(Integer, nullable=False, index=True, primary_key=True, unique=True)
    totp = Column(String(30), nullable=False, unique=True)
    balance = Column(Numeric, nullable=False)

