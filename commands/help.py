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

        #list all commands if no command is passed
        if not command:
            #logic for grabbing all of the commands out of the lists of categories
            def ListToStr(listType):
                #Sort the list so its in alphabetical order (of category name)
                listType=sorted(categoryList[listType])
                #New line each of the strings
                String="\n".join(listType)
                return(String)
            #Auto bring all of the categories in from the json, no more hardcoding!!
            for category in categoryList:
                embed.add_field(name=category, value=ListToStr(category), inline=False)

            await ctx.send(embed=embed)
        #Else give the specific command
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
