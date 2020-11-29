import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        coglist = []
        comlist = []
        #Since this is a weird command, I will explain what each part does
        #This will look for all "Cogs" (AKA Categoies) and add them to a list
        for cog in sorted(self.client.cogs):
            coglist.append(cog + "\n")
        for command in self.client.commands:
            name = command.name
            comlist.append("." + name + "\n")
        #This will then convert both lists into strings, with different functions because its different lists
        def list2str(s):
            cogstr = " "
            return (cogstr.join(s))
        def list2str2(d):
            comstr = " "
            return (comstr.join(d))
        #this is the lists we want to use in above functions
        s=coglist
        d=comlist
        #make embeds and send them
        cogembed = discord.Embed(
            title="Categories",
            description=list2str(s),
            color=0x134256
        )

        comembed = discord.Embed(
            title="Commands",
            description=list2str2(d),
            color=0x134256
        )


        await ctx.send(embed=cogembed)
        await ctx.send(embed=comembed)


def setup(client):
    client.add_cog(Example(client))