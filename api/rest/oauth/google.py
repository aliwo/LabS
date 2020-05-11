# TODO: 설정 json 파일을 PVC 로 마운트 해야 하나?
from flask import request, g

from api.models.oauth.google import OauthGoogle
from api.models.user import User
from api.models.user_session import UserSession
from libs.database.engine import Session, afr
from libs.route.prerequisite import prerequisites
from libs.status import Status


@prerequisites(UserPrerequisites, 'google')
def login_google():
    oauth = Session().query(OauthGoogle).filter(OauthGoogle.party_id == g.info.get('id')).first()
    is_new = True if oauth is None else False

    if is_new:
        user = afr(User(email=g.info.get('email'), picture=g.info.get('picture')))
        oauth = afr(OauthGoogle(user, g.info))
        user.oauth_google_id = oauth.id

    user_session = UserSession(oauth.user, third_party_token=request.json.get('token'))
    Session(changed=True).add(user_session)

    return {'okay':True, 'user_id':oauth.user.id, 'token': user_session.token, 'is_new': is_new}, Status.HTTP_200_OK

