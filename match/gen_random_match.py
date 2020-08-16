from collections import defaultdict
from pprint import pprint

from sqlalchemy import func

from libs.database.engine import SessionMaker
from api.models.animal import Animal
from api.models.animal_correlation import AnimalCorrelation
from api.models.user import User
from api.models.oauth.google import OauthGoogle
from api.models.oauth.apple import OauthApple
from api.models.oauth.kakao import OauthKakao
from api.models.oauth.naver import OauthNaver
from api.models.match import Match
from api.models.heart import Heart
from libs.elastic import es


session = SessionMaker()


def afr(*args):
    session.add_all(args)
    session.flush()

    if len(args) == 1:
        return args[0]

    return args


def gen_random_matches():
    men = session.query(User).filter((User.sex == False) &
                                     (User.animal_id != None)).all()
    for man in men:
        for _ in range(2):
            woman = session.query(User).filter((User.sex == True)
                                       & (User.id.notin_(Match.matched_user_ids(man.id, session))))\
                                        .order_by(func.random()).first()
            afr(Match(from_user_id=man.id, to_user_id=woman.id, type_=Match.TYPE_RANDOM))
            afr(Match(to_user_id=man.id, from_user_id=woman.id, type_=Match.TYPE_RANDOM))


    women = session.query(User).filter((User.sex == True) &
                                     (User.animal_id != None)).all()
    for woman in women:
        for _ in range(2):
            man = session.query(User).filter((User.sex == False)
                                       & (User.id.notin_(Match.matched_user_ids(woman.id, session))))\
                                        .order_by(func.random()).first()
            afr(Match(from_user_id=man.id, to_user_id=woman.id, type_=Match.TYPE_RANDOM))
            afr(Match(to_user_id=man.id, from_user_id=woman.id, type_=Match.TYPE_RANDOM))


if __name__ == '__main__':
    random_match()
