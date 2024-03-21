from database.base_class import Base
from sqlalchemy import Column # Column
from sqlalchemy import Integer # Integer
from sqlalchemy import Numeric # Money
from sqlalchemy import Uuid # UUID
from sqlalchemy import DateTime # Timestamp
from sqlalchemy.orm import column_property, composite, mapper, relationship


class Transaction(Base):
    created_at = Column(DateTime, nullable=False)
    transaction_id = Column(Uuid, nullable=False, primary_key=True)
    customer_id = Column(Integer, nullable=False, index=True)
    transaction_amount = Column(Numeric, nullable=False)