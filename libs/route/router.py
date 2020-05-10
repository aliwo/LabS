from functools import wraps
from libs.route.errors import BaseError
from libs.route.login_required import login_required
from flask import jsonify
from flask import Response
import json


def route(self, func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response_msg, status_code = func(*args, **kwargs)
        except BaseError as e:
            response_msg, status_code = e.json(), e.code
        return Response(json.dumps(response_msg, ensure_ascii=False), status=status_code,
                        mimetype='application/json; charset=utf-8')

    return wrapper

