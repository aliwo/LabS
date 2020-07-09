from api.models.tiers.tier import Tier


class Bronze(Tier):

    @property
    def tier_range(self):
        return {'gte': 0, 'lt': 4} # bronze ~ silver


