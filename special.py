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


    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def apistats(self, ctx):
        async with aiohttp.request("get", "https://status.discordapp.com/api/v2/status.json") as resp:
            json_data = await resp.json()
        status = json_data["status"]
        description = status["description"]
        await ctx.send(f"Discord Api status is: ``{description}``")

    @commands.cooldown(1, 60, commands.BucketType.user)
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

        wins = ["ScrapMan", "scrapman", "Scrapman", "zOm"]
        mentions = ["@everyone", "@moderator"]

        random1 = [f"{words} is not a possible move you can do, therefor I won! :grin:", 
        f"{words} is a word that is totally NOT in the list of moves you can do, cheater :unamused:",
        f"What do you think this is? Some kind of kids game? {words} is not a possible move",
        f"I'm not the smartest, but even I know {words} is not a possible move",
        f"Alright you've won, I can't compete with {words}"]

        random2 = random.choice(random1)
        your_move = words
        scrap_move = random.choice(MOVES)

        if your_move in mentions:
            await ctx.send("Yeaaaah we're not gonna do that mate")
        elif your_move is None:
            await ctx.send(f"I gladly want to play Rock, Paper, Scissors with you, but you need to choose a move!")
        elif your_move in wins:
            await ctx.send(f"Awh man I can't win from {your_move}, you've won this round :frowning2:")
        elif your_move not in MOVES:
            await ctx.send(f"{random2}")
        else:
            await ctx.send(f"You played {your_move}, I played {scrap_move}, {who_won(your_move, scrap_move)}")


    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.request("get", "https://dog.ceo/api/breeds/image/random") as resp:
            json_data = await resp.json()
        img = json_data["message"]
        em = discord.Embed(name="Here have a Doggo", colour=0xc0ffee)
        em.set_image(url=img)
        await ctx.send(embed=em)


    @commands.cooldown(1, 60, commands.BucketType.user)        
    @commands.command()
    async def dogfact(self, ctx):
        async with aiohttp.request("get", "https://fact.birb.pw/api/v1/dog") as resp:
           json_data = await resp.json()
        fact = json_data["string"]
        await ctx.send(f"Did you know that: {fact}")


    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.request("get", "http://aws.random.cat/meow") as resp:
            json_data = await resp.json()
        img = json_data["file"]
        em = discord.Embed(name="Here have a kitten", colour=0xc0ffee)
        em.set_image(url=img)
        await ctx.send(embed=em)

        
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def catfact(self, ctx):
        async with aiohttp.request("get", "https://catfact.ninja/fact") as resp:
           json_data = await resp.json()
        fact = json_data["fact"]
        await ctx.send(f"Did you know that: {fact}")



def setup(bot):
    bot.add_cog(SpecialCommands(bot))
