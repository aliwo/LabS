from api.models.tiers.tier import Tier


class Diamond(Tier):

    @property
    def tier_range(self):
        return {'gte': 8} # ruby ~
