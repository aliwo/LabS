import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class AnimalCorrelation(Base):
    __tablename__ = 'animal_correlations'

    from_animal_id = Column(INTEGER)
    to_animal_ids = Column(LaboratoryTypes.IntTuple)
    weight = Column(Integer) # 1 ~ 5

    def json(self):
        return {
            'from_animal_id': self.from_animal_id,
            'to_animal_ids': self.to_animal_ids,
            'weight': self.weight
        }


