import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["server","serverinfo","guild"])
    async def guildinfo(self, ctx):

        server = ctx.guild

        ServerName = server.name
        ServerID = server.id
        ServerIcon = server.icon_url
        ServerOwner = server.owner
        ServerOwnerID = server.owner_id
        MaxMembers = server.max_members
        ServerDesc = server.description
        NitroLevel = server.premium_tier
        NitroBoosts = server.premium_subscription_count
        ChannelCount = server.channels
        VoiceCount = server.voice_channels
        TextCount = server.text_channels
        CategoriesCount = server.categories
        MemberCount = server.member_count
        CreatedAt = server.created_at
        
        embed=discord.Embed(
            title=f'Server Info: {ServerName}',
            description=f"Server Owner: {ServerOwner} \nOwner ID: {ServerOwnerID}",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=ServerIcon)
        embed.add_field(name="Server Creation Date", value=CreatedAt, inline=True)
        embed.add_field(name="Max Member Count", value=MaxMembers, inline=False)
        embed.add_field(name="Current Members", value=MemberCount, inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Admin(client))