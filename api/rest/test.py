from libs.route.router import route
from libs.status import Status
from match.gen_all import gen_all


@route
def gen_match():
    gen_all()
    return {'okay':True}, Status.HTTP_200_OK


