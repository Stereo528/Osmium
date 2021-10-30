import discord, json
from discord.ext import commands
from random import randint
from main import embedCreator, getAlias


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("headcrab"))
    async def headcrab(self, ctx, member: discord.Member=None):
        
        def WinOrLose(test):
            with open('headcrabs.json', 'r') as source_file:
                oldData = json.load(source_file)
                with open('headcrabs.json', 'w') as dest_file:
                    for line in source_file:
                        element = json.loads(line.strip())
                        if f'{ctx.message.author.id}' in element:
                            del element[f'{ctx.message.author.id}']
                    if test == True:
                        newData={f"{ctx.message.author.id}": [int(userHeadcrab[0])+1, int(userHeadcrab[1])]}
                    elif test == False:
                        newData={f"{ctx.message.author.id}": [int(userHeadcrab[0]), int(userHeadcrab[1])+1]}
                    else:
                        embedCreator("Critical Error", "Somehow Studio528#1225 messed this up *really badly* \nPlease contact them", 0xFF0000)
                    oldData.update(newData)
                    dest_file.seek(0)
                    json.dump(oldData, dest_file, indent=4)


        if not member:
            member = ctx.message.author
        with open("headcrabs.json", "r+") as headcrab:
            headcrabJson = json.load(headcrab)
        #11% chance to fail
        failRate = randint(1, 9)
        #it complains it hasn't been defined, but also useful for showing format
        userHeadcrab = headcrabJson["this is an example"]

        try:
            #try to see if there is a userID already there
            userHeadcrab = headcrabJson[str(ctx.message.author.id)]
        except KeyError:
            #if not make one
            with open("headcrabs.json", "r+") as headcrabWrite:
                Data = json.load(headcrabWrite) #Load JSON
                newData = {f"{ctx.message.author.id}": [0, 0]} #New Data
                Data.update(newData) #Update old data to new data
                headcrabWrite.seek(0) #Go to start of file
                json.dump(Data, headcrabWrite, indent=4) #write it to that file
                userHeadcrab = [0, 0] #just say their stuff is 0 to prevent it using the example values

        embed = embedCreator("", f"{ctx.message.author.mention} threw a Headcrab at {member.mention}. (Headcrab #{int(userHeadcrab[0])+1})", 0x8dd594)

        if failRate == 1:
            embed = embedCreator("", f"{ctx.message.author.mention} tried to Headcrab {member.mention}, but failed. (Headcrab Fail #{int(userHeadcrab[1])+1})", 0x8dd594).set_image(url="https://cdn.discordapp.com/attachments/834263755939512351/902748131429580892/headcrab_fail.gif")
            WinOrLose(False)
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/834263755939512351/902748120100773959/headcrab_success.gif")
            WinOrLose(True)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))