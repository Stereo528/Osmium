import discord, json
from discord.ext import commands
from main import embedCreator

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, command = None):

        #load JSON storing all commands
        with open("commandList.json", "r") as commandLoader:
            commandList = json.load(commandLoader)
        #load JSON storing all categories
        with open("categoryList.json", "r") as categoryLoader:
            categoryList = json.load(categoryLoader)
        #Create embed frame
        embed = embedCreator("Commands", "list of all commands", 0x123456)
        #list all commands
        if not command:

            def ListToStr(listType):
                listType=sorted(categoryList[listType])
                String="\n".join(listType)
                return(String)

            for category in categoryList:
                embed.add_field(name=category, value=ListToStr(category), inline=False)
            await ctx.send(embed=embed)
        else:
            try:
                embed.add_field(name=f".{command}", value=commandList[command], inline=False)
                await ctx.send(embed=embed)
            except:
                embed = embedCreator("Unknown Command", f"The command `.{command}` is not found! Use `.help` with no arguments to list all commands!", 0xFF0000)
                await ctx.send(embed=embed)
                return

def setup(client):
    client.add_cog(Util(client))
