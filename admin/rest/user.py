import hashlib

from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from admin.handlers.auth import get_or_create_admin_session
from admin.models.admin import Admin
from api.models.user import User
from libs.database.engine import Session
from libs.route.login_required import login_required
from libs.route.router import route
from libs.status import Status


@route
def get_users():
    return [x.json(with_animal=False) for x in Session().query(User).all()], Status.HTTP_200_OK, \
           {'X-Total-Count': Session().query(User).count(),
            'access-control-expose-headers': 'X-Total-Count'}


