from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import JSON

from libs.database.types import Base


class LifeStyleQuestion(Base):
    __tablename__ = 'life_style_questions'

    questions = Column(JSON) # 그냥 JSON 저장소로 사용합니다.

    def json(self):
        return {
            'id': self.id,
            'questions': self.questions
        }
