import requests
from flask import request

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
        더블 하트라면 지나갑니다.
        만약 일반 하트라면 accept 하는 유저가 포인트를 갖고 있는지 체크합니다.
        '''
