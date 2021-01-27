import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "d"])
    async def roll(self, ctx, DiceSides, DiceCount=None):
        DiceSides = int(DiceSides)
        DiceFinal = randint(1, DiceSides)
        embed = discord.Embed(
            title=f"Rolling a d{DiceSides}",
            description=f"You Rolled a {DiceFinal}"
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))