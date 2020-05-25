from datetime import datetime
from functools import wraps

from libs.route.log import log_route
from libs.route.errors import BaseError


def route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            request_at = datetime.now()
            response_msg, status_code = func(*args, **kwargs)
            log_route(func.__name__, request_at, response_msg)
        except BaseError as e:
            response_msg, status_code = e.json(), e.status_code
        return response_msg, status_code
    return wrapper

