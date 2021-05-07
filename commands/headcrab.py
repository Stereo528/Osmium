import discord, json
from discord.ext import commands
from random import randint
from main import embedCreator

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["hc"])
    async def headcrab(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        with open("headcrabs.json", "r") as headcrab:
            headcrabJson = json.load(headcrab)
        failRate = randint(1, 5)
        userHeadcrab = headcrabJson["this is an example"]

        try:
            userHeadcrab = headcrabJson[str(member.id)]
        except KeyError:
            with open("headcrabs.json", "r+") as headcrabWrite:
                yes = json.load(headcrabWrite)
                no = {f"{member.id}": [0, 0]}
                yes.update(no)
                headcrabWrite.seek(0)
                test = json.dump(yes, headcrabWrite)
                userHeadcrab = [0, 0]


        embed = embedCreator("", f"{ctx.message.author.mention} threw a Headcrab at {member.mention}. (Headcrab #{userHeadcrab[0]})", 0x8dd594)
        if failRate == 1:
            embed = embedCreator("", f"{ctx.message.author.mention} tried to Headcrab {member.mention}, but failed. (Headcrab Fail #{userHeadcrab[1]})", 0x8dd594)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
