import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dm(self, ctx, member:discord.Member, *, text):
        embed = discord.Embed(
            title="From Osmium",
            description=text,
            color=0x123456
        )
        embed2 = discord.Embed(
            title=f"to {member}",
            description=text,
            color=0x123456
        )
        await member.send(embed=embed)
        await ctx.send(embed=embed2)


def setup(client):
    client.add_cog(Admin(client))