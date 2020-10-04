import json
import os
import requests
from libs.route.errors import ServerError


def retrieve_gat():
    '''
    gat : google access token
    '''
    try:
        result = requests.post('https://www.googleapis.com/oauth2/v4/token', data={
            'client_id': os.environ.get('GOOGLE_OAUTH__CLIENT_ID'),
            'client_secret': os.environ.get('GOOGLE_OAUTH__CLIENT_SECRET'),
            'refresh_token': os.environ.get('GOOGLE_REFRESH_TOKEN'),
            'grant_type': 'refresh_token'
        })
        result = json.loads(result.content)
    except:
        raise ServerError(f'error while refreshing token')

    if result.get('error'):
        raise ServerError(f'{result}')

    return result
