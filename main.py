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

# This kinda isn't needed, commands should all have a context or interaction that contains the guild it is from
GUILD_ID = discord.Object(id=972186275589275649)

@bot.event
async def on_ready():
    print(f"Loaded as: {bot.user.name}")

@bot.command(name='sync_tree')
@commands.is_owner()
async def sync_cmd(ctx):
    ctx.bot.tree.copy_global_to(guild=ctx.guild)
    synced = await bot.tree.sync(guild=ctx.guild)
    print(f"Synced {len(synced)} commands to guild {ctx.guild}")
    await ctx.channel.send(f"Synced {len(synced)} commands.")

@bot.tree.command(name='testing', description="test command")
async def testing_command(ctx : discord.Interaction):
    await ctx.response.send_message("Hello!")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
