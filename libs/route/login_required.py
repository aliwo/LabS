from flask import g
from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from api.models.user_session import UserSession
from werkzeug.exceptions import Unauthorized
from libs.database.engine import Session


def login_required(token):
    user_session = UserSession.get_session(token)
    if user_session is None:
        raise Unauthorized()

    g.user_session = user_session
    g.user_session.user.last_access = datetime.now()
    return {'active': True}


def admin_required(token):
    from admin.models.admin import Admin
    login_required(token)
    try:
        admin = Session().query(Admin).filter((Admin.user_id == g.user_session.user.id)).one()
    except NoResultFound:
        raise Unauthorized()
    g.admin = admin
    return {'active': True}


