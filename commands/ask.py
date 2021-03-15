import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ask(self, ctx):
        dontask = discord.Embed(
            url="https://dontasktoask.com/",
            title="Don't Ask, to Ask.",
            description="Asking to ask just wastes time.\nState your problem first instead.",
            color=0x313131
        )
        await ctx.send(embed=dontask)


def setup(client):
    client.add_cog(Util(client))