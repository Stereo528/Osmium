import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["cooki"])
    async def cookie(self, ctx, member: discord.Member = None):
        if not member:
            error = discord.Embed(
                title="Error",
                description="Please pass a member",
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=error)
        else:
            author = ctx.message.author
            cookieEmbed = discord.Embed(
                title="Cookies!",
                description=f"{author.mention} gave a Cookie to {member.mention}",
                color=0xb4895c
            )
            await ctx.send(embed=cookieEmbed)
                
            


def setup(client):
    client.add_cog(Fun(client))