import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello World!')

client.run('MTA4MTIzNDUwNTQ2Mjk3NjU4Mw.G7AxIk.x4DXW4vxK8xeihoqcaglgDo2uh__geZO3gvql8')
