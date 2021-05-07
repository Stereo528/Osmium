import discord, json
from discord.ext import commands
from random import randint
from main import embedCreator

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["hc"])
    async def headcrab(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        with open("headcrabs.json", "r+") as headcrab:
            headcrabJson = json.load(headcrab)
        #20% chance to fail
        failRate = randint(1, 5)
        #it complains it hasn't been defined, but also useful for showing format
        userHeadcrab = headcrabJson["this is an example"]

        try:
            #try to see if there is a userID already there
            userHeadcrab = headcrabJson[str(member.id)]
        except KeyError:
            #if not make one
            with open("headcrabs.json", "r+") as headcrabWrite:
                Data = json.load(headcrabWrite) #Load JSON
                newData = {f"{member.id}": [0, 0]} #New Data
                Data.update(newData) #Update old data to new data
                headcrabWrite.seek(0) #Go to start of file
                json.dump(Data, headcrabWrite) #write it to that file
                userHeadcrab = [0, 0] #just say their stuff is 0 to prevent it using the example values
        #Counter upper
        def CountUp(state):
            #Load json to write to
            with open("headcrabs.json", "r+") as Count:
                olddata = json.load(Count)

            if state == "succeed":
                with open('headcrabs.json', 'r') as source_file:
                    oldData = json.load(source_file)
                    with open('headcrabs.json', 'w') as dest_file:
                        for line in source_file:
                            element = json.loads(line.strip())
                            if f'{member.id}' in element:
                                del element[f'{member.id}']
                        newData={f"{member.id}": [int(userHeadcrab[0])+1, int(userHeadcrab[1])]}
                        oldData.update(newData)
                        dest_file.seek(0)
                        json.dump(oldData, dest_file)

            elif state == "fail":

                with open('headcrabs.json', 'r') as source_file:
                    oldData = json.load(source_file)
                    with open('headcrabs.json', 'w') as dest_file:
                        for line in source_file:
                            element = json.loads(line.strip())
                            if f'{member.id}' in element:
                                del element[f'{member.id}']
                        newData={f"{member.id}": [int(userHeadcrab[0]), int(userHeadcrab[1])+1]}
                        oldData.update(newData)
                        dest_file.seek(0)
                        json.dump(oldData, dest_file)
            else:
                #if i somehow mispell or break smth
                embedCreator("Critical Error", "Somehow Stereo528#1225 messed this up *really badly* \nPlease contact them", 0xFF0000)




        embed = embedCreator("", f"{ctx.message.author.mention} threw a Headcrab at {member.mention}. (Headcrab #{int(userHeadcrab[0])+1})", 0x8dd594)

        if failRate == 1:
            embed = embedCreator("", f"{ctx.message.author.mention} tried to Headcrab {member.mention}, but failed. (Headcrab Fail #{int(userHeadcrab[1])+1})", 0x8dd594)
            embed.set_image(url="https://i.hiitsdevin.dev/bot/headcrab_fail.gif")
            CountUp("fail")
        else:
            embed.set_image(url="https://i.hiitsdevin.dev/bot/headcrab_success.gif")
            CountUp("succeed")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
# before adding writing of new values, this is at 42 lines, lets see what it is after...
#so far at 78
