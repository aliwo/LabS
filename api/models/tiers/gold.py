from api.models.tiers.tier import Tier


class Gold(Tier):

    @property
    def tier_queries(self):
        return []
