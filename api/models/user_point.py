from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER
from sqlalchemy.orm import relationship, backref

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class UserPointTx(Base):
    __tablename__ = 'user_point_transactions'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    created_at = Column(DATETIME)
    hp = Column(INTEGER, default='0')
    mp = Column(INTEGER, default='0')

    heart_recharge_id = Column(Integer, ForeignKey('heart_recharges.id')) # 하트 포인트가 증가하는 경우
    heart_id = Column(Integer, ForeignKey('hearts.id')) # 하트를 쏴서 포인트가 감소하는 경우

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()


class UserPoint(Base):
    # MP 와 HP 는 증감할때 Lock 을 걸어야 하므로 다른 테이블로 뺐다.
    __tablename__ = 'user_points'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('point', cascade='all,delete', uselist=False))
    hp = Column(INTEGER, server_default='0')
    mp = Column(INTEGER, server_default='0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def heart_point(cls, user_id, hp):
        '''
        hp 는 음수일 수 있습니다. 음수라면 hp 가 감소합니다.
        '''
        from libs.database.engine import Session
        point = Session().query(UserPoint).filter((UserPoint.user_id==user_id)).with_for_update().one()
        point.hp += hp
        Session().flush()
        return point

    @classmethod
    def manner_point(cls, user_id, mp):
        '''
        mp 는 음수일 수 있습니다. 음수라면 hp 가 감소합니다.
        '''
        from libs.database.engine import Session
        point = Session().query(UserPoint).filter((UserPoint.user_id==user_id)).with_for_update().one()
        point.mp += mp
        Session().flush()
        return point
