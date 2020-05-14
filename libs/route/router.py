from functools import wraps
from libs.route.errors import BaseError
from flask import jsonify
from flask import Response
import json


def route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response_msg, status_code = func(*args, **kwargs)
        except BaseError as e:
            response_msg, status_code = e.json(), e.status_code
        return response_msg, status_code
    return wrapper

