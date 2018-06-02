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
    reply = None

    try:
        post_data = format_post_data(caller_key, username, conversation_name)
        response = requests.post(MESSAGE_QUERY_ENDPOINT, data=post_data)
        response_dict = response.json()
        should_send = response_dict.get('should_send')
        if should_send:
            reply = response_dict.get('message')
    except requests.exceptions.RequestException:
        print('Uable to contact HERON; exiting')
    finally:
        return reply
