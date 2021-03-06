from flask import g, request

from api.models.oauth.naver import OauthNaver
from api.models.user_point import UserPoint
from api.models.prerequisites.user_prerequisites import UserPrerequisites
from api.models.user import User
from api.models.user_session import UserSession
from libs.database.engine import Session, afr
from libs.datetime_helper import DateTimeHelper
from libs.route.prerequisite import prerequisites
from libs.route.router import route
from libs.status import Status

@route
@prerequisites(UserPrerequisites, 'naver')
def login_naver():
    g.info = g.info.get('response')
    oauth = Session().query(OauthNaver).filter(OauthNaver.party_id == g.info.get('id')).first()
    is_new = True if oauth is None else False

    if is_new:
        user = afr(User(email=g.info.get('email')))
        oauth = afr(OauthNaver(user, g.info))
        afr(UserPoint(user_id=user.id))

    user_session = UserSession(oauth.user, third_party_token=request.json.get('token'))
    Session(changed=True).add(user_session)

    return {'user_id':oauth.user.id, 'token': user_session.token, 'is_new': is_new, 'expiry': DateTimeHelper.full_datetime(user_session.expiry)}, Status.HTTP_200_OK

