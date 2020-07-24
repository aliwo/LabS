from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import DATETIME, CHAR, BOOLEAN, TEXT, DECIMAL
from datetime import datetime
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Report(Base):
    __tablename__ = 'reports'

    from_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)

    memo = Column(TEXT)
    created_at = Column(DATETIME)
    status = Column(CHAR(10))

    STATUS_SUBMIT = 'SUBMIT' # 신고가 들어온 상태
    STATUS_RESOLVED = 'RESOLVED' # 신고가 해결된 상태
    STATUS_REJECTED = 'REJECTED' # 신고가 거절된 상태

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()
        self.status = self.STATUS_SUBMIT

    def json(self):
        return {
            'id': self.id,
            'from_user_id': self.from_user_id,
            'to_user_id': self.to_user_id,
            'memo': self.memo,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
            'status': self.status,
        }
