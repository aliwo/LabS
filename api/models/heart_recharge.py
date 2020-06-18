
import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class HeartRecharge(Base):
    __tablename__ = 'heart_recharges'

    google_purchase_token = Column(CHAR(100))
    google_order_id = Column(CHAR(100))

    amount = Column(Integer, nullable=False)
    type = Column(CHAR(20), nullable=False)
    created_at = Column(DATETIME)

    TYPE_GOOGLE = 'GOOGLE'
    TYPE_APPLE = 'APPLE'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()

    def json(self):
        return {
            'id': self.id,
            'google_purchase_token': self.google_purchase_token,
            'google_order_id': self.google_order_id,
            'type': self.type,
            'created_at': DateTimeHelper.full_datetime(self.created_at)
        }


