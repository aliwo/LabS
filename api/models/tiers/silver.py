from api.models.tiers.tier import Tier


class Silver(Tier):

    @property
    def tier_range(self):
        return {'gte': 0, 'lt': 6} # bronze ~ gold
