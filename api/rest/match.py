from libs.database.engine import Session


@route
def get_soyeon_match():
    '''
    '소연이 제안하는 인연' 을 만들어 냅니다.

    1. match 들을 쿼리해서 아직 due 가 지나지 않았다면 새로 만들지 않고 있는 매치를 리턴합니다.
    TODO: due 가 지난 카드는 '지난 인연' 에 쌓입니다.
    2. due 가 지났다면 새로운 match 를 생성합니다.
    '''

    Session().query()
