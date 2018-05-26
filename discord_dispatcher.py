import asyncio
import random
from time import sleep
import sys

import discord

from api_helpers import send_online_message

timeout = 5
all_messages = []
conversation_name = 'general'


def run_bot(discord_key):

    client = discord.Client()
    key = discord_key

    @client.event
    async def on_ready():
        send_online_message(key, client.user.name, conversation_name)

    async def send_reply(channel, reply):
        await client.send_message(channel, reply)

    client.run(discord_key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
