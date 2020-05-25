from libs.route.router import route
from libs.status import Status
from libs.storage import gcs
from flask import request

@route
def upload_image():
    file = request.files.get('image')
    return {'url': gcs.upload_file(file.read(), file.filename, file.content_type)}, Status.HTTP_200_OK
