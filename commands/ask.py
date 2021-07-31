import discord
from discord.ext import commands
from main import embedCreator, getAlias

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("ask"))
    async def ask(self, ctx):
        embed=embedCreator("Don't Ask, to Ask.", "Asking to ask just wastes time.\nState your problem first instead.\nhttps://dontasktoask.com/", 0x313131)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Util(client))
