import hashlib

from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from admin.handlers.auth import get_or_create_admin_session
from admin.models.admin import Admin
from libs.database.engine import Session
from libs.route.login_required import login_required
from libs.route.router import route
from libs.status import Status


@route
def login():
    try:
        admin = Session().query(Admin).filter((Admin.name == request.json.get('username'))
                 & (Admin.password == hashlib.sha256(request.json.get('password').encode('utf-8')).hexdigest() )).one()
    except NoResultFound:
        return {'msg': 'wrong account or password', 'okay':False}, Status.HTTP_401_UNAUTHORIZED
    admin_session = get_or_create_admin_session(admin)
    Session().commit()

    return {'token':admin_session.token, 'okay':True}, Status.HTTP_200_OK


@route
def info():
    admin = Session().query(Admin).filter((Admin.user_id == g.user_session.user.id)).one()
    return {'admin': admin.json()}, Status.HTTP_200_OK

