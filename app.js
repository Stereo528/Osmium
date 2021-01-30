//const Discord = require('discord.js');
//const fs = require("fs");
//const Enmap = require("enmap");
//const client = new Discord.Client();
//const config = require("./auth.json");

//client.config = config;

//client.on('ready', () => {
//    console.log(`Logged in as ${client.user.tag}!`);
//});

//fs.readdir("./events/", (err, files) => {
//    if (err) return console.error(err);
//    files.forEach(file => {
//    const event = require(`./events/${file}`);
//    let eventName = file.split(".")[0];
//    client.on(eventName, event.bind(null, client));
//    });
//});

//client.commands = new Enmap();

//fs.readdir("./commands/", (err, files) => {
//    if (err) return console.error(err);
//    files.forEach(file => {
//    if (!file.endsWith(".js")) return;
//    let props = require(`./commands/${file}`);
//    let commandName = file.split(".")[0];
//    console.log(`Attempting to load command ${commandName}`);
//    client.commands.set(commandName, props);
//    });
//});

const Akairo = require('discord-akairo');
const client = new Akairo.AkairoClient(
    ownerID="296116954421264384"
);

const config = require("./auth.json");

client.config = config;

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on("message", message => {
    if (message.content.startsWith(config.prefix) === "ping" && message.author.id == ownerID) {
        message.reply("die")
    }
    else if (!message.content.startsWith(config.prefix) && ) {
        message.reply("help");
    }
})

client.login(config.token);