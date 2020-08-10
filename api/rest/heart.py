from flask import request, g

from api.models.heart import Heart
from api.models.heart_recharge import HeartRecharge
from api.models.match import Match
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
    단 방향 매치의 경우, 상대방을 향한 매치도 생성합니다.
    '''
    heart = afr(Heart(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id')))
    g.pr_result['to_match'].heart_id = heart.id
    g.pr_result['from_match'].heart_id = heart.id
    Session().add(heart)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
@prerequisites(HeartPrerequisites, 'heart')
def send_double_heart():
    '''
    더블하트를 보냅니다.
    '''
    heart = afr(Heart(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'), double=True))
    g.pr_result['to_match'].heart_id = heart.id
    g.pr_result['from_match'].heart_id = heart.id
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
    TODO: 테스트 필요
    구글 영수증을 검증하고 하트를 충전합니다.
    '''
    heart_recharge = afr(HeartRecharge(**request.json.get('recharge_info')))
    afr(UserPointTx(user_id=g.user_session.user.id, hp=heart_recharge.amount))
    UserPoint.heart_point(user_id=g.user_session.user.id, hp=heart_recharge.amount)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def heart2me():
    '''
    자신이 받은 모든 하트를 조회합니다.
    '당신에게 관심있는 인연'을 조회할 때 사용
    '''
    hearts = Session().query(Heart).filter(Heart.to_user_id == g.user_session.user.id).all()
    return {'hearts': [x.json(with_users=True) for x in hearts]}, Status.HTTP_200_OK

