import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Animal(Base):
    __tablename__ = 'animals'
    mbti = Column(CHAR(10))
    prefix = Column(TEXT)
    name = Column(TEXT)
    tags = Column(LaboratoryTypes.TextTuple)

    # profile
    main_profile = Column(TEXT) #
    romance_profile = Column(TEXT) # 사랑과 데이트 설명
    so_profile = Column(TEXT) # 상대에게 조언

    def json(self):
        return {

        }


