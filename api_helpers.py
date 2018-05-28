import json
import sys
import requests

from settings import BOT_ONLINE_ENDPOINT, MESSAGE_QUERY_ENDPOINT


def format_post_data(caller_key, username, conversation_name):
    post_data = json.dumps({'username': username,
                            'key': caller_key,
                            'conversation_name': conversation_name})
    return post_data


def send_logged_in_message(caller_key, username, conversation_name):
    post_data = format_post_data(caller_key, username, conversation_name)
    try:
        response = requests.post(BOT_ONLINE_ENDPOINT, data=post_data)
        return response
    except requests.exceptions.RequestException:
        print('Uable to contact HERON; exiting')
        sys.exit(1)


def get_new_message(caller_key, username, conversation_name):
    post_data = format_post_data(caller_key, username, conversation_name)
    try:
        response = requests.post(MESSAGE_QUERY_ENDPOINT, data=post_data)
# READ THE MESSAGE FROM THE RESPONSE OBJ HERE AND SEND BACK TO DISPATCHER
        return response
    except requests.exceptions.RequestException:
        print('Uable to contact HERON; exiting')
