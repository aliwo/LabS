from datetime import datetime

from api.models.user_session import UserSession
from libs.database.engine import Session


def get_or_create_admin_session(admin):
    user_session = Session().query(UserSession).filter((UserSession.admin == True)
                                        & (UserSession.expiry >= datetime.now())
                                        & (UserSession.user_id == admin.user_id)).first()

    if user_session is None:
        user_session = UserSession(admin.user, admin=True)
        Session().add(user_session)
        Session().flush()

    return user_session
