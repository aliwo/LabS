from datetime import datetime, timedelta

from api.models.match import Match
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from flask import g, request

from libs.status import Status


@route
def get_soyeon_matches():
    '''
    '소연이 제안하는 인연' 을 조회합니다.
    '''
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_SOYEON)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_preference_matches():
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_PREFER)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_random_matches():
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_RANDOM)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_old_matches():
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                        & (Match.created_at <= (datetime.now() - timedelta(days=2)).date())).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_matched_matches():
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                            & (Match.matched == True)).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def open_match():
    try:
        match = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                            & (Match.id == request.json.get('match_id'))).one()
    except:
        raise ClientError('match not found or not your match', status_code=Status.HTTP_404_NOT_FOUND)
    match.opened = True
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

