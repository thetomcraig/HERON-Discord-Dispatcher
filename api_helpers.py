import requests

heron_domain = '206.189.162.225:8000/bots/'


def send_heard_message(key, message, name=None):
    response = requests.post(heron_domain + 'message_received', data={'key': key, 'name': name, 'message': message})
    print(response)


def query_for_reply():
    response = requests.post(heron_domain + 'reply', data={})
    print(response)
