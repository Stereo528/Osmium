import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        joinDate = str(member.joined_at).split('.')
        createDate = str(member.created_at).split('.')

        userRolesList = []
        for i in list(member.roles):
            if "@everyone" in str(i):
                continue
            userRolesList.append(i.mention)
        userRolesList.reverse()
        userRoles = " ".join(userRolesList)

        profileembed = discord.Embed(
            title=f'User Profile',
            description=f"{member.mention}\'s Profile \nUser ID: **{member}** \nUser Status: {member.status} \nUser Custom Status: {member.activity} \nUser Nickname: {member.display_name}",
            color=discord.Color.dark_green()
        )
        profileembed.add_field(name="Account Creation Date", value=f'**{createDate[0]} UTC**', inline=True)
        profileembed.add_field(name="Guild Join Date", value=f'**{joinDate[0]} UTC**', inline=True)
        profileembed.add_field(name='Roles:', value=userRoles, inline=False)
        profileembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=profileembed)

def setup(client):
    client.add_cog(Util(client))