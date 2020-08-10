import requests
from flask import request, g

from api.models.heart import Heart
from api.models.heart_recharge import HeartRecharge
from api.models.match import Match
from api.models.user_point import UserPoint
from libs.database.engine import Session
from api.models.prerequisites.helper import PrerequisitesHelper
from api.models.prerequisites.prerequisites import Prerequisites


helper = PrerequisitesHelper(UserPoint, 'json')


class HeartPrerequisites(Prerequisites):

    base_model = UserPoint
    # TODO 하트 보낼때 hp 감소하도록 수정할 것

    def heart(self):
        '''
        heart 를 보낼 만큼의 포인트를 갖고 있는지 확인합니다.
        '''
        from_match = helper.must_one(Session().query(Match).filter((Match.id == request.json.get('match_id'))))
        helper.must_mine(g.user_session.user, from_match, foreign_value=from_match.to_user_id)
        self.result['from_match'] = from_match

    def double_heart(self):
        '''
        '''
        from_match = helper.must_one(Session().query(Match).filter((Match.id == request.json.get('match_id'))))
        helper.must_mine(g.user_session.user, from_match, foreign_value=from_match.to_user_id)
        self.result['from_match'] = from_match

    def accept(self):
        '''
        자기한테 온 하트가 맞는지 체크합니다.
        더블 하트라면 지나갑니다.
        만약 일반 하트라면 accept 하는 유저가 포인트를 갖고 있는지 체크합니다.
        '''
        heart = Session().query(Heart).filter((Heart.id == request.json.get('heart_id'))).one()
        helper.must_mine(g.user_session.user, heart)
        self.result['heart'] = heart
