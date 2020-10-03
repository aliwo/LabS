from firebase_admin import messaging
from firebase_admin.messaging import Notification

from libs.route.errors import ServerError


class Notifier:

    def __init__(self, token=None, topic=None):
        if token is None and topic is None:
            raise ServerError('token 혹은 topic 이 필요합니다.')
        self.token = token
        self.topic = topic

    def make_message(self, body=None, notification=None):
        topic_or_token = self.topic if self.topic else self.token
        body = {} if not body else body
        notification = {} if not notification else notification
        return messaging.Message(
                    data=body,
                    notification=Notification(**notification),
                    token=topic_or_token,
                    apns=messaging.APNSConfig(
                    headers={'apns-push-type': 'background', 'apns-priority': '5'},
                    payload=messaging.APNSPayload(
                        aps=messaging.Aps(content_available=True)
                        # badge=Session().query(Notification).filter((Notification.to_user_id == self.target_user_id)
                        #                                            & (Notification.read == False)).count() + 1
                    )
                ))

    def notify(self, body=None, notification=None):
        '''
        body 는 모든 key 와 value 가 string 인 딕셔너리입니다.
        '''
        response = messaging.send(self.make_message(body=body, notification=notification))
        return response

