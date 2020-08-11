class QueryStrategy:

    def __init__(self, user):
        self.user = user

    def gen_sy_query(self, session):
        from api.models.match import Match

        matched_user_ids = list(set([x.to_user_id for x in session.query(Match).filter((Match.from_user_id == self.user.id))] + \
        [x.from_user_id for x in session.query(Match).filter((Match.to_user_id == self.user.id))]))

        acquaintance = self.user.acquaintance if self.user.acquaintance_shy else []

        return {
            'query': {
                'function_score': {
                    'query': {
                        'bool': {
                            'must': [
                                {'term': {'sex': not self.user.sex}},
                                {'terms': {'location': [self.user.location1, self.user.location2]}},
                                {'range': {'rate': self.user.tier.tier_range}}
                            ],
                            'must_not': [
                                {'terms': {'_id': matched_user_ids }}, # 빈 배열이어도 정상동작 확인 2020-06-29
                                {'terms': {'phone': acquaintance }}
                            ],
                            'should': [{
                                'bool': {
                                    'must_not': {
                                        'exists': {
                                            'field': 'frozen_until'
                                        }
                                    }
                                }
                            },{
                                'range': {
                                    'frozen_until': {
                                        'lte': 'now/d',
                                        'time_zone': '+09:00'
                                    }
                                }
                            }],
                            'minimum_should_match': 1
                        }
                    } ,
                    'boost': '5',
                    'functions': [
                        {
                            'filter': { 'terms': {'animal_id': list(x.to_animal_ids)} },
                            'weight': x.weight
                        } for x in self.user.animal.correlations
                    ]
                }
            }
        }

    def gen_preference_query(self, session):
        from api.models.match import Match

        matched_user_ids = [x.from_user_id for x in session.query(Match).filter((Match.to_user_id == self.user.id))]

        return {
            'query': {
                'function_score': {
                    'query': {
                        'bool': {
                            'must': [
                                {'term': {'sex': not self.user.sex}},
                                {'terms': {'type_group_id': list(self.user.ideal_type_groups)}}
                            ],
                            'must_not': [
                                {'terms': {'_id': matched_user_ids}} # 빈 배열이어도 정상동작 확인 2020-06-29
                            ],
                            'should': [{
                                'bool': {
                                    'must_not': {
                                        'exists': {
                                            'field': 'frozen_until'
                                        }
                                    }
                                }
                            },{
                                'range': {
                                    'frozen_until': {
                                        'lte': 'now/d',
                                        'time_zone': '+09:00'
                                    }
                                }
                            }],
                            'minimum_should_match': 1
                        }
                    } ,
                    'boost': '5'
                }
            }
        }