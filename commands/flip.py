import discord
from discord.ext import commands
from random import randint
from main import embedCreator, getAlias

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("flip"))
    async def flip(self, ctx, flips=1):
        if flips > 25:
            embed=embedCreator("Too many Coins!", "You can only flip a max of 25 coins.", 0xFF0000)
            await ctx.send(embed=embed)
            return
        flipList=[]
        for num in range(flips):
            coin = randint(0, 1)
            if coin == 0:
                flipList.append("Tails")
            if coin == 1:
                flipList.append("Heads")

        joinedList=", ".join(flipList)
        embed=embedCreator("Flip a Coin", f"Flipped a coin and got: \n{joinedList}", 0xA66969)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
