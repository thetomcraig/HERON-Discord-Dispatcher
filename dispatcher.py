import asyncio
import random

import discord

from local_settings import discord_key


class Bot():

    def __init__(self, name):
        self.name = name
        self.client = discord.Client()

        self.timeout = 5
        self.all_messages = []

        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        @self.client.event
        async def on_message(message):
            """
            This function will loop, it sends a message,
            then gets called again when that message gets sent
            """
            tmp = await self.client.send_message(message.channel, 'Calculating messages...')

            response = self.get_response(message)

            await self.client.edit_message(tmp, response)

            # Sleep for a random amount of time, then send the message
            timeout = random.randrange(1, 10)
            await asyncio.sleep(timeout)
            print('here')
            await self.client.send_message(message.channel, response)
        self.client.run(discord_key)

        self.client.send_message(self.client.channel, 'test')

    def get_response(self, message):
        """
        Send the message to the backend
        The backend will generate a response and save it to the database, then return it
        """
        # r = requests.get('API_ENDPOINT')
        # Do some corner case checking.. is this the first message?
        #  counter = 0
        #  tmp = await client.send_message(message.channel, 'Calculating messages...')
        #  async for log in client.logs_from(message.channel, limit=100):
        #  if log.author == message.author:
        #  counter += 1
        # Maybe look at all the previous messsages?
        self.all_messages.extend(message.content)
        return 'test hi'


anger_bot = Bot('angry_bot')
