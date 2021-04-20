import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "d"])
    async def roll(self, ctx, dieSides, dieNum=0, dieAdd=0):

        rollList = []
        dieSides=int(dieSides)
        dieNum=int(dieNum)
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
        embed.add_field(name="Roll Array",  value=f"Full Roles: {rollList}", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
