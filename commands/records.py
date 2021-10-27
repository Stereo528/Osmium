from typing import List
from discord.member import Member
from main import embedCreator, getAlias, ListToStr
import discord
import json
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("records"))
    async def records(self, ctx, user: discord.Member = None): #REMOVE ": discord.Member" TO DEBUG THIS PARSER WITH THE "example" USER.
        if not user:
            await ctx.send(embed=embedCreator("Error", "Please provide a valid Discord User", 0xFF0000))
        else:
            with open("records.json", "r+") as recordsLdr:
                records = json.load(recordsLdr)
            embed = embedCreator("Records", f"Records For: {user}", 0x123456)
            
            for record in records[user]:
                await ctx.send([record])
                if record["type"] == "mute":
                    embed.add_field(name=record["type"], value=ListToStr([record["duration"], record["reason"],record["moderator"]]), inline=False)
                elif record["type"] == "warn":
                    embed.add_field(name=record["type"], value=ListToStr([record["reason"], record["moderator"]]), inline=False)
                else:
                    pass

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
