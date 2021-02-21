
import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def modmail(self, ctx, *, content):
        channel = self.client.get_channel(742585460760772709)
        guild = ctx.message.guild
        embed = discord.Embed(
            title=f"From {ctx.message.author}",
            description=content,
            color=0x123456
        )
        error = discord.Embed(
            title="DM Only Command",
            color=0xff0000
        )
        messages = []
        async for message in ctx.message.channel.history(limit=1):
            messages.append(message)
        if not guild:
            await channel.send(embed=embed)
        else:
            await ctx.message.channel.delete_messages(messages)
            await ctx.send(embed=error)



def setup(client):
    client.add_cog(Util(client))