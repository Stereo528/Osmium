import discord
from discord.ext import commands
from time import sleep

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Bot wake up"), status=discord.Status.dnd)
        sleep(5)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for .help"), status=discord.Status.online)
        print("Client Is Online")

def setup(client):
    client.add_cog(Util(client))