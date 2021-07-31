import discord
from discord.ext import commands
from main import embedCreator, getAlias


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("slowmode"))
    async def slowmode(self, ctx, newSpeed):
        if ctx.message.author.guild_permissions.manage_channels:
            oldSpeed=ctx.channel.slowmode_delay
            embed=embedCreator("Slowmode Changed", f"from {oldSpeed} to {newSpeed}", 0x00FF00)
            await ctx.channel.edit(slowmode_delay=newSpeed)
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embedCreator("You Have Insuffcient Perms", "You are missing the \"Manage Channel\" Permissions", 0xFF0000))


def setup(client):
    client.add_cog(Admin(client))
