from libs.route.router import route
from match.gen_all import gen_all


@route
def gen_match():
    gen_all()
    return {'okay':True}


