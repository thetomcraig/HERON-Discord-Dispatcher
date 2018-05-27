import json

import requests

from settings import BOT_ONLINE_ENDPOINT


def send_logged_in_message(caller_key, username, conversation_name):
    post_data = json.dumps({'username': username,
                            'key': caller_key,
                            'conversation_name': conversation_name})

    response = requests.post(BOT_ONLINE_ENDPOINT, data=post_data)

    return response
