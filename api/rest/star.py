from flask import g, request
from api.models.star import Star
from libs.database.engine import Session
from libs.route.router import route
from libs.status import Status


@route
def rate_star():
    '''
    TODO: 테스트 필요
    1. 이미 존재하는 스타가 있는지 체크합니다.
    2. 있다면 해당 스타의 별점을 바꿉니다.
    3. 없다면 새로운 스타를 만듭니다.
    '''
    star = Session().query(Star).filter((Star.from_user_id == g.user_session.user.id)
                                        & (Star.to_user_id == request.json.get('user_id'))).one_or_none()
    if not star:
        star = Star(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'))
        Session().add(star)

    star.rate = request.json.get('rate')

    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK
