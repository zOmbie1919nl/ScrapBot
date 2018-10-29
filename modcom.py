import discord
import asyncio
import os
import aiohttp
import time
import json
import traceback
from discord.ext import commands

class Modcommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=304833080563204096)
        result = role in ctx.author.roles
        return result

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            author = ctx.author
            await ctx.send(f"{author.mention} the command is on a cool down. You need to wait {int(error.retry_after) +1} second(s).", delete_after = 5)
            await ctx.message.delete()
        elif isinstance(error, commands.CommandNotFound):
            author = ctx.author
            await ctx.send(f"{author.mention}, {error}, please refrain to >>help", delete_after = 5)
            await ctx.message.delete()
        else:
            raise error

    @commands.command()
    async def modhelp(self, ctx):
        em = discord.Embed(title="Moderator Commands!")
        em.add_field(name="Raidmode", value="enables/disables raid mode, if enabled no members will be able to join.", inline=False)
        em.add_field(name="Clear [amount]", value="clears the amount of message, but unlike Mee6 or Dyno, this has no limit.", inline=False)
        em.add_field(name="Mute [member's mention or id] [time in minutes] [reason]", value="emergency mute in case Dyno is down.", inline=False)
        em.add_field(name="Rule [rule number]", value="Sends a message that contains a picture of the rule.", inline=False)
        em.add_field(name="Alt [your alt account]", value="Gives your alt account the alt role.", inline=False)
        author = ctx.author
        await ctx.message.add_reaction(u"\u2705")
        await author.send(embed=em)

    @commands.command()
    async def clear(self, ctx, amount: int=None):
        if amount is None:
            await ctx.send('Please put in a value for me to clear!')
        else:
            clear = amount +1
            await ctx.channel.purge(limit=clear)
            await ctx.send(f'``{amount}`` message(s) has been cleared', delete_after = 5)

    @commands.command()
    async def mute(self, ctx, member: discord.Member=None, time: int=None, *, reason=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=304833080563204096)
        role2 = discord.utils.get(guild.roles, id=346446365712187393)

        em = discord.Embed(title="Emergency Mute", colour=0xff0000)
        em.set_thumbnail(url=member.avatar_url)
        em.add_field(name="Member:", value=member.mention, inline=True)
        em.add_field(name="Time limit:", value=f"{time} minutes", inline=True)
        em.add_field(name="Reason:", value=reason, inline=False)
        em.add_field(name="Moderator:", value=ctx.author.mention, inline=True)
        id = 332189961145024512
        channel = guild.get_channel(id)

        if member is None:
            await ctx.send("I cannot mute without knowing who I have to mute!")
        elif role in member.roles:
            await ctx.send(f"As much as I want to mute {member.mention}, I can't sadly :(")
        elif time is None:
            await ctx.send("I need a time limit to mute someone")
        elif reason is None:
            await ctx.send("I need a reason to mute someone")
        else:
            await member.add_roles(role2, reason=reason)
            await ctx.message.delete()
            await channel.send(embed=em)
            time2 = int(time)*60
            await member.send(f"You've been muted for {time2} minutes for the reason: {reason}")
            await asyncio.sleep(time2)
            await member.remove_roles(role2)

    @commands.command()
    async def alt(self, ctx, member: discord.Member=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=462663314074501121)
        if member is None:
            await ctx.send("Who needs the alt role?")
        else:
            await member.add_roles(role)
            await ctx.send("Done!", delete_after = 5)
            
    @commands.command()
    async def rule(self, ctx, *, words):
        rules = {"0": 'https://images-ext-2.discordapp.net/external/nwmTBwW3BnaywnBlgNjkwmgdnxpFxro1TcqPR1WnHKc/https/cdn.discordapp.com/attachments/332597002816978944/451389516301991936/Screenshot_20180530-162022_Discord.jpg',
        "1": 'https://media.discordapp.net/attachments/429497161235824651/444164577802846218/1.jpg',
        "2": 'https://media.discordapp.net/attachments/429497161235824651/444164577975074827/2.jpg', 
        "3": 'https://media.discordapp.net/attachments/429497161235824651/444164579501670400/3.jpg',
        "4": 'https://cdn.discordapp.com/attachments/429497161235824651/444164580562960391/4.jpg',
        "5": 'https://media.discordapp.net/attachments/429497161235824651/444164581246631936/5.jpg',
        "6": 'https://media.discordapp.net/attachments/429497161235824651/444164582987137065/6.jpg',
        "7": 'https://media.discordapp.net/attachments/429497161235824651/444164584849408011/7.jpg', 
        "8": 'https://cdn.discordapp.com/attachments/418895187071336458/453822294473703434/rule8..PNG'} 
        if words in rules:
            url = rules[words]
            em = discord.Embed(colour=0xc0ffee)
            em.set_image(url=url)
            await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Modcommands(bot))
