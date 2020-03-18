import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship

from libs.database import Base
from libs.datetime_helper import DateTimeHelper


class User(Base):
    __tablename__ = 'users'
    email = Column(TEXT) # 독자적으로도 로그인 할 수 있도록 email 란이 필요.
    password = Column(TEXT)
    nick_name = Column(CHAR(50), unique=True)
    picture = Column(TEXT)
    background_image = Column(TEXT)
    bio = Column(TEXT)
    fcm_token = Column(TEXT)
    phone = Column(CHAR(20), unique=True, nullable=True)
    registered_at = Column(DATETIME)  # 회원가입 통계낼 때 유용
    last_access = Column(DATETIME)  # 통계낼 때 유용

    # oauth_google_id = Column(Integer, ForeignKey('oauth_google.id', ondelete='CASCADE'))
    # oauth_kakao_id = Column(Integer, ForeignKey('oauth_kakao.id', ondelete='CASCADE'))
    # oauth_facebook_id = Column(Integer, ForeignKey('oauth_facebook.id', ondelete='CASCADE'))
    # oauth_apple_id = Column(Integer, ForeignKey('oauth_apple.id', ondelete='CASCADE'))

    # 다음 backref 가 존재합니다.
    # oauth_google
    # oauth_kakao
    # oauth_facebook
    # oauth_apple

    # @property
    # def oauth(self):
    #     if self.oauth_google_id:
    #         return self.oauth_google
    #     if self.oauth_kakao_id:
    #         return self.oauth_kakao
    #     if self.oauth_facebook_id:
    #         return self.oauth_facebook
    #     if self.oauth_apple_id:
    #         return self.oauth_apple

    def __init__(self, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.registered_at = datetime.now()
        self.last_access = datetime.now()
        self.nick_name = self.nick_name

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def json(self, **kwargs):
        result = {
            'id': self.id,
            'email': self.email,
            'picture': self.picture,
            'background_image': self.background_image,
            'name': self.nick_name if self.nick_name else '',
            'bio': self.bio,
            'fcm_token': self.fcm_token,
            'last_access': DateTimeHelper.full_datetime(self.last_access),
            'registered_at': DateTimeHelper.full_datetime(self.registered_at),
        }

        if self.phone:
            result['phone'] = self.phone

        return result
