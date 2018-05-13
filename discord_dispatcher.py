import asyncio
import random
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
        tmp = await client.send_message(message.channel, 'Calculating messages...')

        response = send_heard_message(
            client.user.id,
            message.channel.name,
            message.content)

        await client.edit_message(tmp, response)

        # Sleep for a random amount of time, then send the message
        # timeout = random.randrange(1, 10)
        timeout = 60
        await asyncio.sleep(timeout)
        await client.send_message(message.channel, response)

    client.run(discord_key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
