from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME

from libs.database.types import Base


class TermsAgreement(Base):
    __tablename__ = 'terms_agreements'
    term_id = Column(Integer, ForeignKey('terms.id'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    agreed_at = Column(DATETIME)

    def __init__(self, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.agreed_at = datetime.now()
