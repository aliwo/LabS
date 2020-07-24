from datetime import datetime, timedelta

from flask import request, g
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from api.models.blacklist import Blacklist
from api.models.occupation_auth import OccupationAuth
from api.models.star import Star
from api.models.user import User
from libs.database.engine import Session, afr
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_user_profile(user_id):
    try:
        user = Session().query(User).filter((User.id == user_id)).one()
    except NoResultFound:
        raise ClientError(f'No User Found id #{user_id}', status_code=Status.HTTP_404_NOT_FOUND)

    return {'user': user.json()}, Status.HTTP_200_OK


@route
def get_my_profile():
    return {'user': g.user_session.user.json()}, Status.HTTP_200_OK


@route
def put_user_profile():
    for key, value in request.json.items():
        if key in User.sensitives:
            continue
        setattr(g.user_session.user, key, value)
        Session(changed=True)
    Session().commit()
    return {'user': g.user_session.user.json()}, Status.HTTP_200_OK


@route
def check_nick_name(nick_name):
    duplicate = Session().query(User).filter((User.nick_name == nick_name)).one_or_none()
    return {'duplicate': False if duplicate is None else True}, Status.HTTP_200_OK


@route
def del_phone():
    g.user_session.user.phone = None
    g.user_session.user.phone_registered = False
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def upload_auth_occupation():
    afr(OccupationAuth(
        user_id=g.user_session.user.id,
        occupation_type=request.json.get('occupation_type'),
        url=request.json.get('url')
    ))
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def get_random_user():
    '''
    1. 자기 자신 제외
    2. 자신이 한 번이라도 평가했던 사람은 제외
    3. 자신과 같은 성별 제외
    '''

    rated_user_ids = [x.to_user_id for x in Session().query(Star).filter((Star.from_user_id == g.user_session.user.id)).all()]

    user = Session().query(User).filter(
        (User.sex != g.user_session.user.sex)
        & (User.id.notin_(rated_user_ids))
        & (User.id != g.user_session.user.id)
    ).order_by(func.random()).first()

    return {'okay': True, 'user': user.json()}, Status.HTTP_200_OK

# FM 대로 하자면, 이상형 정보를 입력하는 라우트를 만들어야 함. (put_user 와 똑같이)

@route
def delete_user():
    '''
    회원 탈퇴합니다.
    1. 블랙리스트 명부에 올리고
    2. 삭제.
    '''
    Session().add(Blacklist(g.user_session.user,
                            kind=Blacklist.KIND_RESIGN, until=datetime.now() + timedelta(days=90)))
    Session().flush()

    Session().delete(g.user_session.user)
    Session().flush()
    return {'okay':True}, Status.HTTP_200_OK

