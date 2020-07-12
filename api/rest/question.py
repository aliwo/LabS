from flask import request, g

from api.models.animal import Animal
from api.models.mbti_questions import MbtiQuestion
from api.models.mbti_result import MbtiResult
from libs.database.engine import Session, afr
from libs.route.router import route
from libs.status import Status


@route
def get_mbti_questions():
    '''
    mbti 문제들을 가져옵니다.:
    '''
    return {'questions': [x.json() for x in Session().query(MbtiQuestion).all()]}, Status.HTTP_200_OK


def get_love_questions():
    '''
    추가예정
    '''

@route
def post_mbti_results():
    mbti_result = afr(MbtiResult(request.json.get('result'), user_id=g.user_session.user.id))
    return {'animal': mbti_result.animal.json()}, Status.HTTP_200_OK

