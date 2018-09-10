import discord
import asyncio
import os
import aiohttp
import collections
import time
import logging
import traceback
from discord.ext import commands

extensions = ['extension', "modcom"]
logging.basicConfig(level='INFO')
logger = logging.getLogger('Loggie')

bot = commands.Bot(description='', command_prefix=commands.when_mentioned_or("sb."), pm_help=False, case_insensitive=True)

setattr(bot, "logger", logger)

for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        logger.error(f"Failed to load {extension} with the folling error: \n{traceback.format_exc()}")

@bot.event
async def on_ready():
    print('Online and ready for action')
    await bot.change_presence(activity=discord.Game(name='with Moderator Commands'))

bot.remove_command('help')


bot.run(os.environ['TOKEN'])
