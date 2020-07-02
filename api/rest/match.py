from api.models.match import Match
from libs.database.engine import Session
from libs.route.router import route


@route
def get_soyeon_matches():
    '''
    '소연이 제안하는 인연' 을 조회합니다.
    '''

    Session().query(Match).filter()


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
