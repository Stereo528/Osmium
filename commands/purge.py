import discord, json
from discord.ext import commands
from main import embedCreator, BotLog, getAlias


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=getAlias("purge"))
    async def purge(self, ctx, msgCount):
        def JSONwriter(filename, data):
            with open(filename+".json", "w") as Writer:
                Writing = {"messages": data}
                json.dump(Writing, Writer, indent=4)


        msgCount = int(msgCount)+1
        botlog = self.client.get_channel(BotLog)
        CurrentChannel = ctx.message.channel
        messages = []
        messagesContent = []
        if ctx.message.author.guild_permissions.manage_messages:

            async for message in CurrentChannel.history(limit=msgCount):
                messages.append(message)
            async for message in CurrentChannel.history(limit=msgCount):
                messagesContent.append(message.content)

            embed=embedCreator(f"Messages Purged From #{CurrentChannel}", f"{msgCount} Messages Purged", 0xFF0000)
            embed2=embedCreator("Purged Messages", f"{msgCount} Messages Purged", 0xFF0000)
            await CurrentChannel.delete_messages(messages)
            await ctx.send(embed=embed2)
            JSONwriter("purge_records", messagesContent)
            jsonfile = discord.File("purge_records.json", filename="PurgeRecord.json")
            await botlog.send(embed=embed, file=jsonfile)
        else:
            await ctx.send(embed=embedCreator("You Have Insuffcient Perms", "You are missing the \"Manage Messages\" Permissions", 0xFF0000))


def setup(client):
    client.add_cog(Admin(client))
