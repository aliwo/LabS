from api.models.tiers.tier import Tier


class Ruby(Tier):

    @property
    def tier_range(self):
        return {'gte': 6} # gold ~
