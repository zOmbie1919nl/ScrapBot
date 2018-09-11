import discord
import asyncio
import os
import aiohttp
import collections
import time
import logging
import traceback
from discord.ext import commands

extensions = ['extension', "modcom", "scrappercom"]
logging.basicConfig(level='INFO')
logger = logging.getLogger('Loggie')

bot = commands.Bot(description='', command_prefix=commands.when_mentioned_or("sb.", ">>"), pm_help=False, case_insensitive=True)

setattr(bot, "logger", logger)

for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        logger.error(f"Failed to load '{extension}' with the folling error: \n{traceback.format_exc()}")

@bot.event
async def on_ready():
    print('Online and ready for action')
    await bot.change_presence(activity=discord.Game(name='with Moderators'))

bot.remove_command('help')

@bot.command()
async def help(ctx):
    em = discord.Embed(title="Commands!")
    em.add_field(name="Raimode", value="enables/disables raid mode, if enabled no members will be able to join.", inline=False)
    em.add_field(name="Poll [message]", value="sends a message with a thumbsup and thumbsdown.", inline=False)
    em.add_field(name="Ping", value="pings the bot and will send a message with the time it took to send that message.", inline=False)
    em.add_field(name="Clear [amount]", value="clears the amount of message, but unlike Mee6 or Dyno, this has no limit.", inline=False)
    em.add_field(name="Info", value="sends a embed message with links to ScrapMan's social-media.", inline=False)
    em.add_field(name="Userinfo [user's ID or mention]", value="Send an embed message with some information about their account.", inline=False)
    em.add_field(name="Altsuspect [user's ID or mention]", value="Will send a message in #alt-suspects where moderators can review the entry.", inline=False)
    await ctx.send(embed=em)


bot.run(os.environ['TOKEN'])
