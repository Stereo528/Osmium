import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dingus(self, ctx, whoisdingus, reason=None):
        dingusembed = discord.Embed(
            title='Dingus!',
            description=f'**{whoisdingus}** is a dingus!',
            color=0xc59200
        )
        if not reason:
            await ctx.send(embed=dingusembed)
        else:
            dingusembed.add_field(name='Reason:', value=f'{reason}', inline=True)
            await ctx.send(embed=dingusembed)

def setup(client):
    client.add_cog(Test(client))