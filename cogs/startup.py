import discord
from discord.ext import commands
from datetime import date
from datetime import datetime

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        today = date.today()
        hour = datetime.now()
        hourString = hour.strftime("%H:%M:%S")

        await self.client.change_presence(activity=discord.Game(name="With the Discord.py API"))

        channel = self.client.get_channel(742585460760772709)
        server = self.client.get_guild(541332714880499735)
        user = self.client.get_user(707318172780331068)
        embed = discord.Embed(
            title='Bot Started',
            description=f'Bot Started in: **{server}** \nBot User is: **{user}**',
            color=discord.Color.green()
        )
        embed.set_footer(text=f'{today} at {hourString}')
        await channel.send(embed=embed)
        print("client Is Online")

def setup(client):
    client.add_cog(Test(client))