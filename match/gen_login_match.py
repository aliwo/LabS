from api.models.match import Match
from libs.elastic import es


def gen_login_matches(user, session, query_name, match_type):
    result = es.search(getattr(user, query_name)(session), index='sy-users')
    if not result['hits']['hits']:
        print(f'유저 #{user.id} hit 없음')
    for target in result['hits']['hits'][:2]:  # 우선 순위 2명의 카드를 만듭니다.
        Match(from_user_id=user.id, to_user_id=target['_id'], type_=match_type)
        Match(to_user_id=user.id, from_user_id=target['_id'], type_=match_type)

    session.commit()
