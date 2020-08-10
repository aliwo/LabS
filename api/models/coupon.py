import random
import string
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, DATETIME

from libs.database.engine import Session
from libs.database.types import Base


class Coupon(Base):
    __tablename__ = 'coupons'
    code = Column(CHAR(50), unique=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True) # 특정 유저에게만 지급할 때
    redeemed = Column(BOOLEAN, server_default='0')
    created_at = Column(DATETIME)
    redeemed_at = Column(DATETIME)

    hp = Column(Integer, server_default='0')
    mp = Column(Integer, server_default='0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        while True:
            self.code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
            if Session().query(Coupon).filter((Coupon.code == self.code)).one_or_none() is None:
                break
        self.created_at = datetime.now()

    def redeem(self, user_id):
        from api.models.user_point import UserPoint
        self.redeemed = True
        self.redeemed_at = datetime.now()
        UserPoint.heart_point(user_id, self.hp)
        UserPoint.manner_point(user_id, self.mp)

    def json(self):
        '''
        서버에서 이걸 리턴하면 안될 거 같은데..?
        '''
        return {
            'id': self.id
        }
