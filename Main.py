import discord, json, os
from discord.ext import commands
from datetime import date
from datetime import datetime

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)
today1 = date.today()
hour1 = datetime.now()
hourString1 = hour1.strftime("%H:%M:%S")

with open("config.json", "r") as config:
    configloaded = json.load(config)


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


@bot.command()
async def reload(ctx):
    try:
        for filename in os.listdir('./commands/'):
            if filename.endswith('.py'):
                bot.unload_extension(f'commands.{filename[:-3]}')
                bot.load_extension(f'commands.{filename[:-3]}')
        await ctx.send("Reloaded Cogs")
    except as error:
        error = discord.Embed(
            title="Oopsie Woopsie!!1",
            description="The code monkeys at our headquarters are working VEWY HAWD to fix this!!1!" + error,
            color=discord.Color.dark_red()
        )
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


############


bot.run(configloaded["token"])
