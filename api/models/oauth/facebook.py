from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, BOOLEAN, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref

from libs.database.engine import Base
from libs.datetime_helper import DateTimeHelper


# {
#     "id": "105611490876798",
#     "name": "Bill Aldbhchdbajdf Huiman",
#     "email": "pudmfvflmq_1572240120@tfbnw.net",
#     "picture": {
#         "data": {
#             "height": 50,
#             "is_silhouette": true,
#             "url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=105611490876798&height=50&width=50&ext=1574833144&hash=AeQNZTIYexwbacr5",
#             "width": 50
#         }
#     }
# }

class OauthFacebook(Base):
    __tablename__ = 'oauth_facebook'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False, backref=backref('oauth_facebook', cascade='all,delete', uselist=False))
    party_id = Column(CHAR(50), nullable=False, unique=True)
    party_name = Column(TEXT, nullable=False)
    party_picture = Column(TEXT)
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
        self.party_picture = info['picture']['data'].get('url')




