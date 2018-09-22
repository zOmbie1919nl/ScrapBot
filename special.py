import discord
import aiohttp
import time
import random
import os
from discord.ext import commands

class SpecialCommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=490167294169841665) #special scrapper
        role2 = discord.utils.get(guild.roles, id=304833080563204096) #mod
        if ctx.channel.id == 490175018664460298 and role in ctx.author.roles or role2 in ctx.author.roles:
            return True
        return False

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            author = ctx.author
            return print(f"command used in {ctx.channel.name} by {author.name}")

    @commands.command()
    async def apistats(self, ctx):
        async with aiohttp.request("get", "https://status.discordapp.com/api/v2/status.json") as resp:
            json_data = await resp.json()
        status = json_data["status"]
        description = status["description"]
        await ctx.send(f"Discord Api status is: ``{description}``")

    @commands.command()
    async def rps(self, ctx, *, words=None):
        ROCK='rock'
        PAPER='paper'
        SCISSORS='scissors'
        WINNING_MOVES = {
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK
        }
        MOVES = list(WINNING_MOVES)
        def who_won(you, scrap):
            if WINNING_MOVES[you] == scrap:
                return 'I won!'
            elif WINNING_MOVES[scrap] == you:
                return 'You won!'
            else:
                return "It's a draw!"
        your_move = words
        scrap_move = random.choice(MOVES)
        if your_move is None:
            await ctx.send(f"I gladly want to play Rock, Paper, Scissors with you, but you need to choose a move!")
        elif your_move not in MOVES:
            await ctx.send(f"{words} is not a possible move you can do, therefor I won! :grin:")
        else:
            await ctx.send(f"You played {your_move}, I played {scrap_move}, {who_won(your_move, scrap_move)}")

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.request("get", "https://dog.ceo/api/breeds/image/random") as resp:
            json_data = await resp.json()
        img = json_data["message"]
        em = discord.Embed(name="Here have a Doggo", colour=0xc0ffee)
        em.set_image(url=img)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(SpecialCommands(bot))