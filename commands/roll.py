import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice"])
    async def roll(self, ctx, DiceSides):
        int(DiceSides)
        DiceFinal = randint(0, DiceSides)
        embed = discord.Embed(
            title=f"Rolling a d",
            description="You Rolled a: " + str(DiceFinal) + "!"
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))