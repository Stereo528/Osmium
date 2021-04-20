def NoPermsEmbed(missingPerms):
    NoPerms = discord.Embed(
        title="Insuffcient Perms",
        description=f"You Do Not Have {missingPerms}",
        color=0xff0000
    )
    return NoPerms

def IsOwner(userID):
    with open("config.json", "r") as config:
        configloaded = json.load(config)
    OwnerId = configloaded["ownerID"]
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
