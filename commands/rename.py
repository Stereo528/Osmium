import discord
from discord.ext import commands
from Main import NoPermsEmbed

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rename(self, ctx, newname):
        if ctx.message.author.guild_permissions.manage_channels:
            oldname=ctx.channel.name
            embed=discord.Embed(
                title="Channel Renamed",
                description=f"From {oldname} to {newname}"
            )
            await ctx.channel.edit(name=newname)
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=NoPermsEmbed("Manage Channels"))


def setup(client):
    client.add_cog(Admin(client))