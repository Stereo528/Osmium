import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["server","serverinfo","guild"])
    async def guildinfo(self, ctx):

        server = ctx.guild

        ServerName = server.name #
        ServerID = server.id #
        ServerIcon = server.icon_url #
        ServerOwner = server.owner #
        ServerOwnerID = server.owner_id #
        ServerDesc = server.description #
        NitroLevel = server.premium_tier #
        NitroBoosts = server.premium_subscription_count #
        MemberCount = server.member_count #
        CreatedAt = server.created_at #
        EmojiLimit = server.emoji_limit
        FilesizeLimit = server.filesize_limit

        Nitro = f"Nitro Level: {NitroLevel}, Nitro Boosters: {NitroBoosts}"
        MainServerInfo = f"Server Desc: {ServerDesc} \nEmoji Limit: {EmojiLimit} \nFilesize Limit: {round(FilesizeLimit/1000000)} megabytes"
        Owner=f"Server Owner: {ServerOwner} \nOwner ID: {ServerOwnerID}"
        
        embed=discord.Embed(
            title=f'Server Info: {ServerName}',
            description=MainServerInfo,
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=ServerIcon)
        embed.add_field(name="Current Members", value=MemberCount, inline=True)
        embed.add_field(name="Other Data", value=Nitro, inline=False)
        embed.add_field(name="Owner Info", value=Owner, inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Admin(client))