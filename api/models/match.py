from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DATETIME, TIMESTAMP

from libs.database.types import Base


class MatchStrategy:

    @classmethod
    def gen(cls):
        '''
        매치 전략에 맞는 Match 의 리스트를 만들어 냅니다.
        '''
        return []


class SoyeonStrategy(MatchStrategy):
    '''
    MBTI 기준으로 매칭
    '''


class PreferenceStrategy(MatchStrategy):
    '''
    선호하는 성격 타입으로 매칭
    '''


class RandomStrategy(MatchStrategy):
    '''
    랜덤 게임~
    '''


class Match(Base):
    '''
    테이블 상속을 쓸까..? 아니면 strategy 패턴으로 할까? -> 당연히 init_on_load 써서 strategy 로 가는게 더 우아하다.

    '''
    __tablename__ = 'matches'
    from_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True)

    matched = Column(BOOLEAN)
    type_ = Column(CHAR(10)) # SOYEON, PREFER, RANDOM 등이 있습니다.

    created_at = Column(DATETIME)
    el_time = Column(TIMESTAMP)
    matched_at = Column(DATETIME)

    def json(self):
        return {
            'id': self.id,
            'rate': self.rate
        }
