from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from api.models.user import User
from libs.database.engine import Session
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
def put_user_profile():
    for key, value in request.json:
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


# FM 대로 하자면, 이상형 정보를 입력하는 라우트를 만들어야 함. (put_user 와 똑같이)
# 그리고 여기서 mp 50 을 늘려 줘야 하는데... 그냥 mp 증가 경로를 만들어 버릴까 ^^
# 솔직히 베타 때는 생각 안 해도 됨

