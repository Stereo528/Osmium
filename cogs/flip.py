import discord
from discord.ext import commands
from random import randint

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def flip(self, ctx):
        author = ctx.message.author.mention
        coinembed = discord.Embed(
            title='Coin Flip',
            description=f'{author} Flipped a coin and got:',
            color=0xA66969
        )

        coin = randint(0, 1)
        if coin == 1:
            coinembed.add_field(name="Heads!", value="\o/", inline=True)
            await ctx.send(embed=coinembed)
        else:
            coinembed.add_field(name="Tails!", value="\o/", inline=True)
            await ctx.send(embed=coinembed)

def setup(client):
    client.add_cog(Test(client))