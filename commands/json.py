import discord, json
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def json(self, ctx, json1=None, json2=None):
        
        error = discord.Embed(
            title="Error",
            description="You are missing One or more Arguments",
            color=discord.Color.dark_red()
        )

        if not json1:
            await ctx.send(embed=error)
        elif not json2:
            await ctx.send(embed=error)
        else:
            jsonopen = open("json.json", "w")
            json3 = {
                f"{json1}": f"{json2}"
            }
            y = json.dumps(json3, indent=4)
            jsonopen.write(y)
            jsonopen.close()
            
            jsonfile = discord.File("json.json", filename="Result.json")
            await ctx.send(f"Wrote: `\"{json1}\": \"{json2}\"` to `Result.json`", file=jsonfile)


def setup(client):
    client.add_cog(Util(client))