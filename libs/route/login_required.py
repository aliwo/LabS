from flask import g
from datetime import datetime
from api.models.user_session import UserSession
from werkzeug.exceptions import Unauthorized


def login_required(token):
    '''
    주의! 반드시 @route 아래에 설치해야 합니다.
    '''
    user_session = UserSession.get_session(token)
    if user_session is None:
        raise Unauthorized()

    g.user_session = user_session
    g.user_session.user.last_access = datetime.now()
    return {'active': True}


