import json

import requests

heron_domain = '206.189.162.225:8000/bots/'
heron_domain = 'http://127.0.0.1:8000/discord/'


def send_heard_message(key, conversation_name, message):
    response = requests.post(heron_domain + 'message_received/',
                             data=json.dumps({'key': key, 'conversation_name': conversation_name, 'message': message}))
    response_string = response.content.decode('utf-8')
    response_dict = json.loads(response_string)
    return response_dict.get('message')


def query_for_reply():
    response = requests.post(heron_domain + 'reply', data={})
    print(response)
    url(r'^get_group_conversation/$', api_views.get_group_conversation),
