import discord
from discord.ext import tasks, commands
import random

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(712996600573722657)
    await channel.send('Words Of Inches Has Awoken')

@client.event
async def on_member_join(member):
    channel = client.get_channel(712996600573722657)
    fmt = 'Welcome {0.mention} to The Holy Church of the Inch God!'
    await channel.send(fmt.format(member))

@tasks.loop(minutes=30)
async def message_of_the_day():
    channel = client.get_channel(712996600573722657)
    msg = ['Pollute not thy mind with the heresy of false gods', 'Thou shall respect all living things that have sprung up from the seed of the great Heyrosa (except Kpop stans they are an abomination unto the great Lord)']
    await channel.send(msg[random.randint(0,1)])

client.run('token')