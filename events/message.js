const { MessageEmbed } = require("discord.js");

module.exports = (client, message) => {
    //Do Nothing if message doesnt have prefix or is by a bot
    if (message.author.bot) return;
    if (message.content.indexOf(client.config.prefix) !== 0) return;

    const args = message.content.slice(client.config.prefix.length).trim().split(/ +/g);
    const command = args.shift().toLowerCase();

    const cmd = client.commands.get(command);
    if (!cmd) {
        const embed = MessageEmbed()
            .setTitle("Error")
            .setDescription("The Command: " + command + "Does not exist, try using \`.help\`")
            .setColor(0xFF0000)
        return message.channel.send(embed);
    }
    else {
        cmd.run(client, message, args);
    }
};