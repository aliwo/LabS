from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME, TIMESTAMP
from sqlalchemy.orm import relationship

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Match(Base):
    __tablename__ = 'matches'
    man_id = Column(Integer, ForeignKey('users.id'), index=True)
    woman_id = Column(Integer, ForeignKey('users.id'), index=True)

    man = relationship('User', foreign_keys=[man_id], lazy='selectin')
    woman = relationship('User', foreign_keys=[woman_id], lazy='selectin')

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
        self.el_time = datetime.now()
        self.matched = False

    @classmethod
    def same_sex_query(cls, session, user):
        if user.sex == False:
            return session.filter((cls.man_id == user.id))
        return session.filter((cls.woman_id == user.id))

    @classmethod
    def query_matched_users(cls, session, user):
        if user.sex == False: # 남자면
            return [x.woman_id for x in session.query(cls).filter((cls.man_id == user.id)).all()]
        return [x.man_id for x in session.query(cls).filter((cls.woman_id == user.id)).all()]

    def json(self):
        return {
            'id': self.id,
            'man_id': self.man_id,
            'man': self.man.json(),
            'woman_id': self.woman_id,
            'woman': self.woman.json(),
            'matched': self.matched,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
        }
