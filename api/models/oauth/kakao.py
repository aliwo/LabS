from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref

from libs.database.engine import Base
from libs.datetime_helper import DateTimeHelper

# {
#     "id": 1198292943,
#     "properties": {
#         "nickname": "정승원",
#         "profile_image": "http://k.kakaocdn.net/dn/kCQyE/btqzkbVQFcQ/sc8u7XhAvSBpTw1Odk9TUk/profile_640x640s.jpg",
#         "thumbnail_image": "http://k.kakaocdn.net/dn/kCQyE/btqzkbVQFcQ/sc8u7XhAvSBpTw1Odk9TUk/profile_110x110c.jpg"
#     },
#     "kakao_account": {
#         "profile_needs_agreement": false,
#         "profile": {
#             "nickname": "정승원",
#             "thumbnail_image_url": "http://k.kakaocdn.net/dn/epDNbq/btqygHHdI7r/23iosZecywbGj9RlaWKPP1/img_110x110.jpg",
#             "profile_image_url": "http://k.kakaocdn.net/dn/epDNbq/btqygHHdI7r/23iosZecywbGj9RlaWKPP1/img_640x640.jpg"
#         },
#         "has_email": true,
#         "email_needs_agreement": false,
#         "is_email_valid": true,
#         "is_email_verified": true,
#         "email": "aliwo@naver.com"
#     }
# }


class OauthKakao(Base):
    __tablename__ = 'oauth_kakao'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('oauth_kakao', cascade='all,delete', uselist=False))
    party_id = Column(CHAR(50), nullable=False, unique=True)
    party_name = Column(TEXT, nullable=False)
    party_email = Column(TEXT)
    party_picture = Column(TEXT)

    def __init__(self, user, info, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.user = user
        self.user_id = user.id
        self.party_id = info.get('id')
        self.party_name = info['properties'].get('nickname')
        self.party_email = info['kakao_account'].get('email')
        self.party_picture = info['properties'].get('profile_image')






