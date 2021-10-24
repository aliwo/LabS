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
    TODO: 7. 만약 10 명 이상의 유저로 부터 평가를 받았다면 rating_required 를 false 로 합니다.
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
    # 대규모 시스템이라면 매 번 rate 를 새로 조정하는 게 아니라, 배치를 돌릴 거다. star 는 star 대로 쌓이고,
    # 배치를 돌릴 때만 rate 를 수정한다면 lock 을 걸 필요가 전혀 없다.
    # 요기요는 별점평가 시스템이 배치로 돌아가나?

    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def get_star_by_user_id(user_id):
    star = Session().query(Star).filter((Star.from_user_id == g.user_session.user.id)
                                        & (Star.to_user_id == user_id)).one_or_none()
    return {'okay': True if star else False}, Status.HTTP_200_OK


