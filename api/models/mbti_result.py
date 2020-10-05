from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN, JSON

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper
from libs.route.errors import ClientError


def get_trait_template():
    return {
        'E': 0,
        'I': 0,
        'N': 0,
        'S': 0,
        'T': 0,
        'F': 0,
        'J': 0,
        'P': 0,
        'EI_TOTAL': 20, # TOTAL은 전부 하드코딩~
        'SN_TOTAL': 20, # TOTAL은 전부 하드코딩~
        'TF_TOTAL': 24, # TOTAL은 전부 하드코딩~
        'JP_TOTAL': 16, # TOTAL은 전부 하드코딩~
    }


class MbtiResult(Base):
    __tablename__ = 'mbti_results'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    raw = Column(JSON) # 테스트 결과 json 을 raw 로 저장합니다.
    result_mbti = Column(CHAR(10))
    result_rate = Column(JSON)
    # result_animal_id 를 result_mbti 와 통합해도 되긴 함! animal 이 mbti aronym 을 가지고 있으니까.
    animal_id = Column(Integer, ForeignKey('animals.id'))
    created_at = Column(DATETIME)

    # determinant 별로 합산 한뒤 E - I 를 하는 방식으로 산출하면 됨.

    def __init__(self, test_results, **kwargs):
        '''

        '''
        super().__init__(**kwargs)
        self.raw = test_results
        self.result_rate = self.calc_rate(test_results)
        self.result_mbti = self.calc_mbti()
        self.animal_id = self.animal.id
        self.created_at = datetime.now()

    def calc_mind(self, E, I):
        return 'E' if E - I > 2 else 'I'

    def calc_energy(self, S, N):
        return 'S' if S - N > 2 else 'N'

    def calc_nature(self, T, F):
        return 'T' if T - F > 2 else 'F'

    def calc_identity(self, J, P):
        return 'J' if J - P > 2 else 'P'

    def calc_rate(self, test_results):
        '''
        1. mbti_question 을 전부 쿼리
        2. test_result 를 id 순으로 정렬.
        3. zip 해서 순회
        '''
        from libs.database.engine import Session
        from api.models.mbti_questions import MbtiQuestion
        template = get_trait_template()

        questions = Session().query(MbtiQuestion).all()
        results = sorted(test_results, key=lambda x: x.get('mbti_id'))
        for result, question in zip(results, questions):
            if result.get('mbti_id') != question.id:
                raise ClientError(f'invalid question_id: client:{result.get("mbti_id")} server:{question.id}')
            template[question.trait] += result.get('point')
        return template

    def calc_mbti(self):
        return f'{self.calc_mind(self.result_rate["E"], self.result_rate["I"])}' \
               f'{self.calc_energy(self.result_rate["S"], self.result_rate["N"])}' \
               f'{self.calc_nature(self.result_rate["T"], self.result_rate["F"])}' \
               f'{self.calc_identity(self.result_rate["J"], self.result_rate["P"])}'

    @property
    def animal(self):
        if not hasattr(self, '_animal'):
            from libs.database.engine import Session
            from api.models.animal import Animal
            self._animal = Session().query(Animal).filter((Animal.mbti ==  self.result_mbti)).one()
        return self._animal

    @property
    def rates_in_100(self):
        '''
        5, 4, 6 등의 "계수" 는 하드코딩
        '''
        return {
            self.result_mbti[0]: self.result_rate[self.result_mbti[0]] * 5,
            self.result_mbti[1]: self.result_rate[self.result_mbti[1]] * 5,
            self.result_mbti[2]: self.result_rate[self.result_mbti[2]] * 4,
            self.result_mbti[3]: self.result_rate[self.result_mbti[3]] * 6,
        }

    def json(self):
        return {
            'id': self.id,
            'result_rate': self.result_rate,
            'result_mbti': self.result_mbti,
            'rates_in_100': self.rates_in_100,
            'user_id': self.user_id,
            'animal_id': self.animal_id,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
        }

