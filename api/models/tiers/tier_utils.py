from api.models.tiers.bronze import Bronze
from api.models.tiers.gold import Gold
from api.models.tiers.diamond import Diamond
from api.models.tiers.ruby import Ruby
from api.models.tiers.silver import Silver


def load_tier(user, name):
    '''
    클래스 이름을 전달받아 해당 클래스를 인스턴스화 해서 넘겨줍니다.
    '''
    if name == 'DIAMOND':
        return Diamond(user)
    if name == 'RUBY':
        return Ruby(user)
    if name == 'GOLD':
        return Gold(user)
    if name == 'SILVER':
        return Silver(user)
    return Bronze(user)

