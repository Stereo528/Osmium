import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slowmode(self, ctx, newspeed):
        oldspeed=ctx.channel.slowmode_delay
        embed=discord.Embed(
            title="SlowMode Changed",
            description=f"From {oldspeed} to {newspeed}"
        )
        await ctx.channel.edit(slowmode_delay=newspeed)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))