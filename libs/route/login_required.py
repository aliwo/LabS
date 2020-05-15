from flask import g
from datetime import datetime
from api.models.user_session import UserSession
from werkzeug.exceptions import Unauthorized


def login_required(token):
    user_session = UserSession.get_session(token)
    if user_session is None:
        raise Unauthorized()

    g.user_session = user_session
    g.user_session.user.last_access = datetime.now()
    return {'active': True}


