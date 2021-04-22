import discord, json, os
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

############

with open("config.json", "r") as config_loader:
    config = json.load(config_loader)

OwnerId = config["owner_id"]

############

#Load logic stuffs

def embedCreator(title, desc, color):
    embed = discord.Embed(
        title=f"{title}",
        description=f"{desc}",
        color=color
    )
    return embed

def IsOwner(userID):
    if userID == OwnerId:
        return True
    else:
        return False

############


@bot.command()
async def stop(ctx):
    if IsOwner(ctx.message.author.id):
        await ctx.send(embed=embedCreator("Stopping", "Shutting Down Bot", 0xFF0000))
        await bot.logout()
    else:
        await ctx.send(embed=embedCreator("Insuffcient Permissions", "You are not the Owner of this Bot", 0xFF0000))

############

# Load Cogs

@bot.command()
async def load(ctx, extension):
    if IsOwner(ctx.message.author.id):
        bot.load_extension(f'commands.{extension}')
        await ctx.send(f"loaded {extension}")
    else:
        await ctx.send(embed=embedCreator("Insuffcient Permissions", "You are not the Owner of this Bot", 0xFF0000))


@bot.command()
async def unload(ctx, extension):
    if IsOwner(ctx.message.author.id):
        bot.unload_extension(f'commands.{extension}')
        await ctx.send(f"unloaded {extension}")
    else:
        await ctx.send(embed=embedCreator("Insuffcient Permissions", "You are not the Owner of this Bot", 0xFF0000))


@bot.command(aliases=["relaod"])
async def reload(ctx):
    if IsOwner(ctx.message.author.id):
        try:
            for filename in os.listdir('./commands/'):
                if filename.endswith('.py'):
                    bot.unload_extension(f'commands.{filename[:-3]}')
                    bot.load_extension(f'commands.{filename[:-3]}')
            await ctx.send(embed=embedCreator("Reloaded", "All cogs reloaded", 0x00ad10))
        except Exception as e:
            await ctx.send(embed=embedCreator("Error Reloading", f"`{e}`", 0xbf1300))


# load cogs on startup
for filename in os.listdir('./commands/'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embedCreator("Unknown Command", f"The command `{ctx.message.content.split(' ')[0]}` is not found! Use `.help` to list all commands!", 0xbf1300))
        return
    else:
        await ctx.send(embed=embedCreator("Error", f"Unexpected Error: `{error}`", 0xff0000))

bot.run(config["token"])
