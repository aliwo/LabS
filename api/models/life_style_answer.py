from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import JSON

from libs.database.types import Base


class LifeStyleAnswer(Base):
    __tablename__ = 'life_style_answers'
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))
    answers = Column(JSON)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'questions': self.answers
        }
