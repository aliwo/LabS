from collections import defaultdict

from libs.database.engine import SessionMaker
from api.models.animal_correlation import AnimalCorrelation
from api.models.user import User
from api.models.animal import Animal
from api.models.match import Match
from libs.elastic import es


session = SessionMaker()
memo = defaultdict(lambda: [])


def afr(*args):
    session.add_all(args)
    session.flush()

    if len(args) == 1:
        return args[0]

    return args

def gen_sy_matches():

    # 남자의 카드를 채웁니다.
    men = session.query(User).filter((User.sex == False)).all()
    for man in men:
        result = es.search(man.gen_query_body(session), index='sy-users')
        if not result['hits']['hits']:
            continue # 더 이상 매칭할 사람이 없다.
        for target in result['hits']['hits'][:2]: # 우선 순위 2명의 카드를 만듭니다.
            memo[man.id].append(int(target['_id']))
            memo[int(target['_id'])].append(man.id)
            afr(Match(from_user_id=man.id, to_user_id=target['_id'], type_=Match.TYPE_SOYEON))

    # 여자의 카드를 채웁니다.
    women = session.query(User).filter((User.sex == True)).all()
    for woman in women:
        if len(memo[woman.id]) >= 2:
            print(f'여자{woman.id}는 2장 찼음!')
        result = es.search(woman.gen_query_body(session), index='sy-users')
        for target in result['hits']['hits'][:2-len(memo[woman.id])]:
            memo[woman.id].append(int(target['_id']))
            memo[int(target['_id'])].append(woman.id)
            afr(Match(from_user_id=woman.id, to_user_id=target['_id'], type_=Match.TYPE_SOYEON))

    session.commit()

gen_sy_matches()
