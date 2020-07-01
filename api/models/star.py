from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT

from libs.database.types import Base


class Star(Base):
    __tablename__ = 'stars'
    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    rate = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'rate': self.rate
        }
