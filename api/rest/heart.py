from flask import request, g

from api.models.heart import Heart
from api.models.heart_recharge import HeartRecharge
from api.models.prerequisites.heart_prerequisites import HeartPrerequisites
from api.models.prerequisites.heart_recharge_prerequisites import HeartRechargePrerequisites
from api.models.user_point import UserPointTx, UserPoint
from libs.database.engine import afr, Session
from libs.route.prerequisite import prerequisites
from libs.route.router import route
from libs.status import Status


@route
@prerequisites(HeartPrerequisites, 'heart')
def send_heart():
    '''
    하트를 보냅니다.
    '''
    heart = Heart(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'), )
    Session().add(heart)
    Session().commit()
    return  {'okay': True}, Status.HTTP_200_OK


@route
@prerequisites(HeartPrerequisites, 'double_heart')
def send_double_heart():
    '''
    더블하트를 보냅니다.
    '''
    heart = Heart(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'), double=True)
    Session().add(heart)
    Session().commit()
    return  {'okay': True}, Status.HTTP_200_OK


@route
@prerequisites(HeartPrerequisites, 'accept')
def accept_heart():
    '''
    받은 하트를 승인합니다.
    '''
    g.pr_result.get('heart').accept()
    Session().commit()
    return  {'okay': True}, Status.HTTP_200_OK


@prerequisites(HeartRechargePrerequisites, 'google')
def recharge_heart_google():
    '''
    구글 영수증을 검증하고 하트를 충전합니다.
    '''
    heart_recharge = afr(HeartRecharge(**request.json.get('recharge_info')))
    afr(UserPointTx(user_id=g.user_session.user.id, hp=heart_recharge.amount))
    UserPoint.heart_point(user_id=g.user_session.user.id, hp=heart_recharge.amount)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

