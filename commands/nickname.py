import discord
from discord.ext import commands
from discord.member import Member
from main import embedCreator

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["nick", "name"])
    async def nickname(self, ctx, member: discord.Member = None, *, nick = None):
        oldNick = member.nick
        if ctx.message.author.guild_permissions.manage_nicknames:
            if not member:
                await ctx.send(embed=embedCreator("Error", "Please provide a valid Discord User", 0xFF0000))
            if not nick:
                await member.edit(nick=member.name)
            else:
                await member.edit(nick=nick)
            
            await ctx.send(embed=embedCreator("Nickname Changed", f"Changed {member}'s Nickname from {oldNick} to {nick}", 0x00FF00))
        else:
            await ctx.send(embed=embedCreator("You Have Insuffcient Perms", "You are missing the \"Manage Nickname\" Permissions", 0xFF0000))


def setup(client):
    client.add_cog(Admin(client))