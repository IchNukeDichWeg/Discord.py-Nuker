# Discord Nuker made with Python

A Nuker I made with commands such as

* Ban all

* Kick all

* Nick all

* DM all

* Nuke

* Guildnuke

* Guilds

* VC Spam

* Channel Spam

* Category Spam 

* DM Spam

Scroll down to see what each command does and how to Create and Invite a Bot if you didnt already know

And feel free to copy and change it like you want.

---

The Nuker addition file was made to get more Pings. If you want to Nuke just run it at the same time as the normal File, change the Variables to what you want (SPAM_MESSAGE is the message its gona spam, WEBHOOK_NAME is the Webhook name) add ur Bot Token and you dont have to do anything else it will spam at the same time as the Bot will after u use the !nuke command.

---

I added a few Variables at the to make it easier for you to use to Bot and adjust it like you wish. They should be self-explanatory, I still added a description to what it is for each of them. If you dont understand them make sure to create a Issue and ill help you out.
Also Check the Nuker Settings to turn on / off (True/False) what you want the Bot to do once you run the Nuke Command

---

### Commands explained

#### Ban all

Will Ban every Memeber below the Bot
```
!banall
```

#### Kick all

Will Kick every Memeber below the Bot

```
!kickall
```
#### Nick all

Will change every Memeber's Nickname thats below the Bot

```
!nickall <nickname>
```
#### DM all

Will DM every member possible with whatever message you want (imput the message in the Source Code under `DM_ALL_MESSAGE = ""`)

```
!dmall
```
#### Nuke

Will Nuke the Server with Give everyone Admin, Delete all channels, Delete all Roles, Delete all Emojies, Change Server Name and Icon, Create Roles with a Custom Name, Spam Create Channels and Spam a set message

```
!nuke
```
#### Guildnuke

Used if you wana Nuke a Server your not in but ur Bot is or If someone leaks his Bot Tokens and you wana Nuke it (use command !guilds to see the Bots Servers and the Server ID)

```
!guildnuke <guildid>
```
#### Guilds

Displays all the Servers the Bot is in including the Server ID (usefull for Guildnuke)

```
!guilds
```
#### VC Spam

Will Spam Voice Channels with whatever name and amount you want

```
!vcspam <amount> <name> 
```
#### Channel Spam

Will Spam Text Channels with whatever name and amount you want

```
!cspam <amount> <name> 
```
#### Category Spam

Will Spam Category with whatever name and amount you want

```
!caspam <amount> <name> 
```
#### DM Span

Will Spam someones DM's with whatever Message and amount you want (User you want to spam needs to be In the same Server as Bot)
```
!dmspam <user> <amount> <message>
```

---

### Usage and How to Create Bot

You need to create your bot application (essentially the bot's account) on the Discord development page. There is an excellent guide here: https://discordpy.readthedocs.io/en/latest/discord.html which outlines the steps on how to make your bot application. Please also make sure you enable PRIVILEGED INTENTS which you can do here (https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents). Once finished, start the application and copy your token into the Code under ``` token = "UR BOT TOKEN HERE" ``` then just Run it , Invite the Bot to the Server and do whatever Command you want.

To create an invite link, head back to https://discord.com/developers/applications/me under the "Applications" section, click on your bot application, and open the OAuth2 page. At the bottom of the page, you'll find Discord's OAuth2 URL generator. Select the bot and `applications.commands` options. Once you select the `bot` option, a list of permissions will appear, allowing you to configure the permissions your bot needs. Chose `Administrator`. Grab the link via the "Copy" button and enter it in your browser. Then chose the Server press `Continue` then Press `Authorize` and then your ready to use it,
