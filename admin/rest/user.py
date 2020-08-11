from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def confirm_registration(user_id):
    try:
        user = Session().query(User).filter((User.id == user_id)).one()
    except NoResultFound:
        raise ClientError(f'user #{user_id} not found', Status.HTTP_404_NOT_FOUND)
    user.registration_confirmed = True
    user.registration_confirmed_at = datetime.now()
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

