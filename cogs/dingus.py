import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dingus(self, ctx, whoisdingus=None, reason=None):
        if not whoisdingus:
            errorembed = discord.Embed(
                title='Error!',
                description='Please provide Text or a User',
                color=0xff0000
            )
            await ctx.send(embed=errorembed)
        else:
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
    client.add_cog(Fun(client))