from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL

from libs.database.types import Base


class MbtiIndicator(Base):
    __tablename__ = 'mbti_indicators'
    synonym = Column(CHAR(10))
    description = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'synonym': self.synonym,
            'description': self.description,
        }
