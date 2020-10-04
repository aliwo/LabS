import os

import requests
from flask import request

from api.models.heart_recharge import HeartRecharge
from api.models.prerequisites.helper import PrerequisitesHelper
from api.models.prerequisites.prerequisites import Prerequisites
from libs.route.errors import ClientError
from libs.status import Status
from libs.util import retrieve_gat

helper = PrerequisitesHelper(HeartRecharge, 'json')


class HeartRechargePrerequisites(Prerequisites):

    base_model = HeartRecharge

    def google(self):
        '''
        1. DB 로 부터 refresh token 을 긁어옵니다.
        2. refresh token 으로 access token 을 얻습니다.
        3. 영수증 검증
        '''
        if not os.environ.get('GOOGLE_REFRESH_TOKEN', ''):
            print('refresh token 이 없으므로 검증 생략!')
            return

        access_token = retrieve_gat().get('access_token')
        result = requests.get(f'https://www.googleapis.com/androidpublisher/v3/applications/'
                              f'buv.co.kr/purchases/products/{request.json.get("google_sku")}/'
                              f'tokens/{request.json.get("google_purchase_token")}'
                              f'?access_token={access_token}')
        if result.json().get('purchaseState') != 0:
            # https://blog.totu.dev/2016/02/10/google-oauth/
            raise ClientError('invalid google inapp purchase', Status.HTTP_400_BAD_REQUEST)


    def apple(self):
        pass