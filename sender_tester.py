import discord

import sleep

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # Send api - this is me, and I heard this message
    sleep(5)
# send api, can I reply?
# if no, return
# if yes, return the text sent
    await client.send_message(message.channel, 'Test')

client.run('NDEyMzAzNDM2OTk1MTAwNjgy.DWIYng._QQ4-O3teZmuO42S92bDLiYi6mg')
