import discord
from discord.ext import commands
from main import getAlias

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("serverinfo"))
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=f"Info for {ctx.guild.name}",
            description=f"Emoji Limit: {ctx.guild.emoji_limit} \nFilesize Limit: {round(ctx.guild.filesize_limit/1000000)} megabytes",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Current Members", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Other Data", value=f"Nitro Level: {ctx.guild.premium_tier}, Nitro Boosters: {ctx.guild.premium_subscription_count}", inline=False)
        embed.add_field(name="Owner Info", value=f"Server Owner: {ctx.guild.owner} \nOwner ID: {ctx.guild.owner_id}", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Util(client))