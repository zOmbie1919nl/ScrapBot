import discord
import asyncio
import os
import aiohttp
import time
from discord.ext import commands

class scrappercommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Heyy it works")

def setup(bot):
    bot.add_cog(scrappercommands(bot))
