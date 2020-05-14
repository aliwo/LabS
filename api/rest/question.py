from api.models.mbti_questions import MbtiQuestion
from libs.database.engine import Session
from libs.status import Status


def get_mbti_questions():
    '''
    mbti 문제들을 가져옵니다.:
    '''
    return {'questions': [x.json() for x in Session().query(MbtiQuestion).all()]}, Status.HTTP_200_OK


def get_love_questions():
    '''
    추가예정
    '''


def post_mbti_results():
    pass

