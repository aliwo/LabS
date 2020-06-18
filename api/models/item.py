from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT

from libs.database.types import Base


class Item(Base):
    __tablename__ = 'items'

    symbol = Column(CHAR(10), unique=True, index=True)
    price = Column(Integer)

    def json(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'price': self.price
        }
