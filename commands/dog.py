import discord
from discord.ext import commands

class Dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        doge = discord.Embed(
            
        )
        await ctx.send(embed=doge)


def setup(client):
    client.add_cog(Fun(client))