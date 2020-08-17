from firebase_admin import messaging
from libs.database.engine import Session


class Notifier:

    def __init__(self, token, target_user_id, topic=None):
        self.token = token
        self.topic = topic
        self.target_user_id = target_user_id

    def make_message(self, body):
        from api.models.notification import Notification

        if self.topic:
            return messaging.Message(data=body, topic=self.topic,
                apns=messaging.APNSConfig(
                    headers={'apns-push-type': 'background', 'apns-priority': '5'},
                    payload=messaging.APNSPayload(
                        aps=messaging.Aps(content_available=True),
                        badge=Session().query(Notification).filter((Notification.to_user_id == self.target_user_id)
                                                                   & (Notification.read == False)).count() + 1
                    )
                ))
        return messaging.Message(data=body, token=self.token,
                    apns=messaging.APNSConfig(
                    headers={'apns-push-type': 'background', 'apns-priority': '5'},
                    payload=messaging.APNSPayload(
                        aps=messaging.Aps(content_available=True),
                        badge=Session().query(Notification).filter((Notification.to_user_id == self.target_user_id)
                                                                   & (Notification.read == False)).count() + 1
                    )
                ))

    def notify(self, body, log=True):
        '''
        body 는 모든 key 와 value 가 string 인 딕셔너리입니다.
        '''
        response = messaging.send(self.make_message(body))

        if log:
            print(f'FCM 전송 - {body} : response = {response}')
        return response

