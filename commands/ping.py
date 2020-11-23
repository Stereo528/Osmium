import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        apiping = int(self.client.latency * 1000)
        apiembed = discord.Embed(
            title="API Ping",
            description=f'{apiping} ms',
            color=discord.Color.blurple()
        )
        await ctx.send(embed=apiembed)

def setup(client):
    client.add_cog(Admin(client))