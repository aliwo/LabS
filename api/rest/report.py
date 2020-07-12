from flask import g, request

from api.models.report import Report
from libs.database.engine import afr
from libs.route.router import route
from libs.status import Status


@route
def report():
    '''
    신고를 때립니다.
    '''
    afr(Report(from_user_id=g.user_session.user.id, to_user_id=request.json.get('user_id'),
               memo=request.json.get('memo')))
    return {'okay': True}, Status.HTTP_200_OK
