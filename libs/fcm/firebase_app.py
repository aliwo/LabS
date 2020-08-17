import os

import firebase_admin
from firebase_admin import credentials, messaging

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'firebase_key.json')
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

messaging.send(messaging.Message(data={
        'kind': 'TEST',
        'title': f'테스트용 title',
        'body': f'테스트용 body'
}, token=''))