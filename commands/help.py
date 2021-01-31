import discord, json
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    #ok so new help command, if they dont give a specific command, just send all, otherwise, get info about that command from the helpList
    @commands.command()
    async def help(self, ctx, command=None):
        #open the file and read its json contents
        with open("./helpList.json", "r") as helpLoad:
            helpList = json.load(helpLoad)
        #create the embed frame, 
        embed = discord.Embed(
            title="Commands",
            color=0x123456
        )
        embed.set_footer("")
        #List all commands
        if not command:
            #seperate each of them from the list
            def ListToStr(listType):
                listType=helpList[listType]
                String="\n".join(listType)
                return(String)
            #Add the fields for commands + categories
            embed.add_field(name="Admin", value=ListToStr("Admin"), inline=False)
            embed.add_field(name="Util", value=ListToStr("Util"), inline=False)
            embed.add_field(name="Fun", value=ListToStr("Fun"), inline=False)
            await ctx.send(embed=embed)
        else:
            try:
                embed.add_field(name=f".{command}", value=helpList[command], inline=False)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Unknown Command",
                    color=0xff0000,
                    description=f"The command `.{command}` is not found! Use `.help` to list all commands!")
                await ctx.send(embed=embed)
                return



def setup(client):
    client.add_cog(Example(client))