import discord
from discord.ext import commands
from time import sleep

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the Bot load files"), status=discord.Status.dnd)
        sleep(2)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for .help"), status=discord.Status.online)
        print("Bot Is Ready to Crash")

def setup(client):
    client.add_cog(Util(client))
