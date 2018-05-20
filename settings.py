HERON_DOMAIN = 'http://127.0.0.1:8000'

from local_settings import *

MESSAGE_RECEIVED_ENDPOINT = '/'.join([HERON_DOMAIN, 'discord', 'message_received'])
REPLY_QUERY_ENDPOINT = '/'.join([HERON_DOMAIN, 'discord', 'reply_query'])
