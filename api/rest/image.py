from api.models.pic import Pic
from libs.database.engine import afr, Session
from libs.route.router import route
from libs.status import Status
from libs.storage import gcs
from flask import request, g


@route
def upload_image():
    '''
    삭제된 유저가 bucket  에 남긴 사진은 나중에 수동으로라도 지울 수 있도록 기록을 납깁니다.
    2020-08-19
    '''
    file = request.files.get('image')
    url = gcs.upload_file(file.read(), file.filename, file.content_type)
    afr(Pic(user_id=g.user_session.user.id, url=url))
    Session().commit()
    return {'url': url}, Status.HTTP_200_OK
