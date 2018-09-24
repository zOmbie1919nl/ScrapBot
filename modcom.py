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
        if role in ctx.auhtor.roles:
            return True
        return False

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            author = ctx.author
            await ctx.send(f"{mention.author}The command is on a cool down. You need to wait {int(error.retry_after) +1} seconnd(s).", delete_after = 5)
        else:
            raise error

    @commands.command()
    async def clear(self, ctx, amount: int=None):
        if amount is None:
            await ctx.send('Please put in a value for me to clear!')
        else:
            clear = amount +1
            await ctx.channel.purge(limit=clear)
            await ctx.send(f'``{amount}`` message(s) has been cleared', delete_after = 5)


def setup(bot):
    bot.add_cog(Modcommands(bot))
