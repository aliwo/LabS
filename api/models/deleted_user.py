from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, orm
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN, TIMESTAMP, DECIMAL
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref

from api.models.tiers.tier_utils import load_tier, tier_case
from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper
from libs.query_strategy import QueryStrategy



class DeletedUser(Base):
    __tablename__ = 'deleted_users'

    name = Column(CHAR(50))
    user_id = Column(Integer) # 과거 가지고 있던 user id 를 기억합니다.
