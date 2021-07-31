from main import getAlias
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("records"))
    async def records(self, ctx, add = None):
        if not add:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")



        await ctx.send("ass")

def setup(client):
    client.add_cog(Admin(client))
