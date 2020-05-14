from flask import request
from sqlalchemy.orm.exc import NoResultFound

from libs.database.engine import Session
from libs.status import Status
from api.models.sms_auth import SmsAuth
from api.models.prerequisites.helper import PrerequisitesHelper
from api.models.prerequisites.prerequisites import Prerequisites


helper = PrerequisitesHelper(SmsAuth, 'json')


class SmsPrerequisites(Prerequisites):

    base_model = SmsAuth

    def on_auth(self):
        self.result['sms_auth'] = helper.must_one(Session().query(SmsAuth).filter(
            (SmsAuth.auth_key == request.json.get('auth_key'))))
