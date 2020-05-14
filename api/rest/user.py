from sqlalchemy.orm.exc import NoResultFound

from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.status import Status


def get_user_profile(user_id):
    if user_id is None:
        raise ClientError(f'No User Found id #{user_id}', status_code=Status.HTTP_404_NOT_FOUND)

    try:
        user = Session().query(User).filter((User.id == user_id)).one()
    except NoResultFound:
        raise ClientError(f'No User Found id #{user_id}', status_code=Status.HTTP_404_NOT_FOUND)

    return {'user': user.json()}, Status.HTTP_200_OK


def put_user_profile():
    pass
