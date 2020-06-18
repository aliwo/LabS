import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN

from api.models.user_point import UserPoint
from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper

# 자기가 충전해서 보유하고 있는 하트는 heart_point.
# 하트를 누군가에게 쐈다면 hearts 가 됩니다.
# A.K.A Heart arrow

class Heart(Base):
    __tablename__ = 'hearts'

    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    double = Column(BOOLEAN)
    accpeted = Column(BOOLEAN)

    created_at = Column(DATETIME)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def accept(self):
        '''
        하트 받기는 기본적으로 3천원~
        '''
        from libs.database.engine import Session
        from api.models.item import Item

        if not self.double:
            accept = Session().query((Item.symbol == 'accept')).one_or_none()
            UserPoint.heart_point(self.to_user_id, accept.price if accept else 3000)

        self.accpeted = True
