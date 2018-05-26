import json

import requests

from settings import BOT_ONLINE_ENDPOINT


def send_online_message(caller_key, username, conversation_name):
    post_data = json.dumps({'username': username,
                            'key': caller_key,
                            'conversation_name': conversation_name})

    response = requests.post(BOT_ONLINE_ENDPOINT, data=post_data)

    response_string = response.content.decode('utf-8')
    response_dict = json.loads(response_string)

    print('api helpers')
    print(response_dict['success'])

    return response
