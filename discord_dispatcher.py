import asyncio
import random
from time import sleep
import sys

import discord

from api_helpers import send_heard_message

timeout = 5
all_messages = []


def run_bot(discord_key):

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        """
        This function will loop, it sends a message,
        then gets called again when that message gets sent
        """
        print('client, got message')
        print(client.user.name)
        print(message.content)
        should_send_reply, reply = send_heard_message(
            client.user.id,
            message.author.name,
            message.channel.name,
            message.content)
        print('client, got response after sending heard')
        print(client.user.name)
        print(should_send_reply)
        print(reply)

        if should_send_reply:
            # Sleep for a random amount of time, then send the message
            # timeout = random.randrange(1, 10)
            print('Sleeping for 60')
            timeout = 6 + len(client.user.name)
            sleep(timeout)
            await client.send_message(message.channel, reply)

    client.run(discord_key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
