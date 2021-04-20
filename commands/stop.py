import discord
from discord.ext import commands
from datetime import date
from datetime import datetime
from Main import NoPermsEmbed, IsOwner

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def stop(self, ctx):
        if IsOwner(ctx.message.author):
            today = date.today()
            hour = datetime.now()
            hourString = hour.strftime("%H:%M:%S")

            channel = self.client.get_channel(742585460760772709)
            stopembed = discord.Embed(
                title='Bot Stopped',
                description=f'Bot Stopped at: {hourString} on {today}',
                color=discord.Color.dark_red()
            )
            await ctx.send("Stopping...")
            await channel.send(embed=stopembed)
            await self.client.close()
            print("Bot Offline")
        else:
            await ctx.send(embed=NoPermsEmbed("Bot Owner"))

def setup(client):
    client.add_cog(Admin(client))
