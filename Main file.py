import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

#bot ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(':)'))
    print ('Bot is ready.')

#add_event
@client.event
async def on_member_join():
    print (f'{member} has joined a server.')

#remove_event
@client.event
async def on_member_remove():
    print (f'{member} has left a server.')

#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#8ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'Outlook good',
                 'You may rely on it',
                 'Ask again later',
                 'Concentrate and ask again',
                 'Reply hazy, try again',
                 'My reply is no',
                 'My sources say no',
                 'Without a doubt',
                 'Very doubtful',
                 'Cannot predict now']

    await ctx.send(f'Question: {question} Answer: {random.choice(responses)}')


#clear   
@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

#kick
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

#say
@client.command()
async def say(ctx, *, text):
    await ctx.send(text)

#help
@client.command(invoke_without_command=True)
async def help(ctx):
    author = ctx.message.author
    em = discord.Embed(title = 'Help', description = 'Use .help <command> for extended usage.', color=0xFF5733)

    em.add_field(name = 'Moderation', value = "'kick', 'ban', 'clear'")
    em.add_field(name = 'Fun', value = "'8ball', 'say', 'roll'")
    em.add_field(name = 'Misc', value = "help = shows this message ,ping, invite")
    em.add_field(name = 'Calc', value = "add, sub, multi, div")
    await ctx.send(embed = em)

#roll
@client.command()
async def roll(ctx):
    responses = ['1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 '10']
    await ctx.send(f'You rolled: {random.choice(responses)}')

@client.command()
async def hi(ctx):
    await ctx.send('Hi, always ready to help! TYPE: .help for usage.')

#Adding
@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

#Subtracting
@client.command()
async def sub(ctx, left: int, right: int):
    """Subs two numbers together."""
    await ctx.send(left - right)

#Multi
@client.command()
async def multi(ctx, left: int, right: int):
    """multi two numbers together."""
    await ctx.send(left * right)

#Div
@client.command()
async def div(ctx, left: int, right: int):
    """multi two numbers together."""
    await ctx.send(left / right)

#Invite
@client.command()
async def invite(ctx):
    author = ctx.message.author
    em = discord.Embed(title = 'Invite', description = 'Use this to invite the bot.', color=0xFF5733)

    em.add_field(name = 'Link', value = "https://discord.com/api/oauth2/authorize?client_id=822074775483711488&permissions=8&scope=bot")
    await ctx.send(embed = em)



#token
client.run('TOKEN')
