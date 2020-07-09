from api.models.tiers.tier import Tier


class Bronze(Tier):

    @property
    def tier_queries(self):
        return [
            {'gt':2, 'lte':4, 'weight':10} # silver
        ]

