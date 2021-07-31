import discord
from discord.ext import commands
from main import getAlias

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("about"))
    async def about(self, ctx):
        infoembed = discord.Embed(
            title="About",
            color=0x345678
        )
        infoembed.add_field(name="Bot Creator:", value=self.client.get_user(296116954421264384), inline=True)
        infoembed.add_field(name="Info", value=f"Id: {self.client.user.id}, \nMention: {self.client.user.mention}", inline=False)
        infoembed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=infoembed)

def setup(client):
    client.add_cog(Util(client))