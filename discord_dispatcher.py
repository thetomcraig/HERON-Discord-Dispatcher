import asyncio
import sys
import os

import discord

from api_helpers import send_logged_in_message
from local_settings import conversation_name


def run_bot(discord_key):

    key = discord_key
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in')
        send_logged_in_message(key, client.user.name, conversation_name)

    @client.event
    async def on_message(message):
        check_forever = True

        while(check_forever):
            # Check the fs to see if message exists
            reply = check_file_system_for_reply(client.user.name)
            if reply:
                await asyncio.sleep(2)
                await client.send_message(message.channel, reply)
            else:
                await asyncio.sleep(20)

    def check_file_system_for_reply(username):
        reply = None
        file_name = '/tmp/discord/{}.txt'.format(username)
        try:
            with open(file_name, 'r') as f:
                lines = f.readlines()
                if len(lines):
                    reply = lines[0]
                    os.remove(file_name)

        except Exception as e:
            print(e)

        return reply

    client.run(key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
