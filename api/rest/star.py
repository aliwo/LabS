from flask import g, request
from api.models.star import Star
from api.models.user import User
from libs.database.engine import Session
from libs.route.router import route
from libs.status import Status


@route
def rate_star():
    '''
    1. 이미 존재하는 스타가 있는지 체크합니다.
    2. 있다면 해당 스타의 별점을 바꿉니다.
    3. 없다면 새로운 스타를 만듭니다.
    4. 스타의 rate 를 set
    5. flush
    6. 유저의 새로운 rate 를 결정합니다.
    '''
    star = Session().query(Star).filter((Star.from_user_id == g.user_session.user.id)
                                        & (Star.to_user_id == request.json.get('user_id'))).one_or_none()
    if not star:
        star = Star(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'))
        Session().add(star)

    star.rate = request.json.get('rate')
    Session().flush()

    stars = [x.rate for x in Session().query(Star).filter((Star.to_user_id == request.json.get('user_id'))).all()]
    user = Session().query(User).filter((User.id == request.json.get('user_id'))).one()
    user.rate = sum(stars) / len(stars)

    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def high_star2me():
    '''
    '나에게 높은 점수를 준 인연' 조회 용
    :return:
    '''

