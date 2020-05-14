
import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class MbtiQuestion(Base):
    __tablename__ = 'mbti_questions'

    question = Column(TEXT)
    determinant = Column(CHAR(5)) # E, I, N, S, T, F, J, P

    # determinant 별로 합산 한뒤 E - I 를 하는 방식으로 산출하면 됨.

    def json(self):
        return {
            'id': self.id,
            'question': self.question,
            'determinant': self.determinant,
        }

