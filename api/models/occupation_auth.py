from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME
from sqlalchemy.orm import relationship
from libs.database.types import Base


class OccupationAuth(Base):
    __tablename__ = 'occupation_auth'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    occupation_type = Column(CHAR(20)) # edu 와 work 가 있다.
    url = Column(TEXT)
    created_at = Column(DATETIME)
    confirmed = Column(BOOLEAN)
    confirmed_at = Column(DATETIME)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def confirm(self):
        self.confirmed = True
        self.confirmed_at = datetime.now()

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'occupation_type': self.occupation_type,
            'url': self.url,
            'confirmed': self.confirmed,
        }
