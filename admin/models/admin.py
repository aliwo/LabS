from sqlalchemy import Column, Integer, ForeignKey, event
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT
from sqlalchemy.orm import relationship

from libs.database.types import Base


class Admin(Base):
    __tablename__ = 'admins'

    name = Column(CHAR(30), server_default='', unique=True)
    password = Column(TEXT)
    avatar = Column(TEXT, default='')
    role = Column(CHAR(30))
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', lazy="selectin")

    ROLE_MASTER = 'Master'

    def json(self):
        return {
            'name': self.name,
            'avatar': self.avatar,
            'roles': self.role
        }



