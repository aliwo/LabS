
import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper

# 자기가 충전해서 보유하고 있는 하트는 heart_point.
# 하트를 누군가에게 쐈다면 hearts 가 됩니다.
# A.K.A Heart arrow

class Heart(Base):
    __tablename__ = 'hearts'

    from_user = Column(Integer)
    to_user = Column(Integer)
    double = Column(BOOLEAN)

    created_at = Column(DATETIME)


