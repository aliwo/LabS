from api.models.tiers.tier import Tier


class Diamond(Tier):

    @property
    def tier_queries(self):
        return []
