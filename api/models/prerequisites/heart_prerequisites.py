import requests
from flask import request, g

from api.models.heart import Heart
from api.models.heart_recharge import HeartRecharge
from api.models.user_point import UserPoint
from libs.database.engine import Session
from api.models.prerequisites.helper import PrerequisitesHelper
from api.models.prerequisites.prerequisites import Prerequisites


helper = PrerequisitesHelper(UserPoint, 'json')


class HeartPrerequisites(Prerequisites):

    base_model = UserPoint

    def heart(self):
        '''
        heart 를 보낼 만큼의 포인트를 갖고 있는지 확인합니다.
        '''

    def double_heart(self):
        '''
        '''

    def accept(self):
        '''
        자기한테 온 하트가 맞는지 체크합니다.
        더블 하트라면 지나갑니다.
        만약 일반 하트라면 accept 하는 유저가 포인트를 갖고 있는지 체크합니다.
        '''
        heart = Session().query(Heart).filter((Heart.id == request.json.get('heart_id'))).one()
        helper.must_mine(g.user_session.user, heart)
        self.result['heart'] = heart