const Discord = require('discord.js');
const client = new Discord.Client();

const fs = require('fs');
const tokenJSON = fs.readFileSync("./auth.json")
const token = JSON.parse(tokenJSON)

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.login(token.token);