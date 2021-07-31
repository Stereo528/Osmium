
import discord
from discord.ext import commands
from random import randint
from main import embedCreator, getAlias

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("roll"))
    async def roll(self, ctx, dieSides, dieNum=1, dieAdd=0):

        if int(dieSides) > 200:
            embed=embedCreator("Too many sides!", "You can only have up to 200 sides.", 0xFF0000)
            await ctx.send(embed=embed)
            return
        if dieNum > 50:
            embed=embedCreator("Too many Dice!", "You can only have up to 50 Dice.", 0xFF0000)
            await ctx.send(embed=embed)
            return

        rollList = []
        rollListString = []
        for num in range(int(dieNum)):
            Roll=randint(1, int(dieSides))
            rollList.append(Roll)
            rollListString.append(str(Roll))

        joinedList=", ".join(rollListString)
        embed = embedCreator(f"Rolling {dieNum}d{dieSides}+{dieAdd}", f"You Rolled: {sum(rollList)+dieAdd}", 0x8b0000)
        embed.add_field(name="Roll Array",  value=f"Full Roles: {joinedList}", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
