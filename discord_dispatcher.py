import asyncio
import sys
import os
import time
from datetime import datetime

import discord

from api_helpers import send_logged_in_message
from local_settings import conversation_name


def run_bot(discord_key):

    key = discord_key
    client = discord.Client()

    @client.event
    async def on_ready():
        print(client.user.name)
        print('Logged in')
        send_logged_in_message(key, client.user.name, conversation_name)

    #  @client.event
    #  async def on_message(message):
        #  if (message.author.name == client.user.name):
            #  print('Will not respond to my own message')
            #  # Ignore your own messages
            #  return

        #  # Check the fs to see if message exists
        #  reply = check_file_system_for_reply(client.user.name)
        #  # DEBUG
        #  if reply:
            #  await client.send_message(message.channel, reply)
            #  print('will sleep 20')
            #  await asyncio.sleep(20)
        #  else:
            #  print('will sleep 2')
            #  await asyncio.sleep(2)

        #  print('done sleeping')
        #  print(datetime.now())
    @client.event
    async def on_message(message):
        print('setting channel')
        await run_generator(client, message.channel)

    async def run_generator(the_client, the_channel):
        check_forever = True

        while(check_forever):
            print('will sleep 20')
            time.sleep(20)

            print('done sleeping')
            print(datetime.now())
            reply = str(datetime.now())
            await the_client.send_message(the_channel, reply)

    def check_file_system_for_reply(username):
        reply = None
        safe_username = username.replace(' ', '_')
        print('/tmp/discord/{}.txt'.format(safe_username))
        file_name = '/tmp/discord/{}.txt'.format(safe_username)
        try:
            with open(file_name, 'r') as f:
                print('File found')
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

    client.run(key)


if __name__ == "__main__":
    run_bot(sys.argv[1])
