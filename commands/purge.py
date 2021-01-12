import discord
from discord.ext import commands
from datetime import date
from datetime import datetime

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def purge(self, ctx, msgCount):
        today = date.today()
        hour = datetime.now()
        hourString = hour.strftime("%H:%M:%S")

        msgCount = int(msgCount)
        channel = ctx.message.channel
        botlog = self.client.get_channel(742585460760772709)
        messages = []

        async for message in channel.history(limit=msgCount):
            messages.append(message)

        purgeembed = discord.Embed(
            title='Purged Messages',
            description=f'Purged **{msgCount}** Messages in **{channel}**',
            color=discord.Color.red()
        )
        purgeembed.set_footer(text=f'{today} at {hourString}')

        await channel.delete_messages(messages)
        await ctx.send('Purged Messages')
        await botlog.send(embed=purgeembed)

def setup(client):
    client.add_cog(Admin(client))