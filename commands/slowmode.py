import discord
from discord.ext import commands
from Main import NoPermsEmbed

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slowmode(self, ctx, newspeed):
        if ctx.message.author.guild_permissions.manage_channels:
            oldspeed=ctx.channel.slowmode_delay
            embed=discord.Embed(
                title="SlowMode Changed",
                description=f"From {oldspeed} to {newspeed}"
            )
            await ctx.channel.edit(slowmode_delay=newspeed)
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=NoPermsEmbed("Manage Channels"))


def setup(client):
    client.add_cog(Admin(client))