from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR, DATE
from sqlalchemy.orm import relationship

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper

class Blacklist(Base):
    __tablename__ = 'blacklist'

    PARTY_GOOGLE = 'GOOGLE'
    PARTY_KAKAO = 'KAKAO'
    PARTY_NAVER = 'NAVER'

    KIND_BAN = 'BAN'
    KIND_RESIGN = 'RESIGN'

    phone = Column(TEXT)
    party_id = Column(TEXT)
    created_at = Column(DATETIME)
    until = Column(DATE)
    party_name = Column(CHAR(20)) # KAKAO , GOOGLE, FACEBOOK 이 있음.
    kind = Column(CHAR(10)) # BAN (블랙 당함) 이랑 RESIGN (일반 탈퇴)

    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        if user.oauth.__tablename__.endswith('google'):
            self.party_name = self.PARTY_GOOGLE
        elif user.oauth.__tablename__.endswith('kakao'):
            self.party_name = self.PARTY_KAKAO
        elif user.oauth.__tablename__.endswith('naver'):
            self.party_name = self.PARTY_NAVER

        self.party_id = user.oauth.party_id
        self.created_at = datetime.now()
        self.phone = user.phone



