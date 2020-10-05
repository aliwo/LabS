from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from api.models.animal import Animal
from api.models.mbti_questions import MbtiQuestion
from api.models.mbti_result import MbtiResult
from libs.database.engine import Session, afr
from libs.route.auth import user_id_or_zero
from libs.route.errors import ClientError
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
    mbti_result = MbtiResult(request.json.get('result'), user_id=user_id_or_zero())
    if user_id_or_zero():
        Session().add(mbti_result)
        Session().commit()
    return {'animal': mbti_result.animal.json()}, Status.HTTP_200_OK


@route
def get_mbti_result(user_id):
    try:
        mbti_result = Session().query(MbtiResult).filter((MbtiResult.user_id == user_id))\
            .order_by(MbtiResult.id.desc()).first()
    except NoResultFound:
        raise ClientError(f'user #{user_id} mbti_result not found', Status.HTTP_404_NOT_FOUND)
    return {'result': mbti_result.json()}, Status.HTTP_200_OK

