import json
import sys
import requests

from settings import BOT_ONLINE_ENDPOINT


def send_logged_in_message(caller_key, username, conversation_name):
    post_data = json.dumps({'username': username,
                            'key': caller_key,
                            'conversation_name': conversation_name})
    try:
        response = requests.post(BOT_ONLINE_ENDPOINT, data=post_data)
        return response
    except requests.exceptions.RequestException:
        print('Uable to contact HERON; exiting')
        sys.exit(1)
