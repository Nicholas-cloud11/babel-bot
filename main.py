import datetime

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


from user import *

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=1453140691072061652)

@bot.event
async def on_ready():
    print(f"Loaded as: {bot.user.name}")
    try:
        guild = discord.Object(id=1453140691072061652)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild {guild.id}")

    except Exception as E:
        print(f"Error syncing commands {E}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.tree.command(name="approve", description="Approves a user for roleplaying", guild=GUILD_ID)
@commands.has_role("Bio Approvers")
async def approve(interaction: discord.Interaction, member: discord.Member ):
    role = discord.utils.get(member.guild.roles, name="Approved RPers")
    if role:
        await member.add_roles(role)
    else:
        interaction.response("Role doesn't exist")
    user_list.append(User(member.id, "Light Red", datetime.now(datetime.UTC)))

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
