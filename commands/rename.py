import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rename(self, ctx, newname):
        oldname=ctx.channel.name
        embed=discord.Embed(
            title="Channel Renamed",
            description=f"From {oldname} to {newname}"
        )
        await ctx.channel.edit(name=newname)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))