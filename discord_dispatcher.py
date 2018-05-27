import asyncio
import sys

import discord

from api_helpers import send_logged_in_message
from local_settings import conversation_name

timeout = 5


def run_bot(discord_key):

    client = discord.Client()
    key = discord_key

    @client.event
    async def on_ready():
        send_logged_in_message(key, client.user.name, conversation_name)

    async def send_reply(channel, reply):
        print('sending reply pt 1')
        await client.send_message(channel, reply)
        print('sending reply pt 2')

    client.run(discord_key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
