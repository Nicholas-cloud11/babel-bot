import datetime

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from pymongo import MongoClient

from user import *

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
mongo_client = MongoClient(os.getenv('MONGO_URI'))
db = mongo_client.get_database()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=972186275589275649)

@bot.event
async def on_ready():
    print(f"Loaded as: {bot.user.name}")


async def sync_cmd():
    synced = await bot.tree.sync(guild=GUILD_ID)
    print(f"Synced {len(synced)} commands to guild {GUILD_ID}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
