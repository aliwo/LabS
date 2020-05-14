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
    }


class MbtiResult(Base):
    __tablename__ = 'mbti_questions'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    raw = Column(JSON) # 테스트 결과 json 을 raw 로 저장합니다.
    result_mbti = Column(CHAR(10))
    # result_animal_id 를 result_mbti 와 통합해도 되긴 함! animal 이 mbti aronym 을 가지고 있으니까.
    animal_id = Column(Integer, ForeignKey('animals.id'))
    created_at = Column(DATETIME)

    # determinant 별로 합산 한뒤 E - I 를 하는 방식으로 산출하면 됨.

    def __init__(self, test_results, **kwargs):
        '''

        '''
        super().__init__(**kwargs)
        self.result_mbti = self.calc_mbti(test_results)
        self.animal_id = self.get_animal_id(self.result_mbti)
        self.created_at = datetime.now()

    def calc_mind(self, E, I):
        return 'E' if E - I > 4 else 'I'

    def calc_energy(self, S, N):
        return 'S' if S - N > 4 else 'N'

    def calc_nature(self, T, F):
        return 'T' if T - F > 4 else 'F'

    def calc_identity(self, J, P):
        return 'J' if J - P > 4 else 'P'

    def calc_mbti(self, test_results):
        '''
            1. mbti_question 을 전부 쿼리
            2. test_result 를 id 순으로 정렬.
            3. zip 해서 순회
        '''
        from libs.database.engine import Session
        from api.models.mbti_questions import MbtiQuestion
        template = get_trait_template()

        questions = Session().query(MbtiQuestion).all()
        for result, question in zip(sorted(test_results, key=lambda x: x.get('mbti_id')), questions):
            if result.get('mbti_id') != question.id:
                raise ClientError(f'invalid question_id: client:{result.get("mbti_id")} server:{question.id}')
            template[question.trait] += result.get('point')

        return f'{self.calc_mind(template["E"], template["I"])}' \
               f'{self.calc_energy(template["S"], template["N"])}' \
               f'{self.calc_nature(template["T"], template["F"])}' \
               f'{self.calc_identity(template["J"], template["P"])}'

    @classmethod
    def get_animal_id(self, mbti):
        from libs.database.engine import Session
        from api.models.animal import Animal
        # one 의 결과가 안 나올 수가 없음
        return Session().query(Animal).filter((Animal.mbti ==  mbti)).one().id

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'animal_id': self.animal_id,
            'created_at': DateTimeHelper.full_datetime(self.created_at),
        }

