from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME, TIMESTAMP

from libs.database.types import Base


class Match(Base):
    '''
    테이블 상속을 쓸까..? 아니면 strategy 패턴으로 할까? -> 당연히 init_on_load 써서 strategy 로 가는게 더 우아하다.

    '''
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
            'rate': self.rate
        }
