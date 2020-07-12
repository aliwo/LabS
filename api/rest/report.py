from flask import g, request

from api.models.report import Report
from api.models.user import User
from libs.database.engine import afr, Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def report():
    '''
    신고를 때립니다.
    '''
    user = Session().query(User).filter((User.id == request.json.get('user_id'))).one_or_none()
    if user is None:
        raise ClientError(f'No User Found id #{request.json.get("user_id")}', status_code=Status.HTTP_404_NOT_FOUND)

    afr(Report(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'),
               memo=request.json.get('memo')))
    return {'okay': True}, Status.HTTP_200_OK
