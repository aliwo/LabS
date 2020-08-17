from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import BOOLEAN, JSON, DATETIME

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper
from libs.fcm.notify import Notifier


class Notification(Base):
    __tablename__ = 'notifications'

    from_user_id = Column(Integer, ForeignKey('users.id', onupdate='SET NULL', ondelete='SET NULL'), nullable=True)
    to_user_id = Column(Integer, ForeignKey('users.id', onupdate='SET NULL', ondelete='SET NULL'))
    body = Column(JSON)
    fire = Column(BOOLEAN)
    read = Column(BOOLEAN, server_default='0')
    created_at = Column(DATETIME)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fire = False
        self.created_at = datetime.now()
        if kwargs.get('body'):
            if kwargs.get('body').get('clip_id'):
                self.clip_id = int(kwargs.get('body').get('clip_id'))

    def notify(self, fcm_token, log=True, topic=None):
        '''
        토큰이 비어있는 유저가 있기 때문에, 토큰 체크를 먼저 한 후, 토큰이 비어 있으면
        fire = False 입니다.
        '''
        if fcm_token or topic:
            result = Notifier(fcm_token, self.to_user_id, topic=topic).notify(self.body, log=log)
            if result:
                self.fire = True
            return result
        else:
            self.fire = False

    def json(self, **kwargs):
        return {
            'id': self.id,
            'to_user_id': self.to_user_id,
            'body': self.body,
            'fire': self.fire,
            'read': self.read,
            'created_at': DateTimeHelper.full_datetime(self.created_at)
        }

