from datetime import datetime, timedelta

from sqlalchemy.orm import aliased
from sqlalchemy.sql.expression import func
from api.models.match import Match
from api.models.star import Star
from api.models.user import User
from libs.database.engine import Session, afr
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
def generate_random_matches():
    user = Session().query(User).filter(
        (User.sex != g.user_session.user.sex)
        & (User.id.notin_(Match.matched_user_ids(g.user_session.user.id, Session())))).order_by(func.random()).limit(1).one()
    match = afr(Match(from_user_id=user.id, to_user_id=g.user_session.user.id, type_=Match.TYPE_RANDOM))
    Session().commit()
    return {'match': match.json()}, Status.HTTP_200_OK


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
def get_hearted_matches():
    '''
    당신에게 관심 있는 인연
    나 혹은 상대가 하트를 쏜 매치만 조회합니다.
    '''
    matches = Session().query(Match).filter((Match.to_user_id == g.user_session.user.id)
                                            & (Match.heart_id != None)).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_high_rated_matches():
    '''
    당신에게 높은 점수를 준 인연
    1. to_user_id 가 자신인 모든 Match 를 쿼리해서
    2. LEFT JOIN star ON star.to_user_id == Match.to_user_id
    3. WHERE star.rate >= 4.0
    4. 만약 내가 그 사람을 별 3개 이하로 줬다면 걸러야 한다.
    '''
    their_star = aliased(Star)
    my_star = aliased(Star)
    matches = Session().query(Match).join(their_star, their_star.to_user_id == Match.to_user_id)\
        .join(my_star, my_star.from_user_id == Match.to_user_id)\
        .filter((Match.to_user_id == g.user_session.user.id)
                & (their_star.rate >= 4.)
                & (my_star.rate >= 3.)).all()
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

