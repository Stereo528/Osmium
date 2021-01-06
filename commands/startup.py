import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        await self.client.change_presence(activity=discord.Game(name="With the Discord.py API"))
        print("Client Is Online")

def setup(client):
    client.add_cog(Util(client))