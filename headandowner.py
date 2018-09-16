import discord
import asyncio
import time
import random
from discord.ext import commands

#head and owner Commands
class HeadAndOwnerCommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=439194953823027200)
        role2 = guild.owner
        if role in ctx.author.roles:
            return True
        return False
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            author = ctx.author
            return print(f"HeadAndOwnerCommand used in {ctx.channel.name} by {author.name}")

    @commands.command()
    async def say(self, ctx, *, words):
        await ctx.send(words)
        await ctx.message.delete()

    @commands.command()
    async def poll(self, ctx, *, words):
        msg = await ctx.send(words)
        await ctx.message.delete()
        await msg.add_reaction(u"\U0001F44E")
        await msg.add_reaction(u"\U0001F44D")


def setup(bot):
    bot.add_cog(HeadAndOwnerCommands(bot))
