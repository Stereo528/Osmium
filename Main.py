import asyncio
import discord
from discord.ext import commands
from datetime import date
from datetime import datetime

bot = commands.Bot(command_prefix='.')
today1 = date.today()
hour1 = datetime.now()
hourString1 = hour1.strftime("%H:%M:%S")


logfile = open('log.txt', 'a')
logfile.write(f'Bot Started {today1} at {hourString1}\n')
logfile.close()


############################################################################################################################

@bot.event
async def on_ready():
    today = date.today()
    hour = datetime.now()
    hourString = hour.strftime("%H:%M:%S")

    channel = bot.get_channel(742585460760772709)
    server = bot.get_guild(541332714880499735)
    user = bot.get_user(707318172780331068)
    embed = discord.Embed(
        title = 'Bot Started',
        description = f'Bot Started in: **{server}** \nBot User is: **{user}**',
        color = discord.Color.green()
    )
    embed.set_footer(text=f'{today} at {hourString}')
    await channel.send(embed=embed)

    

############################################################################################################################

@bot.command()
async def ping(ctx):
    apiping = int(bot.latency * 1000)
    apiembed = discord.Embed(
        title = "API Ping",
        description = f'{apiping} ms',
        color = discord.Color.blurple()
    )
    await ctx.send(embed=apiembed)

############################################################################################################################

@bot.command()
async def stop(ctx):
    today = date.today()
    hour = datetime.now()
    hourString = hour.strftime("%H:%M:%S")

    channel = bot.get_channel(742585460760772709)
    stopembed = discord.Embed(
        title = 'Bot Stopped',
        description = f'Bot Stopped at: {hourString} on {today}',
        color = discord.Color.red()
    )
    await ctx.send("Stopping...")
    await channel.send(embed=stopembed)
    await bot.logout()
    logfile = open('log.txt', 'a')
    logfile.write(f'Bot Stopped {today} at {hourString}\n\n')
    logfile.close()


############################################################################################################################

@bot.command()
async def purge(ctx, i):
    today = date.today()
    hour = datetime.now()
    hourString = hour.strftime("%H:%M:%S")

    i = int(i)
    channel = ctx.message.channel
    botlog = bot.get_channel(742585460760772709)
    messages = []

    async for message in channel.history(limit=i):
        messages.append(message)
    
    purgeembed = discord.Embed(
        title = 'Purged Messages',
        description = f'Purged **{i}** Messages in **{channel}**',
        color = discord.Color.dark_red()
    )
    purgeembed.set_footer(text=f'{today} at {hourString}')

    await channel.delete_messages(messages)
    await ctx.send('Purged Messages')
    await botlog.send(embed=purgeembed)


############################################################################################################################

@bot.command()
async def dingus(ctx, whoisdingus, reason=None):
    author = ctx.message.author.mention
    dingusembed = discord.Embed(
        title='Dingus!', 
        description=f'**{whoisdingus}** is a fucking dingus!', 
        color=0xc59200
    )
    if not reason:
        await ctx.send(embed=dingusembed)
    else:
        dingusembed.add_field(name='Reason:', value=f'{reason}', inline=True)
        await ctx.send(embed=dingusembed)

############################################################################################################################


bot.run(TOKEN)
