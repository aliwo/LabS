from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER
from sqlalchemy.orm import relationship, backref

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class UserPointTx(Base):
    __tablename__ = 'user_point_transactions'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    created_at = Column(DATETIME)
    hp = Column(INTEGER)
    mp = Column(INTEGER)


class UserPoint(Base):
    # MP 와 HP 는 증감할때 Lock 을 걸어야 하므로 다른 테이블로 뺐다.
    __tablename__ = 'user_points'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('point', cascade='all,delete', uselist=False))
    hp = Column(INTEGER, server_default='0')
    mp = Column(INTEGER, server_default='0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

