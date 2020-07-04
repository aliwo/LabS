import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER
from sqlalchemy.orm import relationship

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Animal(Base):
    __tablename__ = 'animals'
    mbti = Column(CHAR(10), unique=True, index=True)
    prefix = Column(TEXT)
    name = Column(TEXT)
    tags = Column(LaboratoryTypes.TextTuple)
    type_group_id = Column(Integer, ForeignKey('type_groups.id'))

    # 다음의 backref 가 존재합니다.
    # user

    # profile
    summary = Column(TEXT)
    main_profile = Column(TEXT) #
    romance_profile = Column(TEXT) # 사랑과 데이트 설명
    so_profile = Column(TEXT) # 상대에게 조언
    best_partners = Column(LaboratoryTypes.IntTuple)

    correlations = relationship('AnimalCorrelation')

    def json(self):
        return {
            'id': self.id,
            'mbti': self.mbti,
            'prefix': self.prefix,
            'name': self.name,
            'tags': self.tags,
            'summary': self.summary,
            'main_profile': self.main_profile,
            'romance_profile': self.romance_profile,
            'so_profile': self.so_profile,
            'best_partners': self.best_partners,
            'type_group_id': self.type_group_id,
        }



