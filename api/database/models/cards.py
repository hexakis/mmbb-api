from database.base_class import Base
from sqlalchemy import Column # Column
from sqlalchemy import Integer # Integer
from sqlalchemy import Numeric # Money
from sqlalchemy import Uuid # UUID
from sqlalchemy import Date # Date
from sqlalchemy import String # VARCHAR
from sqlalchemy import DateTime # Timestamp
from sqlalchemy import ForeignKey
from sqlalchemy.orm import column_property, composite, mapper, relationship


class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    UID = Column(String(8))
    expDate = Column(Date)
    Account_IBAN = Column(String(18), ForeignKey('user.IBAN'))
    pinCode = Column(Integer)


    user = relationship("User", back_populates="cards")