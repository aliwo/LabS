from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import DATETIME, CHAR, BOOLEAN, TEXT, DECIMAL
from datetime import datetime
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Report(Base):
    __tablename__ = 'reports'

    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)

    memo = Column(TEXT)
    created_at = Column(DATETIME)
    status = Column(CHAR(10))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def json(self):
        return {
            'id': self.id,
            'from_user_id': self.from_user_id,
            'to_user_id': self.to_user_id,
            'memo': self.memo,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
            'status': self.status,
        }
