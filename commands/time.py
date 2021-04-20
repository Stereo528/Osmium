import discord, datetime
from discord.ext import commands
from pytz import timezone
from Main import localFormat, timezonelist, getAlias

Aliases = getAlias("time")
UTC=datetime.datetime.now(timezone('UTC'))

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Aliases)
    async def time(self, ctx):
        timezones = discord.Embed(
            title="Timezones",
            description="A list of timezones",
            color=discord.Color.dark_blue()
        )
        #timezones.add_field(name="UTC", value=UTC)
        for tz in timezonelist:
            localDatetime = UTC.astimezone(timezone(tz))
            x = localDatetime.strftime(localFormat)
            timezones.add_field(name=tz, value=x, inline=False)


        await ctx.send(embed=timezones)


def setup(client):
    client.add_cog(Util(client))
