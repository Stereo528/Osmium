import discord, json, os
from discord.ext import commands
from datetime import date
from datetime import datetime
from config import token

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)


############

# Load Cogs

@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == OwnerId:
        bot.load_extension(f'commands.{extension}')
        await ctx.send(f"loaded {extension}")
    else:
        await ctx.send(embed=NoPermsEmbed("Bot Owner"))


@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == OwnerId:
        bot.unload_extension(f'commands.{extension}')
        await ctx.send(f"unloaded {extension}")
    else:
        await ctx.send(embed=NoPermsEmbed("Bot Owner"))


@bot.command(aliases=["relaod"])
async def reload(ctx):
    if ctx.message.author.id == OwnerId:
        try:
            for filename in os.listdir('./commands/'):
                if filename.endswith('.py'):
                    bot.unload_extension(f'commands.{filename[:-3]}')
                    bot.load_extension(f'commands.{filename[:-3]}')
            await ctx.send("Reloaded Cogs")
        except Exception as e:
            error = discord.Embed(
                title="Oopsie Woopsie!!1",
                description="The code monkeys at our headquarters are working VEWY HAWD to fix this!!1!",
                color=discord.Color.dark_red()
            )
            error.add_field(name="Fatal Error", value=f"`{e}`", inline=True)
            await ctx.send(embed=error)
    else:
        await ctx.send(embed=NoPermsEmbed("Bot Owner"))


# load cogs on startup
for filename in os.listdir('./commands/'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')


############

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Unknown Command",
            color=0xbf1300,
            description=f"The command `{ctx.message.content.split(' ')[0]}` is not found! Use `.help` to list all commands!")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="Error",
            color=0xff0000,
            description=f"Unexpected Error: `{error}`"
        )
        await ctx.send(embed=embed)


############


with open("config.json", "r") as configloader:
    config = json.load(configloader)

with open("alias.json", "r") as aliasloader:
    alias = json.load(aliasloader)


def token():
    return config["token"]

def NoPermsEmbed(missingPerms):
    NoPerms = discord.Embed(
        title="Insuffcient Perms",
        description=f"You Do Not Have {missingPerms}",
        color=0xff0000
    )
    return NoPerms

def IsOwner(userID):
    OwnerId = str(config["ownerID"])
    if userID == OwnerId:
        return True
    else:
        return False


def getBot(botParam):
    if not botParam:
        return "Provide a Valid Parameter"
    elif botParam == "id":
        return str(client.user.id)
    elif botParam == "avatar_url":
        return str(client.user.avatar_url)
    elif botParam == "created_at":
        return str(client.user.created_at)
    elif botParam == "mention":
        return str(client.user.mention)
    else:
        return "That Parameter Does Not Exist (Yet)"

def getUser(userParam):
    return client.get_user(userID)


def localFormat():
    return config["localFormat"]
def timezonelist():
    return config["timezonelist"]


def getAlias(command):
    return alias[command]


def getPermissions(perm):
    if perm == "admin":
        if ctx.message.author.guild_permissions.administrator:
            return True
    if perm == "messages":
        if ctx.message.author.guild_permissions.manage_messages:
            return True
    if perm == "channels":
        if ctx.message.author.guild_permissions.manage_channels:
            return True
    if perm == "???":
        return True
    else:
        return False










bot.run(token())
