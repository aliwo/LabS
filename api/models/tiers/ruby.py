from api.models.tiers.tier import Tier


class Ruby(Tier):

    @property
    def tier_queries(self):
        return []
