import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["cm", "xmas"])
    async def christmas(self, ctx):
        x = randint(0,11)
        y = randint(0,1)
        if y == 0:
            ChrColor = discord.Color.red()
        else:
            ChrColor = discord.Color.green()
        quotes=["All I want for Christmas is YOUUUUUUUUUUUUUUUU", "*Sings Carol of the Bells*", "HO HO HO", "YOU WANT A SPRITE CRANBERRY", "Its the thirst- Thirstiest time of the YEARRRRRR", "Jingle Bells. Jingle Bells, they don't stop.", "war, war never changes, neither does christmas. is christmas war?", "keep the change you filty animal", "Happy Holidays", "Can it be new years already?", "I enjoy halloween more, can we go back to october?", "Have a Poggers New Year"]
        ChrEmbed = discord.Embed(
            title="Happy Holidays",
            description=quotes[x],
            color=ChrColor
        )
        await ctx.send(embed=ChrEmbed)

def setup(client):
    client.add_cog(Fun(client))