import os
from flask import request, g

from api.models.prerequisites.sms_prerequisites import SmsPrerequisites
from api.models.sms_auth import SmsAuth
from api.models.user import User
from libs.database.engine import Session, afr
from libs.route.errors import ServerError, ClientError
from libs.route.prerequisite import prerequisites
from libs.route.router import route
from libs.sms import SmsHelper
from libs.status import Status


sms_helper = SmsHelper(os.environ.get('SY_TOAST_APP_KEY', ''), os.environ.get('SY_SMS_SENDER_NO', ''))


@route
def send_sms():
    '''
    문자 인증을 보냅니다.
    '''
    auth = afr(SmsAuth(g.user_session.user.id, request.json.get('phone_num')))
    result = sms_helper.send_auth_sms(auth)

    if not result.get('header').get('isSuccessful'):
        raise ServerError('could not send sms')

    Session().commit()
    return {'auth_key':str(auth.auth_key)}, Status.HTTP_200_OK


@route
@prerequisites(SmsPrerequisites, 'on_auth')
def auth_sms():
    '''
    문자 인증을 검사합니다.
    인증에 성공하면 해당 auth_key, value 는 소거합니다.
    '''
    sms_auth = g.pr_result.get('sms_auth')

    if sms_auth.auth_value != request.json.get('auth_value'):
        raise ClientError('invalid auth')

    if Session().query(User).filter((User.phone == sms_auth.phone_num)).first():
        raise ClientError('duplicate phone num', Status.HTTP_406_NOT_ACCEPTABLE)

    g.user_session.user.phone = sms_auth.phone_num
    g.user_session.user.phone_registered = True

    Session(changed=True).delete(sms_auth)
    return {'okay': True}, Status.HTTP_200_OK
