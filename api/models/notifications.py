import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class Notification(Base):
    __tablename__ = 'notifications'