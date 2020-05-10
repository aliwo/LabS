from functools import wraps
from flask import request
from libs.route.errors import ClientError
from libs.status import Status
from libs.database.engine import Session
from datetime import datetime
from api.models.user_session import UserSession

def login_required(func):
    '''
    주의! 반드시 @route 아래에 설치해야 합니다.
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)

        if token is None or len(token.split()) < 2:
            raise ClientError('Authorization: Bearer <token> not found')

        token = token.split()[1]

        user_session = UserSession.get_session(token)
        if user_session is None:
            return {'okay': False, 'msg': 'Access Denied'}, Status.HTTP_401_UNAUTHORIZED

        if user_session.is_expired():
            return {'okay':False, 'msg':'Session Expired'}, Status.HTTP_401_UNAUTHORIZED

        g.user_session = user_session
        g.user_session.user.last_access = datetime.now()
        Session(changed=True)

        ret = func(*args, **kwargs)
        return ret

    return decorated

