from api.models.tiers.tier import Tier


class Silver(Tier):

    @property
    def tier_queries(self):
        return []
