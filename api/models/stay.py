from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL, DATETIME

from libs.database.types import Base


class Stay(Base):
    __tablename__ = 'stays'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), unique=True)
    created_at = Column(DATETIME)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
        }
