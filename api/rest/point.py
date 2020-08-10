from flask import g

from api.models.stay import Stay
from api.models.user_point import UserPoint
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def stay():
    '''
    회원탈퇴 하시려구요? 가지마세요
    100 포인트 드립니다.
    '''
    stay = Session().query(Stay).filter((Stay.user_id == g.user_session.user.id)).one_or_none()
    if stay:
        raise ClientError('duplicate')
    stay = Stay(user_id=g.user_session.user.id)
    UserPoint.heart_point(g.user_session.user.id, 100)
    Session().add(stay)
    Session().commit()
    return {'okay':True}, Status.HTTP_200_OK


