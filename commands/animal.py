import discord, requests, json
from discord.ext import commands

r = requests.get("https://dog.ceo/api/breeds/image/random")
jsonify=r.json()
jsonopen=open("animal.json", "w")
y=json.dumps(jsonify, indent=4)
jsonopen.write(y)
jsonopen.close()

with open("animal.json", "r") as work:
    pls = json.load(work)

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def animal(self, ctx, wanimal=None):
        if not wanimal:
            await ctx.send(pls["message"])


def setup(client):
    client.add_cog(Fun(client))