from flask import request, g

from api.models.heart import Heart
from api.models.heart_recharge import HeartRecharge
from api.models.prerequisites.heart_prerequisites import HeartPrerequisites
from api.models.prerequisites.heart_recharge_prerequisites import HeartRechargePrerequisites
from api.models.user_point import UserPointTx, UserPoint
from libs.database.engine import afr, Session
from libs.route.prerequisite import prerequisites
from libs.status import Status


def send_heart():
    '''
    하트를 보냅니다.
    '''


def send_double_heart():
    '''
    더블하트를 보냅니다.
    '''


@prerequisites(HeartPrerequisites, 'accept')
def accept_heart():
    '''
    받은 하트를 승인합니다.
    '''


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

