import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["eval"])
    async def evalcmd(self, ctx, args):
        await ctx.send(eval(args))


def setup(client):
    client.add_cog(Owner(client))