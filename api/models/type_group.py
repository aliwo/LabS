from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN
from libs.database.types import Base


class TypeGroup(Base):
    __tablename__ = 'type_groups'

    title = Column(TEXT)
    acronym = Column(CHAR(10))

    def json(self, **kwargs):
        return {
            'id': self.id,
            'title': self.title,
            'acronym': self.acronym
        }


