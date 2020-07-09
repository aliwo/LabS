from sqlalchemy import case

from api.models.tiers.bronze import Bronze
from api.models.tiers.gold import Gold
from api.models.tiers.diamond import Diamond
from api.models.tiers.ruby import Ruby
from api.models.tiers.silver import Silver


TIER_BRONZE = 'BRONZE'
TIER_SILVER = 'SILVER'
TIER_GOLD = 'GOLD'
TIER_RUBY = 'RUBY'
TIER_DIAMOND = 'DIAMOND'


def load_tier(user, rate):
    '''
    클래스 이름을 전달받아 해당 클래스를 인스턴스화 해서 넘겨줍니다.
    '''
    if 0 <=  rate <= 2:
        return Bronze(user)
    elif 2 < rate <= 4:
        return Silver(user)
    elif 4 < rate <= 6:
        return Gold(user)
    elif 6 < rate <= 8:
        return Ruby(user)
    elif 8 < rate <= 10:
        return Diamond(user)


def tier_case(rate):
    return case([(rate <= 2, TIER_BRONZE),
                     (rate <= 4, TIER_SILVER),
                     (rate <= 6, TIER_GOLD),
                     (rate <= 8, TIER_RUBY),
                     (rate <= 10, TIER_DIAMOND),])

