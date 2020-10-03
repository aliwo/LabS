from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import BOOLEAN, JSON, DATETIME
from sqlalchemy.orm import relationship

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper
from libs.fcm.notify import Notifier


class Notification(Base):
    __tablename__ = 'notifications'

    from_user_id = Column(Integer, ForeignKey('users.id', onupdate='SET NULL', ondelete='SET NULL'), nullable=True)
    to_user_id = Column(Integer, ForeignKey('users.id', onupdate='SET NULL', ondelete='SET NULL'))
    to_user = relationship('User', foreign_keys=[to_user_id])
    notification = Column(JSON)
    body = Column(JSON)
    fire = Column(BOOLEAN)
    read = Column(BOOLEAN, server_default='0')
    created_at = Column(DATETIME)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fire = False
        self.created_at = datetime.now()

    def notify(self):
        '''
        to_user 로 부터 fcm_token 을 얻어냅니다. 따라서 flush 이후에 호출해야 합니다.
        '''
        if self.to_user.fcm_token:
            result = \
                Notifier(token=self.to_user.fcm_token).notify(body=self.body, notification=self.notification)
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

