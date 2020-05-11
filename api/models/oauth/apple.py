from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref

from libs.database.engine import Base
from libs.datetime_helper import DateTimeHelper


class OauthApple(Base):
    __tablename__ = 'oauth_apple'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('oauth_apple', cascade='all,delete', uselist=False))
    party_id = Column(CHAR(80), nullable=False, unique=True)
    party_name = Column(TEXT, nullable=False)
    party_email = Column(TEXT)
    party_picture = Column(TEXT)
    refresh_token = Column(TEXT)

    def __init__(self, user, info, **kwargs):
        '''
        애플 로그인은 서버에서 인증을 거치기 때문에
        refresh_token 을 저장합니다.
        '''
        super().__init__(**kwargs)
        self.user = user
        self.user_id = user.id
        self.party_id = info.get('sub')
        self.party_name = info.get('email')
        self.party_email = info.get('email')
        self.party_picture = ''
        self.refresh_token = kwargs.get('refresh_token')






