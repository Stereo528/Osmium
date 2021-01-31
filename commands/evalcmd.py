import discord
from discord.ext import commands
from Main import OwnerId

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["eval"])
    async def evalcmd(self, ctx, *, args):
        print(f"lmfao: {OwnerId} hhdhdh: {ctx.message.author.id}")
        if ctx.message.author.id == OwnerId:
            await ctx.send(eval(args))
        else:
            await ctx.send("You don't have the perms for this")


def setup(client):
    client.add_cog(Owner(client))