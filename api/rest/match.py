from datetime import datetime, timedelta

from api.models.match import Match
from libs.database.engine import Session
from libs.route.router import route
from flask import g

from libs.status import Status


@route
def get_soyeon_matches():
    '''
    '소연이 제안하는 인연' 을 조회합니다.
    '''
    matches = Match.same_sex_query(Session(), g.user_session.user).filter((Match.type_ == Match.TYPE_SOYEON)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_preference_matches():
    matches = Match.same_sex_query(Session(), g.user_session.user).filter((Match.type_ == Match.TYPE_PREFER)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_old_matches():
    matches = Match.same_sex_query(Session(), g.user_session.user).filter((Match.created_at <= (datetime.now() - timedelta(days=2)).date())).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_random_matches():
    matches = Match.same_sex_query(Session(), g.user_session.user).filter((Match.type_ == Match.TYPE_RANDOM)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_matched_matches():
    matches = Match.same_sex_query(Session(), g.user_session.user).filter((Match.matched == True)).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK

