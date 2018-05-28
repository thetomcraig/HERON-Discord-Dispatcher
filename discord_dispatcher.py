import asyncio
import sys
import os
import time

import discord

from api_helpers import send_logged_in_message
from local_settings import conversation_name, sleep_time


def run_bot(discord_key):

    key = discord_key
    client = discord.Client()
    client.generator_started = False

    @client.event
    async def on_ready():
        print(client.user.name)
        print('Logged in')
        send_logged_in_message(key, client.user.name, conversation_name)

    @client.event
    async def on_message(message):
        if not client.generator_started:
            client.generator_started = True
            asyncio.ensure_future(loop_and_send(client, message.channel))

    @asyncio.coroutine
    def loop_and_send(the_client, the_channel):
        """
        Generator continually checks if there is a new message to send
        """
        generator_on = True
        while(generator_on):
            reply = check_file_system_for_reply(the_client.user.name)
            if reply:
                yield from the_client.send_message(the_channel, reply)
            time.sleep(sleep_time)

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

        except Exception as e:
            print('No file found')

        return reply

    # Run the whole ding dang thing
    client.run(key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
