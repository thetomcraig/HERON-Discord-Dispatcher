import asyncio
import sys
import os
import time
from datetime import datetime
from threading import Thread

import discord

from api_helpers import send_logged_in_message
from local_settings import conversation_name


def run_bot(discord_key):

    key = discord_key
    client = discord.Client()
    loop = asyncio.get_event_loop()
    client.started = False

    @client.event
    async def on_ready():
        print(client.user.name)
        print('Logged in')
        send_logged_in_message(key, client.user.name, conversation_name)

    @client.event
    async def on_message(message):
        if not client.started:
            client.started = True
            asyncio.ensure_future(loop_and_send(client, message.channel))
            loop.run_forever()
        print('ON MESSAGE DONE')

    @asyncio.coroutine
    def loop_and_send(the_client, the_channel):
        """
        Generator continually checks if there is a new message to send
        """

        while(True):
            print('looping')
            reply = check_file_system_for_reply(the_client.user.name)
            if reply:
                success = yield from the_client.send_message(the_channel, reply)
                print('success')
                print(success)
            time.sleep(5)

    def check_file_system_for_reply(username):
        reply = None
        safe_username = username.replace(' ', '_')
        file_name = '/tmp/discord/{}.txt'.format(safe_username)
        try:
            with open(file_name, 'r') as f:
                lines = f.readlines()
                if len(lines):
                    reply = lines[0]
                    os.remove(file_name)
            print('got reply:')

        except Exception as e:
            print('No file found')

        print('got reply:')
        print(reply)
        return reply

    # Run the whole ding dang thing
    client.run(key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
