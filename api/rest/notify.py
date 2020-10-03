from flask import g, request

from api.models.heart import Heart
from api.models.match import Match
from libs.fcm import firebase_app # 지우지마
from api.models.notification import Notification
from libs.database.engine import Session
from libs.database.engine import afr
from libs.fcm.notify import Notifier
from libs.route.router import route
from libs.status import Status


@route
def notify_heart_received():
    notification = afr(Notification(from_user_id=g.user_session.user.id,
                                    to_user_id=request.json.get('user_id'),
                                    body={
                                        'kind': 'HEART_RECEIVED',
                                        'user_id': str(g.user_session.user.id),
                                        'title': '하트가 도착하였습니다!',
                                    }))

    notification.notify()
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def notify_heart_accepted():
    heart = Session().query(Heart).filter((Heart.id == request.json.get('heart_id'))).one()
    match = Session().query(Match).filter((Match.heart_id == heart.id)
                                          & (Match.from_user_id == g.user_session.user.id)).one()
    notification = afr(Notification(from_user_id=g.user_session.user.id,
                                    to_user_id=match.to_user_id,
                                    notification={'title': f'{g.user_session.user.nick_name if g.user_session.user.nick_name else "???"} '
                                                 f'님이 하트를 수락하셨습니다'},
                                    body={
                                        'kind': 'HEART_ACCEPTED',
                                        'match_id': str(match.id),
                                        'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                                    }))

    notification.notify()
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def notify_register_confirmed():
    '''
    TODO: 이것도 관리자페이지 기능
    '''
    notification = afr(Notification(from_user_id=g.user_session.user.id,
                                    to_user_id=request.json.get('user_id'),
                                    body={
                                        'kind': 'REGISTER_CONFIRMED',
                                        'title': '가입이 승인되었습니다!',
                                    }))

    notification.notify()
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def notify_today_match():
    '''
    TODO 이거 관리자 페이지로 옮기던가... prod_job 이 수행하도록 하기
    '''
    Notifier(topic='MATCH').notify({
                                        'kind': 'REGISTER_CONFIRMED',
                                        'title': '가입이 승인되었습니다!',
                                    })

    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


# @route
# def notify_announcement():
#     '''
#     TODO 관리자 페이지
#     :return:
#     '''
#     pass



