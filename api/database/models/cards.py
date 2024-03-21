from database.base_class import Base
from sqlalchemy import Column # Column
from sqlalchemy import Integer # Integer
from sqlalchemy import Numeric # Money
from sqlalchemy import Uuid # UUID
from sqlalchemy import Date # Date
from sqlalchemy import String # VARCHAR
from sqlalchemy import DateTime # Timestamp
from sqlalchemy.orm import column_property, composite, mapper, relationship


class Cards(Base):
    iban = Column(String(17), unique=True)
    customer_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    card_id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    expiration_date = Column(Date, nullable=False)
    card_balance = Column(Numeric, nullable=False)
    card_type = Column(String, nullable=False, default="private")
    pincode = Column(String, nullable=False)