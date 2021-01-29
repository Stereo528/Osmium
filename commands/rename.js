const { MessageEmbed } = require("discord.js");

exports.run = (client, message, args) => {
    const oldName = message.channel.name;
    const channel = message.channel;
    if (!message.guild.me.hasPermission("MANAGE_CHANNELS")) {
        return message.channel.send("You don't have the perms to do this!")
    }
    else {
        let newname = args.slice(0).join("-");
        const embed = new MessageEmbed()
            .setTitle("Channel Renamed")
            .setDescription(`Name Changed from ${oldName} to ${newname}`)
        channel.setName(newname)
            .then(channel.send(embed))
    }
}