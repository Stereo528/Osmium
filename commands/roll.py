
import discord
from discord.ext import commands
from random import randint
from main import embedCreator

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dice", "d"])
    async def roll(self, ctx, dieSides, dieNum=1, dieAdd=0):

        rollList = []
        for num in range(int(dieNum)):
            Roll=randint(1, int(dieSides))
            rollList.append(Roll)
            
        embed = embedCreator(f"Rolling {dieNum}d{dieSides}+{dieAdd}", f"You Rolled {sum(rollList)+dieAdd}", 0x8b0000)
        embed.add_field(name="Roll Array",  value=f"Full Roles: {rollList}", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
