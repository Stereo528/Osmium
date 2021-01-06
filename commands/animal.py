import discord, dog, cat
from random import randint
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def animal(self, ctx, wanimal=None):
        if not wanimal:
            error = discord.Embed(
                title="Error",
                description="Please provide a valid argument (dog or cat)",
                color=0xFF0000
            )
            await ctx.send(embed=error)
        elif wanimal == "dog":
            dog.getDog(directory=None, filename="dog")
            dogimg = discord.File("dog.jpg")
            await ctx.send(file=dogimg)
        elif wanimal == "cat":
            cat.getCat(directory=None, filename="cat", format="png")
            catimg = discord.File("cat.png")
            await ctx.send(file=catimg)


def setup(client):
    client.add_cog(Fun(client))