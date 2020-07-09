from api.models.tiers.tier import Tier


class Gold(Tier):

    @property
    def tier_range(self):
        return {'gte': 2, 'lt': 8} # silver ~ ruby
