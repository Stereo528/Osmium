import discord
from discord.ext import commands
from Main import getBot, getUser

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["info"])
    async def about(self, ctx):
        infoembed = discord.Embed(
            title="About",
            description=getBot("id"),
            color=0x345678
        )
        infoembed.add_field(name="Bot Creator:", value=getUser(296116954421264384), inline=True)
        infoembed.add_field(name="Info", value=f"Id: {getBot('id')}, \nMention: {getBot('mention')}", inline=False)
        infoembed.set_thumbnail(url=getBot("avatar_url"))
        await ctx.send(embed=infoembed)
    
def setup(client):
    client.add_cog(Admin(client))