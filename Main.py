import discord, json, os
from discord.ext import commands
# from discord.utils import get
from datetime import date
from datetime import datetime
from random import randint

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents)
today1 = date.today()
hour1 = datetime.now()
hourString1 = hour1.strftime("%H:%M:%S")

logfile = open('log.txt', 'a')
logfile.write(f'Bot Started {today1} at {hourString1}\n')
logfile.close()

try:
    launchload = open("launches.json", "x")
    launchload.close()
    launchwrite = open("launches.json", "w")
    launch = {
        "launches": "1"
    }
    x = json.dumps(launch, indent=4)
    launchwrite.write(x)
    launchwrite.close()

    configload = open("config.json", "x")
    configload.close()
    configwrite = open("config.json", "w")
    config = {
        "token": "Input Token Here from https://discord.com/developers/applications/"
    }

    y = json.dumps(config, indent=4)
    configwrite.write(y)
    configwrite.close()
    print("CHANGE config.json TO HAVE YOUR BOT TOKEN FROM https://discord.com/developers/applications/")
except FileExistsError:
    print("Config File Already Exists")

with open("config.json", "r") as config:
    configloaded = json.load(config)

with open("launches.json", "r") as launch:
    launchp1 = json.load(launch)

launched = launchp1["launches"]
launchp1["launches"] = int(launched) + 1

with open("launches.json", "w") as out:
    out.write(json.dumps(launchp1, indent=4))


############

@bot.event
async def on_ready():
    today = date.today()
    hour = datetime.now()
    hourString = hour.strftime("%H:%M:%S")

    channel = bot.get_channel(742585460760772709)
    server = bot.get_guild(541332714880499735)
    user = bot.get_user(707318172780331068)
    embed = discord.Embed(
        title='Bot Started',
        description=f'Bot Started in: **{server}** \nBot User is: **{user}** \nLaunch #: **{launchp1["launches"]}**',
        color=discord.Color.green()
    )
    embed.set_footer(text=f'{today} at {hourString}')
    await channel.send(embed=embed)
    print("Bot Is Online")


############

@bot.command()
async def ping(ctx):
    apiping = int(bot.latency * 1000)
    apiembed = discord.Embed(
        title="API Ping",
        description=f'{apiping} ms',
        color=discord.Color.blurple()
    )
    await ctx.send(embed=apiembed)


############

@bot.command()
async def stop(ctx):
    today = date.today()
    hour = datetime.now()
    hourString = hour.strftime("%H:%M:%S")

    channel = bot.get_channel(742585460760772709)
    stopembed = discord.Embed(
        title='Bot Stopped',
        description=f'Bot Stopped at: {hourString} on {today}',
        color=discord.Color.dark_red()
    )
    await ctx.send("Stopping...")
    await channel.send(embed=stopembed)
    await bot.logout()
    with open('log.txt', 'a') as logfile1:
        logfile1.write(f'Bot Stopped {today} at {hourString}\n\n')
    print("Bot Offline")


############

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
        title='Purged Messages',
        description=f'Purged **{i}** Messages in **{channel}**',
        color=discord.Color.red()
    )
    purgeembed.set_footer(text=f'{today} at {hourString}')

    await channel.delete_messages(messages)
    await ctx.send('Purged Messages')
    await botlog.send(embed=purgeembed)


############

@bot.command()
async def dingus(ctx, whoisdingus, reason=None):
    dingusembed = discord.Embed(
        title='Dingus!',
        description=f'**{whoisdingus}** is a dingus!',
        color=0xc59200
    )
    if not reason:
        await ctx.send(embed=dingusembed)
    else:
        dingusembed.add_field(name='Reason:', value=f'{reason}', inline=True)
        await ctx.send(embed=dingusembed)


############

@bot.command()
async def flip(ctx):
    author = ctx.message.author.mention
    coinembed = discord.Embed(
        title='Coin Flip',
        description=f'{author} Flipped a coin and got:',
        color=0xA66969
    )

    coin = randint(0, 1)
    if coin == 1:
        coinembed.add_field(name="Heads!", value="\oo/", inline=True)
        await ctx.send(embed=coinembed)
    else:
        coinembed.add_field(name="Tails!", value="\oo/", inline=True)
        await ctx.send(embed=coinembed)


############

@bot.command()
async def profile(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
        joinDate = str(member.joined_at).split('.')
        createDate = str(member.created_at).split('.')

        userRolesList = []
        for i in list(member.roles):
            if "@everyone" in str(i):
                continue
            userRolesList.append(i.mention)
        userRoles = "".join(userRolesList)

        profileembed = discord.Embed(
            title=f'User Profile',
            description=f'{member.mention}\'s Profile \nUser ID: **{member}** \nUser Status: {member.status} \nUser Custom Status: \"{member.activity}\"',
            color=discord.Color.dark_green()
        )
        profileembed.add_field(name="Account Creation Date", value=f'**{createDate[0]} UTC**', inline=True)
        profileembed.add_field(name="Guild Join Date", value=f'**{joinDate[0]} UTC**', inline=True)
        profileembed.add_field(name='Roles:', value=userRoles, inline=False)
        profileembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=profileembed)
    else:
        joinDate = str(member.joined_at).split('.')
        createDate = str(member.created_at).split('.')

        userRolesList = []
        for i in list(member.roles):
            if "@everyone" in str(i):
                continue
            userRolesList.append(i.mention)
        userRoles = "".join(userRolesList)

        profileembed = discord.Embed(
            title=f'User Profile',
            description=f"{member.mention}\'s Profile \nUser ID: **{member}** \nUser Status: {member.status} \nUser Custom Status: \"{member.activity}\"",
            color=discord.Color.dark_green()
        )
        profileembed.add_field(name="Account Creation Date", value=f'**{createDate[0]} UTC**', inline=True)
        profileembed.add_field(name="Guild Join Date", value=f'**{joinDate[0]} UTC**', inline=True)
        profileembed.add_field(name='Roles:', value=userRoles, inline=False)
        profileembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=profileembed)


############

@bot.command(aliases=["info"])
async def about(ctx):
    infoembed = discord.Embed(
        title="About",
        description='',
        color=0x345678
    )
    infoembed.add_field(name="Bot Creator:", value="Stereo528#1225   ", inline=True)
    infoembed.add_field(name="Launch Number:", value=f'**{launchp1["launches"]}**', inline=False)
    infoembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/707318172780331068/f071b6a0c993ac524b261d50f7b403eb.webp?size=1024")
    await ctx.send(embed=infoembed)


############

@bot.command()
async def cape(ctx, username=None):
    if not username:
        errorembed = discord.Embed(
            title="Please Pass a Minecraft Username",
            color=0xff0000
        )
        await ctx.send(embed=errorembed)
    else:
        capeembed = discord.Embed(
        title='Cape',
        color=0xe29f00
        )
        capeembed.set_image(url=f"http://s.optifine.net/capes/{username}.png")
        await ctx.send(embed=capeembed)

###########




############

#Load Cogs

#@bot.command()
#async def load(ctx, extension):
#    bot.load_extension(f'cogs.{extension}')
#
#@bot.command()
#async def unload(ctx, extension):
#    bot.unload_extension(f'cogs.{extension}')
#
#
#for filename in os.listdir('./cogs/'):
#    if filename.endswith('.py'):
#        bot.load_extension(f'cogs.{filename[:-3]}')
        
############

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Unknown Command",
            color=0xff0000,
            description=f"The command `{ctx.message.content.split(' ')[0]}` is not found")
        await ctx.send(embed=embed)
        return

############


bot.run(configloaded["token"])
