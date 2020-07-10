from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL

from libs.database.types import Base


class Star(Base):
    __tablename__ = 'stars'
    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    rate = Column(DECIMAL(10, 3))

    def json(self):
        return {
            'id': self.id,
            'rate': self.rate
        }
