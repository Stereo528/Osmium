import discord
from discord.ext import commands
from Main import OwnerId

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["eval"])
    async def evalcmd(self, ctx, *, args):
        if ctx.message.author.id == OwnerId:
            await ctx.send(eval(args))
        else:
            await ctx.send(embed=NoPermsEmbed("Bot Owner"))


def setup(client):
    client.add_cog(Owner(client))