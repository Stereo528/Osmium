import discord, pytz, datetime
from discord.ext import commands

localFormat = "%Y-%m-%d %H:%M:%S"

UTC=datetime.datetime.utcnow()

timezonelist = ["US/Eastern", "US/Central", "US/Mountain", "US/Pacific", "Etc/UTC", "Europe/Berlin", "Australia/North", "Australia/South", "Australia/West"]




class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["time", "tz", "tzone", "timez", "timezones"])
    async def timezone(self, ctx):
        timezones = discord.Embed(
            title="Timezones",
            description="A list of timezones",
            color=discord.Color.dark_blue()
        )
        #timezones.add_field(name="UTC", value=UTC)
        for tz in timezonelist:
            localDatetime = UTC.datetime.astimezone(datetime.timezone(tz))
            x = localDatetime.datetime.strftime(localFormat)
            timezones.add_field(name=tz, value=x, inline=False)


        await ctx.send(embed=timezones)


def setup(client):
    client.add_cog(Util(client))