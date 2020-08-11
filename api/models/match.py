from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME, TIMESTAMP
from sqlalchemy.orm import relationship

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Match(Base):
    __tablename__ = 'matches'
    __table_args__ = (UniqueConstraint('from_user_id', 'to_user_id', name='from_to_user_id'), )

    heart_id = Column(Integer, ForeignKey('hearts.id', ondelete='SET NULL'))
    from_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)

    heart = relationship('Heart', lazy='selectin')
    from_user = relationship('User', foreign_keys=[from_user_id], lazy='selectin')
    to_user = relationship('User', foreign_keys=[to_user_id])

    matched = Column(BOOLEAN, server_default='0')
    opened = Column(BOOLEAN, server_default='0')
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
    def matched_user_ids(cls, user_id, session):
        return [x.from_user_id for x in session.query(Match).filter((Match.to_user_id == user_id))]

    def json(self):
        result = {
            'id': self.id,
            'from_user_id': self.from_user_id,
            'from_user': self.from_user.json(),
            'to_user_id': self.to_user_id,
            'matched': self.matched,
            'heart_id': self.heart_id,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
        }
        if self.heart:
            result['heart'] = self.heart.json()
        return result
