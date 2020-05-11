from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref
from libs.database.engine import Base


# google 로 부터 오는 user_info 는 다음과 같이 생겼습니다.
# {
#     "id": "105171281182656830722",
#     "email": "recordable0711@gmail.com",
#     "verified_email": true,
#     "name": "recordable542",
#     "given_name": "recordable542",
#     "picture": "https://lh3.googleusercontent.com/a-/AAuE7mApmJ04wBc-McXES5PG7pgeC4sKLMtpkq2g27lR2Q",
#     "locale": "ko"
# }



class OauthGoogle(Base):
    __tablename__ = 'oauth_google'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('oauth_google', cascade='all,delete', uselist=False))
    party_id = Column(CHAR(50), nullable=False, unique=True)
    party_name = Column(TEXT, nullable=False)
    party_email = Column(TEXT)

    def __init__(self, user, info, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.user = user
        self.user_id = user.id
        self.party_id = info.get('id')
        self.party_name = info.get('name')
        self.party_email = info.get('email')
        self.party_picture = info.get('picture')




