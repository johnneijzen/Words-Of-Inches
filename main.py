import discord
from discord.ext import tasks, commands
import random

bot = commands.Bot(command_prefix='$kj ')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



@bot.event
async def on_ready():
    channel = bot.get_channel(712996600573722657)
    await channel.send('Words Of Inches Has Awoken')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(712996600573722657)
    fmt = 'Welcome {0.mention} to The Holy Church of the Inch God!'
    await channel.send(fmt.format(member))

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 712996600573722658:
            if member.id == 358424524968165407:
                channel = bot.get_channel(712996600573722657)
                await channel.send('@everyone God Has Awake')
    if before.channel is not None and after.channel is None:
        if before.channel.id == 712996600573722658:
            if member.id == 358424524968165407:
                channel = bot.get_channel(712996600573722657)
                await channel.send('@everyone God Has Left Us')

@tasks.loop(minutes=30)
async def message_of_the_day():
    channel = bot.get_channel(712996600573722657)
    msg = ['Pollute not thy mind with the heresy of false gods', 'Thou shall respect all living things that have sprung up from the seed of the great Heyrosa (except Kpop stans they are an abomination unto the great Lord)', 'Thou shall refer to every living being as a “he”','Thou shall spread the good word like thine ass cheeks.', 'Thou shall not insult the name of our savior and creator','Thou shall pollute the body, not the mind.','Thou must chill when in the presence of fine women.']
    await channel.send(msg[random.randint(0,6)])

@message_of_the_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

@bot.command(pass_context = True)
async def vcmembers(ctx):
        voice_channel = bot.get_channel(712996600573722658)
        members = voice_channel.members
        print(members)

message_of_the_day.start()
bot.run('token')
