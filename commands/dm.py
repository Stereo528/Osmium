import discord
from discord.ext import commands
from config import NoPermsEmbed, getPermissions

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dm(self, ctx, member:discord.Member, *, text):
        if getPermissions("admin"):
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
        else:
            await ctx.send(embed=NoPermsEmbed("Admin"))



def setup(client):
    client.add_cog(Admin(client))
