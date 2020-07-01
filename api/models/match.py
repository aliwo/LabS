from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME, TIMESTAMP

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Match(Base):
    __tablename__ = 'matches'
    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)

    matched = Column(BOOLEAN, server_default='0')
    type_ = Column(CHAR(10)) # SOYEON, PREFER, RANDOM 등이 있습니다.

    created_at = Column(DATETIME)
    el_time = Column(TIMESTAMP)
    matched_at = Column(DATETIME)

    TYPE_SOYEON = 'SOYEON'
    TYPE_PREFER = 'PREFER'
    TYPE_RANDOM = 'RANDOM'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def json(self):
        return {
            'id': self.id,
            'from_user_id': self.from_user_id,
            'to_user_id': self.to_user_id,
            'matched': self.matched,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
        }