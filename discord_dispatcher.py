import asyncio
import sys
import time

import discord

from api_helpers import get_new_message, send_logged_in_message
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
            asyncio.ensure_future(run_generator(client, message.channel))

    @asyncio.coroutine
    def run_generator(the_client, the_channel):
        """
        Generator continually checks if there is a new message to send
        """
        generator_on = True
        while(generator_on):
            reply = get_new_message(the_client.user.name)
            if reply:
                yield from the_client.send_message(the_channel, reply)
            time.sleep(sleep_time)

    # Run the whole ding dang thing
    client.run(key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
