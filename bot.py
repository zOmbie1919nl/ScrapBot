import discord
import logging
import traceback
import os
from discord.ext import commands

extensions = ['extension', "modcom", "headandowner", "embed", "super", "special", "scrapper"]
logging.basicConfig(level='INFO')
logger = logging.getLogger('Loggie')

bot = commands.Bot(description='', command_prefix=commands.when_mentioned_or("sb.", ">>", "Sb."), pm_help=False, case_insensitive=True)

setattr(bot, "logger", logger)

for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        logger.error(f"Failed to load '{extension}' with the folling error: \n{traceback.format_exc()}")

@bot.event
async def on_ready():
    print('Online and ready for action')
    await bot.change_presence(activity=discord.Game(name='with commands'))

bot.remove_command('help')

@bot.command()
async def help(ctx):
    em = discord.Embed(title="Scrapper Commands!")
    em.add_field(name="Altsuspect [user] [reason]", value="will send a message in #alt-suspects where moderators can review the entry.", inline=False)
    em.add_field(name="Info", value="the bot will send a message containing ScrapMan's social media.", inline=False)
    em.set_footer(text="For other help pages, type 'superhelp', 'specialhelp', or if you're a moderator 'modhelp'")
    author = ctx.author
    await author.send(embed=em)


@bot.command()
async def modhelp(ctx):
    em = discord.Embed(title="Moderator Commands!")
    em.add_field(name="Raidmode", value="enables/disables raid mode, if enabled no members will be able to join.", inline=False)
    em.add_field(name="Clear [amount]", value="clears the amount of message, but unlike Mee6 or Dyno, this has no limit.", inline=False)
    em.add_field(name="Userinfo [user's ID or mention]", value="send an embed message with some information about their account.", inline=False)
    author = ctx.author
    await author.send(embed=em)


@bot.command()
async def superhelp(ctx):
    em = discord.Embed(title="Super Scrapper Commands!")
    em.add_field(name="Ping", value="makes the bot send a message, then edit it and that will show you how long it took to respond.", inline=False)
    em.add_field(name="Serverinfo", value="this will give you some information about the server.", inline=False)
    em.add_field(name="Memberinfo [member's mention or id]", value="this will give you basic information about someone else. \nwhen there is no member, it will show you your own information", inline=False)
    author = ctx.author
    await author.send(embed=em)



@bot.command()
async def specialhelp(ctx):
    em = discord.Embed(name="Special Scrapper Commands!")
    em.add_field(name="Apistats", value="this will show you the current status of Discord's API.", inline=False)
    em.add_field(name="Dog", value="this will send a friendly and cute picture of a dog.", inline=False)
    em.add_field(name="Cat", value="this will send a friendly and cute picture of a cat.", inline=False)
    em.add_field(name="Rps [your move]", value="the bot will play a game of Rock Paper Scissors with you.", inline=False)
    author = ctx.author
    await author.send(embed=em)


bot.run(os.environ['TOKEN'])
