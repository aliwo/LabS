from datetime import datetime, timedelta

from api.models.match import Match
from libs.database.engine import Session
from libs.route.router import route
from flask import g
from sqlalchemy import or_

from libs.status import Status


@route
def get_soyeon_matches():
    '''
    '소연이 제안하는 인연' 을 조회합니다.
    '''

    matches = Session().query(Match).filter(or_(Match.from_user_id == g.user_session.user.id
                                      , Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_SOYEON)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()

    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_preference_matches():
    '''
    '''

    Session().query()


@route
def get_old_matches():
    '''
    '''

    Session().query()
