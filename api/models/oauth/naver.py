from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref

from libs.database.types import Base


class OauthNaver(Base):
    __tablename__ = 'oauth_naver'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('oauth_naver', cascade='all,delete', uselist=False))
    party_id = Column(CHAR(50), nullable=False, unique=True)
    party_email = Column(TEXT)

    def __init__(self, user, info, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.user = user
        self.user_id = user.id
        self.party_id = info.get('id')
        self.party_email = info.get('email')
