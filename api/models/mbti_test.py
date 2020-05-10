
import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Mbti(Base):
    __tablename__ = 'mbtis'

    question = Column(TEXT)
    determinant = Column(CHAR(5)) # EI, SN, TF, JP 가 있다.
    positive = Column(BOOLEAN) # positive 가 true 라면 오른쪽으로, false 라면 왼쪽으로

