import discord, requests, json, dog, cat
from random import randint
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def animal(self, ctx, wanimal=None):
        if not wanimal:
            dog.getDog(directory="C:/Users/Studio528/Documents/GitHub/DBPython/animal", filename="dog")
            dogimg = discord.File("animal/dog.jpg")
            await ctx.send(file=dogimg)


def setup(client):
    client.add_cog(Fun(client))