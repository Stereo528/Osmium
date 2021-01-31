import discord, json, os
from discord.ext import commands
from datetime import date
from datetime import datetime

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

with open("config.json", "r") as config:
    configloaded = json.load(config)

OwnerId = configloaded["ownerID"]
OwnerId=str(OwnerId)

############

# Get Bot Things
def getBot(botParam):
    if not botParam:
        return "Provide a Valid Parameter"
    elif botParam == "id":
        return str(bot.user.id)
    elif botParam == "avatar_url":
        return str(bot.user.avatar_url)
    elif botParam == "created_at":
        return str(bot.user.created_at)
    elif botParam == "mention":
        return str(bot.user.mention)
    else:
        return "That Parameter Does Not Exist (Yet)"


# Get Other Things
def getUser(userParam):
    return bot.get_user(userID)

############

# Load Cogs

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'commands.{extension}')
    await ctx.send(f"loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'commands.{extension}')
    await ctx.send(f"unloaded {extension}")


@bot.command(aliases=["relaod"])
async def reload(ctx):
    try:
        for filename in os.listdir('./commands/'):
            if filename.endswith('.py'):
                bot.unload_extension(f'commands.{filename[:-3]}')
                bot.load_extension(f'commands.{filename[:-3]}')
        await ctx.send("Reloaded Cogs")
    except e:
        error = discord.Embed(
            title="Oopsie Woopsie!!1",
            description="The code monkeys at our headquarters are working VEWY HAWD to fix this!!1!",
            color=discord.Color.dark_red()
        )
        error.add_field(name="Fatal Error", value=f"`{e}`", inline=True)
        await ctx.send(embed=error)


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
            color=0xff0000,
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


bot.run(configloaded["token"])
