from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT

from libs.database.types import Base


class Star(Base):
    __tablename__ = 'stars'
    user_id = Column(TEXT)
    rate = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'rate': self.rate
        }
