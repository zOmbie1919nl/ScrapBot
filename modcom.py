import discord
import asyncio
import os
import aiohttp
import time
from discord.ext import commands

class Modcommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.author.guild_permissions.view_audit_log

    @commands.command()
    async def poll(self, ctx, *, words):
        msg = await ctx.send(words)
        await ctx.message.delete()
        await msg.add_reaction(u"\U0001F44E")
        await msg.add_reaction(u"\U0001F44D")

    @commands.command()
    async def ping(self, ctx):
        start = time.monotonic()
        msg = await ctx.send('Pinging....')
        heartbeat = ctx.bot.latency * 1000
        await msg.edit(content=f'Ping: {heartbeat:,.2f}ms')

    @commands.command()
    async def clear(self, ctx, amount: int=None):
        if amount is None:
            await ctx.send('Please put in a value for me to clear!')
        else:
            clear = amount +1
            await ctx.channel.purge(limit=clear)
            await ctx.send(f'``{amount}`` message(s) has been cleared', delete_after = 5)

    @commands.command()
    async def info(self, ctx):
        guild = ctx.guild
        em = discord.Embed(title="ScrapMan's social Media", colour=0xFF0000)
        em.set_author(name="ScrapMan's discord")
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name="Twitter:", value="Get updates about videos and random day to day thoughts from ScrapMan and his peers! \nhttps://twitter.com/ScrapManYT", inline=False)
        em.add_field(name="Sponser:", value="Become a Sponsor on Youtube for special perks and rewards within the Youtube app by clicking the Sponsor button next to the Sub button on his channel!", inline=False)
        em.add_field(name="Patreon:", value="Directly support ScrapMan for his efforts in exchange for exclusive access to various rewards \nhttps://www.patreon.com/scrapman", inline=False)
        em.add_field(name="Merch:", value="Show off your support for ScrapMan to your friends with a shirt branding the official ScrapMan logo \nhttps://teespring.com/stores/scrapman", inline=False)
        await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Modcommands(bot))
