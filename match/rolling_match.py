from collections import defaultdict
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
memo = defaultdict(lambda: [])


def afr(*args):
    session.add_all(args)
    session.flush()

    if len(args) == 1:
        return args[0]

    return args


def rolling_match(query_name, match_type):
    '''
    남자를 먼저 순회하고, 여자를 순회하는 방식의 매칭입니다.
    양방향 매칭을 생성합니다.
    sy_match 와 preference_match 가 이에 해당합니다.
    '''
    print()
    print(f'rolling match {query_name}')
    print('---------------------------')
    men = session.query(User).filter((User.sex == False) &
                                     (User.animal_id != None)).all()
    for man in men:
        result = es.search(getattr(man, query_name)(session), index='sy-users')
        if not result['hits']['hits']:
            continue # 더 이상 매칭할 사람이 없다.
        for target in result['hits']['hits'][:2]: # 우선 순위 2명의 카드를 만듭니다.
            memo[man.id].append(int(target['_id']))
            memo[int(target['_id'])].append(man.id)
            afr(Match(from_user_id=man.id, to_user_id=target['_id'], type_=match_type))
            afr(Match(to_user_id=man.id, from_user_id=target['_id'], type_=match_type))
            print(f'남자{man.id} 와 여자{target["_id"]} 연결')

    # 여자의 카드를 채웁니다.
    women = session.query(User).filter((User.sex == True)&
                                     (User.animal_id != None)).all()
    for woman in women:
        if len(memo[woman.id]) >= 2:
            continue
        result = es.search(getattr(woman, query_name)(session), index='sy-users')
        for target in result['hits']['hits'][:2-len(memo[woman.id])]:
            memo[woman.id].append(int(target['_id']))
            memo[int(target['_id'])].append(woman.id)
            afr(Match(from_user_id=target['_id'], to_user_id=woman.id, type_=match_type))
            afr(Match(to_user_id=target['_id'], from_user_id=woman.id, type_=match_type))
            print(f'여자{woman.id} 와 남자{target["_id"]} 연결')

    session.commit()

