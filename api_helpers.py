import json

import requests

from settings import MESSAGE_RECEIVED_ENDPOINT, REPLY_QUERY_ENDPOINT


def send_heard_message(caller_key, name, conversation_name, message):
    response = requests.post(MESSAGE_RECEIVED_ENDPOINT,
                             data=json.dumps({'name': name, 'conversation_name': conversation_name, 'message': message}))
    response_string = response.content.decode('utf-8')
    response_dict = json.loads(response_string)

    # The user who called this fn. should send the reply
    # If their key matches the one send back,
    # then they're the sender
    print('api helpers')
    print(response_dict['key'])
    should_send_reply = caller_key == response_dict['key']
    print(should_send_reply)
    print('\n')
    reply = response_dict['reply']

    return should_send_reply, reply


def query_for_reply():
    pass
    print(REPLY_QUERY_ENDPOINT)
    # This might not be needed
