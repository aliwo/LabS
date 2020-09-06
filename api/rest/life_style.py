from flask import g, request

from api.models.life_style_answer import LifeStyleAnswer
from api.models.life_style_question import LifeStyleQuestion
from libs.database.engine import Session, afr
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_life_style_questions():
    return {'questions': Session().query(LifeStyleQuestion).one().questions }, Status.HTTP_200_OK


@route
def get_life_style_answers():
    answer = Session().query(LifeStyleAnswer).filter((LifeStyleAnswer.user_id == g.user_session.user.id)).first()
    if answer is None:
        raise ClientError('answer not found', status_code=Status.HTTP_404_NOT_FOUND)
    return {'answers': answer.answers }, Status.HTTP_200_OK


@route
def post_life_style_answers():
    afr(LifeStyleAnswer(answers=request.json.get('answers'), user_id=g.user_session.user.id))
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

