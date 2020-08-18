import os

import firebase_admin
from firebase_admin import credentials, messaging

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'firebase_key.json')
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

# registration_token = 'cg0axMYwTG24eTpSX5MKn7:APA91bGkl40GfKMfoA1TgMYhsGjluZZxCew0I2uD32TQJxDRWCss-yKOt6K170Umna_Ctx87AqmAQnKdEPj2ywXkgKOz79GC8oVi7WcO-T_4RNHyVhtRbgk9ErpoJqHTmW1W8Kvt7-8G'
# message = messaging.Message(
#     data={
#         'score': '850',
#         'time': '2:45',
#     },
#     token=registration_token,
# )
# response = messaging.send(message)
# print('Successfully sent message:', response)
