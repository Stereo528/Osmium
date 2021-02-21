import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "d"])
    async def roll(self, ctx, dieSides, dieNum=None, dieAdd=None):
        
        rollList = []
        dieSides=int(dieSides)
        if not dieNum:
            dieNum = 1
        else:
            dieNum=int(dieNum)
        if not dieAdd:
            dieAdd = 0
        else:
            dieAdd=int(dieAdd)
        
        def roll(sides):
            dieRoll = randint(1, sides)
            return dieRoll

        for num in range(dieNum):
            Roll=roll(dieSides)
            rollList.append(Roll)

        embed = discord.Embed(
                title=f"Rolling {dieNum}d{dieSides}+{dieAdd}",
                description=f"You Rolled {sum(rollList)+dieAdd}"
            )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))