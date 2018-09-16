import discord
import asyncio
import os
import aiohttp
import time
import random
from discord.ext import commands

#super scrapper and mod
class SuperCommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=344219235527950341) #super scrapper
        role2 = discord.utils.get(guild.roles, id=304833080563204096) #mod
        if ctx.channel.id == 490175018664460298 and role in ctx.author.roles or role2 in ctx.author.roles:
            return True
        return False

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            author = ctx.author
            return print(f"command used in {ctx.channel.name} by {author.name}")

    @commands.command()
    async def ping(self, ctx):
        start = time.monotonic()
        msg = await ctx.send('Pinging....')
        heartbeat = ctx.bot.latency * 1000
        await msg.edit(content=f'Ping: {heartbeat:,.2f}ms')

    @commands.command()
    async def selfinfo(self, ctx):
        member = ctx.author
        joindate = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
        joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
        createddate = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'
        created = f'{createddate}, {str(member.created_at.time())[:-10]}'
        colors = [0xc0ffee, 0xff00e4, 0x00ff17, 0xff0000]
        color = random.choice(colors)
        em = discord.Embed(title='userinfo', colour=color)
        em.set_thumbnail(url=member.avatar_url)
        em.add_field(name='Name:', value=f"{member.name}", inline=True)
        em.add_field(name='Nickname:', value=member.nick, inline=True)
        em.add_field(name='User id', value=member.id, inline=False)
        em.add_field(name='Status:', value=member.status, inline=False)
        em.add_field(name='Created at:', value=created, inline=True)
        em.add_field(name='Joined at:', value=joined, inline=True)
        em.add_field(name='Roles:', value=', '.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
        return await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(SuperCommands(bot))
