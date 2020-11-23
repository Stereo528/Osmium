import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["info"])
    async def about(self, ctx):
        infoembed = discord.Embed(
            title="About",
            description='',
            color=0x345678
        )
        infoembed.add_field(name="Bot Creator:", value="Stereo528#1225   ", inline=True)
        infoembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/707318172780331068/f071b6a0c993ac524b261d50f7b403eb.webp?size=1024")
        await ctx.send(embed=infoembed)
    
def setup(client):
    client.add_cog(Admin(client))