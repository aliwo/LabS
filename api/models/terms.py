from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT
from sqlalchemy.orm import relationship

from libs.database.types import Base


class Term(Base):
    __tablename__ = 'terms'
    title = Column(TEXT)
    symbol = Column(CHAR(10))
    body = Column(TEXT)
    required = Column(BOOLEAN)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'symbol': self.symbol,
            'body': self.body,
            'required': self.required
        }
