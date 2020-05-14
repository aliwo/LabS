import uuid
from datetime import datetime, timedelta
from random import randint

from sqlalchemy.orm import relationship
from libs.database.types import Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import DATETIME, TEXT, BOOLEAN, CHAR


class SmsAuth(Base):
    __tablename__ = 'sms_auth'

    auth_key = Column(CHAR(80))
    auth_value = Column(CHAR(10))
    phone_num = Column(CHAR(20))
    user = relationship('User', lazy="selectin")
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    expiration = Column(DATETIME)

    def __init__(self, user_id, phone_num, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.phone_num = phone_num
        self.auth_key = uuid.uuid4()
        self.auth_value = ''.join([str(randint(0, 9)) for x in range(0, 6)])
        self.expiration = datetime.now() +timedelta(minutes=10)



    @classmethod
    def validate_sms_auth(cls, key, value, user_id=None, dry=False):
        from libs.database.engine import Session
        try:
            sms_auth = Session().query(SmsAuth).filter((SmsAuth.auth_key == key)
                                                        & (SmsAuth.auth_value == value)
                                                        & (SmsAuth.user_id == user_id)
                                                        & (SmsAuth.expiration >= datetime.now())).one()
        except NoResultFound:
            return False
        else:

            if dry:
                return True

            Session().delete(sms_auth)
            Session().flush()
            return True

    @property
    def json(self):
        return {'idx':self.id,
                'auth_key': self.auth_key,
                'auth_value': self.auth_value,
                'user_id': self.user_id
        }


