import discord, json, os

with open("config.json", "r") as configloader:
    config = json.load(configloader)

with open("alias.json", "r") as aliasloader:
    alias = json.load(aliasloader)


def token():
    return config["token"]

def NoPermsEmbed(missingPerms):
    NoPerms = discord.Embed(
        title="Insuffcient Perms",
        description=f"You Do Not Have {missingPerms}",
        color=0xff0000
    )
    return NoPerms

def IsOwner(userID):
    OwnerId = config["ownerID"]
    if userID == OwnerId:
        return True
    else
        return False


def getBot(botParam):
    if not botParam:
        return "Provide a Valid Parameter"
    elif botParam == "id":
        return str(bot.user.id)
    elif botParam == "avatar_url":
        return str(bot.user.avatar_url)
    elif botParam == "created_at":
        return str(bot.user.created_at)
    elif botParam == "mention":
        return str(bot.user.mention)
    else:
        return "That Parameter Does Not Exist (Yet)"

def getUser(userParam):
    return bot.get_user(userID)


def localFormat():
    return config["localFormat"]
def timezonelist():
    return config["timezonelist"]


def getAlias(command):
    return alias[command]


def getPermissions(perm):
    if perm == "admin":
        if ctx.message.author.guild_permissions.administrator:
            return True
    if perm == "messages":
        if ctx.message.author.guild_permissions.manage_messages:
            return True
    if perm == "channels":
        if ctx.message.author.guild_permissions.manage_channels:
            return True
    if perm == "???":
        return True
    else:
        return False
